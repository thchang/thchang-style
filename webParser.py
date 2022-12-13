import yaml

class WebParser:
    """ Class for parsing website config files and producing HTMLs. """

    def __init__(self):
        """ Initialize the webParser object """

        # Read swaplines in from styles document
        self.swaplines = []
        with open("styles/html-subs.csv") as fp:
            self.swaplines = fp.readlines()
        # Read row template
        with open("styles/body-content.html") as fp:
            rowtemp = fp.readlines()
        self.rowtemplate = "".join(rowtemp)
        # Read metadata
        self.metanames = []
        self.metaweb = []
        with open("info/meta.yaml") as fp:
            yamllist = yaml.load(fp, Loader=yaml.Loader)
            for item in yamllist:
                if 'me' in item.keys():
                    self.metanames.append(item['me']['name'])
                    if 'alias' in item['me'].keys():
                        for ai in item['me']['alias']:
                            self.metanames.append(ai)
                if 'web' in item.keys():
                    for key in item['web'].keys():
                        self.metaweb.append((key, item['web'][key]))
        return
        
    def web_swapper(self, line):
        """ Swap tagged lines in the input ``line``

        Args:
            line (str): The line to process for tags

        Returns:
            line with tagged strings replaced by the appropriate html markups

        """

        newline = line
        for swaps in self.swaplines:
            cols = [ci.strip() for ci in swaps.split(",")]
            if all([len(col.split(":")) > 1 for col in cols]):
                substr = newline.split(cols[0].split(":")[0])
                if len(substr) > 1:
                    for i in range(len(substr)):
                        if i % 2 == 1:
                            substr[i] = substr[i].replace(cols[0].split(":")[1],
                                                          cols[1].split(":")[1],
                                                          1)
                    newline = cols[1].split(":")[0].join(substr)
            else:
                newline = newline.replace(cols[0], cols[1])
        for name in self.metanames:
            newline = newline.replace(name, "<b>" + name + "</b>")
        for cols in self.metaweb:
            newline = newline.replace("$" + cols[0], cols[1])
        return newline
   
    def __call__(self, fname):
        """ Read in a formatted template file and process it line-by-line.

        Args:
            fname (str): The filename to read in

        Returns:
            str: The HTML/CSS/JS source code for the corresponding website

        """

        with open(fname, "r") as fp:
            inlines = fp.readlines()
        # Initialize output lines
        outlines = []
        outlines.append("<html>")
        firstRow = True
        # Read template
        with open("styles/head.html", "r") as fp:
            lines = fp.readlines()
        outstr = ""
        for line in lines:
            outstr = outstr + self.web_swapper(line)
        outlines.append(outstr)
        outlines.append("<body>")
        outlines.append(f'<a class="anchor" name="top"></a>')
        outlines.append('<div class="container-fluid">')
        # Do one pass over inlines and store all targets
        with open("targets.temp", "w") as fp:
            pass # To create a new file
        for count, line in enumerate(inlines):
            # Parse first line
            if count == 0:
                continue
            # Check for blank lines
            elif len(line.strip()) == 0:
                continue
            # Just dump all target IDs to a file
            elif line.strip()[0] == "%":
                words = [wi.strip() for wi in line.strip().split()]
                if len(words) > 1:
                    with open("targets.temp", "a") as fp:
                        fp.write(" ".join(words[1:]) + "\n")
        # Loop over lines in file
        for count, line in enumerate(inlines):
            # Parse first line
            if count == 0:
                continue
            # Check for blank lines
            elif len(line.strip()) == 0:
                continue
            # Place anchors at all targets
            elif line.strip()[0] == "%":
                words = [wi.strip() for wi in line.strip().split()]
                if len(words) > 1:
                    outlines.append('<a class="anchor" ' +
                                    f'name="{" ".join(words[1:])}"></a>')
            # Get section/subsection headings
            elif line.strip()[0] == "#":
                words = line.strip().split()
                if len(words[0]) > 1 and words[0][1] == "#":
                    outlines.append("\n<h2>" + " ".join(words[1:]) + "</h2>\n")
                else:
                    if firstRow:
                        firstRow = False
                    else:
                        outlines.append('<br><p style="text-align: ' +
                                        'right"><a href="#top">^top</a></p>')
                        outlines.append('</div>\n</div>\n</div>\n')
                    titleline = " ".join(words[1:])
                    outlines.append(self.rowtemplate.replace("$TITLE",
                                                             titleline))
            # Extract data from yaml/bib files
            else:
                # Parse + tokenize command
                parts = line.strip().split(":")
                style = [si.strip() for si in parts[0].strip().split(",")]
                if len(parts) > 1:
                    if parts[1].strip() == "":
                        content = []
                    else:
                        content = [si.strip()
                                   for si in parts[1].strip().split(",")]
                else:
                    content = []
                if len(style) < 2:
                    raise ValueError(f"Line {count} does not have a filename" +
                                     " and formatter")
                else:
                    spec = style[0].split(".")
                    if len(spec) < 2:
                        raise ValueError(f"Line {count}: {style[0]} is " +
                                         "not a valid filename")
                    fname = ".".join(spec[0:2])
                    # If bib file, run bib2yaml
                    if spec[-1] == "bib":
                        import utils.bib2yml
        
                        yaml_text = utils.bib2yml(fname)
                    # Otherwise, just load yaml
                    else:
                        with open(fname) as fp:
                            yaml_lines = fp.readlines()
                        yaml_text = "\n".join(yaml_lines)
                    # Extract list/dictionary from yaml object
                    H = yaml.load(yaml_text, Loader=yaml.Loader)
                    topic_list = []
                    if len(content) == 0:
                        for item in H:
                            for key in list(item.keys()):
                                topic_list.append(item[key])
                    else:
                        for item2 in H:
                            found = False
                            found_item = item2
                            for item1 in content:
                                spec1 = item1.split(".")
                                found1 = True
                                for s1 in spec1:
                                    if s1 in found_item.keys():
                                        found_item = found_item[s1]
                                    else:
                                        found1 = False
                                if found1:
                                    found = True
                            if found:
                                topic_list.append(found_item)
                    # Load styler
                    import formatters
                    try:
                        styler = getattr(formatters, style[1])
                        outlines.append("<p>\n" +
                                        self.web_swapper(styler(topic_list)) +
                                        "\n</p>")
                    except AttributeError:
                        raise ValueError(f"Line {count} format " +
                                         f"spec {style[1]} not recognized ...")
        outlines.append('<br><p style="text-align: right">' +
                        '<a href="#top">^top</a></p>')
        outlines.append("</div>\n</div>\n</div>\n")
        outlines.append('</div>')
        outlines.append("</body>")
        outlines.append("</html>")
        return "\n".join(outlines)

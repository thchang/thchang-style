import sys
import yaml

with open(sys.argv[1], "r") as fp:
    inlines = fp.readlines()

# Initialize output lines
outlines = []
outlines.append("\\documentclass[10pt]{article}")

# Read template
with open("styles/cv-style.tex", "r") as fp:
    lines = fp.readlines()
outlines.append("".join(lines))
outlines.append("\\begin{document}")

# Read swaps
global swaplines
with open("styles/latex-subs.csv") as fp:
    swaplines = fp.readlines()

# Read metadata
global metanames
metanames = []
with open("info/meta.yaml") as fp:
    yamllist = yaml.load(fp, Loader=yaml.Loader)
    for item in yamllist:
        if 'me' in item.keys():
            metanames.append(item['me']['name'])
            if 'alias' in item['me'].keys():
                for ai in item['me']['alias']:
                    metanames.append(ai)

def latex_swapper(line):
    global swaplines
    global metanames
    newline = line
    for swaps in swaplines:
        cols = [ci.strip() for ci in swaps.split(",")]
        newline = newline.replace(cols[0], cols[1])
    for name in metanames:
        newline = newline.replace(name, "{\\bf " + name + "}")
    return newline

# Loop over lines in file
for count, line in enumerate(inlines):
    # Parse first line
    if count == 0:
        continue
    # Check for blank lines
    elif len(line.strip()) == 0:
        continue
    # Skip over targets, which are only for HTML parser
    elif line.strip()[0] == "%":
        continue
    # Get section/subsection headings
    elif line.strip()[0] == "#":
        words = line.strip().split()
        if len(words[0]) > 1 and words[0][1] == "#":
            outlines.append("\\subsection*{" + " ".join(words[1:]) + "}")
        else:
            outlines.append("\\section*{" + " ".join(words[1:]) + "}")
    # Extract data from yaml/bib files
    else:
        # Parse + tokenize command
        parts = line.strip().split(":")
        style = [si.strip() for si in parts[0].strip().split(",")]
        if len(parts) > 1:
            if parts[1].strip() == "":
                content = []
            else:
                content = [si.strip() for si in parts[1].strip().split(",")]
        else:
            content = []
        if len(style) < 2:
            raise ValueError(f"Line {count} does not have a filename and formatter")
        else:
            spec = style[0].split(".")
            if len(spec) < 2:
                raise ValueError(f"Line {count}: {style[0]} is not a valid filename")
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
            #outlines.append(str(topic_list))
            # Load styler
            import formatters
            try:
                styler = getattr(formatters, style[1])
                outline = styler(topic_list)
                outlines.append(latex_swapper(outline))
            except AttributeError:
                raise ValueError(f"Line {count} format spec {style[1]} not recognized ...")
                #print(f"Line {count} format spec {style[1]} not recognized ...")
outlines.append("\\end{document}")

print("\n".join(outlines))

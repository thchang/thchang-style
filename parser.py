import sys

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

# Loop over lines in file
for count, line in enumerate(inlines):
    # Parse first line
    if count == 0:
        continue
    # Check for blank lines
    elif len(line.strip()) == 0:
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
                import yaml

                with open(fname) as fp:
                    yaml_lines = fp.readlines()
                yaml_text = "\n".join(yaml_lines)
            # Extract list/dictionary from yaml object
            H = yaml.load(yaml_text, Loader=yaml.Loader)
            if len(content) == 0:
                topic_list = H
            else:
                topic_list = []
                for item1 in content:
                    spec1 = item1.split(".")
                    for item2 in H:
                        found = True
                        found_item = item2
                        for s1 in spec1:
                            if s1 in found_item.keys():
                                found_item = found_item[s1]
                            else:
                                found = False
                        if found:
                            topic_list.append(found_item)
            #outlines.append(str(topic_list))
            # Load styler
            import formatters
            try:
                styler = getattr(formatters, style[1])
                outlines.append(styler(topic_list))
            except AttributeError:
                raise ValueError(f"Line {count} format spec {style[1]} not recognized ...")
                #print(f"Line {count} format spec {style[1]} not recognized ...")
outlines.append("\\end{document}")

print("\n".join(outlines))

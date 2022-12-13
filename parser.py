import sys
import os
import shutil

# Read the first line of the input file to determine the parser
fname = sys.argv[1]
with open(fname, "r") as fp:
    lines = fp.readlines()

# Create the output directory
if len(sys.argv) > 2:
    outdir = sys.argv[2]
else:
    outdir = "./build"
if not os.path.exists(outdir) or not os.path.isdir(outdir):
    os.mkdir(outdir)

# Check which parser to use
if lines[0].strip().lower() == "pdflatex":
    from cvParser import CvParser as Parser
    outname = fname.split("/")[-1].split(".")[0] + ".tex"
elif lines[0].strip().lower() == "html":
    from webParser import WebParser as Parser
    outname = fname.split("/")[-1].split(".")[0] + ".html"
else:
    raise ValueError(f"Couldn't parse line 1 of {fname}: {lines[0]}")

# Parse the contents of the file
my_parser = Parser()
content = my_parser(fname)

# Save to build directory, build latex, and move dependencies if needed
with open(outdir + "/" + outname, "w") as fp:
    fp.write(content)
    if lines[0].strip().lower() == "pdflatex":
        os.system(f"cd {outdir} && pdflatex {outname}")
    elif lines[0].strip().lower() == "html":
        if os.path.exists("timeline.svg"):
            os.rename("timeline.svg", f"{outdir}/timeline.svg")
        shutil.copy(os.path.dirname(__file__) + "/styles/bootstrap.min.css",
                    f"{outdir}/bootstrap.min.css")

import sys
import pyyaml

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as fp:
    inlines = fp.readlines()



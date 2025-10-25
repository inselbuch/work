#
# docit
#
# this program will take as an argument a text file
# the assumption is that it is python source
# it will produce as output every line of the original python source
# unmodified
#
# but, for each function that it encounters, a comment will be inserted BEFORE
# the function
# the comment will consist of the name of the function formatted as ASCII art
# using figlet, specifically with the font utopiab
#
# the objective is to produce a header above each function with the name of the function
# encoded large enough so that in the minimap of the source code, the function name
# will be readable
#
# Modification History
#
# October 24, 2025 - Inselbuch
#   new module
#
# Enhancements:
#   should detect when source already has a docit header for a function and not
#   produce a second, duplicate function header
#
#   if "def" is found in the line, but it is not actually function definition
#   the line should be ignored
#   perhaps if the characters before "def" are anything but whitespace?
#

import pyfiglet

import sys
import re

# this could be enhanced with argparse to provide support for command line parameters
# including, the name of the font, for example
try:
    fn = sys.argv[1]
except:
    print('usage: python3 docit.py <python_source_file>')
    sys.exit()

try:
    f = open(fn,"r")
except Exception as ex:
    print(ex)
    sys.exit()


for line in f:

    # use regular expression to find function definitions
    # rex = re.search(r'( *)def (.*)\(',line)
    rex = re.search(r'(\s+)def (.*)\(',line)

    # if we found one, there will be two groups produced
    # the first group is the set of characters leading up to the "def"
    # in this way, the indentation can be matched (spaces or tabs)
    # the second group is the name of the function itself
    if rex:

        print(f"{rex.group(1)}'''docit")
        fig = pyfiglet.figlet_format(rex.group(2),font='utopiab')
        print(fig,end='')
        print(f"{rex.group(1)}'''")
        print(line,end='')
    else:
        print(line,end='')

f.close()



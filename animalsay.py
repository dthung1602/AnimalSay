#!/usr/bin/env python

"""
            Display animal ASCII art with saying
"""

import argparse
import random
import os

# get directory of script
path = os.path.dirname(os.path.realpath(__file__)) + "/"


def random_line(filename):
    """
        return a random line from a file
        reference: https://stackoverflow.com/questions/14924721/how-to-choose-a-random-line-from-a-text-file
    """
    line_num = 0
    selected_line = ''
    try:
        with open(path + filename) as ff:
            while 1:
                line = ff.readline()
                if not line:
                    break
                line_num += 1
                if random.uniform(0, line_num) < 1:
                    selected_line = line
            return selected_line.strip()
    except IOError:
        print "ERROR: file '{}' can not be loaded.".format(path + filename)
        exit(1)


def display_text(text):
    """put text into a box"""

    # split text to lines
    max_line_length = 30
    if isinstance(text, str):
        words = text.strip().split()
    else:
        words = text
    lines = []
    line = []
    length_of_line = 0
    for word in words:
        if length_of_line + len(word) + 1 > max_line_length:
            lines.append(line)
            line = [word]
            length_of_line = len(word) + 1
        else:
            line.append(word)
            length_of_line += len(word) + 1
    lines.append(line)

    # find shortest line & adjust max_line_length
    max_line_length = 0
    for i in xrange(len(lines)):
        lines[i] = " ".join(lines[i])
        ll = len(lines[i])
        if ll > max_line_length:
            max_line_length = ll

    # first line
    print " " + "_" * (max_line_length + 2)
    print "(" + " " * (max_line_length + 2) + ")"

    # body
    for line in lines:
        print "( " + line.ljust(max_line_length, " ") + " )"

    # last line
    print "(" + "_" * (max_line_length + 2) + ")"


def display(text):
    """display text in a box, link to animal ascii pic"""
    display_text(text)

    s = """  \\
   \\
    \\	
    """
    print s,

    # display animal
    print animal_ascii_art.replace("\n", "\n     ")


############################################################################
#                            Parse arguments                               #
############################################################################

parser = argparse.ArgumentParser()

parser.add_argument("animal", type=str, nargs="?",
                    help="animal to display. 'any' will return a random one")

group = parser.add_mutually_exclusive_group()
group.add_argument("-l", "--list", action="store_true",
                   help="list all available animal")
group.add_argument("-r", "--reference", action="store_true",
                   help="print quotes and ASCII arts references")
group.add_argument("-q", "--quote", action="store_true",
                   help="animal will quote random sayings")
group.add_argument("-c", "--communism", action="store_true",
                   help="animal will quote random famous communist sayings!")
group.add_argument("-s", "--say", dest="saying", type=str, nargs="+",
                   help="specifies what animal says")
group.add_argument("-n", "--natural", action="store_true",
                   help="animal makes its natural sound")
group.add_argument("-i", "--insult", action="store_true",
                   help="animal will insult user")
group.add_argument("-g", "--got", action="store_true",
                   help="animal will say quotes from Game Of Thrones!")

args = parser.parse_args()

############################################################################
#                            Read animal list                              #
############################################################################

animal_list = ['any']
try:
    f = open(path + "animal_list.txt", "r")
    for l in f:
        animal_list.append(l.strip())
    f.close()
except IOError:
    print "ERROR: fail to read file {}animal_list.txt".format(path)
    exit(1)

############################################################################
#                          Handle reference option                         #
############################################################################
if args.reference:
    os.system("cat " + path + "reference.txt")
    exit(0)

############################################################################
#                          Handle list option                              #
############################################################################

animal = args.animal
if args.list:
    for animal in animal_list:
        print animal
    exit(0)
else:
    if not animal:
        print "ERROR: please specify an animal or use 'any' to get a random one"
        print "Use option -l or --list to see all available animals"
        exit(1)
    elif animal not in animal_list:
        print "ERROR: '{}' is not available".format(args.animal)
        print "Use option -l or --list to see all available animals"
        exit(1)

############################################################################
#                          Read animal ascii art                           #
############################################################################

animal_ascii_art = ""
while animal == 'any':
    animal = random.choice(animal_list)

try:
    f = open(path + "ascii_art/{}.txt".format(animal))
    animal_ascii_art = f.read() + "\n"
    f.close()
except IOError:
    print "ERROR fail to read {} ascii file".format(animal)
    exit(1)

############################################################################
#                          Handle quote option                             #
############################################################################

if args.quote:
    quote = random_line("quote.txt")  # read random quote from file
    display('"{}"'.format(quote))  # display it in ""
    exit(0)

############################################################################
#                          Handle GOT option                               #
############################################################################

if args.got:
    got = random_line("got.txt")  # read random quote from file
    display(got + " - GOT")
    exit(0)

############################################################################
#                          Handle say option                             #
############################################################################

if args.saying:
    display(args.saying)
    exit(0)

############################################################################
#                         Handle natural option                            #
############################################################################

if args.natural:
    noise = "Hallo, folks!"
    try:
        f = open(path + "noise.txt", "r")
        for l in f:
            tk = l.split(":")
            if tk[0] == animal:
                noise = tk[1] + "!"
                break
        f.close()
    except IOError:
        print "ERROR: fail to read {}noise.txt file".format(path)
        exit(1)

    display(noise)
    exit(0)

############################################################################
#                          Handle insult option                            #
############################################################################

if args.insult:
    insult = random_line("insult.txt")  # read random insult
    display(insult)
    exit(0)

############################################################################
#                        Handle communism option                           #
############################################################################

if args.communism:
    communism = random_line("communism.txt")  # read random communist saying
    display(communism)
    exit(0)

############################################################################
#                          Handle with no-option                           #
############################################################################

print animal_ascii_art
exit(0)

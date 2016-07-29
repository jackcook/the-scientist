import os, sys

sentence = " ".join(str(x) for x in sys.argv[1:])

# Run input through the SyntaxNet demo script, piping output into output.txt
os.system("(cd models/syntaxnet; echo \"%s\" | sh syntaxnet/demo.sh) > output.txt" % sentence)

output_file = open("output.txt", "r")
lines = output_file.readlines()

for line in lines:
    line = line.replace("\n", "")

    # We only need lines that are a part of the ASCII tree
    if line.startswith("Input") or line.startswith("Parse"):
        continue

    # Get the word's indentation level in the tree
    level = 0 if "+--" not in line else (len(line.split("+")[0]) + 3) / 4

    # Remove extraneous spaces
    while "  " in line:
        line = line.replace("  ", " ")

    data = line.split(" ")

    # Remove leftover indentation stuff
    # data is now an array with the word and its fine-grained and coarse-grained part of speech
    while data[0] == "" or data[0] == "|" or data[0] == "+--":
        data.pop(0)

    print "%d %s (%s %s)" % (level, data[0], data[1], data[2])

output_file.close()

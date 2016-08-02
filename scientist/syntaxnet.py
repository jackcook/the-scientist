import argparse, os, sys

from pos import CoarsePOS, FinePOS
from word import Word

root = {}
tree_data = []

def pass_sentence(sentence):
    global root, tree_data

    # Run input through the SyntaxNet demo script, piping output into output.txt
    os.system("(cd ./tf-models/syntaxnet; echo \"%s\" | sh syntaxnet/demo.sh 2>/dev/null) > output.txt" % sentence)

    output_file = open("output.txt", "r")
    lines = output_file.readlines()

    for idx, line in enumerate(lines):
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

        # Temporarily store as an object
        line_obj = {
            "word": data[0],
            "coarse": data[1],
            "fine": data[2],
            "level": level,
            "children": []
        }

        tree_data.append(line_obj)

    output_file.close()

    for idx, element in enumerate(tree_data):
        def has_children():
            if idx == len(tree_data) - 1:
                # The element has no children if it is the last element
                return False
            else:
                # The element has children if the next element has a higher level than the current one
                next_element = tree_data[idx+1]
                return next_element["level"] > element["level"]

        insert_child(element, element["level"], has_children())

    return root

# Inserts an element into the tree
def insert_child(element, level, has_children):
    global root

    # Removes the element's level and children array if it will not have children
    def gen_word(element):
        word = Word(
            word=element["word"],
            coarse=CoarsePOS(element["coarse"]).name,
            fine=FinePOS(element["fine"]).name
        )

        if has_children:
            word.children = []

        return word

    if level == 0:
        # If the level is zero, it is the root element
        root = gen_word(element)
    else:
        # If the level is not zero, we need to find it's parent
        get_element(root, level).children.append(gen_word(element))

# Finds the parent of an element that needs to be inserted into the tree
def get_element(element, level, currentlevel=0):
    if currentlevel == level - 1:
        return element
    else:
        return get_element(element.children[-1], level, currentlevel + 1)

if __name__ == "__main__":
    class JoinAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, " ".join(values))

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sentence", nargs="+", action=JoinAction)
    args = parser.parse_args()

    sentence = args.sentence

    print pass_sentence(sentence)

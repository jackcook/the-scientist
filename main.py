import json, os, sys

sentence = " ".join(str(x) for x in sys.argv[1:])

# Run input through the SyntaxNet demo script, piping output into output.txt
os.system("(cd models/syntaxnet; echo \"%s\" | sh syntaxnet/demo.sh) > output.txt" % sentence)

output_file = open("output.txt", "r")
lines = output_file.readlines()

root = {}
tree_data = []

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

def insert_child(element, level, has_children):
    global root

    # Removes the element's level and children array if it will not have children
    def clean(element):
        obj = {
            "word": element["word"],
            "coarse": element["coarse"],
            "fine": element["fine"]
        }

        if has_children:
            obj["children"] = []

        return obj

    if level == 0:
        # If the level is zero, it is the root element
        root = clean(element)
    else:
        # If the level is not zero, we need to find it's parent
        def get_element(element, level, currentlevel=0):
            if currentlevel == level - 1:
                return element
            else:
                return get_element(element["children"][-1], level, currentlevel + 1)

        get_element(root, level)["children"].append(clean(element))

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

print json.dumps(root, indent=4, sort_keys=True)

output_file.close()

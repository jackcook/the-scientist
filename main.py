import argparse, math, json, re, syntaxnet
from models import Vector
from pos import CoarsePOS, FinePOS

def answer_question(question):
    root = syntaxnet.pass_sentence(question)

    vectors_data = find_given_values(question)
    vectors = {key: Vector(dict=val) for key, val in vectors_data.iteritems()}

    subjects = find_elements(root, fine=[FinePOS.direct_object.name, FinePOS.nominal_subject.name])
    word = subjects[1]["word"]

    if word == "angle":
        return "%d degrees" % int(round(math.degrees(vectors["A"].theta), 0))
    elif word == "magnitude":
        return "%d magnitude" % int(round(vectors["A"].r))

def find_elements(root, found=[], words=None, coarse=None, fine=None, level=0):
    if words and root["word"] in words: found.append(root)
    if coarse and root["coarse"] in coarse: found.append(root)
    if fine and root["fine"] in fine: found.append(root)

    if "children" in root:
        for child in root["children"]:
            find_elements(child, found, words, coarse, fine, level=level+1)

    if level == 0: return found

def find_given_values(question):
    vectors = {}

    data = re.findall(r"([A-z0-9()]+ = [0-9].?[0-9]?)", question)
    values = {x.split(" = ")[0]: x.split(" = ")[1] for x in data}

    for key, val in values.iteritems():
        key_data = re.findall(r"([A-z])\(([A-z])\)", key)
        vector_id = key_data[0][0]
        variable = key_data[0][1]

        if vector_id not in vectors.keys():
            vectors[vector_id] = {}

        vectors[vector_id][variable] = val

    return vectors

if __name__ == "__main__":
    class JoinAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, " ".join(values))

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--question", nargs="+", action=JoinAction)
    args = parser.parse_args()

    print answer_question(args.question)

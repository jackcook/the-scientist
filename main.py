import argparse, math, json, re, syntaxnet
from models import Vector
from pos import CoarsePOS, FinePOS

def answer_question(question):
    info = question.split(". ")[1]
    root = syntaxnet.pass_sentence(info)

    vectors_data = find_given_values(question)
    vectors = {key: Vector(val) for key, val in vectors_data.iteritems()}

    subject = find_element(root, fine=FinePOS.nominal_subject.name)

    if subject["word"] == "angle":
        return "%d degrees" % int(round(math.degrees(vectors["A"].theta), 0))

def find_element(root, word=None, coarse=None, fine=None):
    if word and root["word"] == word: return root
    if coarse and root["coarse"] == coarse: return root
    if fine and root["fine"] == fine: return root

    if "children" in root:
        for child in root["children"]:
            element = find_element(child, word, coarse, fine)
            if element: return element

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

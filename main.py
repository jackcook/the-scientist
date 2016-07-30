import math, json, re, syntaxnet
from models import Vector
from pos import CoarsePOS, FinePOS

def answer_question(question):
    info = question.split(". ")[1]
    root = syntaxnet.pass_sentence(info)

    def find_subject(element):
        if element["fine"] == FinePOS.nominal_subject.name:
            return element
        else:
            return find_subject(element["children"][0])

    data = re.findall(r"([A-z0-9()]+ = [0-9].?[0-9]?)", question)
    values = {x.split(" = ")[0]: x.split(" = ")[1] for x in data}

    vec_data = {}

    for key, val in values.iteritems():
        key_data = re.findall(r"([A-z])\(([A-z])\)", key)
        vec_id = key_data[0][0]
        vec_variable = key_data[0][1]

        if vec_id not in vec_data.keys():
            vec_data[vec_id] = {}

        vec_data[vec_id][vec_variable] = val

    for key, val in vec_data.iteritems():
        x = y = r = theta = None

        for k, v in val.iteritems():
            if k == "x":
                x = v
            elif k == "y":
                y = v

        if x and y:
            vector = Vector(x=float(x), y=float(y))
            subject = find_subject(root)["word"]

            if subject == "angle":
                return "%d degrees" % int(round(math.degrees(vector.theta), 0))

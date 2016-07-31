import argparse, math, json, re, syntaxnet

from models import Vector
from pos import CoarsePOS, FinePOS

def answer_question(question):
    root = syntaxnet.pass_sentence(question)

    vectors_data = find_given_values(question, root)
    vectors = {key: Vector(dict=val) for key, val in vectors_data.iteritems()}

    request = find_request(question, root)

    vector = vectors.itervalues().next() # remove later to support multiple vectors

    if request == "angle":
        return "%d degrees" % int(round(math.degrees(vector.theta)))
    elif request == "horizontal_component":
        return "%d units" % int(round(vector.x))
    elif request == "magnitude":
        return "%d units" % int(round(vector.r))

def find_given_values(question, root):
    vectors = {}

    d1 = find_equal_sign_values(question)
    d2 = find_worded_values(root)

    for d in (d1, d2):
        for key, value in d.iteritems():
            if key not in vectors:
                vectors[key] = {}

            vectors[key].update(value)

    return vectors

# finds values in the form of A(x) = 2.5 / A(y) = 7.5 / etc
def find_equal_sign_values(question):
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

# finds values in the form of "a magnitude of {x} units" / "an angle of {x} degrees" / etc
def find_worded_values(root):
    vectors = {"A": {}}

    elements = root.find_elements(coarse=CoarsePOS.noun.name, fine=FinePOS.direct_object.name,
        ccoarse=[CoarsePOS.determiner.name, CoarsePOS.preposition_or_subordinating_conjunction.name],
        cfine=[FinePOS.determiner.name, FinePOS.prepositional_modifier.name])

    for element in elements:
        value_object = element.find_elements(coarse=CoarsePOS.noun_plural.name, fine=FinePOS.object_of_a_preposition.name,
            ccoarse=[CoarsePOS.cardinal_number.name])[0]

        (name, value) = convert_value_data(element.word, float(value_object.children[0].word))

        vectors["A"][name] = value

    return vectors

def convert_value_data(name, value):
    if name == "angle":
        return ("theta", math.radians(value))
    elif name == "magnitude":
        return ("r", value)

def find_request(question, root):
    return find_determiner_request(question, root)

def find_determiner_request(question, root):
    elements = root.find_elements(fine=FinePOS.object_of_a_preposition.name,
        ccoarse=[CoarsePOS.determiner.name, CoarsePOS.preposition_or_subordinating_conjunction.name],
        cfine=[FinePOS.determiner.name, FinePOS.prepositional_modifier.name])

    if len(elements) == 0:
        elements = root.find_elements(fine=FinePOS.nominal_subject.name,
            ccoarse=[CoarsePOS.wh_determiner.name], cfine=[FinePOS.determiner.name])

    element = elements[0].word

    if element == "magnitude":
        element = check_magnitude_properties(question)

    return element

def check_magnitude_properties(question):
    if "horizontal component" in question.split("magnitude")[-1]: return "horizontal_component"
    else: return "magnitude"

if __name__ == "__main__":
    class JoinAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, " ".join(values))

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--question", nargs="+", action=JoinAction)
    args = parser.parse_args()

    print answer_question(args.question)

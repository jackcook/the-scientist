import re

from physics import Vector
from pos import CoarsePOS, FinePOS
from request import RequestType

class Response:

    request = None
    text = None

    def __init__(self, request):
        self.request = request

    def generate_answer(self):
        if self.request.request_type == RequestType.informational:
            self.generate_informational_answer()
        else:
            self.generate_test_answer()

        return self.text

    def generate_informational_answer(self):
        word = self.request.get_term()

        try:
            filepath = open("./informational/%s.md" % word, "r")
            lines = filepath.readlines()
            self.text = "%s%s" % (lines[0], lines[2]) + \
                        "Read more at https://github.com/jackcook/the-scientist/tree/master/scientist/informational/%s.md" % word
        except IOError:
            self.text = "I don't know what that is! If you think I should be able to answer this\n" + \
                        "question, please submit an issue or pull request at:\n" + \
                        "https://github.com/jackcook/the-scientist/compare"

    def generate_test_answer(self):
        vectors = self.find_given_values()
        print vectors[0].theta

    def find_given_values(self):
        vectors = {}

        d1 = self.find_equal_sign_values()
        d2 = self.find_worded_values()

        for d in (d1, d2):
            for key, value in d.iteritems():
                if key not in vectors:
                    vectors[key] = {}

                vectors[key].update(value)

        actual_vectors = []

        for _, values in vectors.iteritems():
            actual_vectors.append(Vector(dict=values))

        return actual_vectors

    # finds values in the form of A(x) = 2.5 / A(y) = 7.5 / etc
    def find_equal_sign_values(self):
        vectors = {}

        data = re.findall(r"([A-z0-9()]+ = [0-9].?[0-9]?)", self.request.question)
        values = {}

        for x in data:
            values[x.split(" = ")[0]] = x.split(" = ")[1]

        for key, val in values.iteritems():
            key_data = re.findall(r"([A-z])\(([A-z])\)", key)
            vector_id = key_data[0][0]
            variable = key_data[0][1]

            if vector_id not in vectors.keys():
                vectors[vector_id] = {}

            vectors[vector_id][variable] = val

        return vectors

    # finds values in the form of "a magnitude of {x} units" / "an angle of {x} degrees" / etc
    def find_worded_values(self):
        vectors = {"A": {}}

        elements = self.request.element.find_elements(coarse=CoarsePOS.noun.name, fine=FinePOS.direct_object.name,
            ccoarse=[CoarsePOS.determiner.name, CoarsePOS.preposition_or_subordinating_conjunction.name],
            cfine=[FinePOS.determiner.name, FinePOS.prepositional_modifier.name])

        for element in elements:
            value_object = element.find_elements(coarse=CoarsePOS.noun_plural.name, fine=FinePOS.object_of_a_preposition.name,
                ccoarse=[CoarsePOS.cardinal_number.name])[0]

            (name, value) = convert_value_data(element.word, float(value_object.children[0].word))

            vectors["A"][name] = value

        return vectors

    # def find_requested_value(self):

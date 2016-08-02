import math, re

from physics import Vector
from question_model import QuestionModel

class CalculatedValueModel(QuestionModel):

    def matches(self, question, element):
        self.question = question
        self.element = element

        regex_match = False

        for regex in self.regexes:
            if re.match(regex, question):
                regex_match = True
                break

        if not regex_match: return None

        self.given_object = self.given_object_matches(element)
        self.requested_value = self.requested_value_matches(element)

        if self.given_object and self.requested_value:
            return self.solve()

    # finds values in the form of A(x) = 2.5 / A(y) = 7.5 / etc
    def find_equal_sign_values(self):
        vectors = {}

        data = re.findall(r"([A-z0-9()]+ = [0-9].?[0-9]?)", self.question)
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

    def given_object_matches(self, element):
        coarse = self.given_object["coarse"]
        fine = self.given_object["fine"]

        given_object = element.find_elements(coarse=coarse, fine=fine)[0]
        return given_object.word

    # def given_values_match(self, element):
    #     coarse = self.given_values["coarse"]
    #     fine = self.given_values["fine"]
    #
    #     given_values = element.find_elements(coarse=coarse, fine=fine)
    #     if given_values:
    #         for value in given_values:
    #             print "Given Value: %s" % value.word
    #             return True

    def requested_value_matches(self, element):
        coarse = self.requested_value["coarse"]
        fine = self.requested_value["fine"]

        requested_value = element.find_elements(coarse=coarse, fine=fine)[0]
        return requested_value.word

    def solve(self):
        if self.given_object == "vector":
            vectors_data = self.find_equal_sign_values()

            vectors = []

            for _, values in vectors_data.iteritems():
                vectors.append(Vector(dict=values))

            if self.requested_value == "angle":
                return "%d degrees" % int(round(math.degrees(vectors[0].theta)))

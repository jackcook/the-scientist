import math, re

from physics import Vector

class QuestionData:

    question = None

    given_object = None
    requested_value = None

    def __init__(self, question, given_object, requested_value):
        self.question = question
        self.given_object = given_object
        self.requested_value = requested_value

    def solve(self):
        if self.given_object == "vector":
            vectors_data = self.find_equal_sign_values()

            vectors = []

            for _, values in vectors_data.iteritems():
                vectors.append(Vector(dict=values))

            if self.requested_value == "angle":
                return "%d degrees" % int(round(math.degrees(vectors[0].theta)))

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

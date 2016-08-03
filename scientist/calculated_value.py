import json, math, re

from physics import Vector
from question_model import QuestionModel

class CalculatedValueModel(QuestionModel):
    """A model matching questions asking for a calculated value.

    These questions will typically consist of one or two given values, and one
    missing value that needs to be calculated using math. An exampe of this
    could be a question that gives you the x value and magnitude of a vector,
    asking you to calculate theta.

    Attributes:
        given_object: The object being discussed in the question (e.g. vector).
        requested_value: The value being asked for in the question (e.g.
            magnitude).
    """

    def __init__(self, fp):
        super(CalculatedValueModel, self).__init__(fp)

        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.given_object = data["given_object"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        if not super(CalculatedValueModel, self).matches(question, element):
            return False

        self.given_object = self.find_given_object(element)
        self.requested_value = self.find_requested_value(element)

        if self.given_object and self.requested_value:
            return True

    def solve(self, question, element):
        if self.given_object == "vector":
            vectors_data = self.find_given_values(question)

            vectors = []

            for _, values in vectors_data.iteritems():
                vectors.append(Vector(dict=values))

            if self.requested_value == "angle":
                return "%d degrees" % int(round(math.degrees(vectors[0].theta)))
            elif self.requested_value == "magnitude":
                return "%d units" % int(round(vectors[0].y))

    def find_given_object(self, element):
        """Finds the given object could be found in the question.

        Args:
            element: The root word object of the question.

        Returns:
            A string, the given object of the question.
        """

        coarse = self.given_object["coarse"]
        fine = self.given_object["fine"]

        given_objects = element.find_elements(coarse=coarse, fine=fine)

        if len(given_objects) > 0:
            return given_objects[0].word

    def find_requested_value(self, element):
        """Finds the requested value could be found in the question.

        Args:
            element: The root word object of the question.

        Returns:
            A string, the requested value of the question.
        """

        coarse = self.requested_value["coarse"]
        fine = self.requested_value["fine"]

        requested_values = element.find_elements(coarse=coarse, fine=fine)

        if len(requested_values) > 0:
            return requested_values[0].word

    def find_given_values(self, question):
        vectors = {}

        d1 = self.find_equal_sign_values(question)
        d2 = self.find_worded_values(question)

        for d in (d1, d2):
            for key, value in d.iteritems():
                if key not in vectors:
                    vectors[key] = {}

                vectors[key].update(value)

        return vectors

    def find_equal_sign_values(self, question):
        """Looks for given values that are shown with equal signs. An example
        of this could be A(x) = 2.5.

        Args:
            question: The question string being searched.

        Returns:
            A dictionary where the keys are the identifiers of objects and the
            values are dictionaries where the keys are the object's attributes
            and the values are those attributes' values.
        """

        vectors = {}

        data = re.findall(r"([A-z0-9()]+ = [0-9].?[0-9]?)", question)
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

    def find_worded_values(self, question):
        """Looks for given values that are worded into the question. An example
        of this could be "a magnitude of 17 units

        Args:
            question: The question string being searched.

        Returns:
            A dictionary where the keys are the identifiers of objects and the
            values are dictionaries where the keys are the object's attributes
            and the values are those attributes' values.
        """

        vectors = {}

        regexes = [
            ("r", "a magnitude of ([\d]+)"),
            ("theta", "an angle of ([\d]+)")
        ]

        for regex_data in regexes:
            variable = regex_data[0]
            data = re.findall(regex_data[1], question)

            if len(data) == 0: continue

            vector_id = "A"

            if vector_id not in vectors.keys():
                vectors[vector_id] = {}

            vectors[vector_id][variable] = data[0]

        return vectors

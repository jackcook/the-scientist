import json, re

from question_data import QuestionData
from physics import Vector

class QuestionModel:

    # A list of regexes to match the question against. Only one has to match.
    regexes = None

    def __init__(self, fp):
        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.regexes = data["regexes"]
        self.given_object = data["given_object"]
        self.given_values = data["given_values"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        pass

    def solve(self):
        pass

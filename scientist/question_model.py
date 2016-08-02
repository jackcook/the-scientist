import json, re

from question_data import QuestionData

class QuestionModel:

    # A list of regexes to match the question against. Only one has to match.
    regexes = None

    # Properties (word / part of speech) to be matched against the given object.
    given_object = None

    # Properties (word / part of speech) to be matched against given values.
    given_values = None

    # Properties (word / part of speech) to be matched against the requested value.
    requested_value = None

    def __init__(self, fp):
        with open("./questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.regexes = data["regexes"]
        self.given_object = data["given_object"]
        self.given_values = data["given_values"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        regex_match = False

        for regex in self.regexes:
            if re.match(regex, question):
                regex_match = True
                break

        if not regex_match: return None

        given_object = self.given_object_matches(element)
        requested_value = self.requested_value_matches(element)

        if given_object and requested_value:
            return QuestionData(question, given_object, requested_value)

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

    @staticmethod
    def get_all_models():
        return [QuestionModel("calculated_value_001.json")]

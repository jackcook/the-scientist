import json

class QuestionModel:

    regexes = None
    given_object = None
    given_values = None
    requested_value = None

    def __init__(self, fp):
        with open(fp, "r") as model_file:
            data = json.load(model_file)

        self.regexes = data["regexes"]
        self.given_object = data["given_object"]
        self.given_values = data["given_values"]
        self.requested_value = data["requested_value"]

        print self.regexes

    @staticmethod
    def get_all_models():
        return [QuestionModel("calculated_value_001.json")]

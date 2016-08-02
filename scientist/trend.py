import json, re

from question_model import QuestionModel

class TrendModel(QuestionModel):

    def __init__(self, fp):
        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.regexes = data["regexes"]
        self.given_object = data["given_object"]
        self.given_values = data["given_values"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        self.question = question
        self.element = element

        regex_match = False

        for regex in self.regexes:
            if re.match(regex, question):
                regex_match = True
                break

        if not regex_match: return None

        return self.solve()

    def solve(self):
        return "increases"
        # trend = re.findall(r"from (\d+)\s?\w* to (\d+)\s?\w*", question)
        # values = (int(trend[0][0]), int(trend[0][1]))
        # interval = (values[1] - values[0]) / 10
        #
        # x_var = root.children[0].word
        # y_var = root.find_elements(fine=FinePOS.appositional_modifier.name)[0].word
        #
        # if y_var == "magnitude":
        #     y_var = check_magnitude_properties(question)
        #
        # results = []
        #
        # for i in range(interval):
        #     x = values[0] + interval * i
        #     y = create_given_vector(x_var, y_var, x).theta
        #     results.append(y)
        #
        # return "increases" if results[-1] > results[0] else "decreases"

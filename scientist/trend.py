import json, math, re

from physics import Vector
from pos import FinePOS
from question_model import QuestionModel

class TrendModel(QuestionModel):
    """A model matching questions asking about a general trend.

    These questions will typically consist of one independent variable changing
    while all other variables remain constant. This change in the independent
    variable will have a measured effect in the dependent variable, which is
    what is being asked for.

    Attributes:
        given_object: The object being discussed in the question (e.g. angle).
        requested_value: The value being asked for in the question (e.g.
            magnitude).
    """

    def __init__(self, fp):
        super(TrendModel, self).__init__(fp)

        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.given_object = data["given_object"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        if not super(TrendModel, self).matches(question, element):
            return False

        return True

    def solve(self, question, element):
        trend_data = re.findall(r"from (\d+)\s?\w* to (\d+)\s?\w*", question)
        values = (int(trend_data[0][0]), int(trend_data[0][1]))
        interval = (values[1] - values[0]) / 10

        pos = FinePOS.appositional_modifier.name if self.requested_value \
            ["fine"] == "appositional_modifier" else FinePOS.nominal_subject \
            .name

        x_var = element.children[0].word
        y_var = element.find_elements(fine=pos)[0].word

        if y_var == "magnitude":
            y_var = self.check_magnitude_properties(question)

        results = []

        if interval > 0:
            for i in range(interval):
                x = values[0] + interval * i
                y = self.create_given_vector(x_var, y_var, x).theta
                results.append(y)
        else:
            for i in range(abs(interval)):
                x = values[1] + interval * i
                y = self.create_given_vector(x_var, y_var, x).theta
                results.append(y)

        return "increases" if results[-1] > results[0] else "decreases"

    def create_given_vector(self, x_var, y_var, value):
        vector = None

        if x_var == "angle":
            if y_var != "horizontal_component":
                vector = Vector(x=16, theta=math.radians(value))
            else:
                vector = Vector(y=16, theta=math.radians(value))

        return vector

    def check_magnitude_properties(self, question):
        if "horizontal component" in question.split("magnitude")[-1]: return "horizontal_component"
        elif "vertical component" in question.split("magnitude")[-1]: return "vertical_component"
        else: return "magnitude"

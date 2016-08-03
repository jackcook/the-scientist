import math, re

from physics import Vector
from pos import FinePOS
from question_model import QuestionModel

class TrendModel(QuestionModel):

    def matches(self, question, element):
        if not super(TrendModel, self).matches(question, element):
            return False

        return True

    def solve(self, question, element):
        trend_data = re.findall(r"from (\d+)\s?\w* to (\d+)\s?\w*", question)
        values = (int(trend_data[0][0]), int(trend_data[0][1]))
        interval = (values[1] - values[0]) / 10

        x_var = element.children[0].word
        y_var = element.find_elements(fine=FinePOS.appositional_modifier.name)[0].word

        if y_var == "magnitude":
            y_var = self.check_magnitude_properties(question)

        results = []

        for i in range(interval):
            x = values[0] + interval * i
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

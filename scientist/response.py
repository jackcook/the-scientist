import re

from physics import Vector
from question_model import QuestionModel

from calculated_value import CalculatedValueModel
from informational import InformationalModel
from trend import TrendModel

class Response:

    request = None

    def __init__(self, request):
        """Inits a response with a request to answer."""

        self.request = request

    def generate_answer(self):
        """Generates an answer to the user's request.

        Returns:
            A string to be displayed to the user. This is either the answer to
            the question, or an explanation if an answer could not be found.
        """

        for model in Response.get_all_models():
            match = model.matches(self.request.question, self.request.element)
            if match: return model.solve(self.request.question, self.request.element)

        return "I am unable to answer this question. If you think I should be able to answer\n" + \
               "this, please submit an issue or pull request at:\n" + \
               "https://github.com/jackcook/the-scientist/compare"

    @staticmethod
    def get_all_models():
        return [InformationalModel("informational_001.json"), CalculatedValueModel("calculated_value_001.json"), CalculatedValueModel("calculated_value_002.json"), TrendModel("trend_001.json")]

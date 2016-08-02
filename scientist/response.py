import re

from physics import Vector
from request import RequestType
from question_model import QuestionModel

class Response:

    request = None

    def __init__(self, request):
        self.request = request

    def generate_answer(self):
        if self.request.request_type == RequestType.informational:
            return self.generate_informational_answer()
        else:
            return self.generate_test_answer()

    def generate_informational_answer(self):
        word = self.request.get_term()

        try:
            filepath = open("./scientist/informational/%s.md" % word, "r")
            lines = filepath.readlines()
            return "%s%s" % (lines[0], lines[2]) + \
                   "Read more at https://github.com/jackcook/the-scientist/tree/master/scientist/informational/%s.md" % word
        except IOError:
            self.text = "I don't know what that is! If you think I should be able to answer this\n" + \
                        "question, please submit an issue or pull request at:\n" + \
                        "https://github.com/jackcook/the-scientist/compare"

    def generate_test_answer(self):
        for model in QuestionModel.get_all_models():
            match = model.matches(self.request.question, self.request.element)
            if match: return match.solve()

        # no question models matched
        return "I am unable to answer this question. If you think I should be able to answer\n" + \
               "this, please submit an issue or pull request at:\n" + \
               "https://github.com/jackcook/the-scientist/compare"

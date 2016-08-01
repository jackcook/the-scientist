import re, syntaxnet

from aenum import Enum
from stemming.porter2 import stem

class Request:

    element = None
    question = None
    request_type = None

    def __init__(self, question):
        self.question = question
        self.determine_request_type()

    def determine_request_type(self):
        if self.get_term():
            self.request_type = RequestType.informational
        else:
            self.element = syntaxnet.pass_sentence(self.question)
            self.request_type = RequestType.test

    def get_term(self):
        question_formats = [
            "what is a (\w+)",
            "what are (\w+)",
            "describe (\w+)",
            "explain (\w+)"
        ]

        term = None

        for regex in question_formats:
            match = re.match("%s[\.\?]?" % regex, self.question.lower())
            if match:
                term = stem(match.groups(1))
                break

        return term


class RequestType(Enum):
    informational = 0
    knowledge_based = 1
    test = 2

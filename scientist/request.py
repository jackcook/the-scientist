from aenum import Enum
from informational import get_term, serve_answer

class Request:

    question = None
    request_type = None

    def __init__(self, question):
        self.question = question
        self.determine_request_type()

    def determine_request_type(self):
        if get_term(self.question):
            self.request_type = RequestType.informational
            serve_answer(self.question)
        else:
            self.request_type = RequestType.test


class RequestType(Enum):
    informational = 0
    knowledge_based = 1
    test = 2

from aenum import Enum
from informational import is_informational

class Request:

    question = None
    request_type = None

    def __init__(self, question):
        self.question = question
        self.determine_request_type()

    def determine_request_type(self):
        if is_informational(self.question):
            self.request_type = RequestType.informational
        else:
            self.request_type = RequestType.test

        print self.request_type


class RequestType(Enum):
    informational = 0
    knowledge_based = 1
    test = 2

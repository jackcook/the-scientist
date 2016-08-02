import syntaxnet

class Request(object):
    """An object representing a question the scientist is being asked.

    Attributes:
        element: The root word object of the question's representation in
            SyntaxNet.
        question: The string of the question being asked.
    """

    def __init__(self, question):
        """Inits a Request with a question string."""

        self.element = syntaxnet.pass_sentence(question)
        self.question = question

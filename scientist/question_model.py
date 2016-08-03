import json, re

from physics import Vector

class QuestionModel(object):
    """A model to match questions against.

    Attributes:
        regex: The regex that was used to match the question last passed.
        regexes: A list of strings representing regexes that the question will
            be matched against. Only one regex needs to match for this model to
            be considered a match.
    """

    def __init__(self, fp):
        """Inits QuestionModel with the model's file name."""

        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.regexes = data["regexes"]

    def matches(self, question, element):
        """Checks if this model matches the given question.

        Args:
            question: A string of the inputted question.
            element: The root word object of the question after it has been
                passed to SyntaxNet.

        Returns:
            A boolean, true if this model does fit the question, false if it
            does not fit.
        """

        regex_match = False

        for regex in self.regexes:
            if re.match(regex, question.lower()):
                self.regex = regex
                regex_match = True
                break

        return regex_match

    def solve(self, question, element):
        """Solves the given question.

        Args:
            question: A string of the inputted question.
            element: The root word object of the question after it has been
                passed to SyntaxNet.

        Returns:
            A string that should answer the question correctly.
        """

        pass

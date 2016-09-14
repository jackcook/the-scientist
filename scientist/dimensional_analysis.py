import json, re

from question_model import QuestionModel
from physics import Distance, DistanceUnit

class DimensionalAnalysisModel(QuestionModel):
    """A model matching questions that make use of dimensional analysis.

    These questions will often give you one or two given values and ask you to
    convert them into a different unit.

    Attributes:
        given_values: An array of values that have been provided by the
            question.
        requested_value: The value being requested.
    """

    def __init__(self, fp):
        super(DimensionalAnalysisModel, self).__init__(fp)

        with open("./scientist/questions/%s" % fp, "r") as model_file:
            data = json.load(model_file)

        self.given_values = data["given_values"]
        self.requested_value = data["requested_value"]

    def matches(self, question, element):
        if not super(DimensionalAnalysisModel, self).matches(question, element):
            return False

        self.given_values = self.find_given_values(question, element)
        self.requested_value = self.find_requested_value(question, element)

        if self.given_values and self.requested_value:
            return True

    def solve(self, question, element):
        answer = getattr(self.requested_value[1], self.requested_value[0])
        return "%.4f %s" % (answer, self.requested_value[0])

    def find_given_values(self, question, element):
        """Finds the given values that could be found in the question.

        Args:
            question: The question being asked, as a string.
            element: The root word object of the question.

        Returns:
            An array of value objects.
        """

        values = []

        for unit in list(DistanceUnit):
            regex = "(\d+(\.\d+)?) (%s|%s)" % (unit.name, unit.value[1])
            finds = re.findall(regex, question.lower())

            for finding in finds:
                distance = Distance(finding[0], unit)
                values.append(distance)

        return values

    def find_requested_value(self, question, element):
        """Finds the value being requested in the question.

        Args:
            question: The question being asked, as a string.
            element: The root word object of the question.

        Returns:
            The type of value being requested.
        """

        for unit in list(DistanceUnit):
            regex = "how many ([\w]+) .* in (\d+(\.\d+)?) (%s|%s)" % (unit.name,
                unit.value[1])

            finds = re.findall(regex, question.lower())

            for finding in finds:
                return (finding[0], Distance(finding[1], unit))

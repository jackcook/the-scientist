from question_model import QuestionModel

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

        if self.given_objects and self.requested_value:
            return True

    def solve(self, question, element):
        return "10"

    def find_given_values(self, question, element):
        """Finds the given values that could be found in the question.

        Args:
            question: The question being asked, as a string.
            element: The root word object of the question.

        Returns:
            An array of value objects.
        """

        if "regex_groups" in self.given_values:
            finds = re.findall(self.regex, question.lower())
            finds = finds[0] if not isinstance(finds[0], (str, unicode)) else finds
            return finds[int(self.given_values["regex_group"])]
        else:
            coarse = self.given_values["coarse"]
            fine = self.given_values["fine"]

            given_values = element.find_elements(coarse=coarse, fine=fine)

            if len(given_values) > 0:
                return given_values

    def find_requested_value(self, question, element):
        """Finds the value being requested in the question.

        Args:
            question: The question being asked, as a string.
            element: The root word object of the question.

        Returns:
            The type of value being requested.
        """

        return "mile"

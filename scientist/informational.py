import re

from stemming.porter2 import stem

from question_model import QuestionModel

class InformationalModel(QuestionModel):
    """A model matching questions asking for basic information.

    These questions are very simple and are asking for vague information about
    a concept. For example, "what is a vector?"
    """

    def matches(self, question, element):
        if not super(InformationalModel, self).matches(question, element):
            return False

        return self.find_term(question) != None

    def solve(self, question, element):
        try:
            word = self.find_term(question)
            filepath = open("./scientist/informational/%s.md" % word, "r")
            lines = filepath.readlines()
            return "%s%s...\n" % (lines[0], lines[2][:77].replace("\n", "")) + \
                   "Read more at https://github.com/jackcook/the-scientist/tree/master/scientist/informational/%s.md" % word
        except IOError:
            self.text = "I don't know what that is! If you think I should be able to answer this\n" + \
                        "question, please submit an issue or pull request at:\n" + \
                        "https://github.com/jackcook/the-scientist/compare"

    def find_term(self, question):
        """Finds the term being asked about in the question.

        Args:
            question: A string of the question being asked.

        Returns:
            A string, the term being asked about in the question.
        """

        term = None

        for regex in self.regexes:
            match = re.match(regex, question.lower())
            if match:
                term = stem(match.groups(1))
                break

        return term

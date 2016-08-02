from question_model import QuestionModel

class TrendModel(QuestionModel):

    def matches(self, question, element):
        if not super(TrendModel, self).matches(question, element):
            return False

        return True

    def solve(self, question, element):
        return "increases"
        # trend = re.findall(r"from (\d+)\s?\w* to (\d+)\s?\w*", question)
        # values = (int(trend[0][0]), int(trend[0][1]))
        # interval = (values[1] - values[0]) / 10
        #
        # x_var = root.children[0].word
        # y_var = root.find_elements(fine=FinePOS.appositional_modifier.name)[0].word
        #
        # if y_var == "magnitude":
        #     y_var = check_magnitude_properties(question)
        #
        # results = []
        #
        # for i in range(interval):
        #     x = values[0] + interval * i
        #     y = create_given_vector(x_var, y_var, x).theta
        #     results.append(y)
        #
        # return "increases" if results[-1] > results[0] else "decreases"

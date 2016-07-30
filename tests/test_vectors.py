from main import answer_question

def test_question_1():
    question = "A vector is given by its components, A(x) = 2.5 and A(y) = 7.5. What angle does vector A make with the positive x-axis?"
    answer = answer_question(question)
    assert answer == "72 degrees"

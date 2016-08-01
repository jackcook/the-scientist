from scientist import answer_question

def test_question_1():
    question = "A vector is given by its components, A(x) = 2.5 and A(y) = 7.5. What angle does vector A make with the positive x-axis?"
    answer = answer_question(question)
    assert answer == "72 degrees"

def test_question_3():
    question = "A vector has a magnitude of 17 units and makes an angle of 20 degrees with the positive x-axis. The magnitude of the horizontal component of this vector is"
    answer = answer_question(question)
    assert answer == "16 units"

def test_question_4():
    question = "As the angle between a given vector and the horizontal axis increases from 0 degrees to 90 degrees, the magnitude of the vertical component of this vector"
    answer = answer_question(question)
    assert answer == "increases"

from scientist import answer_question as answer

def test_question_1():
    question = "There are 2.54 cm in 1 inch. How many feet are there in 1 meter?"
    assert answer(question) == "3.28 feet"

def test_question_2():
    question = "How many years are there in one 41-minute class period?"
    assert answer(question) == "7.8 × 10^-5 years"

def test_question_2_1():
    question = "How many years are there in 41 minutes?"
    assert answer(question) == "7.8 × 10^-5 years"

def test_question_4a():
    question = "There are 1.61 km in 1 mile. How many km/h is 50 mph?"
    assert answer(question) == "80.5 km/h"

def test_question_4b():
    question = "There are 1.61 km in 1 mile. How many m/s is 50 mph?"
    assert answer(question) == "22.36 m/s"

def test_question_5():
    question = "It takes you 30 minutes to walk 3 km. If you walked constantly for one full day, how many miles would you cover?"
    assert answer(question) == "89.44 miles"

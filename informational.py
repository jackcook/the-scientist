import re

def is_informational(question):
    question_formats = [
        "What is a (\w+)",
        "What are (\w+)",
        "Describe (\w+)",
        "Explain (\w+)"
    ]

    for regex in question_formats:
        if re.match("%s[\.\?]?" % regex, question): return True

    return False

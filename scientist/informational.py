import re

from stemming.porter2 import stem

def get_term(question):
    question_formats = [
        "what is a (\w+)",
        "what are (\w+)",
        "describe (\w+)",
        "explain (\w+)"
    ]

    term = None

    for regex in question_formats:
        match = re.match("%s[\.\?]?" % regex, question.lower())
        if match:
            term = stem(match.groups(1))
            break

    return term

def serve_answer(question):
    word = get_term(question)

    try:
        filepath = open("./informational/%s.md" % word, "r")
        lines = filepath.readlines()
        print "%s\n%s" % (lines[0], lines[2])
        print "Read more at https://github.com/jackcook/the-scientist/tree/master/scientist/informational/%s.md" % word
    except IOError:
        print "I don't know what that is! If you think I should, please create an issue or submit a pull request:"
        print "https://github.com/jackcook/the-scientist/compare"

    # https://github.com/jackcook/the-scientist/tree/master/scientist

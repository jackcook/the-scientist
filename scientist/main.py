import argparse, math, json, re, syntaxnet

from physics import Vector
from pos import CoarsePOS, FinePOS
from response import Response
from request import Request

def answer_question(question):
    request = Request(question)
    response = Response(request)
    return response.generate_answer()

if __name__ == "__main__":
    class JoinAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, " ".join(values))

    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--question", nargs="+", action=JoinAction)
    args = parser.parse_args()

    print answer_question(args.question)

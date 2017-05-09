#!/usr/bin/env python3 

"""
Process (CSV) quiz files of the form:
    Question, answer1, answer2....
Create includes for a test, and not a web form.
"""

import sys
import csv

QUESTION = 0
FIRST_ANSWER = 1
CORRECT = '^'

INDENT1 = "        "
INDENT2 = INDENT1 + INDENT1

quiz_file = None

if len(sys.argv) < 2:
    print("Must supply a quiz file.")
    exit(1)

quiz_file = sys.argv[1]
answer_key = ''
answers = 'abcdefghijklmnopqrstuvwxyz'

with open(quiz_file, "r") as f_in:
    freader = csv.reader(f_in)
    i = 1
    for row in freader:
        print(INDENT1 + '<li>')
        print(INDENT2 + row[QUESTION])
        print(INDENT1 + '</li>')
        print(INDENT1 + '<ol type="a">')
        j = 0
        for a in row[FIRST_ANSWER:]:
            a = a.strip()
            if a.startswith(CORRECT):
                a = a[1:]
                answer_key += str(i) + '. ' + answers[j] + "; "
            print(INDENT2 + '<li>')
            print(INDENT2 + a)
            print(INDENT2 + '</li>')
            j += 1

        print(INDENT1 + '</ol>')
        i += 1

    print(INDENT2 + '</ol>')

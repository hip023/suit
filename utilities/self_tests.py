import hashlib
from typing import Union

# If you got here - you're in the wrong place. go and do your homework please :) :)
ANSWERS = {
    "E1": [311, 31, 'int64', 467],
    "E2": [13607, 311, 'No', 'No', 32568, 13209, 187],
    "E3": [4, 500, 60, 2, 69, 69, 6],
    "E4": [34, 0, 6],
    "E5": [29, True, 15, False],
}


def test_your_notebook(notebook, *args):
    if notebook not in ANSWERS.keys():
        print("Nice try, smarty! Go and Break someone else's code :) ")
        raise ValueError("YOUR GRADE: 0! ")

    answers = ANSWERS.get(notebook)
    correct_answers = [answers[i] == args[i] for i, _ in enumerate(answers)]

    grade = int(100 * sum(correct_answers) / len(correct_answers))

    if grade > 93:
        print(f"You Rockstar! That's an A! Your Final Grade: {grade}")
    elif grade > 85:
        print(f"Not Bad! Your Final Grade: {grade}")
    elif grade > 75:
        print(f"Nice try, I bet you can do better next time! Your grade: {grade}")
    else:
        print(f"We're addicted to excellence here... how about you try again? Your grade: {grade}")

    print("-------------")
    print("Grade analysis:")

    for i, _ in enumerate(answers):
        print(f"{args[i]} - {correct_answers[i]}")

import hashlib
from typing import Union

# If you got here, answers are hashed :) go and do your homework please :) :)
ANSWERS = {
    "E1": [b'\x9d\xfc\xd5\xe5X\xdf\xa0J', b'\xc1jS \xfaGU0', b'\xff\x9b?\x96\xd3sS\xc5', b'U\xa7\xcf\x9cq\xf1\xc9\xc4'],
    "E2": [b'\xd4y&:\x148\xa8\xf9', b'\x9d\xfc\xd5\xe5X\xdf\xa0J', b'\xba\xfds"\xc6\xe9}%', b'\xba\xfds"\xc6\xe9}%',
           b'\x9a\xe0\xa5\x04\xe3\xaf\x13\xe2', b'&\xa9[;\xf6\xc0\xfaK', b'1\xfe\xfc\x0eW\x0c\xb3\x86'],
    "E3": [b'\xa8\x7f\xf6y\xa2\xf3\xe7\x1d', b'\xce\xe61\x12\x1c.\xc9#', b'\x07+\x03\x0b\xa1&\xb2\xf4',
           b'\xc8\x1er\x8d\x9dL/c', b'\x14\xbf\xa6\xbb\x14\x87^E', b'\x14\xbf\xa6\xbb\x14\x87^E',
           b'\x16y\t\x1cZ\x88\x0f\xaf'],
    "E4": [b'\xe3i\x85=\xf7f\xfaD', b'\xcf\xcd \x84\x95\xd5e\xef', b'\x16y\t\x1cZ\x88\x0f\xaf'],
    "E5": [b'n\xa9\xab\x1b\xaa\x0e\xfb\x9e', b"\xf8'\xcfF/b\x84\x8d", b'\x9b\xf3\x1c\x7f\xf0b\x93j', b'\xf82\x0b&\xd3\n\xb43'],
}


def get_hash(s: Union[str, int]):
    if not isinstance(s, str):
        s = str(s)
    return hashlib.md5(s.encode()).digest()[:8]


def test_your_notebook(notebook, *args):
    if notebook not in ANSWERS.keys():
        print("Nice try, smarty! Go and Break someone else's code :) ")
        raise ValueError("YOUR GRADE: 0! ")

    answers = ANSWERS.get(notebook)
    response_hash = [get_hash(a) for a in args]
    correct_answers = [answers[i] == response_hash[i] for i, _ in enumerate(answers)]

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

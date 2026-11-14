import random


def find_gcd(number1, number2):
    while number2 != 0:
        number1, number2 = number2, number1 % number2

    return number1


def generate_round():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]

    question = f"{number1} {number2}"
    correct_answer = str(find_gcd(number1, number2))

    return question, correct_answer

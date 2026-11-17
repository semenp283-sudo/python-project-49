import random


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate_round():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_even(number) else "no"

    return number, correct_answer

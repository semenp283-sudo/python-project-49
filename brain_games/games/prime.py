import random


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def generate_round():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]

    correct_answer = "yes" if is_prime(number) else "no"

    return number, correct_answer

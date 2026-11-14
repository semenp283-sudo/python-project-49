import random


def generate_round():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    operator = random.choice(["+", "-", "*"])  # ruff: ignore[suspicious-non-cryptographic-random-usage]

    match operator:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2

    question = f"{number1} {operator} {number2}"

    return question, str(result)

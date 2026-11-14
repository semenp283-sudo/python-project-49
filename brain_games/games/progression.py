import random


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def generate_round():
    MIN_NUMBER = 1
    MAX_NUMBER = 20
    start = random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    MIN_STEP_NUMBER = 1
    MAX_STEP_NUMBER = 10
    step = random.randint(MIN_STEP_NUMBER, MAX_STEP_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    MIN_LENGTH_NUMBER = 5
    MAX_LENGTH_NUMBER = 10
    length = random.randint(MIN_LENGTH_NUMBER, MAX_LENGTH_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)  # ruff: ignore[suspicious-non-cryptographic-random-usage]
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, correct_answer

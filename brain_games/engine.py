from brain_games.cli import welcome_user


def play(game, rules):
    name = welcome_user()

    print(rules)

    for _ in range(3):
        question, correct_answer = game()

        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

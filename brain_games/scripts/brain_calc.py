from brain_games.engine import play
from brain_games.games.calc import generate_round


def main():
    play(generate_round, "What is the result of the expression?")


if __name__ == "__main__":
    main()

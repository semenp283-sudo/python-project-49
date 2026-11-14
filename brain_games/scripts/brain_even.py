from brain_games.games.even import generate_round
from brain_games.engine import play


def main():
    play(generate_round, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == "__main__":
    main()
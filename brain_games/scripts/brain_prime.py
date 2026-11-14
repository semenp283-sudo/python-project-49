from brain_games.engine import play
from brain_games.games.prime import generate_round


def main():
    play(
        generate_round,
        'Answer "yes" if given number is prime. Otherwise answer "no".',
    )


if __name__ == "__main__":
    main()

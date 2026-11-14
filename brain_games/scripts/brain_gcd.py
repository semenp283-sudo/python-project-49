from brain_games.engine import play
from brain_games.games.gcd import generate_round


def main():
    play(
        generate_round,
        "Find the greatest common divisor of given numbers.",
    )


if __name__ == "__main__":
    main()

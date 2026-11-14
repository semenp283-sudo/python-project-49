from brain_games.engine import play
from brain_games.games.progression import generate_round


def main():
    play(
        generate_round,
        "What number is missing in the progression?",
    )


if __name__ == "__main__":
    main()

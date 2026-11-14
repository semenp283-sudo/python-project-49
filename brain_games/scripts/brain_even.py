from brain_games.engine import play
from brain_games.games.even import generate_round


def main():
    play(generate_round)


if __name__ == "__main__":
    main()

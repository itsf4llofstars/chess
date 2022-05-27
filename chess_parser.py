"""A Functions file for parsing chess *.pgn files
Written by: itsf4llofstars
email: irooted4hal@mailfence.com
Date: 26 May 2022
"""
import os
import re
import sys

# Not needed if not using the logger.py file, adjust code accordingly.
import logger as log


def create_full_path(path, filename) -> str:
    """DOC"""
    if not path.startswith("/") or path.endswith("/"):
        log.error("Leading path slashes missing.")
        print("Exiting; See chess.log")
        sys.exit()

    return os.path.join(path, filename)


def read_file(path):
    """DOC"""
    try:
        with open(path, "r", encoding="utf-8") as file_object:
            pgn_file = file_object.readlines()
    except FileNotFoundError as fnfe:
        log.error(f"FileNotFoundError: {fnfe}")
        print("Exiting; See chess.log")
        sys.exit()
    else:
        return pgn_file


def strip_new_lines(text_lines):
    """DOC"""
    no_newlines = []
    # [no_newlines.append(line[:-1]) for line in text_line]
    for line in text_lines:
        no_newlines.append(line[:-1])
    return no_newlines


def get_games(games):
    """DOC: Game must be on one single line (non-wrapped) with no white-
    space at end of the line (game)."""
    regex_game = r"^[1]\."
    only_games = []
    for game in games:
        if re.search(regex_game, game):
            only_games.append(game)
    return only_games


def wins_list(games, winning_games, white=True) -> None:
    """DOC"""
    wins_regex = re.compile(r"1-0$")
    if not white:
        wins_regex = re.compile(r"0-1$")

    for game in games:
        if re.search(wins_regex, game):
            winning_games.append(game)


def wins_str(games, white=True) -> str:
    """DOC"""
    wins_regex = re.compile(r"1-0$")
    if not white:
        wins_regex = re.compile(r"0-1$")

    winning_str = ""
    for game in games:
        if re.search(wins_regex, game):
            winning_str += f"{game}\n"
    return winning_str


def mate_list(games, mates, white=True) -> None:
    """DOC"""
    mate_regex = re.compile(r"[1-4]\d\.\s.+#\s1-0")
    if not white:
        mate_regex = re.compile(r"[1-4]\d\.\s.+#\s0-1")

    for game in games:
        if re.search(mate_regex, game):
            mates.append(game)


def mate_str(games, white=True) -> str:
    """DOC"""
    mate_regex = re.compile(r"[1-4]\d\.\s.+#\s1-0")
    if not white:
        mate_regex = re.compile(r"[1-4]\d\.\s.+#\s0-1")

    mates = ""
    for game in games:
        if re.search(mate_regex, game):
            mates += f"{game}\n"
    return mates


def all_mates_list(games, mates) -> None:
    """DOC"""
    mate_regex = re.compile(r"[1-4]\d\.\s.+#\s[0-1]-[0-1]")

    for game in games:
        if re.search(mate_regex, game):
            mates.append(game)


def all_mates_str(games) -> str:
    """DOC"""
    mate_regex = re.compile(r"[1-4]\d\.\s.+#\s[0-1]-[0-1]")

    mates = ""
    for game in games:
        if re.search(mate_regex, game):
            mates += f"{game}\n"
    return mates


def opeinings():
    """DOC"""


def main() -> None:
    """main"""
    full_path = create_full_path("/home/bumper/chess", "chess.pgn")
    pgn_games = read_file(full_path)
    stripped_games = strip_new_lines(pgn_games)
    only_the_games = get_games(stripped_games)
    wins = []
    wins_list(only_the_games, wins)
    wins_list(only_the_games, wins, False)
    mate_list(only_the_games, wins)
    mate_list(only_the_games, wins, False)
    all_mates_list(only_the_games, wins)

    wins_string = wins_str(only_the_games)
    wins_string = wins_str(only_the_games, False)
    wins_string = mate_str(only_the_games)
    wins_string = mate_str(only_the_games, False)
    wins_string = all_mates_str(only_the_games)

    print(wins_string)


if __name__ == "__main__":
    main()

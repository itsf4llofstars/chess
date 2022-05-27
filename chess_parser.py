"""A Functions file for parsing chess *.pgn files
Written by: itsf4llofstars
email: irooted4hal@mailfence.com
Date: 26 May 2022
"""
import os
import re
import sys

import logger as log


def create_full_path(path, filename):
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
    """DOC: Game must be on one singel non-wrapped line."""
    regex_game = r"^[1]\."
    only_games = []
    for game in games:
        if re.search(regex_game, game):
            only_games.append(game)
    return only_games


def wins_list(games, winning_games, white=True):
    """DOC"""
    wins_regex = re.compile(r"1-0$")
    if not white:
        wins_regex = re.compile(r"0-1$")

    for game in games:
        if re.search(wins_regex, game):
            winning_games.append(game)


def wins_str(games, white=True):
    """DOC"""
    wins_regex = re.compile(r"1-0$")
    if not white:
        wins_regex = re.compile(r"0-1$")

    winning_str = ''
    for game in games:
        if re.search(wins_regex, game):
            winning_str += f'{game}\n'
    return winning_str


def mate_list(games, mates, white=True):
    mate_regex = re.compile(r'\d{2}\.\s.+#\s1-0')
    if not white:
        mate_regex = re.compile(r'\d\d\.\s.+#\s0-1')

    for game in games:
        if re.search(mate_regex, game):
            mates.append(game)


def mate_str(games, white=True):
    mate_regex = re.compile(r'\d{2}\.\s.+#\s1-0')
    if not white:
        mate_regex = re.compile(r'\d\d\.\s.+#\s0-1')

    mates = ''
    for game in games:
        if re.search(mate_regex, game):
            mates += f'{game}\n'
    return mates


def opeinings():
    """DOC"""
    pass


def main():
    """main"""
    full_path = create_full_path("/home/bumper/chess", "chess.pgn")
    pgn_games = read_file(full_path)
    # [print(game) for game in pgn_games]

    stripped_games = strip_new_lines(pgn_games)
    # [print(game) for game in stripped_games]

    only_the_games = get_games(stripped_games)
    # [print(game) for game in only_the_games]

    game_wins = []
    wins_list(only_the_games, game_wins, False)

    game_win_str = wins_str(only_the_games)
    print(game_win_str)


    for game in game_wins:
        print(game)


if __name__ == "__main__":
    main()

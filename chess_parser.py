"""A Functions file for parsing chess *.pgn files
Written by: itsf4llofstars
email: irooted4hal@mailfence.com
Date: 26 May 2022
"""
import os
import re
import sys

# TODO: Set a return of [n][:-5] to strip hash mark
# TODO: Strip non-essential marks, +, #

# Not needed if not using the logger.py file, adjust code accordingly. Can
# we do a check to see if logger is imported and set a conditional for
# logging?
import logger as log


def create_full_path(path, filename) -> str:
    """DOC"""
    # Path string should start with /
    if not path.startswith("/"):
        log.error("create_full_path(): Leading path slashes missing.")
        print("Exiting; See chess.log")
        sys.exit()

    return os.path.join(path, filename)


def read_file(path):
    """DOC"""
    try:
        with open(path, "r", encoding="utf-8") as file_object:
            pgn_file = file_object.readlines()
    except FileNotFoundError as fnfe:
        log.error(f"read_file(): FileNotFoundError: {fnfe}")
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


def normalize_games(games):
    """DOC"""
    for game in games:
        ...


def write_games(filename, games):
    try:
        with open(filename, 'w') as write:
            for line in games:
                write.write(line)
                write.write(' ')
            write.write('\n')
    except Exception as e:
        log.error(f'write_games(): UNK: {e}')


def remove_long_games(chess_games, n=4):
    """DOC"""
    long_games = re.compile(rf'\s[{n}-9]\d\.\s')
    short_games = []
    for game in chess_games:
        if re.search(long_games, game):
            continue
        short_games.append(game)
    return short_games


def wins_list(games, white=True) -> None:
    """DOC"""
    wins_regex = re.compile(r"1-0$")
    if not white:
        wins_regex = re.compile(r"0-1$")

    wins = []
    [wins.append(game) for game in games if re.search(wins_regex, game)]
    return wins


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


def mate_list(games, white=True) -> None:
    """DOC"""
    mate_regex = re.compile(r'#\s1-0')
    if not white:
        mate_regex = re.compile(r'#\s0-1')

    mates = []
    [mates.append(game) for game in games if re.seach(mate_regex, game)]
    return mates


def mate_str(games, white=True) -> str:
    """DOC"""
    # mate_regex = re.compile(r"[1-4]\d\.\s.+#\s1-0")
    mate_regex = re.compile(r'#\s1-0')
    if not white:
        # mate_regex = re.compile(r"[1-4]\d\.\s.+#\s0-1")
        mate_regex = re.compile(r'#\s0-1')

    mates = ""
    for game in games:
        if re.search(mate_regex, game):
            mates += f"{game}\n"
    return mates


def all_mates_list(games) -> None:
    """DOC"""
    mate_regex = re.compile(r"#\s[0-1]-[0-1]")
    mates = []
    [mates.append(game) for game in games if re.search(mate_regex, game)]
    return mates


def all_mates_str(games) -> str:
    """DOC"""
    # mate_regex = re.compile(r"[1-4]\d\.\s.+#\s[0-1]-[0-1]")
    mate_regex = re.compile(r"#\s[0-1]-[0-1]")

    mates = ""
    for game in games:
        if re.search(mate_regex, game):
            mates += f"{game}\n"
    return mates


def openings(opening, games):
    """DOC"""
    openings_regex = re.compile(opening)

    chess_openings = ""
    for game in games:
        if re.search(openings_regex, game):
            chess_openings += f"{game}\n"
    return chess_openings


def main() -> None:
    """main"""
    full_path = create_full_path('/home/pi/chess', 'bumper.pgn')
    pgn_text = read_file(full_path)
    pgn_new_text = strip_new_lines(pgn_text)
    bumper_games = get_games(pgn_new_text)
    shortened_games = remove_long_games(bumper_games)
    white_mates = mate_list(shortened_games)
    black_mates = mate_list(shortened_games, False)
    all_checkmates = all_mates_list(shortened_games)

    [print(game) for game in white_mates]
    input()
    [print(game) for game in black_mates]
    input()
    [print(game) for game in all_checkmates]


if __name__ == "__main__":
    sys.exit(main())

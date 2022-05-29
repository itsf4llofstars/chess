"""
A Python functions file using only those required for the parsing of chess
games
"""
import os
import sys
import re


def create_full_path(path, filename) -> str:
    """DOC"""
    # Path string should start with / and not end with /
    if not path.startswith("/") or path.endswith("/"):
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
        print("The file was not found.")
        sys.exit()
    else:
        return pgn_file


def strip_new_lines(text_lines):
    """DOC"""
    no_newlines = []
    # [no_newlines.append(line[:-1]) for line in text_line]
    for line in text_lines:
        no_nl = line[:-1]
        if len(no_nl):
            no_newlines.append(no_nl)
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
    ...

def write_games(filename, games):
    """Writes out only the games with one game per line
    to a text file.
    """
    try:
        with open(filename, 'w') as write:
            for line in games:
                write.write(line)
                write.write('\n')
    except Exception as e:
        print(f"UNK ERR: {e}")


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


def openings(opening, games):
    """DOC"""
    openings_regex = re.compile(opening)

    chess_openings = ""
    for game in games:
        if re.search(openings_regex, game):
            chess_openings += f"{game}\n"
    return chess_openings


def get_path():
    """Gets the path form user"""
    print(
        "Enter the path to the pgn file\n",
        "Ex. /home/user/[directory /..]\n"
    )
    path = str(input())
    return path


def get_filename():
    """Gets the filename from user"""
    filename = str(input("Enter the file name\n"))
    return filename

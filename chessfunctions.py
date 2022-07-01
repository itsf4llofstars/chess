"""
A Python functions file using only those required for the parsing of chess
games
"""
import os
import re
import sys

# WHITE[BLACK]_MATE may need the list to be scrubbed to # 1[0]-0[1]
WHITE_MATE = (
    r"\s[2-3]\d\.\s[a-hB-R][1-8a-x][1-8a-h]?#?=?[1-8B-R]?#?[1-8]?#?=?[B-R]?#?\s1-0"
)
BLACK_MATE = r"\s[2-3]\d\.\s[a-hB-R][1-8a-x][1-8a-h]?=?[1-8B-R]?[1-8]?=?[B-R]?\s[a-hB-R][1-8a-x][1-8a-h]?#?=?[1-8B-R]?#?[1-8]?#?=?[B-R]?#?\s0-1"


def create_full_path(path, filename) -> str:
    """Joins path and filename"""
    if not path.startswith("/"):
        print("Leading forward slash needed.")
        sys.exit()

    return os.path.join(path, filename)


def read_file(path):
    """Reads in the text pgn file and returns a list of lines"""
    try:
        with open(path, "r", encoding="utf-8") as fo:
            pgn_file = fo.readlines()
    except FileNotFoundError:
        print("The file was not found.")
        sys.exit()
    else:
        return pgn_file


def strip_new_lines(text_lines):
    """Strips off the ending newlin character"""
    no_newlines = []
    for line in text_lines:
        no_newlines.append(line.strip())
    return no_newlines


def get_games(pgn_list, games):
    """DOC: Game must be on one single line (non-wrapped) with no white-
    space at end of the line (game)."""
    [games.append(game) for game in pgn_list if game.startswith("1.")]


def normalize_games(games):
    """DOC"""
    ...


def write_games(filename, games):
    """Writes out only the games with one game per line to a text file."""
    try:
        with open(filename, "w") as write:
            for line in games:
                write.write(line)
                write.write("\n")
    except Exception as e:
        print(f"UNK ERR: {e}")


def wins_list(games, winning_games, white=True) -> None:
    """DOC"""
    ending = "1-0"
    if not white:
        ending = "0-1"
    [winning_games.append(game) for game in games if game.endswith(ending)]


def mate_list(games, mates, white=True) -> None:
    """DOC"""
    global WHITE_MATE, BLACK_MATE

    mate_regex = re.compile(WHITE_MATE)
    if not white:
        mate_regex = re.compile(BLACK_MATE)

    for game in games:
        if mate_regex.findall(game):
            mates.append(game)


def all_mates_list(games, mates) -> None:
    """DOC"""
    [
        mates.append(game)
        for game in games
        if game.endswith("# 1-0") or game.endswith("# 0-1")
    ]


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
    print("Enter the path to the pgn file\n", "Ex. /path/to/file\n")
    path = str(input("Path: "))
    return path


def get_filename():
    """Gets the filename from user"""
    filename = str(input("Enter the file name: "))
    return filename


def main():
    lines = [
        "34. Rb8 1-0",
        "24. Rxe8# 1-0",
        "53. Qb7# 1-0",
        "23. Bxf6 1-0",
        "23. Bxf6 1-0",
        "53. Kd8 1-0",
        "29. Qxg7 1-0",
        "37. Re6# 1-0",
        "53. Qxg2# 1-0",
        "53. Rh4 1-0",
        "53. Qxb2 1-0",
        "53. Qxb2 1-0",
    ]

    mates = []
    all_mates_list(lines, mates)
    [print(mate) for mate in mates]


if __name__ == "__main__":
    sys.exit(main())

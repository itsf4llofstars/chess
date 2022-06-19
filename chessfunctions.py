"""
A Python functions file using only those required for the parsing of chess
games
"""
import os
import sys
import re

WHITE_MATE = (
    r"\s[2-3]\d\.\s[a-hB-R][1-8a-x][1-8a-h]?#?=?[1-8B-R]?#?[1-8]?#?=?[B-R]?#?\s1-0"
)
BLACK_MATE = (
    r"\s[2-3]\d\.\s[a-hB-R][1-8a-x][1-8a-h]?=?[1-8B-R]?[1-8]?=?[B-R]?\s[a-hB-R][1-8a-x][1-8a-h]?#?=?[1-8B-R]?#?[1-8]?#?=?[B-R]?#?\s0-1"
)


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


def get_games(games):
    """DOC: Game must be on one single line (non-wrapped) with no white-
    space at end of the line (game)."""
    regex_game = r"^[1]\."
    only_games = []
    for game in games:
        if regex_game.search(game):
            only_games.append(game)
    return only_games


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
    wins_regex = re.compile(r'[2-3]\d\.\s.+#\s1-0')
    if not white:
        wins_regex = re.compile(r'[2-3]\d\.\s.+\s.+#\s0-1')

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
    global WHITE_MATE, BLACK_MATE
    mate_regex = re.compile(WHITE_MATE)
    if not white:
        mate_regex = re.compile(BLACK_MATE)

    for game in games:
        if mate_regex.findall(game):
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
    print("Enter the path to the pgn file\n", "Ex. /path/to/file\n")
    path = str(input('Path: '))
    return path


def get_filename():
    """Gets the filename from user"""
    filename = str(input("Enter the file name: "))
    return filename


def main():
    lines = [
        '31. ww a8=Q Kd7 32. Rb6 e3 33. Qa7+ Ke8 34. Rb8 1-0',
        '21. wwm Qe2 Bc6 22. Qe7+ Kg8 23. Qe8+ Bxe8 24. Rxe8# 1-0',
        '50. wwm c6 Ka7 51. c7 Ka8 52. c8=Q+ Ka7 53. Qb7# 1-0',
        '20. dd Rd1 Rxd1+ 21. Kxd1 gxh5 22. Bd4+ f6 23. Bxf6 1/2-1/2',
        '20. dd Rd1 Rxd1+ 21. Kxd1 gxh5 22. Bd4+ f6 23. Rh4 Bxf6 1/2-1/2',
        '50. ww e6 Nf5+ 51. Kg6 Nh4+ 52. Kg7 Nf5+ 53. Kg6 Kd8 1-0',
        '26. bw Qxc6 Qxa3 27. Qd7 Qa1+ 28. Kh2 a4 29. Kg6 Qxg7 0-1',
        '34. bwm Kh3 Kf5 35. g4+ Kg6 36. f4 f5 37. Nh4 Re6# 0-1',
        '50. bwm Nxg3 Rxh3 51. Qe2 Rxg3+ 52. fxg3 Qxg3+ 53. Qg2 Qxg2# 0-1',
        '50. bw Kg5 Rc5+ 51. Kh6 Rc4 52. Kg5 Rb5+ 53. Kh6 Rh4 0-1',
        '50. dd g5 hxg5 51. Bxg5 Qf5+ 52. Ka1 Qxf2 53. Qxb2 1/2-1/2',
        '50. dd g5 hxg5 51. Bxg5 Qf5+ 52. Ka1 Qxf2 53. Rc5 Qxb2 1/2-1/2'
    ]

    white_mates = []
    mate_list(lines, white_mates)
    [print(mate) for mate in white_mates]

if __name__ == '__main__':
    main()

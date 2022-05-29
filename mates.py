#!/usr/bin/env python3
"""mates.py module file that can read in a pgn file, parse out only the
chess games and parse out either the white or black checkmate wins and return
them as either a list of strings or strings themselves.
Module has mild error checking. Logger import may not be needed.
"""

# TODO: Error fixing of pylint errors

import os
import re
import sys

import logger as log


def read_in_file(path: str, filename: str, mode: str = "r"):
    """Reads in a file and strips off the last index which will be
    a newline ('\\n') character.

    imports:
        os, sys

    Attributes:
        path [str]: Path to the file with all forward slashes required.
        filename [str]: Name of the file to read in.
        mode [str]: Read, write, append mode for file action. Defaults to 'r'.

    Return:
        file_text list[str]: The read in data with each index being a line
                             of text.
    """
    if not path.startswith("/") or not path.endswith("/"):
        print("Forward slashed needed")
        sys.exit()

    path_name: str = os.path.join(path, filename)
    file_text = []
    try:
        with open(path_name, mode) as fo:
            file_lines = fo.readlines()
    except FileNotFoundError as fnfe:
        log.error(f"File not found: {fnfe}")
        sys.exit()
    else:
        for line in file_lines:
            file_text.append(line[:-1])
    finally:
        if len(file_text):
            return file_text
    return


def write_out_file(path: str, filename: str, file_text: str, mode: str = "w") -> None:
    """Writes the passed text, 'file_text', to a file in 'path' under the name
    'filename'. Passing 'a' as mode will append instead of write/re-write.

    imports:
        os, sys

    Attributes:
        path [str]: Path to the file with all forward slashes required.
        filename [str]: Name of the file to written to.
        file_text [str]: The file text to write out.
        mode [str]: Write, append mode for file action. Defaults to 'w'.

    Return:
        N/A
    """
    if not path.startswith("/") or not path.endswith("/"):
        os.system("clear")
        print("\nFront and trailing forward slashes are needed.\n")
        sys.exit()
    path_name = os.path.join(path, filename)
    try:
        with open(path_name, mode) as fo:
            fo.write(file_text)
    except Exception as e:
        log.error(f"Unknown error: {e}")


def white_mates(games):
    """Interates through games list searching for games won by white with
    a checkmate and returns those games as a list. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        white_mate list[str]: List of strings containig checkmates by white.
    """
    white_mate = []
    # Any 2 digit number, period, whitespace, all chars, hash, whitespace, 1-0
    mate_regex = re.compile(r"\d{2}\.\s.+#\s1-0")
    for game in games:
        if re.search(mate_regex, game):
            white_mate.append(game)
    return white_mate


def black_mates(games):
    """Interates through games list searching for games won by black with
    a checkmate and returns those games as a list. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        black_mate list[str]: List of strings containig checkmates by black.
    """
    black_mate = []
    mate_regex = re.compile(r"\d{2}\.\s.+\s.+#\s0-1")
    for game in games:
        if re.search(mate_regex, game):
            black_mate.append(game)
    return black_mate


def white_mates_str(games) -> str:
    """Interates through games list searching for games won by white with
    a checkmate and returns those games as a string. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        white_mate [str]: String containig checkmates by white.
    """
    white_mate = ""
    mate_regex = re.compile(r"\d{2}\.\s.+#\s1-0")
    for game in games:
        if re.search(mate_regex, game):
            white_mate = white_mate + game + "\n"
    return white_mate


def black_mates_str(games) -> str:
    """Interates through games list searching for games won by black with
    a checkmate and returns those games as a string. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        black_mate [str]: String containig checkmates by black.
    """
    black_mate = ""
    mate_regex = re.compile(r"\d{2}\.\s.+\s.+#\s0-1")
    for game in games:
        if re.search(mate_regex, game):
            black_mate = black_mate + game + "\n"
    return black_mate


def main():
    """main"""
    game_list = read_in_file("/home/pi/python/chess/", "all-mates.pgn")
    [print(n) for n in game_list]

    checkmates = white_mates(game_list)
    [print(mate) for mate in checkmates]

    checkmates = black_mates(game_list)
    [print(mate) for mate in checkmates]

    checkmates_str = white_mates_str(game_list)
    print(checkmates_str)

    checkmates_str = black_mates_str(game_list)
    print(checkmates_str)

    write_out_file("/home/pi/ed/", "test-games.txt", checkmates_str)


if __name__ == "__main__":
    os.system("clear")
    sys.exit(main())
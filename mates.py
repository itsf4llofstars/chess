#!/usr/bin/env python3
"""mates.py module file that can read in a pgn file, parse out only the
chess games and parse out either the white or black checkmate wins and return
them as either a list of strings or strings themselves.
Module has mild error checking. Logger import may not be needed.
"""
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
    if not path.startswith("/"):
        print("Leading forward slashed needed")
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
            file_text.append(line.strip())
    finally:
        if len(file_text):
            return file_text
    return


def write_out_file(path: str, filename: str, file_text: str) -> None:
    # TODO: DO NOT PASS A LIST TO THIS FUNCTION
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
    if not path.startswith("/"):
        os.system("clear")
        print("\nLeading forward slashe are needed.\n")
        sys.exit()
    path_name = os.path.join(path, filename)
    try:
        with open(path_name, 'w') as fo:
            fo.write(file_text)
    except Exception as e:
        log.error(f"Unknown error: {e}")


def win_by_mate(games, color='white'):
    # TODO: Change doc
    """Interates through games list searching for games won by white with
    a checkmate and returns those games as a list. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        white_mate list[str]: List of strings containig checkmates by white.
    """
    wins_mate = []
    mate_regex = r''
    if color == 'white':
        mate_regex = re.compile(r"#\s1-0")
    elif color == 'black':
        mate_regex = re.compile(r"#\s0-1")
    elif color == 'both' or color == 'all':
        mate_regex = re.compile(r"#\s[0-1]-[0-1]")
    else:
        print('ERROR: mates.py (1)')
    for game in games:
        if mate_regex.search(game):
            wins_mate.append(game)
    return wins_mate


def win_by_mate_str(games, color='white') -> str:
    # TODO: Change doc
    """Interates through games list searching for games won by white with
    a checkmate and returns those games as a string. Games in games list must
    be on one line.

    Attributes:
        games list[str]: List of chess games.

    Return:
        white_mate [str]: String containig checkmates by white.
    """
    wins_mate = ''
    mate_regex = r''
    if color == 'white':
        mate_regex = re.compile(r"#\s1-0")
    elif color == 'black':
        mate_regex = re.compile(r"#\s0-1")
    elif color == 'both' or color == 'all':
        mate_regex = re.compile(r"#\s[0-1]-[0-1]")
    else:
        print('ERROR: mates.py (1)')
    for game in games:
        if mate_regex.search(game):
            wins_mate += game
            wins_mate += '\n'
    return wins_mate


def main():
    """main"""
    game_list = read_in_file("/home/pi/python/chess/", "all-mates2.txt")

    white = win_by_mate(game_list)
    black = win_by_mate(game_list, 'black')
    both = win_by_mate(game_list, 'both')

    str_white = win_by_mate_str(game_list)
    str_black = win_by_mate_str(game_list, 'black')
    str_both = win_by_mate_str(game_list, 'both')


if __name__ == "__main__":
    os.system("clear")

    sys.exit(main())

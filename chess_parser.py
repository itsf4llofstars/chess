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
    if not path.startswith('/') or path.endswith('/'):
        log.error('Leading path slashes missing.')
        print('Exiting; See chess.log')
        sys.exit()

    return os.path.join(path, filename)


def read_file(path):
    try:
        with open(path, 'r') as fo:
            pgn_file = fo.readlines()
    except FileNotFoundError as fnfe:
        log.error(f'FileNotFoundError: {fnfe}')
        print('Exiting; See chess.log')
        sys.exit()
    except Exception as e:
        log.error(f'Unknown Error: {fnfe}')
        print('Exiting; See chess.log')
        sys.exit()
    else:
        return pgn_file


def strip_new_lines(text_lines):
    no_newlines = []
    [no_newlines.append(line[:-1]) for line in text_lines]
    return no_newlines


def get_games(games):
    regex_game = r'^[1]\.'
    only_games = []
    for game in games:
        if re.search(regex_game, game):
            only_games.append(game)
    return only_games


def main():
    """main"""
    full_path = create_full_path('/home/bumper/chess', 'chess.pgn')

    pgn_games = read_file(full_path)
    [print(game) for game in pgn_games]

    stripped_games = strip_new_lines(pgn_games)
    [print(game) for game in stripped_games]

    only_the_games = get_games(stripped_games)
    [print(game) for game in only_the_games]


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import re
import logger as log
import sys


def get_chess_games(filename):
    try:
        with open(filename, 'r') as read:
            chess_games = read.readlines()
    except FileNotFoundError as fnfe:
        log.error(f'{fnfe}')
    except Exception as e:
        log.error(f'UNK: {e}')
    else:
        log.info('File Parsed')
        return chess_games


def strip_newlines(lines, new_lines):
    for line in lines:
        new_lines.append(line[:-1])


def get_only_games(all_data, games):
    game_only = re.compile(r'^[1-9]')
    for line in all_data:
        if re.match(game_only, line):
            games.append(line)


def write_games(filename, games):
    try:
        with open(filename, 'w') as write:
            for line in games:
                write.write(line)
    except Exception as e:
        log.error(f'UNK: {e}')
    else:
        log.info('File written')


def main():
    """main function"""
    chess_pgns = get_chess_games('ex_games.pgn')
    chess_games = []
    strip_newlines(chess_pgns, chess_games)
    only_games = []
    get_only_games(chess_games, only_games)
    write_games('justgames.pgn', only_games)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import os
import re
import sys

import logger as log


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
            line += '\n'
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


def get_italy(all_data, italians):
    italys = re.compile(r'^1\.\s?e4\se5\s2\.\s?Nf3\sNc6\s3\.\s?Bc4')
    # italys = re.compile(r'^1\.e4\se5')
    for i, line in enumerate(all_data):
        if re.match(italys, line):
            j = i
            while j < len(all_data):
                if all_data[j].startswith('['):
                    break
                italians.append(all_data[j])
                j += 1
            italians.append('\n')


def main():
    """main function"""
    print()
    for line in os.listdir():
        if line.endswith('pgn'):
            print(line)

    pgnfile = input('\nEnter the name of the pgn file: ')
    chess_pgns = get_chess_games(pgnfile)

    chess_games = []
    strip_newlines(chess_pgns, chess_games)

    italy = []
    get_italy(chess_games, italy)

    # only_games = []
    # get_only_games(chess_games, only_games)
    # write_games('blackburnes.pgn', only_games)

    new_filename = input('Enter the name of the file to save to: ')
    write_games(new_filename, italy)


if __name__ == '__main__':
    main()

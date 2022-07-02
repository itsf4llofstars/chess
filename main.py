#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import chess_parser as f


def main():
    pgn_path = '/home/pi/chess/'
    pgn_filename = 'bumper.pgn'

    full_path = f.create_full_path(pgn_path, pgn_filename)
    pgn_lines = f.read_file(full_path)
    del full_path

    pgn_new_lines = f.strip_new_lines(pgn_lines)
    del pgn_lines

    pgn_games = f.get_games(pgn_new_lines)
    del pgn_new_lines

    pgn_short_games = f.remove_long_games(pgn_games)
    del pgn_games

    white_mates = f.mate_list(pgn_short_games)
    black_mates = f.mate_list(pgn_short_games, False)
    del pgn_short_games

    [print(game) for game in white_mates]
    input('Continue.. ')
    [print(game) for game in black_mates]


if __name__ == "__main__":
    import sys

    sys.exit(main())

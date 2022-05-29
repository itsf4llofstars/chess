#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import chess_parser as pc

path = '/home/pi/python/chess'
filename = 'a_game.pgn'

full_path = pc.create_full_path(path, filename)
raw_games = pc.read_file(full_path)
chess_games = pc.strip_new_lines(raw_games)

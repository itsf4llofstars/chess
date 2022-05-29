#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import chess_parser as pc

path = '/home/pi/python/chess'
filename = 'a_game.py'

full_path = pc.create_full_path(path, filename)
print(full_path)

#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import chessfunctions as cf

ww = []
bw = []
wm = []
bm = []
am = []

user_path = cf.get_path()
user_file = cf.get_filename()

path_file = cf.create_full_path(user_path, user_file)  # Works
games_file = cf.read_file(path_file)  # Works
cleaned_games = cf.strip_new_lines(games_file)  # Works
just_games = cf.get_games(cleaned_games)  # Works

cf.write_games("bacon.pgn", just_games)  # Works

# cf.wins_list(buz, ww)  # Works
# cf.wins_list(buz, bw, False)  # Works

# wws = cf.wins_str(buz)  # Works
# bws = cf.wins_str(buz, False)  # Works

# cf.mate_list(buz, wm)  # Works
# cf.mate_list(buz, wm, False)  # Works

# wms = cf.mate_str(buz)  # Works
# bms = cf.mate_str(buz, False)  # Works

# cf.all_mates_list(buz, am)  # Works
# ams = cf.all_mates_str(buz)  # Works

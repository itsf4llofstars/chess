#!/usr/bin/env python3
"""main.py file for parsing chess data"""
import chessfunctions as cf

user_path = cf.get_path()
user_file = cf.get_filename()

path_file = cf.create_full_path(user_path, user_file)  # Works
games_file = cf.read_file(path_file)  # Works
cleaned_games = cf.strip_new_lines(games_file)  # Works
just_games = cf.get_games(cleaned_games)  # Works

white_mates = []
cf.wins_list(just_games, white_mates)

for game in white_mates:
    print(game)

print()

black_mates = []
cf.wins_list(just_games, black_mates, False)

for game in black_mates:
    print(game)


print(len(white_mates))
print(len(black_mates))

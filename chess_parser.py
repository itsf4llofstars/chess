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


def main():
    """main"""
    full_path = create_full_path('/home/bumper/chess', 'chess.pgn')
    print(full_path)


if __name__ == '__main__':
    main()

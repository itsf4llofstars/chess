#!/usr/bin/env python3
"""main logging python file"""
import os
import logging

level = logging.DEBUG
fmt = "[%(levelname)s %(asctime)s - %(message)s]"
logging.basicConfig(filename='chess.log', level=level, format=fmt)


def debug(text: str = 'DEBUG'):
    logging.debug(text)


def info(text: str = 'INFO'):
    logging.info(text)


def error(text: str = 'ERROR'):
    logging.error(text)


def warning(text: str = "WARNING"):
    logging.warning(text)


def critical(text: str = "CRITICAL"):
    logging.critical(text)


def main():
    info("main")
    debug()
    info()
    error("An error occured")
    warning()
    critical()


if __name__ == "__main__":
    os.system("clear")
    main()

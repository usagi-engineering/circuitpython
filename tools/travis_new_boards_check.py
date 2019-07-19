#! /usr/bin/env python3

import os
import re
import json

import build_board_info

# Get boards in json format
boards_info_json = build_board_info.get_board_mapping()

# Get all the boards out of the json format
info_boards = boards_info_json.keys()

# We need to know the path of the .travis.yml file
base_path = os.path.dirname(__file__)
travis_path = os.path.abspath(os.path.join(base_path, '..', '.travis.yml'))

# Loading board list based on TRAVIS_BOARDS env variable on .travis.yml
travis_boards = []
with open(travis_path, 'r') as travis:

    # Get all lines that contain the substring 'TRAVIS_BOARDS'
    for line in travis:

        # Get the lines with TRAVIS_BOARDS= in it
        if line.find('TRAVIS_BOARDS=') is not -1:
            # Store all the boards names into travis_boards
            begin_of_names = line.find('TRAVIS_BOARDS=') + len('TRAVIS_BOARDS=') + 1
            end_of_names = line.rfind('"')
            boards = line[begin_of_names:end_of_names]
            boards = boards.split(' ')
            travis_boards.extend(boards)

        # We've reached the end of the env: section
        elif 'addons' in line:
            break
        else:
            pass

# TODO (Carlos) Comparing boards listed in TRAVIS_BOARDS and boards got from get_board_mapping

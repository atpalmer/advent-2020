from argparse import ArgumentParser
import os
import sys
from . import main


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--file', default='input.txt')
    parser.add_argument('--part', type=int, required=True)
    return parser.parse_args()


def get_filepath(currfile, filename):
    currdir = os.path.dirname(os.path.realpath(currfile))
    return os.path.join(currdir, 'data', filename)


args = parse_args()


func = getattr(main, f'part{args.part}')
func(filepath=get_filepath(__file__, args.file))

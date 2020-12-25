from argparse import ArgumentParser
import os


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--file', default='input.txt')
    parser.add_argument('--part', type=int, required=True)
    return parser.parse_args()


def get_datapath(currfile, filename):
    currdir = os.path.dirname(os.path.realpath(currfile))
    return os.path.join(currdir, 'data', filename)


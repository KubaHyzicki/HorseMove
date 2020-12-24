#!/usr/bin/env python3

import argparse
import logging

from src.horsemove import HorseMove

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', '-v', action = 'store_true', required = False, help = 'Sets logging type to DEBUG')

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        # logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
        # logging.getLogger().setLevel(logging.INFO)

    horsemove = HorseMove()

if __name__ == "__main__":
    main()

#!/usr/bin/env python

import argparse
from SportsML import SportsMLParser

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Load SportsML instance file')
    parser.add_argument('filename', help='file to be loaded')
    args = parser.parse_args()

    parser = SportsMLParser(args.filename)

    print(parser.getSportsContent().to_json())

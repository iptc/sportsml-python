# SportsML - Python implementation of the SportsML and SportsJS standards

SportsML is an open standard created by the International Press
Telecommunications Council to share sports data.

This module is a part-implementation of the protocol in Python. Currently it
implements ...

Currently built for Python 3 only - please let us know if you require Python 2
support.

## Installation

Installing from PyPI (doesn't work yet!):

    pip install sportsml

## Usage

Example:

    import sportsml

    parser = SportsMLParser("sportsml-file.xml")

    print(parser.getSportsContent().to_json())


## Release notes

* 0.1 - First release, pinned to Python 3 only (use pip >9.0 to ensure pip Python version requirement works properly)

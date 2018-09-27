# SportsML - Python implementation of the SportsML and SportsJS standards

SportsML is an open standard created by the International Press
Telecommunications Council to share sports data.

This module is a part-implementation of the protocol in Python. Currently it
implements actions, entities (players, officials, teams) and some sports
metadata objects.

Work in progress.

Currently built for Python 3 only - please let us know if you require Python 2
support.

## Installation

Installing from PyPI (after we release it to PyPI...):

    pip install sportsml

## Usage

Example:

    import sportsml

    parser = SportsMLParser("sportsml-file.xml")

    print(parser.getSportsContent().to_json())

## Tools

So far we have included one sample tool, a simple parser that converts an XML
representation of SportsML to the JSON equivalent.

Use it from the command line as follows:

    $ tools/parser.py examples/xml/rugby-match-classic-generic-3.0.xml

## Release notes

* 0.1 - First release, pinned to Python 3 only (use pip >9.0 to ensure pip's
Python version requirement works properly)

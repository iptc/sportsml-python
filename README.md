# SportsML - Python implementation of the SportsML and SportsJS standards

SportsML is an open standard created by the International Press
Telecommunications Council to share sports data. See http://www.sportsml.org/

This module is a part-implementation of the standard in Python. Currently it
reads actions, entities (players, officials, teams) and some sports
metadata objects from SportsML XML files and outputs Python objects or JSON.

Work in progress.

Currently built for Python 3 only - please let us know if you require Python 2
support.

## Installation

Installing from PyPI (after we release it to PyPI...):

    pip install sportsml

## Usage

Example:

    import sportsml

    parser = sportsml.SportsMLParser("sportsml-file.xml")

    print(parser.getSportsContent().to_json())

    parser2 = sportsml.SportsMLParser("""
        <?xml version="1.0"?>
        <sports-content xmlns="http://iptc.org/std/nar/2006-10-01/">
          <sports-metadata date-time="2015-02-02T00:35:00-05:00" doc-id="xt.22956338-box" language="en-US" fixture-key="spfixt:event-stats" document-class="spct:event-summary">
            <catalogRef href="http://www.iptc.org/std/catalog/catalog.IPTC-Sports_1.xml"/>
          </sports-metadata>
          <sports-event>
            <event-metadata key="vendevent:l.nfl.com-2014-e.4481" temporal-unit-value="vendor:l.nfl.com-2014-e.4481" event-status="speventstatus:post-event" duration="PT3H36M" start-date-time="2015-02-01T18:30:00-05:00">
              <sports-content-codes/>
            </event-metadata>
          </sports-event>
        </sports-content>
    """)

    print(parser2.getSportsContent().to_json())

## Testing

A very small unit test library is included.

Run it with:

    python setup.py test

## Tools

So far we have included one sample tool, a simple parser that converts an XML
representation of SportsML to the JSON equivalent using the main `SportsMLParser` class.

Use it from the command line as follows:

    $ tools/parser.py examples/xml/rugby-match-classic-generic-3.0.xml

We have also included an extremely simple shell script that runs the above tool over
the included SportsML XML files
([examples taken from the SportsML repository](https://github.com/iptc/sportsml-3/tree/develop/3.0/examples) saved in `examples/xml`)
and generates the corresponding SportsJS JSON files.

    $ tools/convert-all-xml-to-json.sh

The converted files are available in the `examples/json` folder. They should all validate against the
[SportsJS JSON Schema](https://github.com/iptc/sportsjs-dev/tree/develop/specification)
(but they don't right now - that's probably due to bugs in the SportsJS JSON Schema which is
currently under development).

## Release notes

* 0.1 - First release, pinned to Python 3 only (use pip >9.0 to ensure pip's
Python version requirement works properly)

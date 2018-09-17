#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes
from .entities import Teams, Players, Officials


class Tournaments(object):
    tournaments = []
    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                tournament = Tournament(xmlelement)
                self.tournaments.append(tournament)

    def as_dict(self):
        return self.tournaments

    def __bool__(self):
        return len(self.tournaments) != 0


class Tournament(object):
    # TODO
    pass



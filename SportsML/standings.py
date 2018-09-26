#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata


class Standings(object):
    standings = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                standing = Standings(xmlelement)
                self.standings.append(standing)

    def as_dict(self):
        return self.standings

    def __bool__(self):
        return len(self.standings) != 0


class Standing(object):
    # TODO
    pass



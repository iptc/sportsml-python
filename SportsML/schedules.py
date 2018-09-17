#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes


class Schedules(object):
    schedules = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                schedule = Schedule(xmlelement)
                self.schedules.append(schedule)

    def as_dict(self):
        return self.schedules

    def __bool__(self):
        return len(self.schedules) != 0

class Schedule(object):
    pass



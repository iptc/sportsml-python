#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS


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



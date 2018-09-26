#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray


class Schedule(object):
    # TODO
    pass


class Schedules(GenericArray):
    """
    Array of Schedule objects.
    """
    element_class= Schedule

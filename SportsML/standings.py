#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata


class Standing(object):
    # TODO
    pass


class Standings(GenericArray):
    """
    Array of Standing objects.
    """
    element_class= Standing

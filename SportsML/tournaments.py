#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray


class Tournament(object):
    # TODO
    pass


class Tournaments(GenericArray):
    """
    Array of Tournament objects.
    """
    element_class= Tournament

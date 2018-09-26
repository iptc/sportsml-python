#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata


class Articles(GenericArray):
    """
    Array of Article objects.
    """
    element_module_name = __name__
    element_class_name = 'Article'


class Article(object):
    pass



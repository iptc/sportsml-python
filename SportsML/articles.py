#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes


class Articles(object):
    articles = []
    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                article = Article(xmlelement)
                self.articles.append(article)

    def as_dict(self):
        return self.articles

    def __bool__(self):
        return len(self.articles) != 0

class Article(object):
    pass



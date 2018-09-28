#!/usr/bin/env python

import xml.etree.ElementTree as etree

from .core import NEWSMLG2_NS, NITF_NS
from .sports_content import SportsContent

class SportsMLParser(object):
    _root_element = None
    header = None
    order = None

    def __init__(self, filename):
        if type(filename) == str:
            tree = etree.parse(filename)
            self._root_element = tree.getroot()
            self.sports_content = SportsContent(
                xmlelement = self._root_element
            )
        else:
            raise Exception("filename should be a string")

    def getSportsContent(self):
        return self.sports_content

    def get_order(self):
        return self.order

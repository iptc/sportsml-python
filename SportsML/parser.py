#!/usr/bin/env python

import xml.etree.ElementTree as etree

from .core import NEWSMLG2_NS, NITF_NS
from .sports_content import SportsContent

class SportsMLParser(object):
    _root_element = None
    header = None
    order = None

    def __init__(self, param):
        if type(param) == str:
            tree = None
            try:
                tree = etree.parse(param)
                self._root_element = tree.getroot()
            except IOError:
                self._root_element = etree.fromstring(param)
            if self._root_element.tag == NEWSMLG2_NS+'newsItem':
                # it's a NewsML-G2 item, look for SportsContent inside of it
                sportsml_top_element = self._root_element.find(
                    ".//"+NEWSMLG2_NS+"sports-content"
                )
            elif self._root_element.tag == NEWSMLG2_NS+'sports-content':
                sportsml_top_element = self._root_element
            else:
                raise Exception(
                    filename +
                    " doesn't seem to be a valid NewsML-G2 or SportsML-G2 document."
                )
            self.sports_content = SportsContent(
                xmlelement = sportsml_top_element
            )
        else:
            raise Exception("filename should be a string")

    def getSportsContent(self):
        return self.sports_content

    def get_order(self):
        return self.order

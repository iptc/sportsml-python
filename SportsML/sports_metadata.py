#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS


class SportsMetadata(object):
    """
  <sports-metadata date-time="2015-02-02T00:35:00-05:00" doc-id="xt.22956338-box" language="en-US" fixture-key="spfixt:event-stats" document-class="spct:event-summary">
    <sports-content-codes>
      <sports-content-code code-name="The Sports Network" code-key="publisher:sportsnetwork.com" code-type="spct:publisher"/>
      <sports-content-code code-name="XML Team Solutions, Inc." code-key="distributor:xmlteam.com" code-type="spct:distributor"/>
      <sports-content-code code-type="spct:sport" code-key="sport:15003000" code-name="American Football"/>
      <sports-content-code code-type="spct:league" code-key="vendleague:l.nfl.com" code-name="National Football League"/>
      <sports-content-code code-type="spct:season-type" code-key="season-type:post-season"/>
      <sports-content-code code-type="spct:season" code-key="season:2014"/>
      <sports-content-code code-type="spct:priority" code-key="priority:normal"/>
      <sports-content-code code-type="spct:conference" code-key="vendconf:c.afc" code-name="American"/>
      <sports-content-code code-type="spct:conference" code-key="vendconf:c.nfc" code-name="National"/>
      <sports-content-code code-type="spct:team" code-key="vendteam:l.nfl.com-t.16" code-name="Seattle Seahawks"/>
      <sports-content-code code-type="spct:team" code-key="vendteam:l.nfl.com-t.4" code-name="New England Patriots"/>
    </sports-content-codes>
    <catalogRef href="http://www.iptc.org/std/catalog/catalog.IPTC-G2-Standards_27.xml"/>
    <catalogRef href="http://www.iptc.org/std/catalog/catalog.IPTC-Sports_1.xml"/>
  </sports-metadata>
    """
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.date_time = xmlelement.attrib['date-time']
            self.doc_id = xmlelement.attrib['doc-id']
            self.language = xmlelement.attrib['language']
            self.fixture_key = xmlelement.attrib['fixture-key']
            self.document_class = xmlelement.attrib['document-class']
            self.sports_metadata = SportsMetadata(
                xmlelement.find(NEWSMLG2_NS+'sports-metadata')
            )
        elif kwargs:
            if 'sports_metadata' in kwargs:
                self.set_sports_metadata(kwargs['sports_metadata'])

    def set_sports_metadata(self, sports_metadata):
        self.sports_metadata = sports_metadata

    def __str__(self):
        return (
            '<SportsContent>'
        )

    def as_dict(self):
        return {
            'aa': 'bb'
        }

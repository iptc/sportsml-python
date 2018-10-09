#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Copyright (c) 2018, Brendan Quinn, IPTC
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
SportsML/SportsJS Python library - unit tests 

"""

import unittest
import SportsML

class TestStringMethods(unittest.TestCase):

    def test_parse_from_string(self):
        parser2 = SportsML.SportsMLParser("""<?xml version="1.0"?>
        <sports-content xmlns="http://iptc.org/std/nar/2006-10-01/">
          <sports-metadata date-time="2015-02-02T00:35:00-05:00" doc-id="xt.22956338-box" language="en-US" fixture-key="spfixt:event-stats" document-class="spct:event-summary">
            <catalogRef href="http://www.iptc.org/std/catalog/catalog.IPTC-Sports_1.xml"/>
          </sports-metadata>
          <sports-event>
            <event-metadata key="vendevent:l.nfl.com-2014-e.4481" temporal-unit-value="vendor:l.nfl.com-2014-e.4481" event-status="speventstatus:post-event" duration="PT3H36M" start-date-time="2015-02-01T18:30:00-05:00">
              <sports-content-codes/>
            </event-metadata>
          </sports-event>
        </sports-content>
        """)

        json = parser2.getSportsContent().to_json()
        self.assertEqual(json, """{
    "sportsMetadata": {
        "docId": "xt.22956338-box",
        "dateTime": "2015-02-02T00:35:00-05:00",
        "language": "en-US",
        "documentClass": "spct:event-summary",
        "fixtureKey": "spfixt:event-stats",
        "catalogRefs": [
            {
                "href": "http://www.iptc.org/std/catalog/catalog.IPTC-Sports_1.xml"
            }
        ]
    },
    "sportsEvents": [
        {
            "eventMetadata": {
                "startDateTime": "2015-02-01T18:30:00-05:00",
                "temporalUnitValue": "vendor:l.nfl.com-2014-e.4481",
                "key": "vendevent:l.nfl.com-2014-e.4481",
                "eventStatus": "speventstatus:post-event",
                "duration": "PT3H36M"
            }
        }
    ]
}""")

if __name__ == '__main__':
    unittest.main()

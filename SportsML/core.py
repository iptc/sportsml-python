#!/usr/bin/env python

NEWSMLG2_NS = '{http://iptc.org/std/nar/2006-10-01/}'
NITF_NS = '{http://iptc.org/std/NITF/2006-10-18/}'

VERSION = 0.1

class BaseObject():
    # required for multiple inheritance to work propertly.
    # probably helpful in the future for other objects too.
    def __init__(self, **kwargs):
        pass

    def as_dict(self):
        return

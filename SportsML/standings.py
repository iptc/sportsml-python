#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray, BaseObject
from .base_metadata import BaseMetadata, CommonAttributes
from .entities import Players, Teams


class StandingMetadata(BaseMetadata):
    """
    A series of team or individual records.
    """
    pass  # inherits everything it needs from BaseMetadata


class Standing(CommonAttributes):
    """
    Also known as a (league) table
    A ranked, comparative list of team or individual records.
    """
    standing_metadata = None
    teams = None
    players = None
    attributes = {
        # A displayable label describing this standing.
        'content-label': 'contentLabel'
    }

    def __init__(self, **kwargs):
        super(Standing, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.teams = Teams(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'team')
            )
            self.players = Standings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'players')
            )

    def as_dict(self):
        super(Standing, self).as_dict()
        self.dict.update({'teams': self.teams.as_dict() })
        self.dict.update({'players': self.players.as_dict() })
        return self.dict


class Standings(GenericArray):
    """
    Array of Standing objects.
    """
    element_class= Standing

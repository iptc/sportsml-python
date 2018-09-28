#!/usr/bin/env python

import xml.etree.ElementTree as etree
import importlib
import json

from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes
from .entities import Teams, Players, Officials
from .actions import Actions
from .statistics import WageringStatsSet


class SportsEvent(BaseObject):
    event_metadata = None
    event_stats_set = None
    teams = None
    players = None
    wagering_stats = None
    officials = None
    highlights = None
    awards = None
    sports_events = None

    def __init__(self,  **kwargs):
        super(SportsEvent, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.event_metadata = EventMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'event-metadata')
            )
            self.event_stats = EventStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'event-stats')
            )
            self.teams = Teams(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'team')
            )
            self.players = Players(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'player')
            )
            # wagering-stats, maxOccurs unbounded
            self.wagering_stats_set = WageringStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            # officials, maxOccurs 1
            self.officials = Officials(
                xmlarray = xmlelement.find(NEWSMLG2_NS+'officials')
            )
            # actions, maxOccurs 1
            self.actions = Actions(
                xmlarray = xmlelement.find(NEWSMLG2_NS+'actions')
            )
            # highlights, maxOccurs unbounded
            self.highlights = Highlights(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'highlight')
            )
            # award, maxOccurs unbounded
            self.awards = Awards(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'award')
            )
            self.sports_events = SportsEvents(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )
        elif kwargs:
            if 'event_metadata' in kwargs:
                self.set_event_metadata(kwargs['event_metadata'])
            if 'event_stats' in kwargs:
                self.set_event_stats(kwargs['event_stats'])
            if 'teams' in kwargs:
                self.set_teams(kwargs['teams'])
            if 'players' in kwargs:
                self.set_players(kwargs['players'])
            if 'wagering_stats_set' in kwargs:
                self.set_wagering_stats(kwargs['wagering_stats'])
            if 'officials' in kwargs:
                self.set_officials(kwargs['officials'])
            if 'actions' in kwargs:
                self.set_actions(kwargs['actions'])
            if 'highlights' in kwargs:
                self.set_highlights(kwargs['highlights'])
            if 'awards' in kwargs:
                self.set_awards(kwargs['awards'])
            if 'sports_events' in kwargs:
                self.set_awards(kwargs['sports_events'])

    def __str__(self):
        return (
            '<SportsEvent>'
        )

    def as_dict(self):
        dict = {}
        if self.event_metadata:
            dict.update({
                'eventMetadata': self.event_metadata.as_dict()
            })
        if self.event_stats_set:
            dict.update({
                'eventStats': self.event_stats_set.as_dict(),
            })
        if self.teams:
            dict.update({
                'teams': self.teams.as_dict(),
            })
        if self.players:
            dict.update({
                'players': self.players.as_dict(),
            })
        if self.wagering_stats_set:
            dict.update({
                'wageringStats': self.wagering_stats_set.as_dict(),
            })
        if self.officials:
            dict.update({
                'officials': self.officials.as_dict(),
            })
        if self.actions:
            dict.update({
                'actions': self.actions.as_dict(),
            })
        if self.highlights:
            dict.update({
                'highlights': self.highlights.as_dict(),
            })
        if self.awards:
            dict.update({
                'awards': self.awards.as_dict(),
            })
        # FIXME we get recursion errors if this is left in... 
        # what am I doing wrong??
        #if self.sports_events:
        #    dict.update({
        #        'sportsEvents': self.sports_events.as_dict(),
        #    })
        return dict

    def default(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.as_dict(), indent=4)


class SportsEvents(GenericArray):
    """
    Array of SportsEvent objects.
    """
    element_class = SportsEvent


class EventStats(CommonAttributes, CoverageAttributes):
    """
    Stats applying to the game as a whole. Initially designed for motor-racing, but potentially applicable to many sports.
    """
    sports_properties = None

    def __init__(self, **kwargs):
        super(SportsEvent, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sports_properties = SportsProperties(
                xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.event_stats_motor_racing = EventStatsMotorRacing(
                xmlelement.findall(NEWSMLG2_NS+'event-stats-motor-racing')
            )


class EventStatsSet(GenericArray):
    """
    Array of EventStats objects.
    """
    element_class= EventStats


class Highlight(BaseObject):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Highlights(GenericArray):
    """
    Array of Highlight objects.
    """
    element_class= Highlight


class Award(BaseObject):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Awards(GenericArray):
    """
    Array of Award objects.
    """
    element_class= Award

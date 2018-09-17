#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes
from .entities import Teams, Players, Officials
from .actions import Actions
from .statistics import WageringStats

class SportsEvents(object):
    """
    Array of SportsEvent objects.
    """
    sports_events = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                sports_event = SportsEvent(xmlelement)
                self.sports_events.append(sports_event)

    def __str__(self):
        return (
            '<SportsContent>'
        )

    def as_dict(self):
        return [ se.as_dict() for se in self.sports_events ]

    def to_json(self):
        return json.dumps(self.as_dict(), indent=4)


# class SportsEvent(object):
class SportsEvent(json.JSONEncoder):
    event_metadata = None
    event_stats_set = None
    teams = None
    players = None
    wagering_stats = None
    officials = None
    highlights = None
    awards = None
    sports_events = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.event_metadata = EventMetadata(
                xmlelement.find(NEWSMLG2_NS+'event-metadata')
            )
            self.event_stats = EventStatsSet(
                xmlelement.findall(NEWSMLG2_NS+'event-stats')
            )
            self.teams = Teams(
                xmlelement.findall(NEWSMLG2_NS+'team')
            )
            self.players = Players(
                xmlelement.findall(NEWSMLG2_NS+'player')
            )
            self.wagering_stats = WageringStats(
                xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            self.officials = Officials(
                xmlelement.find(NEWSMLG2_NS+'officials')
            )
            self.actions = Actions(
                xmlelement.findall(NEWSMLG2_NS+'actions')
            )
            self.highlights = Highlights(
                xmlelement.findall(NEWSMLG2_NS+'highlights')
            )
            self.awards = Awards(
                xmlelement.findall(NEWSMLG2_NS+'awards')
            )
            self.sports_events = SportsEvents(
                xmlelement.findall(NEWSMLG2_NS+'sports-event')
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
            if 'wagering_stats' in kwargs:
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
        if self.wagering_stats:
            dict.update({
                'wageringStats': self.wagering_stats.as_dict(),
            })
        if self.officials:
            dict.update({
                'officials': self.officials.as_dict(),
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


class EventStatsSet(object):
    event_stats_set = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                event_stats = EventStats(xmlelement)
                self.event_stats_set.append(event_stats)

    def as_dict(self):
        return [es.as_dict() for es in event_stats_set]

class EventStats(CommonAttributes, CoverageAttributes):
    """
    Stats applying to the game as a whole. Initially designed for motor-racing, but potentially applicable to many sports.
    """
    sports_properties = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.sports_properties = SportsProperties(
                xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.event_stats_motor_racing = EventStatsMotorRacing(
                xmlelement.findall(NEWSMLG2_NS+'event-stats-motor-racing')
            )


class Highlights(object):
    highlights = []

    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                highlight = Highlight(xmlelement)
                self.highlights.append(highlight)

    def as_dict(self):
        return [h.as_dict() for h in self.highlights]

    def __bool__(self):
        return len(self.highlights) != 0


class Highlight(object):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Awards(object):
    awards = []
    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                award = Award(xmlelement)
                self.awards.append(award)

    def as_dict(self):
        return self.awards

    def __bool__(self):
        return len(self.awards) != 0


class Award(object):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None

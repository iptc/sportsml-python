#!/usr/bin/env python

import json
import xml.etree.ElementTree as etree

from .core import NEWSMLG2_NS
from .articles import Articles
from .sports_metadata import SportsMetadata
from .sports_events import SportsEvents
from .schedules import Schedules
from .standings import Standings
from .statistics import Statistics
from .tournaments import Tournaments

class SportsContent(object):
    """
    The root element of all SportsML documents.
    """
    sports_metadata = None
    sports_events = None
    tournaments = None
    schedules = None
    standings = None
    statistics = None
    articles = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.sports_metadata = SportsMetadata(
                xmlelement.find(NEWSMLG2_NS+'sports-metadata')
            )
            self.sports_events = SportsEvents(
                xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )
            self.tournaments = Tournaments(
                xmlelement.findall(NEWSMLG2_NS+'tournament')
            )
            self.schedules = Schedules(
                xmlelement.findall(NEWSMLG2_NS+'schedule')
            )
            self.standings = Standings(
                xmlelement.findall(NEWSMLG2_NS+'standing')
            )
            self.statistics = Statistics(
                xmlelement.findall(NEWSMLG2_NS+'statistic')
            )
            self.articles = Articles(
                xmlelement.findall(NEWSMLG2_NS+'article')
            )
        elif kwargs:
            if 'sports_metadata' in kwargs:
                self.set_sports_metadata(kwargs['sports_metadata'])
            if 'sports_events' in kwargs:
                self.set_sports_events(kwargs['sports_events'])
            if 'tournaments' in kwargs:
                self.set_tournaments(kwargs['tournaments'])
            if 'schedules' in kwargs:
                self.set_schedules(kwargs['schedules'])
            if 'standings' in kwargs:
                self.set_standings(kwargs['standings'])
            if 'statistics' in kwargs:
                self.set_statistics(kwargs['statistics'])
            if 'articles' in kwargs:
                self.set_articles(kwargs['articles'])

    def set_sports_metadata(self, sports_metadata):
        self.sports_metadata = sports_metadata

    def set_sports_events(self, sports_events):
        self.sports_events = sports_events

    def set_tournaments(self, tournaments):
        self.tournaments = tournaments

    def set_schedules(self, schedules):
        self.schedules = schedules

    def set_standings(self, standings):
        self.standings = standings

    def set_statistics(self, statistics):
        self.statistics = statistics

    def set_articles(self, articles):
        self.articles = articles

    def __str__(self):
        return (
            '<SportsContent>'
        )

    def as_dict(self):
        dict = {}
        if self.sports_metadata:
            dict.update({ 'sportsMetadata': self.sports_metadata.as_dict() })
        if self.sports_events:
            dict.update({ 'sportsEvents': self.sports_events.as_dict() })
        if self.tournaments:
            dict.update({ 'tournaments': self.tournaments.as_dict() })
        if self.schedules:
            dict.update({ 'schedules': self.schedules.as_dict() })
        if self.standings:
            dict.update({ 'standings': self.standings.as_dict() })
        if self.statistics:
            dict.update({ 'statistics': self.statistics.as_dict() })
        if self.articles:
            dict.update({ 'articles': self.articles.as_dict() })
        return dict

    def to_json(self):
        return json.dumps(self.as_dict(), indent=4)

#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes
# from .entities import Teams, Players, Officials


class Statistics(object):
    statistics = []
    def __init__(self, xmlarray=None, **kwargs):
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                statistic = Statistic(xmlelement)
                self.statistics.append(statistic)

    def as_dict(self):
        return self.statistics

    def __bool__(self):
        return len(self.statistics) != 0


class Statistic(object):
    pass


class BaseStats(CommonAttributes):
    """
    The very basic stats type for persons and teams.
    Extended by base2stats and used directly by officalstats.
    """
    ratings = None
    sportsProperties = None
    stats = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def __bool__(self):
        return (self.ratings or self.sportsProperties or self.stats) is not None


class GenericStats():
    pass

class OfficialStats(BaseStats):
    # inherits everything from BaseStats
    pass

class TeamStatsSet(object):
    team_stats_set = None

    def __init__(self, xmlarray=None, **kwargs):
        self.team_stats_set = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                team_stats = TeamStats(xmlelement)
                self.team_stats_set.append(team_stats)

    def as_dict(self):
        return [ts.as_dict() for ts in self.team_stats_set]

    def __bool__(self):
        return len(self.team_stats_set) != 0


class TeamStats(object):
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None


class PlayerStatsSet(object):
    player_stats_set = None

    def __init__(self, xmlarray=None, **kwargs):
        self.player_stats_set = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                player_stats = PlayerStats(xmlelement)
                self.player_stats_set.append(player_stats)

    def as_dict(self):
        return [ts.as_dict() for ts in self.player_stats_set]

    def __bool__(self):
        return len(self.player_stats_set) != 0


class PlayerStats(object):
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None


class WageringStatsSet(object):
    wagering_stats_set = None

    def __init__(self, xmlarray=None, **kwargs):
        self.wagering_stats_set = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                wagering_stats = WageringStats(xmlelement)
                self.wagering_stats_set.append(wagering_stats)

    def as_dict(self):
        return [wss.as_dict() for wss in self.wagering_stats_set]

    def __bool__(self):
        return len(self.wagering_stats_set) != 0


class WageringStats(object):
    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        # TODO
        return None



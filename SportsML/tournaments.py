#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json
from .core import NEWSMLG2_NS, GenericArray, BaseObject
from .base_metadata import CommonAttributes, Base2Metadata
from .sports_events import SportsEvents
from .standings import Standings


class TournamentAttributes(BaseObject):
    """
    Attributes that are used in all tournament constructions.
    """
    attributes = {
        # The state of the tournament or tournament part, describing whether it has started,
        # is in progress, etc.
        'status': 'status',
        # The minimum number of subparts for this level in a tournament.
        # The subparts can either be tournament-part or sports-event.
        'minimum-subparts': 'minimumSubparts',
        # The maximum number of subparts for this level in a tournament.
        # The subparts can either be tournament-part or sports-event.
        'maximum-subparts': 'maximumSubparts',
        # The number of the particular tournament part eg. 2 for second round or second leg
        'number': 'number',
    }


class BaseTournamentMetadata(Base2Metadata, TournamentAttributes):
    """
    Background data about a tournament or tournament part.
    Where and when the this tournament took place.
    """
    pass # inherits everything it needs from parents


class TournamentMetadata(BaseTournamentMetadata):
    """
    Background data about a tournament.
    Where and when the this tournament took place.

    TODO:
    <xs:element name="tournament-metadata-golf" type="golfTournamentMetadataComplexType"/>
    <xs:element name="tournament-metadata-tennis" type="tennisTournamentMetadataComplexType"/>
    """
    pass

class TournamentDivisionMetadata(BaseTournamentMetadata):
    """
    General information about the division of this tournament.
    Where and when this division is competing.

    TODO:
    <xs:element name="tournament-division-metadata-golf" type="golfTournamentDivisionMetadataComplexType"/>
    """
    attributes = {
        # The number of the division.
        'division-number': 'divisionNumber'
    }


class TournamentDivision(CommonAttributes):
    """
    A tournament subcategory, often with its own trophy and prize.
    Use it to divide specific overall competitions in a large multi-sport tournament such as
    Olympics. Can also divide gender competitions, for example in tennis tournaments.
    Can be nested to divide gender at a higher level (tournament/tournament-division)
    and then to divide specific sport competitions futher down the tree
    (tournament-part/tournament-division).
    """
    tournament_division_metadata = None
    standings = None
    tournament_parts = None
    sports_events = None

    def __init__(self, **kwargs):
        super(TournamentDivision, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.tournament_division_metadata = TournamentDivisionMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'tournament-division-metadata')
            )
            self.standings = Standings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'standing')
            )
            self.tournament_parts = TournamentParts(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'tournament-part')
            )
            self.sports_events = SportsEvents(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )

    def as_dict(self):
        super(TournamentDivision, self).as_dict()
        if self.tournament_division_metadata:
            self.dict.update({'tournamentDivisionMetadata': self.tournament_division_metadata.as_dict() })
        if self.standings:
            self.dict.update({'standings': self.standings.as_dict() })
        if self.tournament_parts:
            self.dict.update({'tournamentParts': self.tournament_parts.as_dict() })
        if self.sports_events:
            self.dict.update({'sportsEvents': self.sports_events.as_dict() })
        return self.dict


class TournamentPartMetadata(BaseTournamentMetadata):
    """
    General information about the division of this tournament.
    Where and when this division is competing.
    """
    attributes = {
        # The phase of the tournament: semi-final, quarter-final, etc.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/sptournamentphase/
        'type': 'type',
        # The format type of tournament or tournament phase: group, elimination, etc.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/sptournamentform/
        'format-type': 'formatType'
    }


class TournamentPart(CommonAttributes):
    """
    A tournament part. Use it do group specific parts of a tournament, like a stage or a round.
    """
    tournament_part_metadata = None
    standings = None
    tournament_parts = None
    sports_events = None

    attributes = {
        # For provider-specific tournament indexing systems. DPA, for
        # example, has one that looks like this: part-name="Group A"
        # part-index="p1/1/p2/A"
        'part-index': 'partIndex'
    }

    def __init__(self, **kwargs):
        super(TournamentPart, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.tournament_part_metadata = TournamentPartMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'tournament-part-metadata')
            )
            self.standings = Standings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'standings')
            )
            self.tournament_parts = TournamentParts(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'tournament-part')
            )
            self.sports_events = SportsEvents(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )

    def as_dict(self):
        super(TournamentPart, self).as_dict()
        if self.tournament_part_metadata:
            self.dict.update({'tournamentPartMetadata': self.tournament_part_metadata.as_dict() })
        if self.standings:
            self.dict.update({'standings': self.standings.as_dict() })
        if self.tournament_parts:
            self.dict.update({'tournamentParts': self.tournament_parts.as_dict() })
        if self.sports_events:
            self.dict.update({'sportsEvents': self.sports_events.as_dict() })
        return self.dict


class TournamentParts(GenericArray):
    element_class = TournamentPart


class TournamentDivisions(GenericArray):
    element_class = TournamentDivision


class Tournament(CommonAttributes):
    """
    A structured series of competitions within one sport.
    Generally organized by a particular sponsoring body.
    Can happen all in one day, or be spread out - like the Davis Cup in tennis.
    """

    tournament_metadata = None
    standings = None
    # should have only one of the below three, but we don't enforce that here
    tournament_divisions = None
    tournament_parts = None
    sports_events = None

    def __init__(self, **kwargs):
        super(Tournament, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.tournament_metadata = TournamentMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'tournament-metadata')
            )
            self.standings = Standings(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'standing')
            )
            self.tournament_divisions = TournamentDivisions(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'tournament-division')
            )
            self.tournament_parts = TournamentParts(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'tournament-part')
            )
            self.sports_events = SportsEvents(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )

    def as_dict(self):
        super(Tournament, self).as_dict()
        if self.tournament_metadata:
            self.dict.update({'tournamentMetadata': self.tournament_metadata.as_dict() })
        if self.standings:
            self.dict.update({'standings': self.standings.as_dict() })
        if self.tournament_divisions:
            self.dict.update({'tournamentDivisions': self.tournament_divisions.as_dict() })
        if self.tournament_parts:
            self.dict.update({'tournamentParts': self.tournament_parts.as_dict() })
        if self.sports_events:
            self.dict.update({'sportsEvents': self.sports_events.as_dict() })
        return self.dict


class Tournaments(GenericArray):
    """
    Array of Tournament objects.
    """
    element_class = Tournament

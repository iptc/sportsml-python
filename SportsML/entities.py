#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes, Sites, SportsContentCodes, SportsProperties
from .newsmlg2 import ConceptNameType, FlexLocationPropType
from .statistics import TeamStatsSet, PlayerStatsSet, WageringStatsSet, OfficialStats


class Teams(object):
    """
    Array of Team objects.
    """

    def __init__(self, xmlarray=None, **kwargs):
        self.teams = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                team = Team(xmlelement)
                self.teams.append(team)

    def __str__(self):
        return (
            '<Teams>'
        )

    def as_dict(self):
        return [ team.as_dict() for team in self.teams ]

    def to_json(self):
        return json.dumps(self.as_dict(), indent=4)


class Team(CommonAttributes):
    """
    A team participating in a sporting event. 
    Holds metadata and statistical data for team.
    """
    team_metadata = None
    team_stats_set = None
    players = None
    wagering_stats_set = None
    associates = None
    affiliations = None

    def __init__(self, xmlelement=None, **kwargs):
        super(Team, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.team_metadata = TeamMetadata(
                xmlelement.find(NEWSMLG2_NS+'team-metadata')
            )
            self.team_stats_set = TeamStatsSet(
                xmlelement.findall(NEWSMLG2_NS+'team-stats')
            )
            self.players = Players(
                xmlelement.findall(NEWSMLG2_NS+'player')
            )
            self.wagering_stats_set = WageringStatsSet(
                xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            self.associates = Associates(
                xmlelement.findall(NEWSMLG2_NS+'associate')
            )
            self.affiliations = Affiliations(
                xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        obj = super(Team, self).as_dict()
        if self.team_metadata:
            obj.update({
                'teamMetadata': self.team_metadata.as_dict()
            })
        if self.team_stats_set:
            obj.update({
                'teamStats': self.team_stats_set.as_dict()
            })
        if self.players:
            obj.update({
                'players': self.players.as_dict()
            })
        if self.wagering_stats_set:
            obj.update({
                'wageringStatsSet': self.wagering_stats_set.as_dict()
            })
        if self.associates:
            obj.update({
                'associates': self.associates.as_dict()
            })
        if self.affiliations:
            obj.update({
                'affiliations': self.affiliations.as_dict()
            })
        return obj

class BaseEntityMetadata(CommonAttributes):
    """
    Base metadata for different entities.
    Extended by baseTeamMetadata and basePersonMetadata and siteMetadata
    """
    names = None
    home_location = None
    sports_properties = None
    # The symbol or identifying key for the entity.
    key = None
    # The country of citizinship of the entity.
    nationality = None
    
    def __init__(self, xmlelement=None, **kwargs):
        super(BaseEntityMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.names = Names(
                xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.home_location = FlexLocationPropType(
                xmlelement.find(NEWSMLG2_NS+'home-location')
            )
            self.sports_properties = SportsProperties(
                xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.key = xmlelement.get('key')
            self.nationality = xmlelement.get('nationality')

    def as_dict(self):
        dict = super(BaseEntityMetadata, self).as_dict()
        if self.names:
            dict.update({
                'names': self.names.as_dict()
            })
        if self.home_location:
            dict.update({
                'homeLocation': self.home_location.as_dict()
            })
        if self.sports_properties:
            dict.update({
                'sportsProperties': self.sports_properties.as_dict()
            })
        if self.key:
            dict.update({
                'key': self.key
            })
        if self.nationality:
            dict.update({
                'nationality': self.nationality
            })
        return dict


class BaseTeamMetadata(object):
    """
    Info about the team. Properties of a team that are not based on their competitive performance.
    An included sports-content-code element can hold what division it is in, etc.
    """
    sites = None
    sports_content_codes = None
    # Home or visiting. This is more information about the
    # alignment of the team or player in the event regarding rules etc. It
    # does not necessarily indicate that it is the geographical home-site of
    # the team or player.
    # enumeration: home, away, none
    alignment = None
    # Date (and time) when the team was established.
    established = None
    # Date (and time) when the team was dissolved. 
    dissolved = None
    # Optional reference to a team in which this team is a member. Example: The U.S. Davis Cup team consists of many sub-teams.
    team_idref = None
    # The fully-qualified URL for the official home page of the team.
    home_page_url = None
    # The seed or position in this particular round for which this team started. Useful for bracketed tournaments, such as tennis.
    round_position = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.sites = Sites(
                xmlelement.findall(NEWSMLG2_NS+'site')
            )
            self.sports_content_codes = SportsContentCodes(
                xmlelement.findall(NEWSMLG2_NS+'sports-content-code')
            )
            self.alignment = xmlelement.get('alignment')
            self.established = xmlelement.get('established')
            self.dissolved = xmlelement.get('dissolved')
            self.team_idref = xmlelement.get('team_idref')
            self.home_page_url = xmlelement.get('home_page_url')
            self.round_position = xmlelement.get('round-position')

    def as_dict(self):
        dict = {}
        if self.sites:
            dict.update({
                'sites': self.sites.as_dict()
            })
        if self.sports_content_codes:
            dict.update({
                'sportsContentCodes': self.sports_content_codes.as_dict()
            })
        if self.alignment:
            dict.update({
                'alignment': self.alignment
            })
        if self.established:
            dict.update({
                'established': self.established
            })
        if self.dissolved:
            dict.update({
                'dissolved': self.dissolved
            })
        if self.team_idref:
            dict.update({
                'teamIdRef': self.team_idref
            })
        if self.home_page_url:
            dict.update({
                'homePageURL': self.home_page_url
            })
        if self.round_position:
            dict.update({
                'roundPosition': self.round_position
            })
        return dict


class TeamMetadata(BaseTeamMetadata):
    team_metadata_baseball = None
    # Holds metadata about a team (foursome perhaps) playing in the match. | Currently only holds the rank of the team.
    team_metadata_golf = None
    team_metadata_motor_racing = None

    def __init__(self, xmlelement=None, **kwargs):
        super(TeamMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.team_metadata_baseball = TeamMetadataBaseball(
                xmlelement.find(NEWSMLG2_NS+'team-metadata-baseball')
            )
            self.team_metadata_golf = TeamMetadataGolf(
                xmlelement.find(NEWSMLG2_NS+'team-metadata-golf')
            )
            self.team_metadata_motor_racing = TeamMetadataMotorRacing(
                xmlelement.find(NEWSMLG2_NS+'team-metadata-motor-racing')
            )

    def as_dict(self):
        dict = super(TeamMetadata, self).as_dict()
        if self.team_metadata_baseball:
            dict.update({ 'teamMetadataBaseball': self.team_metadata_baseball.as_dict() })
        if self.team_metadata_golf:
            dict.update({ 'teamMetadataGolf': self.team_metadata_golf.as_dict() })
        if self.team_metadata_motor_racing:
            dict.update({ 'teamMetadataMotorRacing': self.team_metadata_motor_racing.as_dict() })
        return dict

class TeamMetadataBaseball(CommonAttributes):
    """
    Metadata about the team.
    Specific to the sport of baseball.
    """
    # ID of the pitcher who will probably start the game.
    probable_starting_pitcher_idref = None

    def __init__(self, xmlelement=None, **kwargs):
        super(TeamMetadataBaseball, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.probable_starting_pitcher_idref = xmlelement.get(
                'probable-starting-pitcher-idref'
            )


class BaseGolfMetadata(CommonAttributes):
    """
    Holds metadata about a golf player. | Currently only holds the rank of the player.
    """
    # How this player ranks among the other competing players.
    rank = None

    def __init__(self, xmlelement=None, **kwargs):
        super(BaseGolfMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.rank = xmlelement.get("rank")

    def as_dict(self):
        dict = super(BaseGolfMetadata, self).as_dict()
        if self.rank:
            dict.update({ 'rank': self.rank })
        return dict

class TeamMetadataGolf(BaseGolfMetadata):
    """
    Holds metadata about a team (foursome perhaps) playing in the match.
    Currently only holds the rank of the team.
    """
    pass


class TeamMetadataMotorRacing(CommonAttributes):
    """
    Metadata about the team.
    Specific to the sport of motor racing.
    """
    motor_racing_vehicles = None
    
    def __init__(self, xmlelement=None, **kwargs):
        super(TeamMetadataMotorRacing, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            motor_racing_vehicles = MotorRacingVehicles(
                xmlelement.findall(NEWSMLG2_NS+'metadata-motor-racing-vehicle')
            )


class MotorRacingVehicles(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.motor_racing_vehicles = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                vehicle = MotorRacingVehicle(xmlelement)
                self.motor_racing_vehicles.append(vehicle)

    def as_dict(self):
        return [mrv.as_dict() for mrv in self.motor_racing_vehicles]


class MotorRacingVehicle(object):
    pass

    def as_dict(self):
        # TODO
        return None


class Players(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.players = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                player = Player(xmlelement)
                self.players.append(player)

    def as_dict(self):
        return [p.as_dict() for p in self.players]


class Player(CommonAttributes):
    """
    A competitor.
    Their athletic talents help them decide who wins a sports-event.
    """
    def __init__(self, xmlelement=None, **kwargs):
        super(Player, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.player_metadata = PlayerMetadata(
                xmlelement.find(NEWSMLG2_NS+'player-metadata')
            )
            self.player_stats_set = PlayerStatsSet(
                xmlelement.findall(NEWSMLG2_NS+'player-stats')
            )
            self.wagering_stats_set = WageringStatsSet(
                xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            self.associates = Associates(
                xmlelement.findall(NEWSMLG2_NS+'associate')
            )
            self.affiliations = Affiliations(
                xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        dict = super(Player, self).as_dict()
        if self.player_metadata:
            dict.update({ 'playerMetadata': self.player_metadata.as_dict() })
        if self.player_stats_set:
            dict.update({ 'playerStats': self.player_stats_set.as_dict() })
        if self.wagering_stats_set:
            dict.update({ 'wageringStats': self.wagering_stats_set.as_dict()})
        if self.associates:
            dict.update({ 'associates': self.associates.as_dict() })
        if self.affiliations:
            dict.update({'affiliations': self.affiliations.as_dict() })
        return dict

class CareerPhaseMetadata(object):
    # TODO

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

class InjuryPhaseMetadata(object):
    # TODO

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            # TODO
            pass

class BasePlayerMetadata(object):
    """
    Metadata that describes a person. | Generally does not change over the course of a sports-events.
    """

    career_phase = None
    injury_phase = None
    # A reference to the team for which this player competes.
    team_idref = None
    # Whether a player starts playing at the beginning of a sports-event, joins mid-game, or is not available to participate.
    status = None
    # The order in which a player participated in an event.
    lineup_slot = None
    # For baseball, cricket, relay races if they substituted for a player in the original lineup, the order in which they served at the above lineup-slot value. Defaults to 1.
    lineup_slot_sequence = None
    # An indication as to why this player did not play in an event.
    scratch_reason = None
    # The number currently displayed on the uniform or jersey of the player.
    uniform_number = None
    # The fully-qualified URL for the official home page of the team.
    home_page_url = None
    # The seed or position in this particular round for which this player started. Useful for bracketed tournaments, such as tennis.
    round_position = None

    def __init__(self, xmlelement=None, **kwargs):
        if type(xmlelement) == etree.Element:
            self.career_phase = CareerPhaseMetadata(
                xmlelement.find(NEWSMLG2_NS+'career-phase')
            )
            self.injury_phase = InjuryPhaseMetadata(
                xmlelement.find(NEWSMLG2_NS+'injury-phase')
            )
            self.team_idref = xmlelement.get('team-idref')
            self.status = xmlelement.get('status')
            self.lineup_slot = xmlelement.get('lineup-slot')
            self.lineup_slot_sequence = xmlelement.get('lineup-slot-sequence')
            self.scratch_reason = xmlelement.get('scratch-reason')
            self.uniform_number = xmlelement.get('uniform-number')
            self.home_page_url = xmlelement.get('home-page-url')
            self.round_position = xmlelement.get('round-position')

    def as_dict(self):
        dict = {}
        if self.career_phase:
            dict.update({ 'careerPhase': self.career_phase })
        if self.injury_phase:
            dict.update({ '': self.injury_phase })
        if self.team_idref:
            dict.update({ 'teamIdRef': self.injury_phase })
        if self.status:
            dict.update({ 'status': self.status })
        if self.lineup_slot:
            dict.update({ 'lineupSlot': self.lineup_slot })
        if self.lineup_slot_sequence:
            dict.update({ 'lineupSlotSequence': self.lineup_slot_sequence })
        if self.scratch_reason:
            dict.update({ 'scratchReason': self.scratch_reason })
        if self.uniform_number:
            dict.update({ 'uniformNumber': self.uniform_number })
        if self.home_page_url:
            dict.update({ 'homePageURL': self.home_page_url })
        if self.round_position:
            dict.update({ 'roundPosition': self.round_position })


class PlayerMetadata(BasePlayerMetadata):
    def __init__(self, xmlelement=None, **kwargs):
        super(PlayerMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            """ TODO
            self.player_metadata_baseball = PlayerMetadataBaseball(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_golf = PlayerMetadataGolf(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_ice-hockey = PlayerMetadataIceHockey(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_soccer = PlayerMetadataSoccer(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_motor_racing = PlayerMetadataMotorRacing(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_curling = PlayerMetadataCurling(
                xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            """

    def as_dict(self):
        dict = super(PlayerMetadata, self).as_dict()
        # TODO
        return dict


class Associates(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.associates = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                associate = Associate(xmlelement)
                self.associates.append(associate)

    def as_dict(self):
        return [a.as_dict() for a in self.associates]

    def __bool__(self):
        return len(self.associates) != 0


class Associate(object):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Affiliations(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.affiliations = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                affiliation = Affiliation(xmlelement)
                self.affiliations.append(affiliation)

    def as_dict(self):
        return [a.as_dict() for a in self.affiliations]

    def __bool__(self):
        return len(self.affiliations) != 0


class Affiliation(object):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class BasePersonMetadata(BaseEntityMetadata):
    """
    Metadata that describes a person.
    Generally does not change over the course of a sports-events. Extends the baseEntityMetadata type
    """
    # The day on which a person was born, normalized to ISO 8601
    # extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time
    # is available. Can also be YYYY-MM or just YYYY if year and/or month not available.
    date_of_birth = None
    # The day on which a person died, normalized to ISO 8601
    # extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available.
    date_of_death = None
    # Height of the person. Generally in cm.
    height = None
    # Weight of a person. Generally in kg.
    weight = None
    # The code for the typical position of the person.
    position_regular = None
    # The code for the position held by the person at this  particular sports-event.
    position_event = None
    # A ranking amongst players on the team who share the same position.
    position_depth = None
    # An indication of the health of the person.
    health = None
    # Male or female.
    gender = None
    
    def __init__(self, xmlelement=None, **kwargs):
        super(BasePersonMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.date_of_birth = xmlelement.get('date-of-birth')
            self.date_of_death = xmlelement.get('date-of-death')
            self.height = xmlelement.get('height')
            self.weight = xmlelement.get('weight')
            self.position_regular = xmlelement.get('position-regular')
            self.position_event = xmlelement.get('position-event')
            self.position_depth = xmlelement.get('position-depth')
            self.health = xmlelement.get('health')
            self.gender = xmlelement.get('gender')

    def as_dict(self):
        dict = super(BasePersonMetadata, self).as_dict()
        if self.date_of_birth:
            dict.update({ 'dateOfBirth': self.date_of_birth })
        if self.date_of_death:
            dict.update({ 'dateOfDeath': self.date_of_death})
        if self.height:
            dict.update({ 'height': self.height })
        if self.weight:
            dict.update({ 'weight': self.weight })
        if self.position_regular:
            dict.update({ 'positionRegular': self.position_regular })
        if self.position_event:
            dict.update({ 'positionEvent': self.position_event })
        if self.position_depth:
            dict.update({ 'positionDepth': self.position_depth })
        if self.health:
            dict.update({ 'health': self.health })
        if self.gender:
            dict.update({ 'gender': self.gender })
        return dict


class Officials(object):
    """
    XML wrapper element for Offical elements.
    """
    def __init__(self, xmlelement=None, **kwargs):
        self.officials = []
        if type(xmlelement) == etree.Element:
            for childelem in xmlelement:
                official = Official(childelem)
                self.officials.append(official)

    def as_dict(self):
        return [o.as_dict() for o in self.officials]

    def __bool__(self):
        return len(self.officials) != 0


class BaseOfficialMetadata(BasePersonMetadata):
    """
    Metadata about the official.
    Generally does not change over the course of a sports-events.
    """
    uniform_number = None

    def __init__(self, xmlelement=None, **kwargs):
        super(BaseOfficialMetadata, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.uniform_number = xmlelement.findtext('uniform-number')

    def as_dict(self):
        dict = super(BaseOfficialMetadata, self).as_dict()
        if self.uniform_number:
            dict.update({ 'uniform_number': self.uniform_number })
        return dict


class OfficialMetadata(BaseOfficialMetadata):
    # inherits everything from BaseOfficialMetadata
    pass


class Official(CommonAttributes):
    """
    Also referred to as umpire or referree. 
    Ensures that the sports-event is played according to its rules.
    """
    official_metadata = None
    official_stats = None
    affiliations = None

    def __init__(self, xmlelement=None, **kwargs):
        super(Official, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.official_metadata = OfficialMetadata(
                xmlelement.find(NEWSMLG2_NS+'official-metadata')
            )
            self.official_stats = OfficialStats(
                xmlelement.find(NEWSMLG2_NS+'official-stats')
            )
            self.affiliations = Affiliations(
                xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        dict = super(Official, self).as_dict()
        if self.official_metadata:
            dict.update({'officialMetadata': self.official_metadata.as_dict()})
        if self.official_stats:
            dict.update({'officialStats': self.official_stats.as_dict()})
        if self.affiliations:
            dict.update({'affiliations': self.affiliations.as_dict()})
        return dict


class Affiliation(CommonAttributes, CoverageAttributes):
    """
    A mechanism for assigning the membership of a player, team, or
    associate within a division or larger organizational structure.
    Also, to indicate an official's affiliation with a team, club or
    federation, for example.
    """

    # A pointer to the ID for the larger organizational structure.
    membership_idref = None
    # The type of organizational structure in which this item is a member.
    membership_type = None
    # A unique key for the organizational structure in which this item is a member.
    membership_key = None
    # The name associated with the organizational structure in which this item is a member.
    membership_name = None
 
    def __init__(self, xmlelement=None, **kwargs):
        super(Affiliation, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.membership_idref = xmlelement.findtext(NEWSMLG2_NS+'membership-idref')
            self.membership_type = xmlelement.findtext(NEWSMLG2_NS+'membership-type')
            self.membership_key = xmlelement.findtext(NEWSMLG2_NS+'membership-key')
            self.membership_name = xmlelement.findtext(NEWSMLG2_NS+'membership-name')

    def as_dict(self):
        dict = super(Affiliation, self).as_dict()
        if self.membership_idref:
            dict.update({'membership_idref': self.membership_idref})
        if self.membership_type:
            dict.update({'membership_type': self.membership_type})
        if self.membership_key:
            dict.update({'membership_key': self.membership_key})
        if self.membership_name:
            dict.update({'membership_name': self.membership_name})
        return dict


class Names(object):
    names = None

    def __init__(self, xmlarray=None, **kwargs):
        self.names = []  # clear list for this instance
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                name = ConceptNameType(xmlelement)
                self.names.append(name)

    def as_dict(self):
        return [n.as_dict() for n in self.names]

    def __bool__(self):
        return len(self.names) != 0

#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .sports_metadata import SportsMetadata
from .base_metadata import (
    CommonAttributes, CoverageAttributes,
    SportsContentCodes, SportsProperties
)
from .newsmlg2 import ConceptNameType, FlexLocationPropType
from .statistics import TeamStatsSet, PlayerStatsSet, WageringStatsSet, OfficialStats



class Team(CommonAttributes):
    """
    A team participating in a sporting event. 
    Holds metadata and statistical data for team.
    """
    dict = {}

    team_metadata = None
    team_stats_set = None
    players = None
    wagering_stats_set = None
    associates = None
    affiliations = None

    def __init__(self, **kwargs):
        super(Team, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.team_metadata = TeamMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'team-metadata')
            )
            self.team_stats_set = TeamStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'team-stats')
            )
            self.players = Players(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'player')
            )
            self.wagering_stats_set = WageringStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            self.associates = Associates(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'associate')
            )
            self.affiliations = Affiliations(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        super(Team, self).as_dict()
        if self.team_metadata:
            self.dict.update({
                'teamMetadata': self.team_metadata.as_dict()
            })
        if self.team_stats_set:
            self.dict.update({
                'teamStats': self.team_stats_set.as_dict()
            })
        if self.players:
            self.dict.update({
                'players': self.players.as_dict()
            })
        if self.wagering_stats_set:
            self.dict.update({
                'wageringStatsSet': self.wagering_stats_set.as_dict()
            })
        if self.associates:
            self.dict.update({
                'associates': self.associates.as_dict()
            })
        if self.affiliations:
            self.dict.update({
                'affiliations': self.affiliations.as_dict()
            })
        return self.dict


class Teams(GenericArray):
    """
    Array of Team objects.
    """
    element_class = Team


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
    
    def __init__(self, **kwargs):
        super(BaseEntityMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.names = Names(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.home_location = FlexLocationPropType(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'home-location')
            )
            self.sports_properties = SportsProperties(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
            self.key = xmlelement.get('key')
            self.nationality = xmlelement.get('nationality')

    def as_dict(self):
        super(BaseEntityMetadata, self).as_dict()
        if self.names:
            self.dict.update({
                'names': self.names.as_dict()
            })
        if self.home_location:
            self.dict.update({
                'homeLocation': self.home_location.as_dict()
            })
        if self.sports_properties:
            self.dict.update({
                'sportsProperties': self.sports_properties.as_dict()
            })
        if self.key:
            self.dict.update({
                'key': self.key
            })
        if self.nationality:
            self.dict.update({
                'nationality': self.nationality
            })
        return self.dict


class BaseTeamMetadata(BaseObject):
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
        super(BaseTeamMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sites = Sites(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'site')
            )
            self.sports_content_codes = SportsContentCodes(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-content-code')
            )
            self.alignment = xmlelement.get('alignment')
            self.established = xmlelement.get('established')
            self.dissolved = xmlelement.get('dissolved')
            self.team_idref = xmlelement.get('team_idref')
            self.home_page_url = xmlelement.get('home_page_url')
            self.round_position = xmlelement.get('round-position')

    def as_dict(self):
        super(BaseTeamMetadata, self).as_dict()
        if self.sites:
            self.dict.update({
                'sites': self.sites.as_dict()
            })
        if self.sports_content_codes:
            self.dict.update({
                'sportsContentCodes': self.sports_content_codes.as_dict()
            })
        if self.alignment:
            self.dict.update({
                'alignment': self.alignment
            })
        if self.established:
            self.dict.update({
                'established': self.established
            })
        if self.dissolved:
            self.dict.update({
                'dissolved': self.dissolved
            })
        if self.team_idref:
            self.dict.update({
                'teamIdRef': self.team_idref
            })
        if self.home_page_url:
            self.dict.update({
                'homePageURL': self.home_page_url
            })
        if self.round_position:
            self.dict.update({
                'roundPosition': self.round_position
            })
        return self.dict


class TeamMetadata(BaseTeamMetadata):
    dict = {}
    team_metadata_baseball = None
    # Holds metadata about a team (foursome perhaps) playing in the match. | Currently only holds the rank of the team.
    team_metadata_golf = None
    team_metadata_motor_racing = None

    def __init__(self, xmlelement=None, **kwargs):
        self.dict = {}
        super(TeamMetadata, self).__init__(xmlelement, **kwargs)
        xmlelement = kwargs.get('xmlelement')
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
        super(TeamMetadata, self).as_dict()
        if self.team_metadata_baseball:
            self.dict.update({ 'teamMetadataBaseball': self.team_metadata_baseball.as_dict() })
        if self.team_metadata_golf:
            self.dict.update({ 'teamMetadataGolf': self.team_metadata_golf.as_dict() })
        if self.team_metadata_motor_racing:
            self.dict.update({ 'teamMetadataMotorRacing': self.team_metadata_motor_racing.as_dict() })
        return self.dict


class TeamMetadataBaseball(CommonAttributes):
    """
    Metadata about the team.
    Specific to the sport of baseball.
    """
    # ID of the pitcher who will probably start the game.
    probable_starting_pitcher_idref = None

    def __init__(self,  **kwargs):
        super(TeamMetadataBaseball, self).__init__(xmlelement, **kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.probable_starting_pitcher_idref = xmlelement.get(
                'probable-starting-pitcher-idref'
            )
    # TODO


class BaseGolfMetadata(CommonAttributes):
    """
    Holds metadata about a golf player. | Currently only holds the rank of the player.
    """
    # How this player ranks among the other competing players.
    rank = None

    def __init__(self, **kwargs):
        super(BaseGolfMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.rank = xmlelement.get("rank")

    def as_dict(self):
        super(BaseGolfMetadata, self).as_dict()
        if self.rank:
            self.dict.update({ 'rank': self.rank })
        return self.dict


class TeamMetadataGolf(BaseGolfMetadata):
    """
    Holds metadata about a team (foursome perhaps) playing in the match.
    Currently only holds the rank of the team.
    """
    # TODO
    pass


class TeamMetadataMotorRacing(CommonAttributes):
    """
    Metadata about the team.
    Specific to the sport of motor racing.
    """
    motor_racing_vehicles = None
    
    def __init__(self, **kwargs):
        super(TeamMetadataMotorRacing, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            motor_racing_vehicles = MotorRacingVehicles(
                xmlelement.findall(NEWSMLG2_NS+'metadata-motor-racing-vehicle')
            )

    # TODO


class MotorRacingVehicle(BaseObject):
    pass

    def as_dict(self):
        # TODO
        return None


class MotorRacingVehicles(GenericArray):
    """
    Array of MotorRacingVehicle objects.
    """
    element_class = MotorRacingVehicle


class Player(CommonAttributes):
    """
    A competitor.
    Their athletic talents help them decide who wins a sports-event.
    """
    dict = {}

    # def __init__(self, xmlelement=None, **kwargs):
    def __init__(self, **kwargs):
        self.dict = {}
        super(Player, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.player_metadata = PlayerMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata')
            )
            self.player_stats_set = PlayerStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'player-stats')
            )
            self.wagering_stats_set = WageringStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'wagering-stats')
            )
            self.associates = Associates(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'associate')
            )
            self.affiliations = Affiliations(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        super(Player, self).as_dict()
        if self.player_metadata:
            self.dict.update({ 'playerMetadata': self.player_metadata.as_dict() })
        if self.player_stats_set:
            self.dict.update({ 'playerStats': self.player_stats_set.as_dict() })
        if self.wagering_stats_set:
            self.dict.update({ 'wageringStats': self.wagering_stats_set.as_dict()})
        if self.associates:
            self.dict.update({ 'associates': self.associates.as_dict() })
        if self.affiliations:
            self.dict.update({'affiliations': self.affiliations.as_dict() })
        return self.dict


class Players(GenericArray):
    """
    Array of Player objects.
    """
    element_class= Player


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
    
    def __init__(self, **kwargs):
        super(BasePersonMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
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
        super(BasePersonMetadata, self).as_dict()
        if self.date_of_birth:
            self.dict.update({ 'dateOfBirth': self.date_of_birth })
        if self.date_of_death:
            self.dict.update({ 'dateOfDeath': self.date_of_death})
        if self.height:
            self.dict.update({ 'height': self.height })
        if self.weight:
            self.dict.update({ 'weight': self.weight })
        if self.position_regular:
            self.dict.update({ 'positionRegular': self.position_regular })
        if self.position_event:
            self.dict.update({ 'positionEvent': self.position_event })
        if self.position_depth:
            self.dict.update({ 'positionDepth': self.position_depth })
        if self.health:
            self.dict.update({ 'health': self.health })
        if self.gender:
            self.dict.update({ 'gender': self.gender })
        return dict


class CareerPhaseMetadata(BaseObject):
    # TODO

    def __init__(self, **kwargs):
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        return {}


class InjuryPhaseMetadata(BaseObject):
    # TODO

    def __init__(self, **kwargs):
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            # TODO
            pass

    def as_dict(self):
        return {}


class BasePlayerMetadata(BasePersonMetadata):
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

    def __init__(self, **kwargs):
        super(BasePlayerMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.career_phase_metadata = CareerPhaseMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'career-phase')
            )
            self.injury_phase_metadata = InjuryPhaseMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'injury-phase')
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
        super(BasePlayerMetadata, self).as_dict()
        if self.career_phase_metadata:
            self.dict.update({ 'careerPhaseMetadata': self.career_phase_metadata.as_dict() })
        if self.injury_phase_metadata:
            self.dict.update({ 'injuryPhaseMetadata': self.injury_phase_metadata.as_dict() })
        if self.team_idref:
            self.dict.update({ 'teamIdRef': self.injury_phase })
        if self.status:
            self.dict.update({ 'status': self.status })
        if self.lineup_slot:
            self.dict.update({ 'lineupSlot': self.lineup_slot })
        if self.lineup_slot_sequence:
            self.dict.update({ 'lineupSlotSequence': self.lineup_slot_sequence })
        if self.scratch_reason:
            self.dict.update({ 'scratchReason': self.scratch_reason })
        if self.uniform_number:
            self.dict.update({ 'uniformNumber': self.uniform_number })
        if self.home_page_url:
            self.dict.update({ 'homePageURL': self.home_page_url })
        if self.round_position:
            self.dict.update({ 'roundPosition': self.round_position })
        return self.dict


class PlayerMetadata(BasePlayerMetadata):
    dict = {}

    def __init__(self, **kwargs):
        self.dict = {}
        super(PlayerMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            pass
            """
            TODO
            self.player_metadata_baseball = PlayerMetadataBaseball(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-baseball')
            )
            self.player_metadata_golf = PlayerMetadataGolf(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-golf')
            )
            self.player_metadata_ice_hockey = PlayerMetadataIceHockey(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-ice-hockey')
            )
            self.player_metadata_soccer = PlayerMetadataSoccer(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-soccer')
            )
            self.player_metadata_motor_racing = PlayerMetadataMotorRacing(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-motor-racing')
            )
            self.player_metadata_curling = PlayerMetadataCurling(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'player-metadata-curling')
            )
            """

    def as_dict(self):
        super(PlayerMetadata, self).as_dict()
        # TODO
        return self.dict


class Associate(BaseObject):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Associates(GenericArray):
    """
    Array of Associate objects.
    """
    element_class = Associate


class Affiliation(BaseObject):
    # TODO
    pass

    def as_dict(self):
        # TODO
        return None


class Affiliations(GenericArray):
    """
    Array of Affiliation objects.
    """
    element_class= Affiliation


class BaseOfficialMetadata(BasePersonMetadata):
    """
    Metadata about the official.
    Generally does not change over the course of a sports-events.
    """
    dict = {}
    uniform_number = None

    def __init__(self,  **kwargs):
        super(BaseOfficialMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.uniform_number = xmlelement.findtext('uniform-number')

    def as_dict(self):
        super(BaseOfficialMetadata, self).as_dict()
        if self.uniform_number:
            self.dict.update({ 'uniform_number': self.uniform_number })
        return self.dict


class OfficialMetadata(BaseOfficialMetadata):
    # inherits everything from BaseOfficialMetadata
    pass


class Official(CommonAttributes):
    """
    Also referred to as umpire or referree. 
    Ensures that the sports-event is played according to its rules.
    """
    dict = {}
    official_metadata = None
    official_stats = None
    affiliations = None

    def __init__(self, **kwargs):
        super(Official, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.official_metadata = OfficialMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'official-metadata')
            )
            self.official_stats = OfficialStats(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'official-stats')
            )
            self.affiliations = Affiliations(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'affiliation')
            )

    def as_dict(self):
        super(Official, self).as_dict()
        if self.official_metadata:
            self.dict.update({'officialMetadata': self.official_metadata.as_dict()})
        if self.official_stats:
            self.dict.update({'officialStats': self.official_stats.as_dict()})
        if self.affiliations:
            self.dict.update({'affiliations': self.affiliations.as_dict()})
        return self.dict


class Officials(GenericArray):
    """
    Array of Official objects.
    """
    element_class= Official


class Affiliation(CommonAttributes, CoverageAttributes):
    """
    A mechanism for assigning the membership of a player, team, or
    associate within a division or larger organizational structure.
    Also, to indicate an official's affiliation with a team, club or
    federation, for example.
    """
    dict = {}
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
        super(Affiliation, self).as_dict()
        if self.membership_idref:
            self.dict.update({'membership_idref': self.membership_idref})
        if self.membership_type:
            self.dict.update({'membership_type': self.membership_type})
        if self.membership_key:
            self.dict.update({'membership_key': self.membership_key})
        if self.membership_name:
            self.dict.update({'membership_name': self.membership_name})
        return self.dict


class Names(GenericArray):
    """
    Array of ConceptNameType objects.
    """
    element_class = ConceptNameType


class SiteMetadata(BaseEntityMetadata):
    """
    Metadata about the site.
    """
    dict = {}
    sports_content_codes = None
    # How many spectators can fill the site.
    capacity = None
    # Whether it is an indoor or outdoor site.
    site_style = None
    # Describes the surface upon which events are played.
    # For example, in tennis, could be hard-court or grass or clay.
    surface = None
    # A controlled vocabulary for the site's shape. Example for motor-racing: oval.
    shape = None
    # The pitch or embankment of the field of play.
    # Generally in degrees. Example for motor-racing: 13.
    incline = None
    # The length of the arena or field of play.
    length = None
    # The units used for the length attribute.
    length_units = None
    # A controlled vocabulary for the type or class of arena.
    # Example for motor-racing: super-speedway.
    type = None
    # The website for the venue or arena.
    home_page_url = None
    # Date (and time) when a place was built, opened or so.
    created = None
    # Date (and time) when a place ceased to exist.
    # (note camel case, this is to match XML Schema attribute definition)
    ceasedToExist = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(SiteMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sports_content_codes = SportsContentCodes(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'sports-content-codes')
            )
            self.capacity = xmlelement.get('capacity')
            self.site_style= xmlelement.get('site-style')
            self.surface = xmlelement.get('surface')
            self.incline = xmlelement.get('incline')
            self.length = xmlelement.get('length')
            self.length_units = xmlelement.get('length-units')
            self.type = xmlelement.get('type')
            self.home_page_url = xmlelement.get('home-page-url')
            self.created = xmlelement.get('created')
            self.ceasedToExist = xmlelement.get('ceasedToExist')

    def as_dict(self):
        super(SiteMetadata, self).as_dict()
        if self.sports_content_codes:
            self.dict.update({'sportsContentCodes': self.sports_content_codes.as_dict() })
        if self.capacity:
            self.dict.update({'capacity': self.capacity })
        if self.site_style:
            self.dict.update({'siteStyle': self.site_style })
        if self.surface:
            self.dict.update({'surface': self.surface })
        if self.incline:
            self.dict.update({'incline': self.incline })
        if self.length:
            self.dict.update({'length': self.length })
        if self.length_units:
            self.dict.update({'lengthUnits': self.length_units })
        if self.type:
            self.dict.update({'type': self.type })
        if self.home_page_url:
            self.dict.update({'homePageURL': self.home_page_url })
        if self.created:
            self.dict.update({'created': self.created })
        if self.ceasedToExist:
            self.dict.update({'ceasedToExist': self.ceasedToExist })
        return self.dict


class SiteStats(BaseObject):
    # TODO
    pass


class SiteStatsSet(GenericArray):
    """
    Array of SiteStats objects.
    """
    element_class = SiteStats


class Site(CommonAttributes):
    """
    An element housing data having to do with a venue, stadium, arena, field, etc.
    """
    dict = {}
    site_metadata = None
    site_stats_set = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(Site, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.site_metadata = SiteMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'site-metadata')
            )
            self.site_stats_set = SiteStatsSet(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'site-stats')
            )

    def as_dict(self):
        super(Site, self).as_dict()
        if self.site_metadata:
            self.dict.update({'siteMetadata': self.site_metadata.as_dict() })
        if self.site_stats_set:
            self.dict.update({'siteStats': self.site_stats_set.as_dict() })
        return self.dict


class Sites(GenericArray):
    """
    Array of Site objects.
    """
    element_class = Site




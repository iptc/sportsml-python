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
    attributes = {
        # The symbol or identifying key for the entity.
        'key': 'key',
        # The country of citizinship of the entity.
        'nationality': 'nationality'
    }
    
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
        return self.dict


class BaseTeamMetadata(BaseObject):
    """
    Info about the team. Properties of a team that are not based on their competitive performance.
    An included sports-content-code element can hold what division it is in, etc.
    """
    sites = None
    sports_content_codes = None
    attributes = {
        # Home or visiting. This is more information about the
        # alignment of the team or player in the event regarding rules etc. It
        # does not necessarily indicate that it is the geographical home-site of
        # the team or player.
        # enumeration: home, away, none
        'alignment': 'alignment',
        # Date (and time) when the team was established.
        'established': 'established',
        # Date (and time) when the team was dissolved. 
        'dissolved': 'dissolved',
        # Optional reference to a team in which this team is a member. Example: The U.S. Davis Cup team consists of many sub-teams.
        'team-idref': 'teamIdref',
        # The fully-qualified URL for the official home page of the team.
        'home-page-url': 'homePageURL',
        # The seed or position in this particular round for which this team started. Useful for bracketed tournaments, such as tennis.
        'round-position': 'roundPosition'
    }

    def __init__(self, **kwargs):
        super(BaseTeamMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sites = Sites(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'site')
            )
            self.sports_content_codes = SportsContentCodes(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-content-code')
            )

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
        return self.dict


class TeamMetadata(BaseTeamMetadata):
    team_metadata_baseball = None
    # Holds metadata about a team (foursome perhaps) playing in the match.
    # Currently only holds the rank of the team.
    team_metadata_golf = None
    team_metadata_motor_racing = None

    def __init__(self, **kwargs):
        super(TeamMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.team_metadata_baseball = TeamMetadataBaseball(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'team-metadata-baseball')
            )
            self.team_metadata_golf = TeamMetadataGolf(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'team-metadata-golf')
            )
            self.team_metadata_motor_racing = TeamMetadataMotorRacing(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'team-metadata-motor-racing')
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
    (from sportsml-specific-baseball.xsd)
    """
    attributes = {
        # ID of the pitcher who will probably start the game.
        'probable_starting_pitcher_idref': 'probableStartingPitcherIdref'
    }


class BaseGolfMetadata(CommonAttributes):
    """
    Holds metadata about a golf player.
    Currently only holds the rank of the player.
    (from sportsml-specific-golf.xsd)
    """
    attributes = {
        # How this player ranks among the other competing players.
        'rank': 'rank'
    }


class TeamMetadataGolf(BaseGolfMetadata):
    """
    Holds metadata about a team (foursome perhaps) playing in the match.
    Currently only holds the rank of the team.
    (from sportsml-specific-golf.xsd)
    """
    pass


class TeamMetadataMotorRacing(CommonAttributes):
    """
    Metadata about the team.
    Specific to the sport of motor racing.
    (from sportsml-specific-motor-racing.xsd)
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
    """
    (from sportsml-specific-motor-racing.xsd)
    """
    pass

    def as_dict(self):
        # TODO
        return None


class MotorRacingVehicles(GenericArray):
    """
    Array of MotorRacingVehicle objects.
    (from sportsml-specific-motor-racing.xsd)
    """
    element_class = MotorRacingVehicle


class Player(CommonAttributes):
    """
    A competitor.
    Their athletic talents help them decide who wins a sports-event.
    """

    def __init__(self, **kwargs):
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
    attributes = {
        # The day on which a person was born, normalized to ISO 8601
        # extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time
        # is available. Can also be YYYY-MM or just YYYY if year and/or month not available.
        'date-of-birth': 'dateOfDeath',
        # The day on which a person died, normalized to ISO 8601
        # extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available.
        'date-of-death': 'dateOfDeath',
        # Height of the person. Generally in cm.
        'height': 'height',
        # Weight of a person. Generally in kg.
        'weight': 'weight',
        # The code for the typical position of the person.
        'position-regular': 'positionRegular',
        # The code for the position held by the person at this  particular sports-event.
        'position-event': 'positionEvent',
        # A ranking amongst players on the team who share the same position.
        'position-depth': 'positionDepth',
        # An indication of the health of the person.
        'health': 'health',
        # Male or female.
        'gender': 'gender'
    }
    

class BasePlayerMetadata(BasePersonMetadata):
    """
    Metadata that describes a person. | Generally does not change over the course of a sports-events.
    """

    career_phase_metadata = None
    injury_phase_metadata = None

    attributes = {
        # A reference to the team for which this player competes.
        'team_idref': 'teamIdref',
        # Whether a player starts playing at the beginning of a sports-event, joins mid-game, or is not available to participate.
        'status': 'status',
        # The order in which a player participated in an event.
        'lineup_slot': 'lineupSlot',
        # For baseball, cricket, relay races if they substituted for a player in the original lineup, the order in which they served at the above lineup-slot value. Defaults to 1.
        'lineup_slot_sequence': 'lineupSlotSequence',
        # An indication as to why this player did not play in an event.
        'scratch_reason': 'scratchReason',
        # The number currently displayed on the uniform or jersey of the player.
        'uniform_number': 'uniformNumber',
        # The fully-qualified URL for the official home page of the team.
        'home_page_url': 'homePageURL',
        # The seed or position in this particular round for which this player started. Useful for bracketed tournaments, such as tennis.
        'round_position': 'roundPosition',
    }

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

    def as_dict(self):
        super(BasePlayerMetadata, self).as_dict()
        if self.career_phase_metadata:
            self.dict.update({ 'careerPhaseMetadata': self.career_phase_metadata.as_dict() })
        if self.injury_phase_metadata:
            self.dict.update({ 'injuryPhaseMetadata': self.injury_phase_metadata.as_dict() })
        return self.dict

    # FIXME
    # def __bool__(self):
    #    return self.career_phase_metadata or self.injury_phase_metadata or self.attr_values


class PlayerMetadata(BasePlayerMetadata):

    def __init__(self, **kwargs):
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


class CareerPhaseMetadata(BasePlayerMetadata):
    """
    A description of where a player is playing, or has previously played.
    Can be used to state where the player went to college.
    Can also list previous teams of the player.
    """
    attributes = {
        # Value can be college or professional, etc.
        'phase-type': 'phaseType',
        # When the player started this phase in the career,
        # normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM.
        # Use YYYY-MM-DD when no time is available.
        'start-date': 'startDate',
        # When the player ended this phase in the career,
        # normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM.
        # Use YYYY-MM-DD when no time is available.
        'end-date': 'endDate',
        # In lieu of a start-date and end-date. Generally in years.
        # Could hold the number of years that a player was a pro.
        # Use temporal-unit vocabulary.
        'duration': 'duration',
        # A subcategory of the phase-type, for example could be sophomore or rookie.
        'subphase-type': 'subphaseType',
        # Player's status within a particular phase.
        # For example, active, injured, etc.
        'phase-status': 'phaseStatus',
        # A controlled vocabulary for the name attribute.
        # States organization this player was in, for the duration of the phase.
        # For example, league or team.
        'phase-caliber': 'phaseCaliber',
        # The metadata key within the phase-caliber.
        # For example, l.nfl.com if phase-caliber is league.
        # Or l.nfl.com-t.2 if phase-caliber is team.
        'phase-caliber-key': 'phaseCaliberKey',
        # The reason why the player entered this phase. For example, draft or trade.
        'entry-reason': 'entryReason',
        # The level within which the player was selected to enter this phase. For example, 1, if drafted in 1st round.
        'selection-level': 'selectionLevel',
        # The sublevel of the selection-level. For example, 27, if picked as 27th selection in 1st round.
        'selection-sublevel': 'selectionSublevel',
        # The total ranking amongst all levels in a draft.
        'selection-overall': 'selectionOverall',
        # The reason why the player exitted this phase. For example, retired or waived.
        'exit-reason': 'exitReason'
    }


class InjuryPhaseMetadata(BasePlayerMetadata):
    """ 
    A description of where a player is playing, or has previously played.
    Can be used to state where the player went to college.
    Can also list previous teams of the player.
    """
    attributes = {
        # Value can be college or professional, etc.
        'phase-type': 'phaseType',
        # When the player started this phase in the career, normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available.
        'start-date': 'startDate',
        # When the player ended this phase in the career, normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available.
        'end-date': 'endDate',
        # Player's status within a particular phase. For example, active, injured, etc.
        'phase-status': 'phaseStatus',
        # A controlled vocabulary for the injury. For example, thigh or hand or lower-back.
        'injury-type': 'injuryType',
        # A controlled vocabulary for the body side of the injury. For example, left or right.
        'injury-side': 'injurySide',
        # Generally, the date on which this player has a non-injured status, and has some probability of playing again.
        'upcoming-event-date': 'upcomingEventDate',
        # The key for the forthcoming event taking place on upcoming-event-date.
        'upcoming-event-key': 'upcomingEventKey',
        # A measurement of the status of the player for that upcoming event. For example, probable or likely.
        'upcoming-event-status': 'upcomingEventStatus',
        # A textual description for the injury phase.
        'comment': 'comment'
    }


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
 
    def __init__(self, **kwargs):
        super(Affiliation, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
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
    sports_content_codes = None
    attributes = {
        # How many spectators can fill the site.
        'capacity': 'capacity',
        # Whether it is an indoor or outdoor site.
        'site-style': 'siteStyle',
        # Describes the surface upon which events are played.
        # For example, in tennis, could be hard-court or grass or clay.
        'surface': 'surface',
        # A controlled vocabulary for the site's shape. Example for motor-racing: oval.
        'shape': 'shape',
        # The pitch or embankment of the field of play.
        # Generally in degrees. Example for motor-racing: 13.
        'incline': 'incline',
        # The length of the arena or field of play.
        'length': 'length',
        # The units used for the length attribute.
        'length-units': 'lengthUnits',
        # A controlled vocabulary for the type or class of arena.
        # Example for motor-racing: super-speedway.
        'type': 'type',
        # The website for the venue or arena.
        'home-page-url': 'homePageURL',
        # Date (and time) when a place was built, opened or so.
        'created': 'created',
        # Date (and time) when a place ceased to exist.
        # (note camel case, it's written this way in the XML Schema attribute definition)
        'ceasedToExist': 'ceasedToExist'
    }


class SiteStats(CommonAttributes, CoverageAttributes):
    """
    Holder for statistics about the site.
    """
    attributes = {
        # Statistics about the site, accurate for a particular occasion. home means the site is home for one of the teams or players. neutral that it is neutral to all participants in the event.</xs:documentation>
        # enum: home or neutral
        'alignment': 'alignment',
        # How many spectators attended during the event.</xs:documentation>
        'attendance': 'attendance',
        # Average number of spectators that have attended.</xs:documentation>
        'attendance-average': 'attendanceAverage',
        # Temperature of the event recorded during the competition.</xs:documentation>
        'temperature': 'temperature',
        # Units of the temperature value.</xs:documentation>
        'temperature-units': 'temperatureUnits',
        # A controlled-vocabulary description of the weather, such as sunny, partly-cloudy, etc.</xs:documentation>
        'weather-code': 'weatherCode',
        # Additional comment about the weather.</xs:documentation>
        'weather-label': 'weatherLabel',
        # Wind reading of the event recorded during the competition.</xs:documentation>
        'weather-wind': 'weatherWind',
        # Predicted weather conditions for the event.</xs:documentation>
        'weather-prediction': 'weatherPrediction',
        # Percentage likelihood of precipitation.</xs:documentation>
        'probability-of-precipitation': 'probabilityOfPrecipitation'
    }


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

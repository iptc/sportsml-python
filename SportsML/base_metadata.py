#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject, GenericArray


class CommonAttributes(BaseObject):
    attributes = {
        # An XML-specific identifier for the element.
        'id': 'id',
        # An open placeholder for categorization.
        'class': 'class',
        # An open placeholder for reference by an external stylesheet.
        'style': 'style'
    }


class CoverageAttributes(BaseObject):
    attributes = {
        # A relative indication of how many statistics are included in the item. SportsML vocab uri: http://cv.iptc.org/newscodes/spstatscoverage/</xs:documentation>
        'stats-coverage': 'statsCoverage',
        # Indicates whether the item contains information about one team, or many teams.
        # enum: single-team, multi-team
        'team-coverage': 'teamCoverage',
        # Indicates that the included statistics apply only to while played at a particular position.
        'duration-scope': 'durationScope',
        # Indicates that the included statistics apply only to values that set a record, such as a team-high, or an individual-low.
        'record-making-scope': 'recordMakingScope',
        # A textual description for the scope.
        'scoping-label': 'scopingLabel',
        # Used for tracking stats and events by period.
        'period-value': 'periodValue',
        # For certain types of periods: overtime, declared (cricket), etc.
        'period-type': 'periodType',
        # The starting date, with optional time, of the event for which the stats are relevant.
        'start-date-time': 'startDateTime',
        # The ending date, with optional time, of the event for which the stats are relevant.
        'end-date-time': 'endDateTime',
        # The starting date, with optional time, of the period for which the stats are relevant.
        'period-start-date-time': 'periodStartDateTime',
        # The ending date, with optional time, of the period for which the stats are relevant.
        'period-end-date-time': 'periodEndDateTime',
        # The unit of performance to which the stats apply eg. single-event, season, career.
        'temporal-unit-type': 'temporalUnitType',
        # The key of performance unit to which the stats apply.
        'temporal-unit-value': 'temporalUnitValue',
        # Qualifier of "most-recent-events" value for temporal-unit attribute. Specify the number of events eg. 10 for last 10 games.
        'event-span': 'eventSpan',
        # The key of the player, team, division, conference, league or other unit which provide the opposition relevant to the stat.
        'opponent-value': 'opponentValue',
        # Whether the opponent was a player, team, etc.
        'opponent-type': 'opponentType',
        # The key of the team for which the player or team generated the stats.
        'team': 'team',
        # The key of the league or competition for which the player or team generated the stats.
        'competition': 'competition',
        # The key, other than team or league/competition, of the competitive unit for which the player or team generated the stats.
        'unit-value': 'unitValue',
        # The type, other than team or league/competition, of the competitive unit for which the player or team generated the stats.
        'unit-type': 'unitType',
        # Final or current score of the team or player.
        'situation': 'situation',
        # The key of the site,venue or location where the stats were generated.
        'location-key': 'locationKey',
        # The type of event (eg. indoor, outdoor, etc.) in which the stats were generated.
        'venue-type': 'venueType',
        # The type of surface (eg. clay, artificial grass, etc.) upon which the stats were generated.
        'surface-type': 'surfaceType',
        # A code for the weather situation in which the stats were generated. SportsML weather codes recommended.
        'weather-type': 'weatherType',
        # A generic scope indicator. Use only if none of the other coverage attributes are suitable.
        'scope-value': 'scopeValue',
        # Measure of distance for the generated stat.
        'distance': 'distance',
        # Maximum distance for the generated stat.
        'distance-maximum': 'distanceMaximum',
        # Minimum distance for the generated stat.
        'distance-minimum': 'distanceMinimum',
        # The type of unit used to measure distance, speed, etc. Could be mph, kph, metres, yards, etc.
        'measurement-units': 'measurementUnits'
    }


class BaseMetadata(CommonAttributes, CoverageAttributes):
    """
    Basic metadata elements and attributes. Used directly by
    sports, standing, schedule and statistic and extended
    further by base2MetadataComplexType
    """
    sports_content_codes = None
    sports_properties = None

    def __init__(self, **kwargs):
        super(BaseMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sports_content_codes = SportsContentCodes(
                xmlarray = xmlelement.find(NEWSMLG2_NS+'sports-content-codes')
            )
            self.sports_properties = SportsProperties(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )

    def as_dict(self):
        super(BaseMetadata, self).as_dict()
        if self.sports_content_codes:
            self.dict.update({ 'sportsContentCodes': self.sports_content_codes.as_dict() })
        if self.sports_properties:
            self.dict.update({ 'sportsProperties': self.sports_properties.as_dict() })
        return self.dict


class Base2Metadata(BaseMetadata):
    """
    Extends the baseMetadata with more elements and attributes. Used by baseEvent and baseTournament
    """
    names = None
    sites = None
    awards = None
    attributes = {
        'key': 'key'
    }

    def __init__(self, **kwargs):
        super(Base2Metadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            from .newsmlg2 import Names
            from .entities import Sites
            self.names = Names(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.sites = Sites(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'site')
            )
            from .sports_events import Awards
            self.awards = Awards(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'award')
            )

    def as_dict(self):
        super(Base2Metadata, self).as_dict()
        if self.names:
            self.dict.update({'names': self.names.as_dict() })
        if self.sites:
            self.dict.update({'sites': self.sites.as_dict() })
        if self.awards:
            self.dict.update({'awards': self.awards.as_dict() })
        return self.dict


class SportsContentQualifier(CommonAttributes):
    """
    Further refinement/elaboration of a sports-content-code.
    If the document covers more than one of these, additional
    sports-content-qualifier elements may be used.
    """
    attributes = {
        # One specific gender or mixed.
        # enum: 'male', 'female', 'mixed'
        'gender': 'gender',
        # Number of participants playing on a team or side in the events covered.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/spparticipantcount/
        'participant-count': 'participantCount',
        # The professional-status of the events covered.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/spprofessionalstatus/
        'professional-status': 'professionalStatus',
        # If the events covered are for special groups.
        # Can be school-oriented, age-oriented, or group names, like Firefighters.
        'special-group': 'specialGroup',
        # Lowest age for participants, in years. Examples: 0, 14, 21.5.
        'minimum-age': 'minimumAge',
        # Highest age for participants, in years. Examples: 8, 65, 120.
        'maximum-age': 'maximumAge',
        # Events for persons with special-needs.
        'special-needs': 'specialNeeds'
    }
 

class SportsContentQualifiers(GenericArray):
    """
    A container for content-codes.
    Can hold as many codes as needed to describe all contents at this level and below.
    """
    element_class = SportsContentQualifier


class SportsContentCode(CommonAttributes):
    """
    An individual code that describes an entity one may want to filter for.
    Describes what sports, what teams, etc., are covered.
    """
    sports_content_qualifiers = None
    attributes = {
        # What type of item is being described.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/spct/
        'code-type': 'codeType',
        # The symbol for the identified content.
        'code-key': 'codeKey',
        # A displayable name for the code.
        'code-name': 'codeName'
    }

    def __init__(self, **kwargs):
        super(SportsContentCode, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.sports_content_qualifiers = SportsContentQualifiers(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-content-qualifier')
            )

    def as_dict(self):
        super(SportsContentCode, self).as_dict()
        if self.sports_content_qualifiers:
            self.dict.update({ 'sportsContentQualifiers': self.sports_content_qualifiers.as_dict() })
        return self.dict


class SportsContentCodes(GenericArray):
    """
    A container for content-codes.
    Can hold as many codes as needed to describe all contents at this level and below.
    """
    element_class = SportsContentCode


class SportsProperties(GenericArray):
    """
    Array of SportsProperty objects.
    """
    element_module_name = __name__
    element_class_name = 'SportsProperty'


class SportsProperty(CommonAttributes):
    """
    An extensible property, similar to structures in NewsML 1.
    """
    attributes = {
        # The code or key for the property.
        'formal-name': 'formalName',
        # Provides a pointer to a Topic Set which is the controlled vocabulary
        # that can be used to resolve the meaning of the formal-name.
        'vocabulary': 'vocabulary',
        # Distinguishes which of possibly multiple naming schemes in the
        # controlled vocabulary is the one that governs this formal-name.
        'scheme': 'scheme',
        # The value of the property. For example, if formal-name equals
        # favorite-color, then value might equal blue.
        'value': 'value',
        # Points to a controlled vocabulary that delimits the set of
        # allowed values for the property.
        'allowed-values': 'allowedValues'
    }

#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject
# from .entities import Names, Sites
#from .sports_events import Awards

class CommonAttributes(BaseObject):
    # An XML-specific identifier for the element.
    id = None
    # An open placeholder for categorization.
    class_attr = None
    # An open placeholder for reference by an external stylesheet.
    style = None

    def __init__(self, **kwargs):
        super(CommonAttributes, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement', None)
        if type(xmlelement) == etree.Element:
            self.id = xmlelement.get('id')
            self.class_attr = xmlelement.get('class')
            self.style = xmlelement.get('style')
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'class' in kwargs:
                self.class_attr = kwargs['class']
            if 'style' in kwargs:
                self.style = kwargs['style']

    def as_dict(self):
        super(CommonAttributes, self).as_dict()
        if self.id:
            self.dict.update({'id': self.id})
        if self.class_attr:
            self.dict.update({'class': self.class_attr})
        if self.style:
            self.dict.update({'style': self.style})
        return self.dict


class CoverageAttributes(BaseObject):
    # A relative indication of how many statistics are included in the item. SportsML vocab uri: http://cv.iptc.org/newscodes/spstatscoverage/</xs:documentation>
    stats_coverage = None
    # Indicates whether the item contains information about one team, or many teams.
    # enum: single-team, multi-team
    team_coverage = None
    # Indicates that the included statistics apply only to while played at a particular position.
    duration_scope = None
    # Indicates that the included statistics apply only to values that set a record, such as a team-high, or an individual-low.
    record_making_scope = None
    # A textual description for the scope.
    scoping_label = None
    # Used for tracking stats and events by period.
    period_value = None
    # For certain types of periods: overtime, declared (cricket), etc.
    period_type = None
    # The starting date, with optional time, of the event for which the stats are relevant.
    start_date_time = None
    # The ending date, with optional time, of the event for which the stats are relevant.
    end_date_time = None
    # The starting date, with optional time, of the period for which the stats are relevant.
    period_start_date_time = None
    # The ending date, with optional time, of the period for which the stats are relevant.
    period_end_date_time = None
    # The unit of performance to which the stats apply eg. single-event, season, career.
    temporal_unit_type = None
    # The key of performance unit to which the stats apply.
    temporal_unit_value = None
    # Qualifier of "most-recent-events" value for temporal-unit attribute. Specify the number of events eg. 10 for last 10 games.
    event_span = None
    # The key of the player, team, division, conference, league or other unit which provide the opposition relevant to the stat.
    opponent_value = None
    # Whether the opponent was a player, team, etc.
    opponent_type = None
    # The key of the team for which the player or team generated the stats.
    team = None
    # The key of the league or competition for which the player or team generated the stats.
    competition = None
    # The key, other than team or league/competition, of the competitive unit for which the player or team generated the stats.
    unit_value = None
    # The type, other than team or league/competition, of the competitive unit for which the player or team generated the stats.
    unit_type = None
    # Final or current score of the team or player.
    situation = None
    # The key of the site,venue or location where the stats were generated.
    location_key = None
    # The type of event (eg. indoor, outdoor, etc.) in which the stats were generated.
    venue_type = None
    # The type of surface (eg. clay, artificial grass, etc.) upon which the stats were generated.
    surface_type = None
    # A code for the weather situation in which the stats were generated. SportsML weather codes recommended.
    weather_type = None
    # A generic scope indicator. Use only if none of the other coverage attributes are suitable.
    scope_value = None
    # Measure of distance for the generated stat.
    distance = None
    # Maximum distance for the generated stat.
    distance_maximum = None
    # Minimum distance for the generated stat.
    distance_minimum = None
    # The type of unit used to measure distance, speed, etc. Could be mph, kph, metres, yards, etc.
    measurement_units = None

    def __init__(self, xmlelement=None, **kwargs):
        super(CoverageAttributes, self).__init__(**kwargs)
        if type(xmlelement) == etree.Element:
            self.stats_coverage = xmlelement.get('stats-coverage')
            self.team_coverage = xmlelement.get('team-coverage')
            self.duration_scope = xmlelement.get('duration-scope')
            self.stats_coverage = xmlelement.get('stats-coverage')
            self.team_coverage = xmlelement.get('team-coverage')
            self.record_making_scope = xmlelement.get('record-making-scope')
            self.scoping_label = xmlelement.get('scoping-label')
            self.period_value = xmlelement.get('period-value')
            self.period_type = xmlelement.get('period-type')
            self.start_date_time = xmlelement.get('start-date-time')
            self.end_date_time = xmlelement.get('end-date-time')
            self.period_start_date_time = xmlelement.get('period-start-date-time')
            self.period_end_date_time = xmlelement.get('period-end-date-time')
            self.temporal_unit_type = xmlelement.get('temporal-unit-type')
            self.temporal_unit_value = xmlelement.get('temporal-unit-value')
            self.event_span = xmlelement.get('event-span')
            self.opponent_value = xmlelement.get('opponent-value')
            self.opponent_type = xmlelement.get('opponent-type')
            self.team = xmlelement.get('team')
            self.competition = xmlelement.get('competition')
            self.unit_value = xmlelement.get('unit-value')
            self.unit_type = xmlelement.get('unit-type')
            self.situation = xmlelement.get('situation')
            self.location_key = xmlelement.get('location-key')
            self.venue_type = xmlelement.get('venue-type')
            self.surface_type = xmlelement.get('surface-type')
            self.weather_type = xmlelement.get('weather-type')
            self.scope_value = xmlelement.get('scope-value')
            self.distance = xmlelement.get('distance')
            self.distance_maximum = xmlelement.get('distance-maximum')
            self.distance_minimum = xmlelement.get('distance-minimum')
            self.measurement_units = xmlelement.get('measurement-units')
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'class' in kwargs:
                self.class_attr = kwargs['class']
            if 'style' in kwargs:
                self.style = kwargs['style']

    def as_dict(self):
        super(CoverageAttributes, self).as_dict()
        if self.stats_coverage:
            self.dict.update({ 'statsCoverage': self.stats_coverage })
        if self.team_coverage:
            self.dict.update({ 'teamCoverage': self.team_coverage })
        if self.duration_scope:
            self.dict.update({ 'durationScope': self.duration_scope })
        if self.stats_coverage:
            self.dict.update({ 'statsCoverage': self.stats_coverage })
        if self.team_coverage:
            self.dict.update({ 'teamCoverage': self.team_coverage })
        if self.record_making_scope:
            self.dict.update({ 'recordMakingScope': self.record_making_scope })
        if self.scoping_label:
            self.dict.update({ 'scopingLabel': self.scoping_label })
        if self.period_value:
            self.dict.update({ 'periodValue': self.period_value })
        if self.period_type:
            self.dict.update({ 'periodType': self.period_type })
        if self.start_date_time:
            self.dict.update({ 'startDateTime': self.start_date_time })
        if self.end_date_time:
            self.dict.update({ 'endDateTime': self.end_date_time })
        if self.period_start_date_time:
            self.dict.update({ 'periodStartDateTime': self.period_start_date_time })
        if self.period_end_date_time:
            self.dict.update({ 'periodEndDateTime': self.period_end_date_time })
        if self.temporal_unit_type:
            self.dict.update({ 'temporalUnitType': self.temporal_unit_type })
        if self.temporal_unit_value:
            self.dict.update({ 'temporalUnitValue': self.temporal_unit_value })
        if self.event_span:
            self.dict.update({ 'eventSpan': self.event_span })
        if self.opponent_value:
            self.dict.update({ 'opponentValue': self.opponent_value })
        if self.opponent_type:
            self.dict.update({ 'opponentType': self.opponent_type })
        if self.team:
            self.dict.update({ 'team': self.team })
        if self.competition:
            self.dict.update({ 'competition': self.competition })
        if self.unit_value:
            self.dict.update({ 'unitValue': self.unit_value })
        if self.unit_type:
            self.dict.update({ 'unitType': self.unit_type })
        if self.situation:
            self.dict.update({ 'situation': self.situation })
        if self.location_key:
            self.dict.update({ 'locationKey': self.location_key })
        if self.venue_type:
            self.dict.update({ 'venueType': self.venue_type })
        if self.surface_type:
            self.dict.update({ 'surfaceType': self.surface_type })
        if self.weather_type:
            self.dict.update({ 'weatherType': self.weather_type })
        if self.scope_value:
            self.dict.update({ 'scopeValue': self.scope_value })
        if self.distance:
            self.dict.update({ 'distance': self.distance })
        if self.distance_maximum:
            self.dict.update({ 'distanceMaximum': self.distance_maximum })
        if self.distance_minimum:
            self.dict.update({ 'distanceMinimum': self.distance_minimum })
        if self.measurement_units:
            self.dict.update({ 'measurementUnits': self.measurement_units })
        return self.dict


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
                xmlelement.findall(NEWSMLG2_NS+'sports-content-codes')
            )
            self.sports_properties = SportsProperties(
                xmlelement.findall(NEWSMLG2_NS+'sports-property')
            )
        elif kwargs:
            if 'sports_content_codes' in kwargs:
                self.set_sports_content_codes(kwargs['sports_properties'])
            if 'sports_properties' in kwargs:
                self.set_sports_properties(kwargs['sports_properties'])

    def set_sports_content_codes(self, sports_content_codes):
        self.sports_content_codes = sports_content_codes

    def set_sports_properties(self, sports_properties):
        self.sports_properties = sports_properties

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
    key = None

    def __init__(self, **kwargs):
        super(Base2Metadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            from .entities import Names, Sites
            self.names = Names(
                xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.sites = Sites(
                xmlelement.findall(NEWSMLG2_NS+'site')
            )
            from .sports_events import Awards
            self.awards = Awards(
                xmlelement.findall(NEWSMLG2_NS+'award')
            )
            self.key = xmlelement.get('key')
        elif kwargs:
            if 'names' in kwargs:
                self.set_names(kwargs['names'])
            if 'sites' in kwargs:
                self.set_sites(kwargs['sites'])
            if 'awards' in kwargs:
                self.set_awards(kwargs['awards'])

    def set_names(self, names):
        self.names = names

    def set_sites(self, sites):
        self.sites = sites

    def set_awards(self, awards):
        self.awards = awards

    def as_dict(self):
        super(Base2Metadata, self).as_dict()
        if self.names:
            self.dict.update({'names': self.names.as_dict() })
        if self.sites:
            self.dict.update({'sites': self.sites.as_dict() })
        if self.awards:
            self.dict.update({'awards': self.awards.as_dict() })
        if self.key:
            self.dict.update({'key': self.key })
        return self.dict


class SportsContentCodes(BaseObject):
    sports_content_codes = []

    def __init__(self, xmlarray=None, **kwargs):
        super(SportsContentCodes, self).__init__(**kwargs)
        self.sports_content_codes = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                scc = SportsContentCode(
                    xmlelement = xmlelement
                )
                self.sports_content_codes.append(scc)

    def as_dict(self):
        return [scc.as_dict() for scc in self.sports_content_codes]

    def __bool__(self):
        return len(self.sports_content_codes) != 0


class SportsContentCode(BaseObject):
    # TODO
    pass
    def as_dict(self):
        return { "SportsContentCode": "TODO" }


class SportsProperties(BaseObject):
    def __init__(self, xmlarray=None, **kwargs):
        super(SportsProperties, self).__init__(**kwargs)
        self.sports_properties = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                scc = SportsProperty(xmlelement)
                self.sports_properties.append(scc)

    def as_dict(self):
        return [sp.as_dict() for sp in self.sports_properties]

    def __bool__(self):
        return len(self.sports_properties) != 0

class SportsProperty(BaseObject):
    # TODO
    pass

    def as_dict(self):
        return None


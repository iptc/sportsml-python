#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS

class CommonAttributes(object):
    # An XML-specific identifier for the element.
    id = None
    # An open placeholder for categorization.
    class_attr = None
    # An open placeholder for reference by an external stylesheet.
    style = None

    def __init__(self, xmlelement=None, **kwargs):
        super(CommonAttributes, self).__init__(**kwargs)
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
        dict = {}
        if self.id:
            dict.update({'id': self.id})
        if self.class_attr:
            dict.update({'class': self.class_attr})
        if self.style:
            dict.update({'style': self.style})
        return dict


class CoverageAttributes(object):
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
        dict = super(CoverageAttributes, self).as_dict()
        # TODO
        return dict


class BaseMetadata(CommonAttributes, CoverageAttributes):
    """
    Basic metadata elements and attributes. Used directly by
    sports, standing, schedule and statistic and extended
    further by base2MetadataComplexType
    """
    def __init__(self, xmlelement=None, **kwargs):
        super(BaseMetadata, self).__init__(**kwargs)
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

    def __str__(self):
        return (
            '<SportsContent>'
        )

    def as_dict(self):
        dict = super(BaseMetadata, self).as_dict()
        # TODO
        return dict


class Base2Metadata(BaseMetadata):
    """
    Extends the baseMetadata with more elements and attributes. Used by baseEvent and baseTournament
    """
    names = None
    sites = None
    awards = None
    key = None

    def __init__(self, xmlelement=None, **kwargs):
        super(Base2Metadata, self).__init__(**kwargs)
        if type(xmlelement) == etree.Element:
            self.names = Names(
                xmlelement.findall(NEWSMLG2_NS+'name')
            )
            self.awards = Sites(
                xmlelement.findall(NEWSMLG2_NS+'site')
            )
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
        dict = super(Base2Metadata, self).as_dict()
        if self.names:
            dict.update({'names': names})
        if self.sites:
            dict.update({'sites': sites})
        if self.awards:
            dict.update({'awards': awards})
        return dict


class Sites(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.sites = []
        super(Sites, self).__init__(**kwargs)
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                site = Name(xmlelement)
                self.sites.append(site)

    def as_dict(self):
        return self.sites

    def __bool__(self):
        return len(self.sites) != 0

class Site(object):
    site = None

    def __init__(self, xmlarray=None, **kwargs):
        super(Sites, self).__init__(**kwargs)
        # TODO

    def as_dict(self):
        return self.site


class SportsContentCodes(object):

    def __init__(self, xmlarray=None, **kwargs):
        self.sports_content_codes = []
        super(SportsContentCodes, self).__init__(**kwargs)
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                scc = SportsContentCode(xmlelement)
                self.sports_content_codes.append(scc)

    def as_dict(self):
        return self.sports_content_codes

    def __bool__(self):
        return len(self.sports_content_codes) != 0


class SportsContentCode(object):
    # TODO
    pass


class SportsProperties(object):
    def __init__(self, xmlarray=None, **kwargs):
        self.sports_properties = []
        super(SportsProperties, self).__init__(**kwargs)
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                scc = SportsProperty(xmlelement)
                self.sports_properties.append(scc)

    def as_dict(self):
        return [sp.as_dict() for sp in self.sports_properties]

    def __bool__(self):
        return len(self.sports_properties) != 0

class SportsProperty(object):
    # TODO
    pass

    def as_dict(self):
        return None


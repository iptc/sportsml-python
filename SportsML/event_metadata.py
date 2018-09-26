#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject
from .base_metadata import Base2Metadata

class BaseEventState(BaseObject):
    """
    "baseEventStateAttributeGroup" in XML Schema
    """

    # Number of minutes that have elapsed since the beginning of the game.
    minutes_elapsed = None
    # The time elapsed, but only given as whole minutes.
    period_minute_elapsed = None
    # The time elapsed in the current period.
    period_time_elapsed = None
    # The time remaining in the current period.
    period_time_remaining = None

    def __init__(self, xmlelement=None, **kwargs):
        super(BaseEventState, self).__init__(**kwargs)
        if type(xmlelement) == etree.Element:
            self.minutes_elapsed = xmlelement.get('minutes-elapsed')
            self.period_minute_elapsed = xmlelement.get('period-minute-elapsed')
            self.period_time_elapsed = xmlelement.get('period-time-elapsed')
            self.period_time_remaining = xmlelement.get('period-time-remaining')

    def as_dict(self):
        super(BaseEventState, self).as_dict()
        if self.minutes_elapsed:
            self.dict.update({'minutesElapsed': self.minutes_elapsed })
        if self.period_minute_elapsed:
            self.dict.update({'periodMinuteElapsed': self.period_minute_elapsed })
        if self.period_time_elapsed:
            self.dict.update({'periodTimeElapsed': self.period_time_elapsed })
        if self.period_time_remaining:
            self.dict.update({'periodTimeRemaining': self.period_time_remaining })
        return self.dict


class BaseEventMetadata(Base2Metadata, BaseEventState):
    dict = {}
    event_sponsors = None
    event_recurring_names = None
    # The symbol for an identified sports-event that recurs every season.
    # This same key should be used from season to season.
    event_recurring_key = None
    # Indicates whether competitors are trying to defeat each other or just outdo one another.
    # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstyle/
    event_style = None
    # The ranked position this event had among other events.
    event_number = None
    # The stage of the event, describing whether it has started, is in progress, etc.
    # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstatus/
    event_status = None
    # The type of event, esp. in relation to tournament phase.
    # Recommended SportsML vocabulary uri: http://cv.iptc.org/newscodes/sptournamentphase/
    event_type = None
    # The reason for the event status. Eg. why the cancellation, postponement, etc.
    # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstatusreason
    event_status_reason = None
    # A textual description of the reason or context of the event-status or event-status-reason value.
    event_status_note = None
    # If the day had multiple events involving these competitors,
    # which event of the day it was. Example values: 1, 2, 3, etc.
    event_of_day = None
    # How many events involving these competitors have been planned for that day.
    events_day_total = None
    # Day of the week in which the game starts.
    start_weekday = None
    # Day of the week in which the game ends.
    end_weekday = None
    # The ranked position this heat had among other heats.
    heat_number = None
    # The length of time the event took place.
    duration = None
    # For TBA times.
    # enum: certain, to-be-announced
    time_certainty = None
    # The season this event is in.
    season_key = None
    # A subcategory of the season.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/spseasontype/
    season_type = None
    # The tournament division or series to which an event belongs.
    series_index = None
    # What type of outcome. Includes overtime, random (eg. by coin toss), etc.
    # SportsML vocab uri: http://cv.iptc.org/newscodes/speventoutcometype/
    event_outcome_type = None
    # To which round in the current competition this event belong.
    # (Added after decision at meeting 2017-06-13.)
    round_number = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(BaseEventMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.event_sponsors = EventSponsors(
                xmlelement.findall(NEWSMLG2_NS+'event-sponsor')
            )
            self.event_recurring_names = EventRecurringNames(
                xmlelement.findall(NEWSMLG2_NS+'event-recurring-name')
            )
            self.event_recurring_key = xmlelement.get('event-recurring-key')
            self.event_style = xmlelement.get('event-style')
            self.event_number = xmlelement.get('event-number')
            self.event_status = xmlelement.get('event-status')
            self.event_type = xmlelement.get('event-type')
            self.event_status_reason = xmlelement.get('event-status-reason')
            self.event_status_note = xmlelement.get('event-status-note')
            self.event_of_day = xmlelement.get('event-of-day')
            self.events_day_total= xmlelement.get('events-day-total')
            self.start_weekday= xmlelement.get('start-weekday')
            self.end_weekday= xmlelement.get('end-weekday')
            self.heat_number = xmlelement.get('heat-number')
            self.duration = xmlelement.get('duration')
            self.time_certainty = xmlelement.get('time-certainty')
            self.season_key = xmlelement.get('season-key')
            self.season_type = xmlelement.get('season-type')
            self.series_index = xmlelement.get('series-index')
            self.event_outcome_type = xmlelement.get('event-outcome-type')
            self.round_number = xmlelement.get('round-number')
        elif kwargs:
            pass

    def as_dict(self):
        super(BaseEventMetadata, self).as_dict()
        if self.event_sponsors:
            self.dict.update({ 'eventSponsors': self.event_sponsors.as_dict() })
        if self.event_recurring_names:
            self.dict.update({ 'eventRecurringNames': self.event_recurring_names.as_dict() })
        if self.event_recurring_key:
            self.dict.update({ 'eventRecurringKey': self.event_recurring_key })
        if self.event_style:
            self.dict.update({ 'eventStyle': self.event_style })
        if self.event_number:
            self.dict.update({ 'eventNumber': self.event_number })
        if self.event_status:
            self.dict.update({ 'eventStatus': self.event_status })
        if self.event_type:
            self.dict.update({ 'eventType': self.event_type })
        if self.event_status_reason:
            self.dict.update({ 'eventStatusReason': self.event_status_reason })
        if self.event_status_note:
            self.dict.update({ 'eventStatusNote': self.event_status_note })
        if self.event_of_day:
            self.dict.update({ 'eventOfDay': self.event_of_day })
        if self.events_day_total:
            self.dict.update({ 'eventsDayTotal': self.events_day_total })
        if self.start_weekday:
            self.dict.update({ 'startWeekday': self.start_weekday })
        if self.end_weekday:
            self.dict.update({ 'endWeekday': self.end_weekday })
        if self.heat_number:
            self.dict.update({ 'heatNumber': self.heat_number })
        if self.duration:
            self.dict.update({ 'duration': self.duration })
        if self.time_certainty:
            self.dict.update({ 'timeCertainty': self.time_certainty })
        if self.season_key:
            self.dict.update({ 'seasonKey': self.season_key })
        if self.season_type:
            self.dict.update({ 'seasonType': self.season_type })
        if self.series_index:
            self.dict.update({ 'seriesIndex': self.series_index })
        if self.event_outcome_type:
            self.dict.update({ 'eventOutcomeType': self.event_outcome_type })
        if self.round_number:
            self.dict.update({ 'roundNumber': self.round_number })
        return self.dict


class EventMetadata(BaseEventMetadata):
    """
    Background information about a game.
    Where, when, and what an event is.
    """

    pass

    """
    TODO: implement sport-specific event metadata:
    <xs:choice minOccurs="0">
        <xs:element name="event-metadata-american-football" type="americanFootballEventMetadataComplexType"/>
        <xs:element name="event-metadata-baseball" type="baseballEventMetadataComplexType"/>
        <xs:element name="event-metadata-golf" type="golfEventMetadataComplexType"/>
        <xs:element name="event-metadata-ice-hockey" type="iceHockeyEventMetadataComplexType"/>
        <xs:element name="event-metadata-soccer" type="soccerEventMetadataComplexType"/>
        <xs:element name="event-metadata-tennis" type="tennisEventMetadataComplexType"/>
        <xs:element name="event-metadata-motor-racing" type="motorRacingEventMetadataComplexType"/>
        <xs:element name="event-metadata-curling" type="curlingEventMetadataComplexType"/>
        <xs:element name="event-metadata-rugby" type="rugbyEventMetadataComplexType"/>
    </xs:choice>
    """


class EventSponsors(BaseObject):
    event_sponsors = []

    def __init__(self, xmlarray=None, **kwargs):
        self.event_sponsors = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                es = EventSponsor(xmlelement=xmlelement)
                self.event_sponsors.append(es)

    def as_dict(self):
        return [ es.as_dict() for es in self.event_sponsors ]

    def __bool__(self):
        return len(self.event_sponsors) != 0


class EventSponsor(BaseObject):
    # TODO
    def __init__(self, xmlelement=None, **kwargs):
        super(EventSponsor, self).__init__(**kwargs)


class EventRecurringNames(BaseObject):
    event_recurring_names = []

    def __init__(self, xmlarray=None, **kwargs):
        self.event_recurring_names = []
        if type(xmlarray) == list:
            for xmlelement in xmlarray:
                es = EventRecurringName(xmlelement=xmlelement)
                self.event_recurring_names.append(es)

    def as_dict(self):
        return [ es.as_dict() for es in self.event_recurring_names ]

    def __bool__(self):
        return len(self.event_recurring_names) != 0


class EventRecurringName(BaseObject):
    # TODO
    def __init__(self, xmlelement=None, **kwargs):
        super(EventRecurringName, self).__init__(**kwargs)

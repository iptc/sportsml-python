#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject, GenericArray
from .base_metadata import Base2Metadata


class BaseEventStateAttributes(BaseObject):
    """
    Called "baseEventStateAttributeGroup" in XML Schema
    """
    attributes = {
        # Number of minutes that have elapsed since the beginning of the game.
        'minutes-elapsed': 'minutesElapsed',
        # The time elapsed, but only given as whole minutes.
        'period-minute-elapsed': 'periodMinuteElapsed',
        # The time elapsed in the current period.
        'period-time-elapsed': 'periodTimeElapsed',
        # The time remaining in the current period.
        'period-time-remaining': 'periodTimeRemaining',
    }


class BaseEventMetadata(Base2Metadata, BaseEventStateAttributes):
    event_sponsors = None
    event_recurring_names = None
    attributes = {
        # The symbol for an identified sports-event that recurs every season.
        # This same key should be used from season to season.
        'event-recurring-key': 'eventRecurringKey',
        # Indicates whether competitors are trying to defeat each other or just outdo one another.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstyle/
        'event-style': 'eventStyle',
        # The ranked position this event had among other events.
        'event-number': 'eventNumber',
        # The stage of the event, describing whether it has started, is in progress, etc.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstatus/
        'event-status': 'eventStatus',
        # The type of event, esp. in relation to tournament phase.
        # Recommended SportsML vocabulary uri: http://cv.iptc.org/newscodes/sptournamentphase/
        'event-type': 'eventType',
        # The reason for the event status. Eg. why the cancellation, postponement, etc.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/speventstatusreason
        'event-status-reason': 'eventStatusReason',
        # A textual description of the reason or context of the event-status or event-status-reason value.
        'event-status-note': 'eventStatusNote',
        # If the day had multiple events involving these competitors,
        # which event of the day it was. Example values: 1, 2, 3, etc.
        'event-of-day': 'eventOfDay',
        # How many events involving these competitors have been planned for that day.
        'events-day-total': 'eventsDayTotal',
        # Day of the week in which the game starts.
        'start-weekday': 'startWeekday',
        # Day of the week in which the game ends.
        'end-weekday': 'endWeekday',
        # The ranked position this heat had among other heats.
        'heat-number': 'heatNumber',
        # The length of time the event took place.
        'duration': 'duration',
        # For TBA times.
        # enum: certain, to-be-announced
        'time-certainty': 'timeCertainty',
        # The season this event is in.
        'season-key': 'seasonKey',
        # A subcategory of the season.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/spseasontype/
        'season-type': 'seasonType',
        # The tournament division or series to which an event belongs.
        'series-index': 'seriesIndex',
        # What type of outcome. Includes overtime, random (eg. by coin toss), etc.
        # SportsML vocab uri: http://cv.iptc.org/newscodes/speventoutcometype/
        'event-outcome-type': 'eventOutcomeType',
        # To which round in the current competition this event belong.
        # (Added after decision at meeting 2017-06-13.)
        'round-number': 'roundNumber'
    }
    attribute_types = {
        'event-number': 'integer',
    }

    def __init__(self, **kwargs):
        super(BaseEventMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.event_sponsors = EventSponsors(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'event-sponsor')
            )
            self.event_recurring_names = EventRecurringNames(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'event-recurring-name')
            )

    def as_dict(self):
        super(BaseEventMetadata, self).as_dict()
        if self.event_sponsors:
            self.dict.update({ 'eventSponsors': self.event_sponsors.as_dict() })
        if self.event_recurring_names:
            self.dict.update({ 'eventRecurringNames': self.event_recurring_names.as_dict() })
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


class EventSponsor(BaseObject):
    # TODO
    def __init__(self,  **kwargs):
        super(EventSponsor, self).__init__(**kwargs)


class EventSponsors(GenericArray):
    """
    Array of EventSponsor objects.
    """
    element_class= EventSponsor


class EventRecurringName(BaseObject):
    # TODO
    def __init__(self, **kwargs):
        super(EventRecurringName, self).__init__(**kwargs)


class EventRecurringNames(GenericArray):
    """
    Array of EventRecurringName objects.
    """
    element_class= EventRecurringName

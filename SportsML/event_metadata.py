#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS
from .base_metadata import Base2Metadata

class BaseEventState(object):
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


class EventMetadata(Base2Metadata, BaseEventState):
    event_sponsors = None
    event_recurring_names = None
    event_recurring_key = None
    event_style = None
    event_number = None
    event_status = None
    event_type = None
    event_status_reason = None
    event_status_note = None
    event_of_day = None
    events_day_total = None
    start_weekday = None
    end_weekday = None
    heat_number = None
    duration = None
    # enum: certain, to-be-announced
    time_certainty = None
    season_key = None
    season_type = None
    series_index = None
    event_outcome_type = None
    round_number = None

    def __init__(self, xmlelement=None, **kwargs):
        super(EventMetadata, self).__init__(**kwargs)
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

    def __str__(self):
        return (
            '<SportsContent>'
        )

    def as_dict(self):
        return {
            'aa': 'bb'
        }

class EventSponsors(object):
    event_sponsors = []

    def __init__(self, xmlelement=None, **kwargs):
        super(EventSponsors, self).__init__(**kwargs)

class EventSponsor(object):
    def __init__(self, xmlelement=None, **kwargs):
        super(EventSponsor, self).__init__(**kwargs)

class EventRecurringNames(object):
    event_recurring_names = []

    def __init__(self, xmlelement=None, **kwargs):
        super(EventRecurringNames, self).__init__(**kwargs)

class EventRecurringName(object):
    pass
    def __init__(self, xmlelement=None, **kwargs):
        super(EventRecurringName, self).__init__(**kwargs)

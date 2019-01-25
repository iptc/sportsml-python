#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS, GenericArray
from .base_metadata import BaseMetadata, CommonAttributes


class ScheduleMetadata(BaseMetadata):
    """
    Background information about the schedule.
    Describes the time period which the schedule covers, and which teams or events may be covered.
    """
    pass

class Schedule(CommonAttributes):
    """
    A series of games.
    Usually grouped by date.
    """
    attributes = {
        # Displayable label that describes what dates this schedule covers.
        'date-label': 'dateLabel',
        # Displayable label that describes what events this schedule includes.
        'content-label': 'contentLabel'
    }

    def __init__(self, **kwargs):
        super(Schedule, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.schedule_metadata = ScheduleMetadata(
                xmlelement = xmlelement.find(NEWSMLG2_NS+'schedule-metadata')
            )
            self.sports_events = SportsEvents(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-event')
            )

    def as_dict(self):
        super(Schedule, self).as_dict()
        self.dict.update({'scheduleMetadata': self.schedule_metadata.as_dict() })
        self.dict.update({'sportsEvents': self.sports_events.as_dict() })
        return self.dict


class Schedules(GenericArray):
    """
    Array of Schedule objects.
    """
    element_class= Schedule

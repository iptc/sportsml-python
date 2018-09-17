#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import NEWSMLG2_NS
from .sports_metadata import SportsMetadata
from .event_metadata import EventMetadata
from .base_metadata import CommonAttributes, CoverageAttributes, Sites, SportsContentCodes


class TimeValidityAttributes(object):
    def __init__(self, xmlelement=None, **kwargs):
        # TODO
        pass

    def as_dict(self):
        dict = {}
        # TODO
        return dict


class ConceptNameType(TimeValidityAttributes):
    """
    The type of a natural language name for the concept (Type defined in this XML Schema only)

    TODO - extends IntlStringType
    """
    name = None
    # A refinement of the semantics of the name - expressed by a QCode
    role = None
    # A refinement of the semantics of the name - expressed by a URI
    roleuri = None
    # Specifies which part of a full name this property provides - expressed by a QCode
    part = None
    # Specifies which part of a full name this property provides - expressed by a URI
    parturi = None
    
    def __init__(self, xmlelement=None, **kwargs):
        super(ConceptNameType, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            self.name = xmlelement.text
            self.role = xmlelement.get('role')
            self.roleuri = xmlelement.get('roleuri')
            self.part = xmlelement.get('part')
            self.parturi = xmlelement.get('parturi')

    def as_dict(self):
        dict = super(ConceptNameType, self).as_dict()
        if self.name:
            dict.update({'name': self.name})
        if self.role:
            dict.update({'role': self.role})
        if self.roleuri:
            dict.update({'roleuri': self.roleuri})
        if self.part:
            dict.update({'part': self.part})
        if self.parturi:
            dict.update({'parturi': self.parturi})
        return dict


class FlexAttributes(object):
    pass

class CommonPowerAttributes(object):
    pass

class I18NAttributes(object):
    pass

class FlexLocationPropType(object):
    """
    Flexible location (geopolitical area of point-of-interest)
    data type for both controlled and uncontrolled values
    plus: <xs:anyAttribute namespace="##other" processContents="lax" />
    """

    def __init__(self, xmlelement=None, **kwargs):
        # super(FlexLocationPropType, self).__init__(xmlelement, **kwargs)
        if type(xmlelement) == etree.Element:
            # TODO <xs:group ref="ConceptDefinitionGroup" minOccurs="0" />
            # TODO <xs:group ref="ConceptRelationshipsGroup" minOccurs="0" />
            pass

    def as_dict(self):
        # TODO
        return None

    def __bool__(self):
        # TODO
        return False

    """
    <xs:complexType name="FlexLocationPropType">
        <xs:sequence>
            <xs:choice minOccurs="0">
                <xs:element ref="geoAreaDetails" />
                <xs:element ref="POIDetails" />
            </xs:choice>
            <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Extension point for provider-defined properties from other namespaces</xs:documentation>
                </xs:annotation>
            </xs:any>
        </xs:sequence>
    </xs:complexType>
    """

#!/usr/bin/env python

import xml.etree.ElementTree as etree
import json

from .core import BaseObject


class TimeValidityAttributes(BaseObject):
    def __init__(self, **kwargs):
        super(TimeValidityAttributes, self).__init__(**kwargs)
        # TODO
        pass

    def as_dict(self):
        super(TimeValidityAttributes, self).as_dict()
        # TODO
        return self.dict


class IntlStringType(BaseObject):
    # TODO
    pass

class ConceptNameType(TimeValidityAttributes, IntlStringType):
    """
    The type of a natural language name for the concept (Type defined in this XML Schema only)
    """
    name = None
    attributes = {
        # A refinement of the semantics of the name - expressed by a QCode
        'role': 'role',
        # A refinement of the semantics of the name - expressed by a URI
        'roleuri': 'roleuri',
        # Specifies which part of a full name this property provides - expressed by a QCode
        'part': 'part',
        # Specifies which part of a full name this property provides - expressed by a URI
        'parturi': 'parturi'
    }
    
    def __init__(self, **kwargs):
        super(ConceptNameType, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.name = xmlelement.text

    def as_dict(self):
        super(ConceptNameType, self).as_dict()
        if self.name:
            self.dict.update({'name': self.name})
        return self.dict


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

    def __init__(self, **kwargs):
        # super(FlexLocationPropType, self).__init__(xmlelement, **kwargs)
        xmlelement = kwargs.get('xmlelement')
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


class CatalogRef(BaseObject):
    """
    A reference to a remote catalog. A hyperlink to a set of scheme alias declarations.
    """
    attributes = {
        # A short natural language name for the catalog.
        'title': 'title',
        # A hyperlink to a remote Catalog.
        'href': 'href'
    }


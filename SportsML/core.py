#!/usr/bin/env python

import importlib
import xml.etree.ElementTree as etree

NEWSMLG2_NS = '{http://iptc.org/std/nar/2006-10-01/}'
NITF_NS = '{http://iptc.org/std/NITF/2006-10-18/}'

VERSION = 0.1

class BaseObject():
    # required for multiple inheritance to work propertly.
    # probably helpful in the future for other objects too.
    def __init__(self, **kwargs):
        pass

    def as_dict(self):
        return


class GenericArray(BaseObject):
    """
    Helper class to handle arrays of objects.
    To be subclassed by every array class.
    Subclass defines object class either as a reference in 'element_class',
    or by module and class name in strings as 'element_module_name' and
    'element_class_name'
    """
    array_contents = []
    element_module_name = None
    element_class_name = None
    element_class = None

    def __init__(self, **kwargs):
        self.array_contents = []
        xmlarray = kwargs.get('xmlarray')
        if type(xmlarray) == list or type(xmlarray) == etree.Element:
            if not self.element_class:
                self.element_class = getattr(
                    importlib.import_module(self.element_module_name),
                    self.element_class_name
                )
            for xmlelement in xmlarray:
                # array_elem = self.element_class_name(xmlelement)
                array_elem = self.element_class(xmlelement = xmlelement)
                self.array_contents.append(array_elem)

    def __str__(self):
        return (
            '<GenericArray of ' +
            len(self.array_contents) + ' ' +
            self.element_class_name +' objects>'
        )

    def __bool__(self):
        return len(self.array_contents) != 0

    def as_dict(self):
        return [ elem.as_dict() for elem in self.array_contents ]

    def to_json(self):
        return json.dumps(self.as_dict(), indent=4)

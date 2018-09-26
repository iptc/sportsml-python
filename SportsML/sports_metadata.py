#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject
from .base_metadata import BaseMetadata, CommonAttributes


class CatalogRefs(BaseObject):
    pass

class SportsTitles(BaseObject):
    pass

class SportsTitle(BaseObject):
    pass

class Advisory(CommonAttributes):
    dict = {}
    pass

class FeatureNames(BaseObject):
    pass

class FeatureName(BaseObject):
    pass

class SportsMetadata(BaseMetadata):
    dict = {}
    # A reference to document(s) listing externally-supplied controlled vocabularies.
    # The catalog file can be in NewsML 1.
    catalog_refs = None
    # A short textual description of the document.
    # Can  show up in search results.
    sports_titles = None    
    # A short textual message to editors receiving the document.
    # Not generally published through to end-users.
    advisory = None
    # A displayable name for the resource identified by the fixture-key.
    feature_names = None
    # The often-unique ID of the document, tracked by publishers.
    doc_id = None
    # Publisher of the data.
    publisher = None
    # Date-timestamp for the document, normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available
    date_time = None
    # The default language of the document. NAR-construction. Values must be valid BCP 47 language tags.
    language = None
    # A keyword used by editors to refer to the document.
    slug = None
    # A category code for the document type (fixture-key).
    # Recommended categories contained in SportsML vocabulary uri: http://cv.iptc.org/newscodes/spct/
    document_class = None
    # A publisher-specific key for the type of regularly-published document
    # (or genre) being transmitted. Eg. event-stats, roster, standings (table), etc.
    # SportsML vocabulary uri: http://cv.iptc.org/newscodes/spfixt/
    fixture_key = None

    def __init__(self, **kwargs):
        self.dict = {}
        super(SportsMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.catalog_refs = CatalogRefs(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'catalogRef')
            )
            self.sports_titles = SportsTitles(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-title')
            )
            self.advisory = Advisory(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'advisory')
            )
            self.feature_names = FeatureNames(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'feature-name')
            )
            self.doc_id = xmlelement.get('doc-id')
            self.publisher = xmlelement.get('publisher')
            self.date_time = xmlelement.get('date-time')
            self.language = xmlelement.get('language')
            self.slug = xmlelement.get('slug')
            self.document_class = xmlelement.get('document-class')
            self.fixture_key = xmlelement.get('fixture-key')

    def as_dict(self):
        dict = super(SportsMetadata, self).as_dict()
        if self.catalog_refs:
            self.dict.update({'catalogRefs': self.catalog_refs.as_dict() })
        if self.sports_titles:
            self.dict.update({'sportsTitles': self.sports_titles.as_dict() })
        if self.advisory:
            self.dict.update({'advisory': self.advisory.as_dict() })
        if self.feature_names:
            self.dict.update({'featureNames': self.feature_names.as_dict() })
        if self.doc_id:
            self.dict.update({'docId': self.doc_id })
        if self.publisher:
            self.dict.update({'publisher': self.publisher })
        if self.date_time:
            self.dict.update({'dateTime': self.date_time })
        if self.language:
            self.dict.update({'language': self.language })
        if self.slug:
            self.dict.update({'slug': self.slug })
        if self.document_class:
            self.dict.update({'documentClass': self.document_class })
        if self.fixture_key:
            self.dict.update({'fixtureKey': self.fixture_key })
        return self.dict

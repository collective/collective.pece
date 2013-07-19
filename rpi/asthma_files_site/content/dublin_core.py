from zope.schema import TextLine


# XXX Poor man's Dublin Core (re)implementation
_coverage = TextLine(title=u"Coverage", required=False)

_format = TextLine(title=u"Format", required=False)

_identifier = TextLine(title=u"Identifier", required=False)

_language = TextLine(title=u"Language", required=False)

_publisher = TextLine(title=u"Publisher", required=False)

_relation = TextLine(title=u"Relation", required=False)

_rights = TextLine(title=u"Rights", required=False)

_source = TextLine(title=u"Source", required=False)

_subject = TextLine(title=u"Subject", required=False)

_type = TextLine(title=u"Type", required=False)

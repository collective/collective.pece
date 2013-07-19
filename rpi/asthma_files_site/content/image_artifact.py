from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from zope.schema import TextLine

# XXX Poor man's Dublin Core (re)implementation
#from .dublin_core import _coverage
#from .dublin_core import _format
#from .dublin_core import _identifier
#from .dublin_core import _language
#from .dublin_core import _publisher
#from .dublin_core import _relation
#from .dublin_core import _rights
#from .dublin_core import _source
#from .dublin_core import _subject
#from .dublin_core import _type


class IImageArtifact(form.Schema):
    """
    Content type
    """

    image_artifact = NamedBlobImage(title=u"Image Artifact")

    # XXX Poor man's Dublin Core (re)implementation
#    coverage = _coverage
#    dublin_core_format = _format
#    identifier = _identifier
#    language = _language
#    publisher = _publisher
#    relation = _relation
#    rights = _rights
#    source = _source
#    subject = _subject
#    dublin_core_type = _type





    # XXX Poor man's Dublin Core (re)implementation
    coverage = TextLine(title=u"Coverage", required=False)

    dublin_core_format = TextLine(title=u"Format", required=False)

    identifier = TextLine(title=u"Identifier", required=False)

    language = TextLine(title=u"Language", required=False)

    publisher = TextLine(title=u"Publisher", required=False)

    relation = TextLine(title=u"Relation", required=False)

    rights = TextLine(title=u"Rights", required=False)

    source = TextLine(title=u"Source", required=False)

    subject = TextLine(title=u"Subject", required=False)

    dublin_core_type = TextLine(title=u"Type", required=False)

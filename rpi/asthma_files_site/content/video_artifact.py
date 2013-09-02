from plone.directives import form
from plone.namedfile.field import NamedBlobFile
from zope.schema import TextLine


class IVideoArtifact(form.Schema):
    """
    Content type
    """

    video_artifact = NamedBlobFile(title=u"Video Artifact")
    form.primary('video_artifact')

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

from plone.directives import form
from plone.namedfile.field import NamedBlobFile
from zope.schema import TextLine


class IAudioArtifact(form.Schema):
    """
    Content type
    """

    # XXX How else can I make title field optional (i.e. without turning
    # off dublin core behavior and re-implementing the same
    # fields it already provides for me)?
    title = TextLine(title=u"Title", required=False)
    description = TextLine(title=u"Description", required=False)

    audio_artifact = NamedBlobFile(title=u"Audio Artifact")
    form.primary('audio_artifact')

    coverage = TextLine(title=u"Coverage", required=False)

    format_ = TextLine(title=u"Format", required=False)

    identifier = TextLine(title=u"Identifier", required=False)

    language = TextLine(title=u"Language", required=False)

    publisher = TextLine(title=u"Publisher", required=False)

    relation = TextLine(title=u"Relation", required=False)

    rights = TextLine(title=u"Rights", required=False)

    source = TextLine(title=u"Source", required=False)

    subject = TextLine(title=u"Subject", required=False)

    type_ = TextLine(title=u"Type", required=False)

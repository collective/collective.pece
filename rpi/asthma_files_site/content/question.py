from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from zope.schema import TextLine


class IQuestion(form.Schema):
    """
    Content type
    """

    title = TextLine(title=u"Question", required=True)

from plone.directives import form
from zope.schema import TextLine


class IAsthmaQuestion(form.Schema):
    """
    Content type
    """

    title = TextLine(title=u"Question", required=True)

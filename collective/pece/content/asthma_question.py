from plone.directives import form
from zope.schema import TextLine


class IAsthmaQuestion(form.Schema):
    """
    Questions facilitate Annotations of Artifacts when researchers respond to
    them in context.
    """

    title = TextLine(title=u"Question", required=True)

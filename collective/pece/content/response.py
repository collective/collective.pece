from plone.app.textfield import RichText
from plone.directives import form
from plone.supermodel import model
from zope.schema import TextLine


class IResponse(model.Schema, form.Schema):
    """
    Questions facilitate Annotations of Artifacts when researchers respond to
    them in context.
    """

    title = TextLine(title=u"Question", required=True)

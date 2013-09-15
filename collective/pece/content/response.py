from plone.app.textfield import RichText
from plone.supermodel import model


class IResponse(model.Schema):
    """
    """

    body = RichText(title=u"Response")

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile as view_with_template
from zope.publisher.browser import BrowserPage as View


class ImageArtifactView():
    """
    """
    def __call__(self):
        return view_with_template('image_artifact_view.pt')(self)

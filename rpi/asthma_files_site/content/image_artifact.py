from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import base64


class ImageArtifactView():
    """
    """

    image_artifact_view = ViewPageTemplateFile('image_artifact_view.pt')

    def __call__(self):
        return self.image_artifact_view()

    def get_image(self):
        return "data:%s;base64,%s" % (self.context.image.contentType,
            base64.encodestring(self.context.image.data))

    def get_questions(self):
        return self.context.portal_catalog(portal_type="question")

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ImageArtifactView():
    """
    Return a list of questions
    """

    image_artifact_view = ViewPageTemplateFile('image_artifact_view.pt')

    def __call__(self):
        return self.image_artifact_view()

    def get_image(self):
        return "data:%s;%s" % (self.context.image.contentType,
            self.context.image.data)

    def get_questions(self):
        return self.context.portal_catalog(portal_type="question")

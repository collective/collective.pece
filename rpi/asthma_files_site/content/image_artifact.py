from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.dexterity.utils import createContentInContainer
from zope.annotation.interfaces import IAnnotations as IStorage  # Avoid
                                # confusion with annotation content type


class ImageArtifactView():
    """
    """

    image_artifact_view = ViewPageTemplateFile('image_artifact.pt')

    def __call__(self):
        """
        """
        if self.request.method == 'POST':
            annotation = createContentInContainer(self.context, 'annotation')
            for uid, question in self.request.form.items():
                response = createContentInContainer(annotation, 'response')
                storage = IStorage(response)
                storage[uid] = question
        return self.image_artifact_view()

    def get_questions(self):
        """
        """
        return self.context.portal_catalog(
            portal_type="question", sort_on="id", sort_order="ascending")

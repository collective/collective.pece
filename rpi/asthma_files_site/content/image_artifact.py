from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.uuid.utils import uuidToObject
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
        new_question = False
        if self.request.method == 'POST':
            questions = []
            items = self.request.form.items()
            for item, text in items:
                if item != 'new-question':  
                    questions.append((item, text))
                else:  # Add another question
                    new_question = True
            annotation = createContentInContainer(self.context, 'annotation')
            for uid, text in questions:
                if text is not '':
                    question = uuidToObject(uid)
                    question = question.Title()
                    title = "Response to %s"
                    response = createContentInContainer(
                        annotation, 'response', title=title % question)
                    storage = IStorage(response)
                    storage[uid] = question
                    response.description = text

            if new_question:
                portal = self.context.portal_url()
                self.request.response.redirect("%s/++add++question" % portal)
        return self.image_artifact_view()

    def get_questions(self):
        """
        """
        return self.context.portal_catalog(
            portal_type="question", sort_on="id", sort_order="ascending")

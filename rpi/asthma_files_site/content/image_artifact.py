from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.uuid.utils import uuidToObject
from plone.dexterity.utils import createContentInContainer
from zope.annotation.interfaces import IAnnotations as IStorage  # Avoid
                                # confusion with annotation content type


class ImageArtifactEditTags():
    """
    Browser page
    """

    def __call__(self):
        """
        Set tags; redirect to context
        """
        tags = self.request.form.get('tags').split('\r\n')
        self.context.setSubject(tags)
        self.context.reindexObject()
        return self.request.response.redirect(self.context.absolute_url())


class ImageArtifactView():
    """
    Browser page
    """

    image_artifact_view = ViewPageTemplateFile('image_artifact.pt')

    def __call__(self):
        """
        Return the view template; handle form posts
        """
        add_another_question = False
        if self.request.method == 'POST':
            questions = []
            items = self.request.form.items()  # XXX Why not use .get()?
            for item, text in items:  # Add another question?
                if item != 'new-question':  # No
                    questions.append((item, text))
                else:  # Yes
                    add_another_question = True
            annotation = createContentInContainer(self.context, 'annotation')
            for uid, text in questions:  # Process questions
                if text is not '':
                    question = uuidToObject(uid)
                    question = question.Title()
                    title = "Response to %s"
                    response = createContentInContainer(
                        annotation, 'response', title=title % question)
                    storage = IStorage(response)
                    storage[uid] = question
                    response.description = text
            if add_another_question:
                portal = self.context.portal_url()
                self.request.response.redirect("%s/++add++question" % portal)
        return self.image_artifact_view()

    def get_questions(self):
        """
        Return content items of type "question" from the catalog
        """
        return self.context.portal_catalog(
            portal_type="question", sort_on="id", sort_order="ascending")

    def get_tags(self):
        """
        Return tags as a string separated by newlines
        """
        return '\n'.join(self.context.Subject())

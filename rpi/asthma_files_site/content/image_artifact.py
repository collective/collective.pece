from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.uuid.utils import uuidToObject
from plone.dexterity.utils import createContentInContainer
from plone.directives import form
from zope.annotation.interfaces import IAnnotations as IStorage  # Avoid
                                # confusion with annotation content type


class IImageArtifact(form.Schema):
    """
    """

#    <property
##    name="model_source">&lt;model xmlns:security="http://namespaces.plone.org/supermodel/security" xmlns:marshal="http://namespaces.plone.org/supermodel/marshal" xmlns:form="http://namespaces.plone.org/supermodel/form" xmlns="http://namespaces.plone.org/supermodel/schema"&gt;
#    &lt;schema&gt;
#      &lt;field name="image" type="plone.namedfile.field.NamedBlobImage"&gt;
#        &lt;description/&gt;
#        &lt;title&gt;Image&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="coverage" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Coverage&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="format" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Format&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="identifier" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Identifier&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="language" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Language&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="publisher" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Publisher&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="relation" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Relation&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="rights" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Rights&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="source" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Source&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="subject" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Subject&lt;/title&gt;
#      &lt;/field&gt;
#      &lt;field name="dublin_core_type" type="zope.schema.TextLine"&gt;
#        &lt;description/&gt;
#        &lt;required&gt;False&lt;/required&gt;
#        &lt;title&gt;Type&lt;/title&gt;
#      &lt;/field&gt;
#    &lt;/schema&gt;
#  &lt;/model&gt;</property>


class ImageArtifactEditMetadata():
    """
    Browser page
    """

    def __call__(self):
        """
        Set metadata; redirect to context
        """
        contributor = self.request.form.get('contributor').split('\r\n')
        self.context.contributors = contributor

        coverage = self.request.form.get('coverage')
        self.context.coverage = coverage

        creator = self.request.form.get('creator').split('\r\n')
        self.context.creators = creator

        description = self.request.form.get('description')
        self.context.description = description

        identifier = self.request.form.get('identifier')
        self.context.identifier = identifier

        publisher = self.request.form.get('publisher')
        self.context.publisher = publisher

        relation = self.request.form.get('relation')
        self.context.relation = relation

        rights = self.request.form.get('rights')
        self.context.rights = rights

        source = self.request.form.get('source')
        self.context.source = source

        dublin_core_type = self.request.form.get('dublin_core_type')  # type
        self.context.dublin_core_type = dublin_core_type  # is a reserved word

        self.context.reindexObject()

        return self.request.response.redirect(self.context.absolute_url())


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

    def get_contributor(self):
        """
        Return contributor field as a string separated by newlines
        """
        return '\n'.join(self.context.Contributors())

    def get_creator(self):
        """
        Return creator field as a string separated by newlines
        """
        return '\n'.join(self.context.creators)

    def get_tags(self):
        """
        Return tags as a string separated by newlines
        """
        return '\n'.join(self.context.Subject())

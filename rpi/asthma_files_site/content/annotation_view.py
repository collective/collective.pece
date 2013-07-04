from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class AnnotationView():
    """
    """

    annotation_view = ViewPageTemplateFile('annotation_view.pt')

    def __call__(self):
        """
        """
        return self.annotation_view()

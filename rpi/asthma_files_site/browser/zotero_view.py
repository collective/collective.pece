from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.publisher.browser import BrowserPage


class ZoteroView(BrowserPage):
    """
    Browser page
    """
    zotero_view = ViewPageTemplateFile('zotero_view.pt')

    def __call__(self):
        return self.zotero_view

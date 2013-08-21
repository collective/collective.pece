from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from pyzotero import zotero

from zope.publisher.browser import BrowserPage

import os


library_id = os.environ.get('ZOTERO_LIBRARY_ID', 'null')
library_type = os.environ.get('ZOTERO_LIBRARY_TYPE', 'group')
api_key = os.environ.get('ZOTERO_API_KEY', 'null')


class ZoteroView(BrowserPage):
    """
    Browser page
    """
    zotero_view = ViewPageTemplateFile('zotero_view.pt')
#    zotero_library = zotero.Zotero(library_id, library_type, api_key)

    def __call__(self):
        return self.zotero_view()


#    def get_tags(self):
#        return self.zotero_library.tags()

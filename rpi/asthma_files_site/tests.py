from Products.PloneTestCase import PloneTestCase


PloneTestCase.setupPloneSite(
    extension_profiles=('rpi.asthma_files_site:default',)
)


class TestAsthmaFilesSiteContentTypes(PloneTestCase.PloneTestCase):
    """
    Test Asthma Files Site content types
    """

    def test_add_document_artifact(self):
        """
        Test add document artifact to folder
        """
        self.folder.invokeFactory('document_artifact', 'asthma.pdf')
        assert 'asthma.pdf' in self.folder

    def test_add_image_artifact(self):
        """
        Test add image artifact to folder
        """
        self.folder.invokeFactory('image_artifact', 'asthma.jpg')
        assert 'asthma.jpg' in self.folder


if __name__ == '__main__':
    unittest.main()

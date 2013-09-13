from Products.PloneTestCase import PloneTestCase


PloneTestCase.setupPloneSite(
    extension_profiles=('collective.pece:default',)
)


class TestAsthmaFilesSiteContentTypes(PloneTestCase.PloneTestCase):
    """
    Test Asthma Files Site content types
    """

    def test_add_asthma_file(self):
        """
        Test add asthma file to folder
        """
        self.folder.invokeFactory(
            'asthma_file', 'distinctively-simplify-leading-edge-sources')
        assert 'distinctively-simplify-leading-edge-sources' in self.folder

    def test_add_asthma_question(self):
        """
        Test add asthma question to folder
        """
        self.folder.invokeFactory(
            'asthma_question', 'proactively-pursue-enabled-technology')
        assert 'proactively-pursue-enabled-technology' in self.folder

    def test_add_audio_artifact(self):
        """
        Test add audio artifact to folder
        """
        self.folder.invokeFactory('audio_artifact', 'asthma.ogg')
        assert 'asthma.ogg' in self.folder

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

    def test_add_video_artifact(self):
        """
        Test add video artifact to folder
        """
        self.folder.invokeFactory('video_artifact', 'asthma.ogv')
        assert 'asthma.ogv' in self.folder

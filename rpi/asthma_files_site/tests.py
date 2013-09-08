from Products.PloneTestCase import PloneTestCase


PloneTestCase.setupPloneSite(
    extension_profiles=('rpi.asthma_files_site:default',)
)


class TestAsthmaFilesSite(PloneTestCase.PloneTestCase):
    """
    """

    def test_add_artifact_image(self):
        """
        """
        self.folder.invokeFactory('image_artifact', 'asthma.jpg')
        assert 'asthma.jpg' in self.folder


if __name__ == '__main__':
    unittest.main()

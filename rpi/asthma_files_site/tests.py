from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
import unittest


class Fixture(PloneSandboxLayer):
    """
    """

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'rpi.asthma_files_site:default')


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='rpi.asthma_files_site:Integration',
    )


class TestAsthmaFilesSite(unittest.TestCase):
    """
    """

    layer = INTEGRATION_TESTING

    def test_add_artifact_image(self):
        """
        """
        import pdb ; pdb.set_trace()


if __name__ == '__main__':
    unittest.main()

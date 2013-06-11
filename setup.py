from setuptools import find_packages
from setuptools import setup


setup(
    name='rpi.asthma_files_site',
    package=find_packages(),
    namespace_package=['rpi'],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    }
)

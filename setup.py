from setuptools import find_packages
from setuptools import setup


setup(
    name='rpi.asthma_files_site',
    packages=find_packages(),
    namespace_packages=['rpi'],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    install_requires=[
        'setuptools',
        'collective.documentviewer',
        'five.grok',
        'plone.app.referenceablebehavior',
        'pyzotero',
        'z3c.jbot',
    ],
)

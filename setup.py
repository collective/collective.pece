from setuptools import find_packages
from setuptools import setup


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    description="Asthma Files Site",
    long_description=open("README.rst").read(),
    name='rpi.asthma_files_site',
    packages=find_packages(),
    namespace_packages=['rpi'],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    install_requires=[
        'setuptools',
        'collective.cover',
        'five.grok',
        'pyzotero',
        'z3c.jbot',
    ],
)

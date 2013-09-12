from setuptools import find_packages
from setuptools import setup


VERSION="0.0.5"


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    classifiers=[
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python :: 2.7",
    ],
    description="The Platform for Experimental Collaborative Ethnography (PECE)",
    keywords=[
        "Plone",
    ],
    license="GPL",
    long_description=(
        open("README.rst").read() + '\n' +
        open("CHANGES.rst").read()
        ),
    name='rpi_pece',
    packages=find_packages(),
    test_suite="rpi_pece.tests",
    url="https://github.com/ACLARKNET/rpi_pece",
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
        'collective.cover',
        'collective.documentviewer',
        'five.grok',
        'pyzotero',
        'z3c.jbot',
    ],
    version=VERSION,
    zip_safe=True,
)

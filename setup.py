from setuptools import find_packages
from setuptools import setup


VERSION="0.0.4"


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    classifiers=[
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python :: 2.7",
    ],
    description="Asthma Files Site",
    keywords=[
        "Plone",
    ],
    license="GPL",
    long_description=(
        open("README.rst").read() + '\n' +
        open("CHANGES.rst").read()
        ),
    name='rpi.asthma_files_site',
    packages=find_packages(),
    test_suite="rpi.asthma_files_site.tests",
    url="https://github.com/ACLARKNET/rpi.asthma_files_site",
    namespace_packages=[
        'rpi'
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
    include_package_data=True,
    install_requires=[
        'setuptools',
        'collective.cover',
        'collective.documentviewer',
        'five.grok',
#        'pyzotero',
        'z3c.jbot',
    ],
    version=VERSION,
    zip_safe=True,
)

from setuptools import find_packages
from setuptools import setup


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
    long_description=open("README.rst").read(),
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
    install_requires=[
        'setuptools',
        'collective.cover',
        'collective.monkeypatcher',
        'five.grok',
        'pyzotero',
        'z3c.jbot',
    ],
    version="0.0.1",
    zip_safe=True,
)

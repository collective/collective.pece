# Pyroma says:
# ------------------------------
# Checking .
# Found collective.pece
# ------------------------------
# Final rating: 10/10
# Your cheese is so fresh most people think it's a cream: Mascarpone
# ------------------------------

from setuptools import find_packages
from setuptools import setup


VERSION="0.0.8"


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
    name='collective.pece',
    namespace_packages=[
        'collective',
    ],
    packages=find_packages(),
    test_suite="collective.pece.tests",
    url="https://github.com/collective/collective.pece",
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

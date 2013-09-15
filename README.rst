Platform for Experimental Ethnography (PECE)
============================================

A collective inquiry in to complex conditions. Development sponsored by `Rensselaer Polytechnic Institute (RPI) <http://www.hass.rpi.edu/>`_.

.. Warning::

    To install ``collective.pece`` you must use ``feedparser`` version 5.1.3.

About
-----

The PECE add-on for Plone is a research tool, currently in use by `RPI <http://theasthmafiles.org>`_ but available to anyone doing similar research. It features `Dexterity Content Types <https://github.com/plone/plone.dexterity>`_ and a `Collective Cover <https://github.com/collective/collective.cover>`_ integration to enable the creation of an "Asthma File": a collectively developed document containing artifacts and annotations.

Installation
------------

To install PECE functionality on your Plone site, add ``collective.pece`` to your list of Plone "instance eggs" in your ``buildout.cfg`` file. Run Buildout and restart Plone. Create a new Plone site with the add-on selected:

.. image:: screenshot1.png

Or add the functionality to an existing site:

.. image:: screenshot2.png

After installation, you should be able to add 6 new content types to your Plone site:

.. image:: screenshot8.png

Usage
-----

Follow these steps to begin using the PECE functionality in your Plone site.

Add a Question
--------------

*Questions* facilitate *Annotations* of *Artifacts* when researchers respond to them in context. Before you do anything else, add an Asthma Question to your site.

.. image:: screenshot4.png

Create Artifacts
----------------

An "Asthma File" is produced via the assembly of artifacts and annotations. So next, add some artifacts to your site. E.g.:

Audio artifact
~~~~~~~~~~~~~~

.. Note:: Currently only OGG audio supported

.. image:: screenshot9.png

Document artifact
~~~~~~~~~~~~~~~~~

Image artifact
~~~~~~~~~~~~~~

.. image:: screenshot5.png

Video artifact
~~~~~~~~~~~~~~

.. Note:: Currenly only OGG video supported

.. image:: screenshot10.png

Create an Asthma File
---------------------

Now we can create an Asthma File, which is a collaborative document consisting of multiple Artifacts, Annotations, etc. Made possible via the use of Collective Cover. [1]_

.. image:: screenshot6.png

.. [1] Catch 22: We'd like to customize the available types for Cover, but they don't exist until we install ourselves first. Workaround: customize TTW e.g.

.. image:: screenshot7.png

Zotero Integration
------------------

This add-on provides experimental integration with ``zotero.com``, currently in proof-of-concept stage i.e. there is API connectivity and nothing else. We are waiting for community input to help us decide the first feature.

To configure the demo view, set the following environment variables in your shell before running Plone e.g.::

    $ export ZOTERO_API_KEY=dFXmvyQvLMQpdfNs
    $ export ZOTERO_LIBRARY_ID=1234
    $ export ZOTERO_LIBRARY_TYPE=group

Then check: http://localhost:8080/Plone/@@zotero.

Known Issues
------------

feedparser
~~~~~~~~~~

PyZotero's feedparser version spec conflicts with Plone, see: https://github.com/urschrei/pyzotero/issues/29. To work around this issue, override Plone's feedparser version spec in your ``buildout.cfg`` e.g.::

    [versions]
    feedparser = 5.1.3


documentviewer
~~~~~~~~~~~~~~

``collective.documentviewer``'s Dexterity integration is in alpha stage, see:

- https://github.com/collective/collective.documentviewer/issues/39
- http://stackoverflow.com/questions/18722104/how-do-i-integrate-collective-documentviewer-with-my-custom-dexterity-type.

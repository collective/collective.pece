Asthma Files Site
=================

A collective inquiry in to complex conditions. Development sponsored by Rensselaer Polytechnic Institute (RPI).

About
-----

The "Asthma Files Site" add-on for Plone is a research tool, currently in use by RPI but available to anyone doing similar research. It features Dexterity content types and a Collective Cover integration to enable the creation of an "Asthma File": a collectively developed document containing artifacts and annotations.

Installation
------------

To install "Asthma Files Site" functionality on your Plone site, add ``rpi.asthma_files_site`` to your list of Plone "instance eggs" in your ``buildout.cfg`` file. Run Buildout and restart Plone. Create a new Plone site with the add-on selected:

.. image:: screenshot1.png

Or add the functionality to an existing site:

.. image:: screenshot2.png

After installation, you should be able to add 6 new content types:

.. image:: screenshot8.png

Usage
-----

Follow these steps to begin using the "Asthma Files Site" functionality in your Plone site.

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

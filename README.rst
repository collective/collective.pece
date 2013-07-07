.. image:: screenshot.png

Requirements
============

#1
~~

User story
++++++++++

We want to be able to change the tags without losing the integrity of the file structure that an artifact is embedded within. This means that artifacts should not be organized by tags, but should point to tags. Each Artifact should have a separate top-level object ID. Whenever a suer needs to access an artifact, all of the tags should be listed, and each of the artifacts that are identified with that tag shouuld be listed underneath it. As long as it points to the tag rather than stored within tag files, we shouldn't have to worry about duplicating artifacts with multiple tags.

Plone implementation
++++++++++++++++++++

This should work with Plone OOB with the addition of the Artifact types e.g. Image Artifact. Please test on http://localhost:8080/taf and report any issues with the above.

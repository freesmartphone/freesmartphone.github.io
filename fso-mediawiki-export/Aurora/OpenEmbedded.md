---
title: Aurora OpenEmbedded
permalink: /Aurora/OpenEmbedded/
---

All images provided by FSO for flashing on the supported devices are build with OpenEmbedded.

General
-------

We decided to base our work for now on the Classic OpenEmbedded Development Tree (http://git.openembedded.net/cgit.cgi/openembedded/). All work is done based on a snapshot of the upstream OE repository. The snapshot is available for access via the FSO Git Web-Interface (http://git.freesmartphone.org/?p=openembedded.git;a=summary). All changes will be even part of upstream OE.

Branch Layout
-------------

There are currently three branches in the repository:

-   **master**: tracks upstream's master branch
-   **for-upstream**: our changes which should commited upstream
-   **aurora/development**: our development branch where all changes related to aurora goes into

Development
-----------

-   All development for Aurora is done within the aurora/development branch
-   Commits that should go upstream are cherry-pick'ed into the for-upstream branch which is merged into upstream/master after review.
-   aurora/development branch is merged from time to time with upstream/master branch
-   When a new version of aurora should be released all testing and bugfixing is done within the aurora/development branch. For every release a tag is created with the name aurora-va.b where a is the major and b the minor release version number.

### Helpfull Git Commands

-   git log --online origin/master..for-upstream - Shows which commits are only in for-upstream but not in the origin/master branch
-   git log --online for-upstream..aurora/development -Shows which commits are only in the aurora/development branch but no in the for-upstream branch

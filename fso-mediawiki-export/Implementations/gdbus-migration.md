---
title: Implementations gdbus-migration
permalink: /Implementations/gdbus-migration/
---

Information
===========

As glib now has its own dbus protocol implementation named gdbus (which is better than the combination of dbus-glib/libdbus in numerous aspects), the reference implementation of FSO will migrate the components to using gdbus. This page will give you some informations about which components of the FSO framework and userland are affected by the migration.

Dependencies
============

-   vala: We need at least version 0.11.2 + git 5926198b8e458fc47bc9e12ec7d990a8b036d3ee
-   glib: We need at least 2.26.1

Affected software in git.freesmartphone.org
===========================================

-   libfso-glib
-   cornucopia
-   msmcommd

Roadmap
=======

1.  (done) Vala: cut inofficial release snapshot 0.11.2.1 from 0.11.2 + git 5926198b8e458fc47bc9e12ec7d990a8b036d3ee
2.  (done) OE: add glib 2.26.1
3.  (done) OE: build vala 0.11.2.1
4.  (done) OE: build libfso-glib from the gdbus branch
5.  (done) Cornucopia: Tag and branch out dbus-glib branch
6.  (done) Cornucopia: Merge gdbus branch into master

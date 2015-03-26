---
title: Implementations fsotdld
permalink: /Implementations/fsotdld/
---

fsotdld
=======

A time, data, and location manager.

fsotdld implements the FSO Device Time, Data, and Location APIs.

...

fsotdld compiles to C and is very lightweight. It features a plugin-architecture, so you only pay for the features you really need.

Vala bindings are available.

Plugins
=======

-   `alarm`: wakeup alarm handling for dbus system services.
-   `provider_gps`: generic GPS location provider.
-   `provider_gps_nmea`: GPS location provider support for receivers using NMEA protocol.
-   `source_gps`: time, date & location source plugin for GPS sources.
-   `source_gsm`: time, date & location source plugin for GSM sources.
-   `source_ntp`: time, date & location source plugin for NTP sources.
-   `sync_time`: generic time synchronization support.

Documentation
=============

-   See the org.freesmartphone.Device section of <http://docs.freesmartphone.org>

Dependencies
============

-   [glib, gio, gobject](http://www.gtk.org)
-   [libgee](http://live.gnome.org/Libgee)
-   [libdbus, dbus-glib](http://dbus.freedesktop.org/)
-   [libfsobasics](http://www.freesmartphone.org/index.php/Implementations/libfsobasics)
-   [libfsoframework](http://www.freesmartphone.org/index.php/Implementations/libfsoframework)

Download
========

-   The last released version can be downloaded from <http://www.freesmartphone.org/sources/>
-   The git version can be downloaded from <http://git.freesmartphone.org/>

[Category:System Developers](/Category:System_Developers "wikilink")
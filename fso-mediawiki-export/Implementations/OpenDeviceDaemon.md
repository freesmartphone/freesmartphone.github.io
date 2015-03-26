---
title: Implementations OpenDeviceDaemon
permalink: /Implementations/OpenDeviceDaemon/
---

Purpose and Boundaries
======================

See [Florian's post](http://fl0rian.wordpress.com/2006/05/29/platform-integration-for-mobile-linux-devices/) for a nice basic introduction. In a nutshell, an open device daemon is about a hardware abstraction layer that multiplexes sysfs, controls subsystem and peripheral power, input and output events, device locking. It hides all the nasty differences that are inherent to embedded devices (although they got a bit less thanks to Kernel 2.6.x). Our open device daemon offers all its services through a comprehensive [dbus interface](/Standards/OpenDeviceDaemonAPI "wikilink"), hence you can use its services from almost every language and toolkit that has support for dbus.

One thing to consider is that we do *not* want to make existing dbus interfaces obsolete, i.e. we will rather only complement already established interfaces. Examples:

-   [gypsy](http://svn.o-hand.com/repos/gypsy/trunk/gypsy/): GPS dbus interface
-   [bluez](http://bluez.cvs.sourceforge.net/bluez/): Bluetooth dbus interface
-   [Gnome network manager](http://www.gnome.org/projects/NetworkManager/): Networking dbus interface

...

Existing Approaches
===================

All these approaches are specific to a certain device or device class. However, our device daemon needs to be a complete substitute for all of them, so we should take a close look at their specific needs:

-   [Opie's ODevice Abstraction Layer](http://handhelds.org/cgi-bin/cvsweb.cgi/opie/libopie2/opiecore/device/): A C++ API covering device button handling, suspend/resume, UI rotation, backlight, LED, sound.
-   [Richard Purdie's zaurusd](http://svn.o-hand.com/repos/misc/trunk/zaurusd/): A script based device daemon (somewhat like apmd) covering alsa audio scenario changes on headphone insertion/removal, automatic display rotation based on hinge sensor, out-of-display-bounds touchscreen keys.
-   [GPE Phone's machined](http://projects.linuxtogo.org/frs/download.php/66/machined-0.1.tar.gz): A daemon that relays battery information via dbus.
-   [OpenEZX's ezxd](http://svnweb.openezx.org/cgi-bin/viewcvs.cgi/trunk/src/userspace/ezxd/): A daemon that talks to the baseband processor to keep the device from shutting down. This may not be a good example, since it should rather be covered by our [Open Phone Server](/Implementations/OpenPhoneServer "wikilink").
-   [OpenMoko's neod](http://svnweb.openmoko.org/trunk/src/target/OM-2007.2/daemons/neod/): A daemon that controls power management, display brightness, button handling, headphone insertion/removal, display rotation, display locking.
-   Maemo?

High Level Requirements
=======================

High Level Requirements are client-centric and don't contain references nor suggestions to a particular implementation.

-   Support the [freesmartphone.org Open Device API standard](/Standards/OpenDeviceDaemonAPI "wikilink") via dbus.
-   Support standalone operation as well as being embedded in a larger program
-   Support configurations where the daemon can contain code for only one device or up to multiple devices

Architecture
============

Architectural consequences are created by translating the High Level Requirements into implementation-specific recommendations.

-   All framework code resides in a library that is linked with the main program. For non-standalone-mode, another program (i.e. an application launcher) can embed the library to get a single executable.
-   A PluginArchitecture with loadable modules leaves the decision about the configuration (i.e. which actual devices and which feature of these devices to support) to the distribution builder.
-   [Individual modules](/Implementations/OpenDeviceDaemon/Modules "wikilink") implement necessary functionality.

Download
========

-   See [Community infrastructure](/Community_infrastructure "wikilink").

[Category:System Developers](/Category:System_Developers "wikilink")
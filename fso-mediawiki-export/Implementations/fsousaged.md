---
title: Implementations fsousaged
permalink: /Implementations/fsousaged/
---

fsousaged
=========

A Resource Manager.

fsousaged implements the FSO Usage DBus API. This API is concerned with coordinating application I/O requirements (think reference counting for resources). Applications are not supposed to turn on or off devices, since they do not have any knowledge about concurrent applications that may also be using the device.

It also ensures proper high-level suspend and resume preparation for available resources. Although it might be tempting, preparing a GSM modem for suspend can't sanely be handled in kernelspace, since you need to send several AT commands to it in order to prevent bogus wakeups. Which commands exactly is very device and situation specific, hence should be handled by userspace.

fsousaged compiles to C and is very lightweight. It needs less than 100 KB of disk space and typically operates with a RES segment of about 2 MB.

Plugins
=======

-   `controller`: controls resource requests and handles communication with the resource providers.
-   `lowlevel_kernel26`: low level plugin for handling suspend/resume on a Linux 2.6 kernel.
-   `lowlevel_openmoko`: low level plugin for handling suspend/resume on Openmoko devices.

Documentation
=============

-   For an introduction, see [usage-intro](http://docs.freesmartphone.org/usage-intro.html).
-   Client/Server API Reference is available as [org.freesmartphone.Usage](http://docs.freesmartphone.org/org.freesmartphone.Usage.html).
-   Resource Provider API Reference is available as [org.freesmartphone.Resource](http://docs.freesmartphone.org/org.freesmartphone.Resource.html).

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
---
title: Implementations fso-abyss
permalink: /Implementations/fso-abyss/
---

fso-abyss
=========

A 3GPP 07.10 multiplexing server.

This application implements a multiplexing server for the 3GPP 07.10 multiplexing protocol. It has a [DBus](http://www.freedesktop.org/wiki/IntroductionToDBus?action=show&redirect=DBus) interface to control and manage the virtual channels. Transportation is handled via pseudo tty devices.

Dependencies
============

-   glib, gio, gobject
-   dbus, glib-dbus
-   [libgsm0710mux](http://www.freesmartphone.org/index.php/Implementations/libgsm0710mux)

Download
========

-   The last released version can be downloaded from <http://www.freesmartphone.org/sources/>
-   The git version can be downloaded from <http://git.freesmartphone.org/>

Configuring
===========

fso-abyss can be configured via an (optional) configuration file /etc/abyss.conf:

`[omuxerd]`
`# set to 1, when the first AllocChannel request opens a session`
`autoopen = 1`
`# set to 1, when the last ReleaseChannel closes the session`
`autoclose = 1`
`# set to 1, when closing the session should close the program`
`autoexit = 1`
`[session]`
`# set 0 for 07.10 basic multiplexing, 1 for advanced`
`mode = 0`
`# set maximum 07.10 frame size`
`framesize = 89`
`# configure modem port`
`port = /dev/ttyUSB0`
`speed = 115200`
`[device]`
`# if the device needs a wakeup before transmitting data,`
`# set the number of seconds after which is falls asleep.`
`# 0 = disable`
`wakeup_threshold = 0`
`# set number of milliseconds to wait after wake up`
`# before transmitting again`
`wakeup_waitms = 0`

Using
=====

If you're using the FSO frameworkd, you only need to change one line in your /etc/frameworkd.conf:

`[ogsmd]`
`ti_calypso_muxer = fso-abyss`

If you're not using the FSO frameworkd, you can utilize the provided dbus interface [org.freesmartphone.GSM.MUX.html](http://docs.freesmartphone.org/org.freesmartphone.GSM.MUX.html). fso-abyss provides this interface as `org.freesmartphone.omuxerd` via `/org/freesmartphone/GSM/Muxer`.

[Category:System Developers](/Category:System_Developers "wikilink")
---
title: Implementations fsogsmd
permalink: /Implementations/fsogsmd/
---

fsogsmd
=======

A GSM Communications Manager.

fsogsmd implements the FSO GSM DBus API. This API delivers a simple way to handle voice and data communication with GSM modems.

fsogsmd compiles to C and is very lightweight. Vala bindings are available.

Plugins
=======

-   `dbus_service`: implements the dbus service.
-   `lowlevel_openmoko`: low level vendor plugin for Openmoko devices.
-   `lowlevel_gta04`: low level vendor plugin for Golden Delicious GTA04
-   `lowlevel_motorola_ezx`: low level vendor plugin for Motorola EZX devices
-   `lowlevel_samsung_crespo`: low level vendor plugin for the Samsung Nexus S
-   `modem_singleline`: modem plugin for a singleline AT modem.
-   `modem_qualcomm_htc`: modem plugin for Qualcomm MSM modems with firmware for HTC.
-   `modem_cinterion_mc75`: modem plugin for SIEMENS / CINTERION MC75 (and compatible).
-   `modem_ti_calypso`: modem plugin for TI Calypso.
-   `modem_option_gtm601`: modem plugin for Golden Delicious GTA04
-   `modem_cinterion_mc75`: modem plugin for the Cinterion MC75
-   `modem_dummy`: a dummy modem plugin
-   `modem_freescale_neptune`: modem plugin for the Freescale Neptune modem
-   `modem_nokia_isi`: modem plugin with support for the Nokia ISI protocol
-   `modem_phonesim`: modem plugin for phonesim support
-   `modem_samsung`: modem plugin for Samsung's IPC protocol based modems
-   `pdp_ppp`: implements data connectivity using ppp.
-   `pdp_ppp_mux`: implements data connectivity using ppp over [libgsm0710mux](/Implementations/libgsm0710mux "wikilink").
-   `pdp_qmi`: implements data connectivity using the Qualcomm Management Interface (QMI).
-   `pdp_nokia_isi`: implements data connectivity using the Nokia ISI protocol
-   `pdp_ppp_internal`: implements data connectivity using an internal PPP stack

Dependencies
============

-   [glib, gio, gobject](http://www.gtk.org)
-   [libgee](http://live.gnome.org/Libgee)
-   [libfsobasics](http://www.freesmartphone.org/index.php/Implementations/libfsobasics)
-   [libfsotransport](http://www.freesmartphone.org/index.php/Implementations/libfsotransport)
-   [libfsoframework](http://www.freesmartphone.org/index.php/Implementations/libfsoframework)
-   [libfsoresource](http://www.freesmartphone.org/index.php/Implementations/libfsoresource)
-   [libgsm0710mux](http://www.freesmartphone.org/index.php/Implementations/libgsm0710mux)
-   [libsamsung-ipc](https://github.com/morphis/libsamsung-ipc)
-   [libgisi](http://www.freesmartphone.org/index.php/Implementations/libgisi)

Download
========

-   The last released version can be downloaded from <http://www.freesmartphone.org/sources/>
-   The git version can be downloaded from <http://git.freesmartphone.org/>

Features to implement
=====================

-   Multi device support. See [Implementations/fsogsmd/MultiDeviceSupport](/Implementations/fsogsmd/MultiDeviceSupport "wikilink")
-   Rework for the device status handling. See [Implementations/fsogsmd/DeviceStatusRework](/Implementations/fsogsmd/DeviceStatusRework "wikilink")

[Category:System Developers](/Category:System_Developers "wikilink")
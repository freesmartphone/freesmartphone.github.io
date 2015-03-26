---
title: Modems
permalink: /Modems/
---

By Phone
========

openmoko freerunner
-------------------

-   The openmoko freerunner has a modem that speaks AT commands over a real serial port
-   the GPS and the audio CODEC are not attached to the modem, but to the main CPU

HTC Dream
---------

-   The GPS(nmea on /dev/smd27,need an activator named gps) and the audio DSP are connected to the modem

The HTC Dream's modem can be accessed trough:

-   AT commands on a virtual serial port(/dev/smd0) (preferred way),the virtual serial port is an abstraction on top of shared memory

Palm pre
--------

-   The GPS is connected to the modem

The palm pre's modem can be accessed trough:

-   AT command on the serial port (incomplete way)
-   the way used by msmcommd:
    -   Link Layer (mostly the same as found in the bluetooth HCI uart protocol)
    -   The HCI protocol (not the same like the bluetooth HCI protocol)
    -   The msmcomm protocol on top of it

Nokia N900
----------

-   The GPS only is connected to the modem(not the audio CODEC)

The Nokia N900's modem can be accessed trough:

-   the phonet0 network interface(speaks only phonet) /dev/cmt_speech are over an HSI serial link

A page exists on the [Phonet_Implementation](/Phonet_Implementation "wikilink")

Nexus one
---------

-   The GPS(nmea on /dev/smd27,need an activator) and the audio DSP are connected to the modem

The Nexus one's modem can be accessed trough:

-   AT commands on a virtual serial port(/dev/smd0) (preferred way), the virtual serial port is an abstraction on top of shared memory

By modem
========

AT
--

Some modems use AT like the openmoko devices, but also some of the devices with a qualcomm SOC(like the htc dream and the nexus one). It is implemented by fsogsmd.

msmcomm
-------

The msmcomm protocol can be found in palm/hp devices like the palm-pre,palm pre plus, palm pre 2,but also hp veer. It is implemented by msmcommd+fsogsmd

ISI
---

ISI can be found in the nokia n900 modem and is partially implemented in libgisi+fsogsmd

Samsung
-------

[a library exist](https://github.com/ius/samsung_h1_libmsm) for msm modems in samsung phones, like for instance the Samsung H1
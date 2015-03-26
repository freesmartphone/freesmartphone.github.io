---
title: Hardware GTA04
permalink: /Hardware/GTA04/
---

[130px|left](/Image:gta04-case.jpg "wikilink")

Presentation
============

The GTA04 is a high quality OMAP3 based motherboard for the Openmoko GTA01 and GTA02 systems.

-   Web: [GTA04 project](http://www.gta04.org)

Status
======

Modem
-----

| component          | status                                                                | notes           |
|--------------------|-----------------------------------------------------------------------|-----------------|
| enter PIN          | working                                                               |                 |
| change PIN         | working                                                               |                 |
| disable/enable PIN | working                                                               |                 |
| read SIM contacts  | working                                                               |                 |
| outgoing call      | working                                                               | needs fsoaudiod |
| incoming call      | working                                                               | needs fsoaudiod |
| USSD request       | working                                                               |                 |
| outgoing SMS       | working                                                               |                 |
| incoming SMS       | working                                                               |                 |
| DTMF               | working <s>[\#fso-669](http://trac.freesmartphone.org/ticket/669)</s> |                 |
| Hangup from remote | working <s>[\#fso-670](http://trac.freesmartphone.org/ticket/670)</s> |                 |

Todo
====

-   Integrate USB Host:
    -   The command for enabling USB host is:

`echo host > /sys/devices/platform/musb-omap2430/musb-hdrc/mode`

-   -   The command for disabling USB host is:

`echo otg > /sys/devices/platform/musb-omap2430/musb-hdrc/mode`

-   -   <s>also the kernel must be configured to supply enough power trough VBUS.</s> configured for 100mA max
-   <s>Fix the GPS with systemd in SHR:</s>
    -   <s>Add /dev/ttyO1 to the gpsd systemd unit</s>
    -   <s>Add a gta04-gps-handler systemd unit</s>
-   <s>[fso \#687](http://trac.freesmartphone.org/ticket/687)</s>
-   <s>[fso \#688](http://trac.freesmartphone.org/ticket/688)</s>
-   Test extensively the alsaloop forwarder
-   <s>Fix the bug where it was silent on gta04 side after ringing, but worked fine when you removed the ringing</s>
-   Add more sound scenarios:
    -   <s>scenario for headphones</s>.
        -   Fix the bouncing between headphones and speakers/earpiece during a call:
            -   <s> handle negative values/error codes comming from the ADC</s>
            -   Create a more clever algorithm.
    -   Add gsmspeaker scenario
    -   Add more controls in /etc/libphoneui.conf
    -   <s>hardware routing scenarios for A4+ models</s>
        -   <s>Detect between A3(that lacks hardware routing) and more recent revisions(that have hardware routing) GTA04 revisions in fsodeviced for the scenarios</s>
-   Add vibrator support
-   <s>find out how headphone detection work (it should be on the gta04 mailing list)</s>
-   Bluetooth
    -   make emtooth2 depend on libasound-module-bluez
    -   add a quirk for the gta04 bluetooth
-   NAND installation
    -   Generate the config automatically
    -   make it flash the kernel at kernel upgrades.
-   Newer kernel
-   <s>XV:</s>
    -   <s>configure the kernel for having /dev/fb{0,1,2}</s>
    -   <s>configure the kernel to allocate the right framebuffer memory</s>
    -   <s>make the config depend on the right xorg extensions</s>
-   <s>fix usb0 not coming up</s>
-   xrandr -o 1 in xf86-video-omapfb
-   Sensors and Misc devices
    -   <s>Accelerometers</s> FSO plugin made
    -   Compass
    -   barometric Altimeter
    -   Gyroscope
    -   FM transceiver
    -   FM receiver
-   <s>Test and if necessary</s> improve the first start experience (E17 is broken, .e missing, no first start wizzard)
-   <s>Fix DNS (/etc/resolv.conf missing)</s>

Communications
==============

You can find us on IRC:

Server: irc.freenode.net

Channel: \#openmoko-cdevel

people: slyon, mrmoku, GNUtoo, morphis, JaMa

[Category:Hardware](/Category:Hardware "wikilink")
---
title: Implementations fsodeviced
permalink: /Implementations/fsodeviced/
---

fsodeviced
==========

A device abstraction manager.

fsodeviced implements the FSO Device DBus API. This API allows peripheral control, such as managing audio, backlight brightness, LEDs, Vibrator, Accelerometer, and power control for devices without dedicated controlling daemon. It can deal with charging notification and RTC, forwarding button events and notifying about the system's idleness status.

It also ensures proper high-level suspend and resume preparation for available resources. Although it might be tempting, preparing a GSM modem for suspend can't sanely be handled in kernelspace, since you need to send several AT commands to it in order to prevent bogus wakeups. Which commands exactly is very device and situation specific, hence should be handled by userspace.

fsodeviced compiles to C and is very lightweight. It has been written to superseed all the device-specific control daemons Linux-based mobile systems have used in the past, such as the Zaurus' zaurusd, the Neo's neod, Kernel Concepts' deviced, etc. It also superseeds the non-customizable hald. It features a plugin-architecture, so you only pay for the features you really need.

Plugins
=======

-   `accelerometer`: generic accelerometer handling, needs one of the device-specific accelerometer plugins.
-   `accelerometer_kxsd9`: Kionix KXSD9 accelerometer support.
-   `accelerometer_lis302`: STMicroelectronics LIS302 accelerometer support.
-   `ambientlight_palmpre`: Palm Pre specific ambient light device.
-   `audio`: generic audio playing and routing support.
-   `backlight_omappanel`: Omap Panel specific backlight support.
-   `player_alsa`: alsa PCM output support.
-   `player_canberra`: PCM output support via libcanberra.
-   `player_gstreamer`: PCM output support via gstreamer.
-   `router_alsa`: audio routing via alsa.
-   `router_palmpre`: Palm Pre specific audio routing.
-   `router_qdsp5`: Qualcomm DSP5 specific audio routing.
-   `kernel_idle`: system idle notifications.
-   `kernel_input`: system input handling.
-   `kernel_info`: kernel information.
-   `kernel26_display`: display class-device based brightness control.
-   `kernel26_rfkill`: peripheral power supply control via rfkill.
-   `kernel26_rtc`: realtime clock, wakeup alarm.
-   `kernel26_leds`: LED class-device based brightness control.
-   `kernel26_powersupply`: peripheral power supply control.
-   `openmoko_powercontrol`: device-specific power supply controls for Openmoko devices.
-   `proximity_palmpre`: Palm Pre specific proximity device.
-   `thinkpad_powercontrol`: device-specific power supply controls for IBM Thinkpad devices.

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
-   [libcanberra](http://0pointer.de/lennart/projects/libcanberra/) (optional, forthe player_canberra plugin)
-   [alsa-lib](http://www.alsa-project.org) (for the alsa_audio and player_alsa plugin)
-   [gstreamer](http://gstreamer.freedesktop.org/) (optional, for the player_gstreamer plugin)

Download
========

-   The last released version can be downloaded from <http://www.freesmartphone.org/sources/>
-   The git version can be downloaded from <http://git.freesmartphone.org/>

[Category:System Developers](/Category:System_Developers "wikilink")
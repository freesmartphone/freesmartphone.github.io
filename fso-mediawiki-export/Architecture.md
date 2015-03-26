---
title: Architecture
permalink: /Architecture/
---

Boiler-plate diagram
====================

[image:Fso-architecture.png](/image:Fso-architecture.png "wikilink")

Description
===========

Overview
--------

The freesmartphone.org architecture is based on four tiers:

1.  Application Layer
2.  Middleware Layer
3.  Low-Level Services Layer
4.  Kernel Layer

### Application Layer

The application layer communicates with the middleware layer solely over dbus. This allows a great degree of freedom for the application layer is there are no programming language nor toolkit constraints involved.

### Middleware Layer

The middleware layer contains the freesmartphone.org services. The middleware is composed from discrete subsystems split into two abstraction layers. Middleware subsystems communicate both horizontally and vertically over dbus.

### Low-Level Services Layer

The Low-Level services layer contains existing solutions for lower level services such as networking, bluetooth, audio, etc. Some of these services offer dbus interfaces as well.

### Kernel Layer

The kernel layer contains the hardware drivers and provides low level access via sysfs, ioctls, and similar interfaces.

Concepts and Paradigms
----------------------

### Interface Consistency

Freesmartphone.org supports a consistent interface for application programmers. We believe that application programmers should be able to concentrate on their business logic, rather than wrapping their heads around the multitude of library or interprocess communication interfaces around. Consistency is good paradigm, that's why we chose to provide exactly one way to interact with the middleware.

While this may look to you as sometimes reinventing the wheel, it's an important step towards middleware acceptance -- often we are actually reusing the wheel and just covering the itchy details behind our dbus interfaces.

Thanks to the popularity of dbus, we can gradually include existing dbus-based services (such as bluez4, connman, wpa-supplicant, etc.) directly, only providing few higher level calls where cross-layer issues make this a necessity.

Middleware Subsystems (Lower Level)
-----------------------------------

The middleware subsystems are split into higher-level services (depicted as blue) and lower-level services (depicted as red). First, we discuss the lower level services:

-   Device
-   GSM
-   GPS

### Device

The lowlevel device service manages peripheral control, such as managing audio, backlight brightness, LEDs, Vibrator, Accelerometer, and power control for devices without dedicated controlling daemon. It also deals with charging notification and RTC. On some systems it also forwards button events and notifies about the system's idleness status.

### GSM

The low level GSM service expects a modem complying to GSM 07.07, GSM 07.05, and assorted GSM specifications, talking an AT-protocol over a serial line. If GSM 07.10 is supported, we use a multiplexing daemon to export multiple virtual AT-capable serial lines.

### GPS

The low level GPS service assumes a GPS device that talks NMEA or UBLOX-UBX over a device node. An auxilliary standalone service implements gpsd compatibility.

Middleware Subsystems (Higher Level)
------------------------------------

The higher level subsystems are:

-   Usage
-   Phone
-   PIM
-   Networking
-   Events
-   Preferences
-   Time

### Usage

The Usage subsystem is concerned with coordinating application I/O requirements (think *reference counting* for resources). Applications are not supposed to turn on or off devices, since they do not have any knowledge about concurrent applications that may also be using the device.

It also ensures proper high-level suspend and resume preparation for available resources. Although it might be tempting, preparing a GSM modem for suspend can't sanely be handled in kernelspace, since you need to send several AT commands to it in order to prevent bogus wakeups. Which commands exactly is very device and situation specific, hence should be handled by userspace.

### Phone

The phone subsystem can be used to create and manage voice communication over multiple protocols. It also connects to bluetooth for facilitating headset control. It uses GSM, bluez4, and connman.

### PIM

The PIM subsystem offers a data storage for personal user data. It uses GSM.

### Networking

The networking API provides high level queries for networking setup. It uses bluez4, GSM, and connman.

### Events

The events service processes rules that connects triggers (actions such as an incoming call, a charger insertion, etc.) via filters (such as depending on the current profile) to events (such as playing a ringtone). Depending on the rules, the events service glues to many other subsystems.

Note that the events service is just a convenience layer, full-fledged applications may handle most of these kind of connections themselves.

### Preferences

The preferences service contains a settings database.

### Time

The time service aggregates multiple time sources and sets the time and timezone accordingly. It also contains an alarm service which you can register with.

API
===

The DBus-API specifications are autogenerated and live on <http://docs.freesmartphone.org>.

[Category:About](/Category:About "wikilink")
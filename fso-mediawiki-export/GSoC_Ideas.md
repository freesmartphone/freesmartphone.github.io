---
title: GSoC Ideas
permalink: /GSoC_Ideas/
---

freesmartphone.org is applying as a mentoring organization for Google Summer of Code 2010. This is our list of potential ideas. You might also want to take a look at the [Brainstorming](/Brainstorming "wikilink") set of pages.

FSO GSoC 2010 Middleware Ideas
==============================

### Fine grained resource management

While FSO contains basic Resource management, there is a strong demand to enhance this to feature capabilities and requirements, rather than on/off requests. This task would contain specification and architecture work, then implementation in Vala.

### Audio Manager

Audio scenario handling in smartphones is a complex task; solutions like PulseAudio are not applicable when it comes to low-power devices. This project would work on a full-fledged alsa audio scenario with FSO integration.

Implementation would be in Vala.

### BlueZ & Connman integration

Both BlueZ and Connman provide plugin-based architectures for networking. The FSO middleware needs to cooperate with these two services in order to resuse these projects.

In this project, a telephony plugin for bluez would be implemented that interfaces with the FSO GSM service. Another project would consist of writing a connman plugin to interface with the FSO resource services.

Implementation of these would have to be done in Vala.

### Cross-Layer PIM

Personal Information Management is one of the most complex tasks in mobile devices middleware. The lion's share of dozens of half-finished existing solutions is desktop-centric and thus unusable on a mobile device. More over, full PIM support is inherently cross-layer as it ties into lots of other subsystems, such as GSM, GPS, Preferences, etc.

This project would base on the opimd results from the Openmoko GSoC 2008 and continue developing this, researching and possibly integrating existing solutions, where appropriate.

Implementation would be done in Vala.

### Mobile Device Simulator

Middleware testing often needs to be carried out directly on the device, since the required peripherals are not present on a typical desktop system. More over, testing with life data hardly leads to reproducable test processes.

It would be of tremendous help if there was a software available simulating, e.g., a GSM modem and a GPS device, providing these as data sources for the FSO middleware layer.

This project could base on the qtopiaphonesim project found in Qt/Extended and enhance this to feature full FSO API coverage.

### Porting FSO to other devices

-   There is a large number of HTC Smartphones out there running Windows Mobile or Android. The HTCLinux project is making good progress in bringing a GNU/Linux kernel space to these. By porting the FSO middleware to these devices, a viable alternative to Windows Mobile would be present.

<!-- -->

-   The MOTOROLA EZX-series as powered by the OpenEZX kernel 2.6 has come a long way, almost all features are complete now. Since Motorola discontinued the EZX series and never delivered the promised Linux-SDK, the FSO middleware would put these devices to new life. Although base features have already been ported, there are still many open spots regarding modem and GPS support.

<!-- -->

-   The Palm Pre is a Linux-based Smartphone that ships with a closed middleware.

<!-- -->

-   The [N900](/Hardware/N900 "wikilink") is Linux-based Smartphone that ships with many proprietary components, thus the need for a free middleware on the [N900](/Hardware/N900 "wikilink") arises.

### API and implementation for Accelerometers Gestures

Using accelerometers comes very natural on other platforms (eg. switching the screen off when placing a call and holding the phone vertical, and switching the screen back on when the device is no longer held in a vertical fashion). The GSoC student shall summarise the various efforts also on other platforms to use the accelerometer, prepare a concept for either adapting an existing solution for the OpenMoko or to newly create an API if no other solution could be found. If time permits, the student shall investigate the possibility to use the OpenMoko as a 3D input device to the desktop.

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
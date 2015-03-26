---
title: Meeting 2008-12-18 Braunschweig
permalink: /Meeting_2008-12-18_Braunschweig/
---

Date: 2008-12-18

Attendees: Mickeyl, Jan, Daniel, Stefan, Harald

Agenda
------

### Architectural

-   opimd

Mickey had a meeting with Soeren 'Abraxa' Apel. First action is to sync with his latest changes on opimd and docs until end of the year. Interested people should try it out and let us know what they think about the API.

-   networking

Card gets not detected on the device so far. Should be a problem with the new netlink device detection. Stefan will work together with Werner to get this working.

-   preferences

Oeventsd and opreferenced are more or less without maintainer. Orthogonal profiles. Categories. Needs change to profile API. Tasks into the bugtracker. TODO: Send mail about this to SHR list.

Still a good idea to tie rules to profiles?

-   vala migration

Starting migration with odeviced in form of fsod after full test coverage. TODO mickey: Enhance subsytem class to allow starting an external subsystem like fsod. (external=pathname).

-   Kernel version migration

Two small things that differ from the versions from our perspective. MS5 support for both kernels.

### Organiziation

-   update Task Juggler

Daniel will look into bringing our high-level tasks into it. Our tool of choice is still trac and we will keep using it.

-   work assignments for new FSO people

opimd and fsod

### Annoyances

-   oeventsd race

Oeventsd is async, does not wait until playsound() is back. If a call gets cancelled while the audio subsystem still builds the pipeline oeventsd stop a not yet there sound. Therefor the sound keeps playing. Needs further investigation.

-   cancelling an outgoing call

Change call handler to allow modem specific hooks. Fixed now.

-   the battery issue

We have to decide how we export the battery class informations. One object for every battery and powerclasses. We also could think about an object that have all the informations already aggregated. On USB power? What power level? Battery level?

-   gst-plugin-sid

Perhaps OE bug (Skip package)? Mail to OE list.

-   gpsd vs. fso-gpsd in OE

Not as easy as thought. Needs more thinking. Maybe virtual RDEPENDS in bitbake. Mickey will write a summary to the OE list.

-   does the TI Calypso send while recamping (\#1024)?

Mickey will do this at home.

-   test Ublox 5 board

Daniel will work on this later. --

### EZX

-   SMS

After sending some magic init command using the normal SMS commands is working.

-   Phone numbers

International phone numbers got fixed.

### Glofiish

-   GPS

Patch for basic support commited.

-   LEDs and keys

Needs defining oin frameworkd.conf

-   Anything specifically required to support hardware-keyboard devices?

Needs more thinking.

### MS5

-   When to branch?

A stabilization branch for frameworkd will get created in the first week in january.

-   Update features

Features and tasks got updated fro MS5. The only major change is that we will not have opimd fully ready then. We will put it in, disabled, but easy to enable. Feedback for the API is very welcome.

-   Assign features to people

Done

### Misc

-   Update roadmap for MS6

Not done

-   Alsa configuration:

Harald replicated his setup for injecting a PCM stream into a call. Send to the ml. Recording oops the ASoC driver. Bug filled.

-   Rxr kernel errors on GPS \#2180

Also happening on the M800. Needs further investigation.

[Category:Community Updates](/Category:Community_Updates "wikilink")
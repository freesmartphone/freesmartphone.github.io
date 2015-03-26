---
title: Meeting 2008-11-13 Braunschweig
permalink: /Meeting_2008-11-13_Braunschweig/
---

Date: 2008-11-13 & 14 Attendees: Mickeyl, Jan, Daniel, Stefan

Orga
----

-   Status relationship FSO & Openmoko Inc.

Openmoko will found FSO development. Sourcing out functional units.

FSO Releases
------------

Plan the next 2 milestone. Three major tasks per MS plus misc tasks from bugtracker.

MS5 (2009-01-31) (Stefan release dude)

-   PIM (contacts and messages)
-   More robust SMS handling
-   SIM country code for locale default setting
-   Timezone from network country code
-   Time from GPS and if available from GSM
-   MC75i modem support

MS6 (2009-03-31) (Release dude to be nominated)

-   USSD high level API
-   Basic networking
-   Finishing ogpsd tasks
-   ublox5 support
-   Location awareness

<!-- -->

-   Release dude

Yes, round robin. For MS5 it will be Stefan.

-   Tarball releases for fsod

Need more thinking. General agreement.

-   Informal release todo list

In the wiki on the way.

-   Any chance to sync milestone dates with SHR ones? (Hard due to feature based

releases)

We try to improve this a bit from the FSO perspective by going with a more formal release process and a -rc phase befor ethe actual milestone.

-   Test driven release

Unit tests and blackbox test is in thinkin phase

-   May be a list for people working with the frameworkd to get informed before a

new MS is released. so they can adjust to the api changes.

With -rc two weeks before a release we get the people informed.

Frameword
---------

-   Responsibilities for MS5
    -   Networking (Stefan)
    -   mc75i (Mickey)
    -   SMS and ogsmd maintainence (Daniel)
    -   Automatic time handling (Daniel)
    -   Accelerometer and Remoko integration (Jan)
    -   Docs and tests (All)

<!-- -->

-   Updates for MS4

Fix bugs in the milestone branch plus sane-srcrev bump.

-   OpenEZX support for MS4

<!-- -->

-   Git kernel recipe with known good rev
-   Alsa state files in OE
-   Frameworkd test for neptune
-   Rules file for A780
-   Sane SRCREV bumpen
-   Let rwithby know to build for a780

OE
--

-   Rasters Patches and newer EFLSRCREV

On the way. Need some more testing before pushing.

-   SHR OE access

Daniel will propose with pointer to SHR git.

-   Juliens numpyphysics patches mergen

On the way. Need to finish the push with rasters patches first

-   E-Ten Glofiish M800 demo

Stefan will push his local stuff out soon.

Misc
----

-   Motivate people woking on other platforms

<!-- -->

-   -   HTC Magician

Stefan will ask Philipp about his status / plans

-   -   HTC Kaiser

Jan tries to get communication started to integrate Kaiser better into OE and then think about FSO

-   -   MIO A701 smartphone

Stefan will ask Robert about his plans for userland

-   -   HTC G1

Anybody working on this?

-   -   iPhone

Some progress with linux on the iPhone: <http://linuxoniphone.blogspot.com/> Will still take a long time until that gets into a posistion where FSO would make sense.

-   -   Notebooks with UMTS and perhaps gps

The full FSO team needs the new and shiny Linevo ThinkPad X200s notebooks with integrated UMTS and gps to test fso on it. ;)

-   Update on OpenEZX kernel side

See OpenEZX support for MS4

-   FSO powered web based SMS PDU generator and parser

During SMS PDU handling Daniel found some shortcommings on PDU generators and decoders in the web. Perhaps offer one based on fso.

UI
--

-   How do we like to handle the illume theme and config in the future
    -   Maintain an own set is not cheap
    -   Use upstream version
    -   Let new UI decide on

Stefan will look into how to make it a tiny patch against the illume theme and config instead of a full blown theme.

-   What is the plan to let zhone fade out?

Need to stay until one of the alternatives has a equal feature set ready

-   -   Can we coordinate a SHR release somehow matching our schedule for MS5?
    -   What can we expect from swisscom/raster?
    -   Paroli

All three are different in details, but have some common goals. Basic telephony, dialer, contact, SMS, based on FSO.

[Category:Community Updates](/Category:Community_Updates "wikilink")
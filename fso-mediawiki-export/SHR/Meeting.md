---
title: SHR Meeting
permalink: /SHR/Meeting/
---

**SHR Conferences**

Future of SHR project
=====================

Where is SHR now and where should it go ?

Items
-----

**Current situation**

-   full OpenEmbedded integration
-   several devices supported and more being included (see below) Openmoko, HTC Dream, PalmPré, n900, Geeksphone?
-   phone suite under development (SHR phoneui)
-   comprehensive user manual exists
-   FSO middleware used
-   desktop environment based on E and Illume2, with the possible evolution of Mokosuite
-   Major external components:

<!-- -->

-   -   **FSO:**

<!-- -->

-   -   Pretty good current state with the next major update of our Vala needs will be when glib 2.26 comes out and we can all move to GDBus.

<!-- -->

-   -   **Enlightenment:**

<!-- -->

-   -   E17 being stabilized, alpha released already, meaning stable E in near future

<!-- -->

-   -   **Kernel:**

<!-- -->

-   -   2.6.29 used in Testing
    -   2.6.32 used in Unstable version
    -   2.6.34 being tested, X input filter needed, Alsa scenarii? <please confirm>

Questions for discussion

-   direction, goals and how to achive it

**Supported devices at the moment:**

**Openmoko GTA01 and GTA02**

-   testing and unstable images available
-   full hw support
-   being improved with SHR
-   recently added Glamo speedups, WS fixes

**HTC Dream**

-   has SHR images available
-   medium support (BT, GSM, GPS, WiFi supported)
-   bad kernel drivers
-   hardware partially works but requires improvements:
    -   audio buffer underruns
    -   wifi PSM
    -   battery life too short
    -   minor bugs in 3G
-   hardware needs integration plugins for FSO
-   keyboard needs UI + integration

**PalmPré**

-   no SHR images
-   nearly all core stuff is decoded: calls, sms etc...
-   sms need to be implemented

**n900**

-   SHR images available
-   good spread of the hardware in SHR core team

**Questions for discussion**

-   what are next steps for each device

**Where is help needed and what can we offer to newcoming developers**

-   <please fill in>
-   bug administrations

**Current SHR (core/user) team roles and responsibilities**

-   <please fill in>
-   repository/buildhost maintainers
-   documentation maintainers
-   resources maintainers (blog, wiki)
-   programmers
-   release maintainers
-   users

**Questions for discussion**

-   ideas for near/long term future for each subteam

**Who is using / participating in SHR now ?**

-   Competitors: Android, Meego, WebOS, WinMO, Bada

**Possibilities / Aims**

-   Attract a broader audience of users and developers. Provide a basic linux platform for any mobile phone.

**How to get there**

-   Give the SHR project a strong identity: Who is it? What is it? What is making it *unique* Where does it go?
-   Improve infrastructures, documentation, design, ..
    -   Uniqueness
        -   Emancipation of the user: Everybody can proactively design the project rather than one big company
        -   100% (or 99,7%, thinking of closed kernel modules) free code
-   Make it known

**Software**

-   -   Userspace
        -   Graphical ipkg-Manager
        -   Phone suite
        -   Calendar (Meetings, Lectures, Birthdays, etc.)
        -   Composite (Make expose default on devices where its possible)
    -   Kernel
        -   DRI/OpenGL
        -   Wifi
        -   GPS

**Outcome**:

-   -   Roadmap
    -   Enable non geeks to install SHR and to use it on their daily driver
    -   Make it easier and more dynamic to use

Time
----

|---------------------------|------------------------------------|-----------|---------|------|---------|-----------|--------|
| Time                      | GNUtoo                             | leviathan | dcordes | JAMA | morphis | RuiSeabra | Mickey |
| Monday 09/06/10 20:00 CET | ?                                  | ?         | ?       | ?    | ?       | ?         | ?      |
| Sunday 09/05/10 20:00 CET | any day, usually after 17h00 UTC+1 | ?         | bad     | ?    | OK      | OK        | OK     |

Place
-----

1.  SHR on freenode ?

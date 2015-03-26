---
title: FSOSHRCON 2011 AGENDA
permalink: /FSOSHRCON_2011_AGENDA/
---

FSOSHRCON 2011 Agenda
=====================

**Day 1** Friday, 16th December 2011
------------------------------------

### 19:00 - ????? *Dinner*

### 22:00 - Bug Database TRAC cleanup

-   SHR TRAC bug database cleanup [added by nschle85]

**Day 2** Saturday, 17th December 2011
--------------------------------------

### 06:00 - 07:30 *early morning exercise (optional)*

### 08:00 - 08:30 *Breakfast*

### 12:00 - 13:00 *Lunch*

### 19:00 - ????? *Dinner*

**Day 3** Sunday, 18th December 2011
------------------------------------

### 06:00 - 07:30 *early morning exercise (optional)*

### 08:00 - 08:30 *Breakfast*

### 12:00 - 13:00 *Lunch*

Collection of Lectures
----------------------

-   Status report; what has changed last year ? Speaker: ??? [added by nschle85]
-   Short overview of current software architecture, Speaker: ??? [added by nschle85]

Collection of topics to talk about
----------------------------------

### Most Important topics

-   Stability(regressions/bugs) and QA [added by GNUtoo] =\> addressed by shr-staging
    -   Q: How to provide an always compiling code tree for developers ? [added by nschle85]
    -   Task: identifying build system issues belonging identifying build issues eg. API changes, what can be improved ? [added by nschle85]
        -   Should QA issues break a build ? [added by nschle85]
    -   Q: Should pushes from developers which breaks builds be reverted and fixed on separate branch ? [nschle85]
    -   Q: How to decouple OE - FSO development from SHR development ?
-   Testing the FSO stack (see [fsotest](http://git.freesmartphone.org/?p=cornucopia.git;a=tree;f=fsotest;h=faa1ec0fe3d9877ba080fda4b6c091112de649af;hb=HEAD)) [added by morphis]
-   What is/should be the impact of WebOS as open source on our software stack? (added by mickey)
-   Which devices to support [added by GNUtoo]
-   maintainability( for instance how much of a device is upstream(kernel,Xorg driver etc...) [added by GNUtoo] And:
    -   completeness/doability of the port(how much the port is finished, or how easy is the device to adapt). =\> talk about status of devices
    -   In what way all the stack depends on the recentness of kernel and userland?
        -   Udev, devtmpfs(since 2.6.32)
        -   Systemd(depend on recent features of the kernel)
        -   Xorg: we have to maintain the following xorg drives:
            -   xf86-video-glamo for the openmoko gta02([not maintained by the Xorg people](http://cgit.freedesktop.org/xorg/driver/))
            -   xf86-video-omapfb for the omap devices(nokia900,gta04)([not maintained by the Xorg place](http://cgit.freedesktop.org/xorg/driver/))
            -   The input driver for the palm pre([not maintained by the Xorg people](http://cgit.freedesktop.org/xorg/driver/))
            -   xf86-input-mtev for the nexus S([not maintained by the Xorg people](http://cgit.freedesktop.org/xorg/driver/) [but by morphis](git://github.com/morphis/xf86-input-mtev.git))
        -   impact of new system calls on glib
        -   linux-libc-headers
    -   Where is the time of the developers spent?
        -   Bugfixes:
            -   Bugs and work to do introduced by the migration to shr-core
            -   Bugs and adaptations needed that were introduced by bumping some parts of the system(kernel like for om-gta02,enlightenment,vala etc...) =\> shr-staging helps isolating and identifying the cause of theses bugs
        -   Systemd migration ( mrmoku and JaMa work on it)
        -   Device adaptation:
            -   Nexus S (GNUtoo and morphis work on it, mostly morphis)

### Other Topics

-   to udev or not to udev - final decision [added by mrmoku]
-   which init system – final decision [added by Mickey]
-   integration of VoIP [added by mromoku]
-   release planning and management [added by mrmoku]
-   SHR application developer (docs/example-application) [added by Slyon]
-   SHR website [added by Slyon]
-   GPS for N900 - How to implement ? (extend 2.x/3.x GPSd or extend gypsy and use fso-gpsd for gpsd compatiblity ?) [added by nschle85]
-   connmand issues(conflict between fso and connmand) [added by GNUtoo]

Collection of things to hack on
-------------------------------

-   GTA04 FSO integration [added by Slyon]
-   fsoaudiod [added by mrmoku]
-   fsopimd (if there is a lot of free time left ;)) [added by Heinervdm]

temporary Results
=================

The Stack - which components we want to use
-------------------------------------------

### pro udev

### pro devtmpfs

### cons udev

-   device initialisation too early , no control about on demand starting (not evaluated yet)

### conclusion

-   target platform is phone
-   resource management is very important. how are resources handled in a way udev does ?
-   special hardware still needs special handling

### systemd or not ?

FSO/SHR will switch to systemd in future.

The Ports which hardware support
--------------------------------

Testing Stability / Organization
--------------------------------

-   SHR makes releases in future
    -   for testing the new features, staging images are published and tested by developers and the community
    -   releases consists of a set of features and/or bug fixes
-   developers are working on feature branches which are merged after work has finished and never before
-   versions of major components are locked in shr and updated by features

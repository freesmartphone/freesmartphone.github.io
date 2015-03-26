---
title: FSOSHRCON 2011
permalink: /FSOSHRCON_2011/
---

About
=====

The core developers of the freesmartphone.org middleware and the SHR project decide to meet to discuss the strategy for the next months and years. Which devices do we want to support and which features most relevant to be developed and integrated. The details are planned in the [FSOSHRCON 2011 Agenda](/FSOSHRCON_2011_AGENDA "wikilink").

Where?
======

-   [<http://www.linuxhotel.de/>| Linux Hotel] in Essen (Germany)

When?
=====

We need to decide for a date. Please vote for one here: <http://www.doodle.com/cvwv38ykahx9b3uy>

=\> 16,17,18 December 2011

Who?
====

Please add your name if you're interested in attending the meeting.

-   Simon Busch (morphis)
-   Klaus Kurzmann (mrmoku)
-   Lukas Märdian (slyon)
-   Denis Carikli (GNUtoo)
-   Sylvain Paré (GarthPS) (but will be difficult to be there)
-   Michael Lauer (mickeyl)
-   Martin Jansa (JaMa)
-   Norman Schleicher (nschle85)

Summary as sent to the MLs
==========================

    Dear all,

    as a participant of the FSOSHRCON'11 in Essen (Germany) this year, I'd like to summarize the topics we discussed and the work we did this last weekend.

    * Date and Location
    * Participants
    * The Ports (which Devices to support)
    * The Stack (SysV Init vs. Systemd / Udev vs. Devtmpfs)
    * Stability and Organization
    * Solved Tasks
    * Openmoko Community Survey 2011 – please take part!


    Date and Location:
      The FSOSHRCON'11 took place from 16.12. - 18.12.2011 at the Linux
      Hotel in Essen, Germany.


    Participants:
      antrik, GNUtoo, Heinervdm, JaMa, mickeyl, morphis, mrmoku,
      nschle85, slyon


    The Ports (which Devices to support):
      FSO status:
      [working] Openmoko GTA01, Openmoko GTA02, Palm Pre (+variants)
      [work in progress] Goldelico GTA04, Nokia N900, Google Nexus S

      SHR supports:
      Openmoko GTA02, Goldelico GTA04, Nokia N900, Palm Pre (+variants),
      Google Nexus S


    The Stack (SysV Init vs. Systemd / Udev vs. Devtmpfs):
      * SHR will switch from SysV init to Systemd in the (near) future, to
        provide a faster and cleaner bootup.
      * There will probably be a minimal FSO init process, which can be used
        to bootup a minimal FSO featurephone stack.
      * We see phones as mostly static devices with fixed use cases, thus we
        prefer devtmpfs over udev and will use it on all devices running
        SHR.
      * Udev will stay in the feeds, so power users who want to use their
        phone as a mini computer can install it anyways.


    Stability and Organization:
      * SHR will make releases in the future
      * Release will be created from best staging image + feed, but
        without maintaining release branch.
      * releases consists of a set of features and/or bug fixes
      * for testing the new features, staging images are published and
        tested by developers and the community
      * developers are working on feature branches which are merged after
        the work is finished
      * versions of major components are locked in SHR and updated as
        features


    Solved Tasks:
      * GTA04 support: you can now build SHR-Core images, which are almost
        working. Still lacking proper power management (kernel) and proper
        audio routing (fso/alsa) – both are worked on
      * shr_elm_softkey: fixed a long standing bug which prevented you from
        closing several applications (ffphonelog, ffalarms, iliwi)
      * ffalarms: fixed segfault on adding an alarm
      * trac cleanup: we started to clean up our trac bug database, which
        included closing a lot of outdated/obsolete bugs.


    Openmoko Community Survey 2011 – please take part!
      We decided to start a poll about which hardware and which software you
      use or are interested in these days. The results will help us to
      focus on relevant hard-/software.
      Please participate in the survey at Doodle and spread the word about
      it!

      => http://www.doodle.com/sh6insnivnvqyz7h
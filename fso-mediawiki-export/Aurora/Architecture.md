---
title: Aurora Architecture
permalink: /Aurora/Architecture/
---

Overview
--------

System Components
-----------------

FIXME: We need to describe each component and the role it plays within the whole system.

-   **Aurora**
    -   [aurora-daemon](/Aurora/AuroraDaemon "wikilink")
    -   [aurora-components](/Aurora/AuroraComponents "wikilink")
    -   [aurora-theme](/Aurora/AuroraTheme "wikilink")
    -   [aurora-applications](/Aurora/AuroraApplications "wikilink")

<!-- -->

-   **FSO**
    -   fsoappd
    -   fsoeventsd
    -   fsoaudiod - audio services
    -   fsodeviced - hardware abstraction services
    -   fsotdld - time, date, location services
    -   fsogsmd - telephony services
    -   fsonetwork - sharing connections
    -   libfsobasics - generic utility library
    -   libfsoframework - subsystems & plugins
    -   libfsoresource - resource handling
    -   libfsotransport - data transport
    -   libfsosystem - lowlevel support

<!-- -->

-   **Other**
    -   connman - network services
    -   bluez - bluetooth services

For further details, please see [Implementations](/Implementations "wikilink").
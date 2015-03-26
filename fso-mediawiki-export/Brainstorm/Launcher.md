---
title: Brainstorm Launcher
permalink: /Brainstorm/Launcher/
---

Purpose
=======

The purpose of this interface is to integrate an application launcher into the FSO framework.

Requirements
============

-   Start Apps
-   handle instances ( any apps out there which need multiple instances?)
-   handle resources
-   handle network connections
-   interact with user/UI if necessary
-   start apps for special use cases
-   ...

Basic ideas
===========

Resource requirements:

-   Mandatory Resources: App can't start/ is unusable without it
-   Required Resources: App might need this resource to work completely
-   OnDemand Resources: App tries to get the resource on demand.

Resource rules:

-   Denied: The App is not allowed to the resource
-   Allowed: Just request if required
-   Ask: Prompt the user for permission

**This might cause several problems:** we have to do reference counting on our own, because usaged counts only 1 ref per dbus connection and would make usaged completeley useless. maybe this idea should get into usaged directly? --[Playya](/User:Playya "wikilink") 20:29, 10 December 2009 (UTC) Option: Save choice

Additional reply for ondemand resources:

-   AskAgain: App can request the resource again

Network rules: Network needs special handling because we have different speed/amount of costs.

Should use the same rules as resources, but with a higher granularity.

we should cover different case:

-   connect to a WiFi network with specific subconditions
    -   connected to specific AP/network
    -   ...
-   connect via GPRS/UMTS/... with subconditions
    -   SIM card
    -   APN
-   connect to a other device via USB
    -   Device name
    -   ...
-   connect to a network via Bluetooth (see USB connection)
-   connected to SOCKS-Proxy/VPN (and combination of the above?)

Autostart
=========

-   Upper rules but the other way around //TODO

Namespaces / Subsystems
=======================

-   org.freesmartphone.Launcher
-   org.freesmartphone.Launcher.Resource
-   org.freesmartphone.Launcher.Resource.Network
-   org.freesmartphone.Launcher.Resource.Reply
-   org.freesmartphone.Launcher.Autostart

Proposals to evaluate
=====================

-   Maybe just extend the XDG-Standard
-   Apparmor for blocking network connections [1](http://forge.novell.com/modules/xfmod/project/?apparmor)
-   libunique for unique instances (unique instace should be handled by [Brainstorm/LifeCycle](/Brainstorm/LifeCycle "wikilink")
-   fsoeventsd for starting apps based on the situation: [Brainstorm/fsoeventsd](/Brainstorm/fsoeventsd "wikilink")

Use cases
=========

-   Connect to your asterisk box when connected to my AP
-   Allow/deny tangogps to download maps
-   Deny GPS access for navit if only want to view a location

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
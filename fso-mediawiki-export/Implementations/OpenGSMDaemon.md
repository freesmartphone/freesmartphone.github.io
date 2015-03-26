---
title: Implementations OpenGSMDaemon
permalink: /Implementations/OpenGSMDaemon/
---

Purpose
=======

...

High Level Requirements
=======================

High Level Requirements are client-centric and don't contain references nor suggestions to a particular implementation.

-   Support the [freedesktop.org telephony API standard](/Standards/OpenPhoneServerAPI "wikilink") via dbus
-   ...

Architecture
============

Architectural consequences are created by translating the High Level Requirements into implementation-specific recommendations.

We will distinguish a frontend and a backend.

Frontend
--------

The Frontend

-   handles the dbus communication
-   relays to individual backend methods
-   caches data gathered from backend
-   periodicly requests data from the backend

Backend
-------

The backend

-   receives requests from the frontend
-   communicates with the modem (preferably in-process and direct, but I expect us to see some shared library backends first)
-   informs the frontend on incoming events

Unresolved Issues
=================

...

[Category:System Developers](/Category:System_Developers "wikilink")
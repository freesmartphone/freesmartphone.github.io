---
title: Brainstorm General
permalink: /Brainstorm/General/
---

Purpose
=======

This should not result in a service, but in general interfaces which a required really often. This makes it easier to provide generic UI widgets.

Interfaces
==========

Interfaces in this group should use the prefix org.freesmartphone.General(?)

Login/Account
-------------

-   A generic interface for a login. Most Logins are quite simple and only need few things to work:
    -   Username
    -   Password
    -   Protocol
    -   Port
    -   Optional stuff: Proxy, TODO

possible interface

-   [s:protocols] SupportedProtocols()
-   {s:name,v:value} GetProperties()
-   {s:name(s:type,[s]options}
-   {sv} GetOptional()
-   ChangeProperty(s:name,v:value)
-   ChangeOptionalProperty @see ChangeProperty
-   LoadFromUri(s:uri)
-   TODO

Download
--------

-   A generic interface for downloads

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
---
title: DBus API Style Guide
permalink: /DBus_API_Style_Guide/
---

DBus API Style Guide
====================

-   Bus names are all lowercase with . separation, e.g. org.freesmartphone.odeviced
-   Object names all lowercase with / separation, e.g. /org/freesmartphone/device/idlenotifier/0
-   Method and Signal names are CamelCased, e.g. ListFoo, GetBar.
-   Use Get/Set prefixes for accessors (GetServiceCenter, SetServiceCenter)
-   Use verbs for operations (ListProviders, Unlock, SendAuthCode)
-   Use similar terms for similar operations (ListProviders, ListCells)
-   Keep the vocabulary as simple as possible, but as large as necessary

[Category:Developer resources](/Category:Developer_resources "wikilink")
---
title: Implementation OpenPhoneDaemon
permalink: /Implementation/OpenPhoneDaemon/
---

About
-----

The ophoned service provides a high level interface to any kind of voice communications. It can use different protocols, even though for the moment the only ones are GSM (using ogsmd) and a test protocol that allow us to test the service.

Unlike ogsmd, ophoned provides a real object oriented interface to the calls : Once a call instance has been created it can be used like an independent object.

API
---

ophoned export the following DBus object :

`/org/freesmartphone/Phone`

implementing interface :

`org.freesmartphone.Phone`

The DBus API for the service can be found there : [Standards/PhoneAPI](/Standards/PhoneAPI "wikilink")

[Category:System Developers](/Category:System_Developers "wikilink")
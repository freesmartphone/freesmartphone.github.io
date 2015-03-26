---
title: Implementations msmcomm
permalink: /Implementations/msmcomm/
---

[Category:Palm Pre](/Category:Palm_Pre "wikilink")

Msmcomm
=======

Overview
--------

Msmcomm is the name used for the modem communication protocol found in various Palm Pre devices. Current implementation is found in the FSO git repository (http://git.freesmartphone.org/?p=msmcomm.git;a=summary). It consists of three parts:

-   libmsmcomm: The implementation of the various messages send from and to the modem
-   msmcommd: The daemon handling message passing to and from the modem and link layer stuff
-   msmcomm-specs: The DBus API specification for the msmcommd

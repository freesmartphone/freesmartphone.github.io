---
title: Standards PhoneAPI
permalink: /Standards/PhoneAPI/
---

org.freedesktop.DBus.Introspectable
===================================

method Introspect()
-------------------

-   in:
-   out: s
-   Return a string of XML encoding this object's supported interfaces,

`       methods and signals.`
`       `

org.freesmartphone.Phone.Call
=============================

method Activate()
-----------------

-   in:
-   out: s
-   Accept the call

method GetPeer()
----------------

-   in:
-   out: s
-   Return the number of the peer (usually the number of the call)

method GetStatus()
------------------

-   in:
-   out: s
-   Return the current status of the call

method Initiate()
-----------------

-   in:
-   out: s
-   Initiate the call

method Release()
----------------

-   in:
-   out: s
-   Release the call

method Remove()
---------------

-   in:
-   out:
-   Remove the call object when it is not needed anymore

signal Activated()
------------------

-   out:
-   Emitted when the call is activated

signal Outgoing()
-----------------

-   out:
-   Emitted when the call is outgoing

signal Released()
-----------------

-   out:
-   Emitted when the call is released

org.freesmartphone.Phone
========================

method CreateCall(number,protocol,force)
----------------------------------------

-   in: ssb
-   out: o
-   Return a new Call targeting the given number, with an optional protocol.

`           If the protocol is not provided, the service will determine the best protocol to use.`
`           if force is set to true, then we kill the channel if it is already opened`
`       `

method InitProtocols()
----------------------

-   in:
-   out: as
-   Initialize all the protocols

`          It is not compulsory to call this method, since it will be automatically called the first time`
`          we attempt to create a call.`
`       `

signal Incoming(call)
---------------------

-   out: o
-   Emitted when a call is incoming

[Category:Developer resources](/Category:Developer_resources "wikilink")
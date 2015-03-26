---
title: Standards OpenTelephonyAPI
permalink: /Standards/OpenTelephonyAPI/
---

Purpose
=======

The purpose of the phone interface is to provide common and language independent interface for applications, e.g. dialer application (dial, answer, hold, resume, hangup, dtfm), addressbook application (contact information, vcard), sms application (send, receive, manage) and audio apps (speaker level, etc.).

Requirements
============

-   All blocking method calls must be carefully designed: The interface is used mostly by graphical user interface applications which should not block user interaction. For example if dial is performed with a blocking method the user may not hang up the call while the modem is still connecting.

<!-- -->

-   Suitable abstraction level: We must not blindly map GSM 07.07 calls to the dbus interface. We can and should design the method calls slightly more high level.

Namespaces / Subsystems
=======================

Global Prefix
-------------

Global prefix: **org.freesmartphone.GSM**

Rationales:

-   GSM is ubiquitous and not going away soon.
-   It's more concrete than a 'Phone' or 'Telephony' prefix. Usually, conceptual terms should be preferred over technical terms, however in the mobile phone space these terms are so ubiquitous and established that we don't want to make people learn new taxonomy just for our API.
-   Many subsystems are specific to GSM and are too unspecific if used without a prefix (i.e. Network).

Subsystem Prefixes & API Purpose
--------------------------------

*Note that these links are pointing to our generated docbook documentation. Please checkout our [code repository](/Community_infrastructure#SCM "wikilink") for the actual DBus XML specification files.*

### Device

**Access to mobile station information:**

-   Identify version and supported functionality
-   [IMEI](/IMEI "wikilink") and country code
-   Prepare for a suspend, recover from suspend

See [org.freesmartphone.GSM.Device](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.Device.html;hb=HEAD)

### SIM

**Access to the [SIM](/SIM "wikilink") card:**

-   [IMSI](/IMSI "wikilink")
-   Subscriber Numbers
-   Authorization (PIN, PUK, Locking)
-   Phonebook handling
-   Messagebook handling
-   Configure the preferred SMS centre
-   Incoming Message on SIM notification
-   (planned) SIM card application toolkit handling

See [org.freesmartphone.GSM.SIM](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.SIM.html;hb=HEAD)

### Network

**Access to [GSM](/GSM "wikilink") networks:**

-   Operator availability and registration
-   Connection status and signal strength
-   Call forwarding settings

See [org.freesmartphone.GSM.Network](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.Network.html;hb=HEAD)

### Call

**Access to Voice Calls:**

-   Place and receive single-party calls
-   Configure and send DTMF tones
-   Multiparty handling
-   Configure identity representation and restriction
-   Call forwarding and deflection

See [org.freesmartphone.GSM.Call](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.Call.html;hb=HEAD)

### SMS

**Access to Short Message Service ([SMS](/SMS "wikilink")):**

-   Send and receive a short messages directly (not via SIM)

See [org.freesmartphone.GSM.SMS](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.SMS.html;hb=HEAD)

### CB

**Access to Cell Broadcast Service ([CBS](/CBS "wikilink")):**

-   Configure categories and languages
-   Recieve cell broadcast messages

See [org.freesmartphone.GSM.CB](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.CB.html;hb=HEAD)

### HZ

**Access to Home Zone (HZ) functionality:**

-   Get known home zones
-   Get current zone
-   Receive zone change messages

See [org.freesmartphone.GSM.HZ](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.HZ.html;hb=HEAD)

### PDP

**Access to Packet Data Protocol (PDP) connections:**

-   Configure PDP contexts
-   Initiate/Release connection
-   Get/Set GPRS class

See [org.freesmartphone.GSM.PDP](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.PDP.html;hb=HEAD)

[Category:Developer resources](/Category:Developer_resources "wikilink")
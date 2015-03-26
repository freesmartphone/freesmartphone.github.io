---
title: Brainstorm fsodeviced
permalink: /Brainstorm/fsodeviced/
---

Current Interfaces
==================

Accelerometer
-------------

-   Only basic orientation, no gestures (see below)

Audio
-----

-   wishlist
    -   Say method: It's possible to use espeak, but this doesn't fit into the FSO framework, e.g. missing SoundStatus signal. Signature should be something like: Say(string:language, string text (,HashTable<string,Value> parameters))

Display
-------

-   Add a orientation part:
    -   GetOrientation() -\> s current orientation
    -   SetOrientation(s) -\> ()
    -   LockOrientation(s:application): some Applications always want to have the same orientation, like games (mokomaze,etc.)
    -   UnlockOrientation(s:application): Allow changes to the orientation
    -   SupportedOrientations(): (as:orientations) return all supported orientations
    -   New errors: OrientationLocked, UnknownOrientation
-   Add a screen resolution part:
    -   GetResolution() -\> (i:x,i:y): Get the current resolution
    -   SetResolution(i:x,i:y) -\>(): Set the resolution
    -   SupportedResoltions(s:orientation) -\>(a(i:x,i:y)): returns all supported resolutions for the given orientation.
    -   new Errors: ResolutionNotSupported

LED
---

-   LED names should get a unique name which describes what the LED is supposed to show.

the problem is the following:

LED names on the freerunner:

`gta02_aux_red       `
`gta02_power_blue    `
`gta02_power_orange`

LED names on the milestone

`blue  `
`spotlight`
`button_backlight`
`lcd_backlight       `
`torch_flash`
`green               `
`red`

this is not a good abstraction for application devolopers and needs device specific options on their side. Instead they should have names like:

-   alarm
-   critical
-   info
-   flash
-   TODO

This could be easyily done by adding an option in the machine config like: led_gta02_power_blue = info

Maybe this should even happen through a proxy and configurable for users. This gives us the options to use more LEDs at the same time. --[Playya](/User:Playya "wikilink") 11:59, 6 February 2010 (UTC)

Info
----

Input
-----

-   Key Mappings

Many smartphone have more hardware keys than the Freerunner. This list should cover all known keys from all supported devices. Don't rely that all keys are available on all devices.

-   -   AUX
    -   POWER: Power on/off device
    -   HOME: Go back to home screen (same as AUX?)
    -   MENU:
    -   CAMERA: Activate camera
    -   ZOOM_IN/ZOOM_OUT
    -   BACK
    -   SEARCH
    -   MEDIA_NEXT
    -   MEDIA_PREVIOUS
    -   MEDIA_PLAY_PAUSE
    -   MEDIA_STOP

<!-- -->

-   Add GrabKeys(Keys:as)/ReleaseKeys(keys:as) to grant exclusive access to applications. Needs a notification API on the applications side.
    -   KeyNotification.Pressed(keys:as): keys is a combination of pressed keys

IdleNotifier
------------

Orientation
-----------

PowerControl
------------

PowerSupply
-----------

RealtimeClock
-------------

Rfkill
------

Missing
=======

Gesture Recognition
-------------------

-   I'll try to implement this plugin at 26c3 --[Playya](/User:Playya "wikilink") 22:26, 8 December 2009 (UTC)
    -   Implemented Math stuff using GSL. Sent it to paul for a review --[Playya](/User:Playya "wikilink") 20:37, 7 January 2010 (UTC)
-   More information in Paul Borza's bachelor thesis: [1](http://accelges.googlecode.com/files/ThesisPaper.pdf)
-   His source on [2](http://accelges.googlecode.com/)
-   Interface Gesture
    -   signal void Recognised( string name(,string sensor) ): emited if gesture was recognised
    -   signal void NewGesture( string name ): emitted if a new gesture was registered
    -   ObjectPath StartTraining(string name): start a new trainig. return a path to the new Gesture.Trainig object
    -   string[] KnownGestures(): list all known gestures
-   Interface Gesture.Training
    -   bool Stop(): returns true if Learning was successful
    -   bool Split(): split the recording between several tries

Bluetooth
---------

-   Add things like remoko:
    -   <http://code.google.com/p/remoko/>
-   more bluetooth stuff
    -   headset
    -   use phone as a headset
    -   Network
    -   GPS
    -   Accel
-   Heinervdm's PBAP plugin
-   might it be possible to run gabriel(dbus over SSH) over bluetooth?

USB Handling
------------

-   Handle different USB modes, at the same time if possible
    -   network
    -   data
    -   audio
    -   Synchronisation
    -   Thering(both ways)
-   Enable selection of a single mode by dialog

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
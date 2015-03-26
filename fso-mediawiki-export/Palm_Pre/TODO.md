---
title: Palm Pre TODO
permalink: /Palm_Pre/TODO/
---

TODO
----

There are currently a lot of things we have to do to get a running FSO powered system on the Palm Pre. Below all points are listed which needs to be done in the future. They are not prioritised - we have to do this too!

-   fsodeviced
    -   ~~palmpre audio router needs testing~~ Audio routing will be implemented in the new fsoaudiod (morphis is working on it) as SHR is not really using FSO's current audio API
-   fsousaged
    -   ~~check suspend/resume handling~~ OK
    -   ~~check if resume reason is read correctly from sysfs node~~ OK
-   fsogsmd
    -   finish modem_qualcomm_palm plugin (morphis)
        -   the following parts needs to be done: SMS, PDP, VM, SUPS
        -   This needs more commands to be implemented in msmcomm (morphis): basic commands are working
-   msmcomm (morphis)
    -   implement SMS/GPS (morphis)
-   Bluetooth: needs investigation how we can run the Bluez stack on the Palm Pre. There is already a interface for Bluetooth shown by ifconfig.
    -   We have a first start on a power control plugin for activating bluetooth, someone needs to finish it
-   Shutdown/reboot does not working with shutdown or reboot (without any arguments)
    -   reboot -d -f works
    -   halt -d -f works
    -   reboot (without arguments) is hanging somewhere in the init process
-   finish xkeyboard-config (http://git.shr-project.org/git/?p=xkeyboard-config.git;a=summary)
    -   keys like .:; does not work
    -   shift + character does not work
    -   we need support for the orange key

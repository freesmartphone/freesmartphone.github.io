---
title: Palm Pre Forwarding
permalink: /Palm_Pre_Forwarding/
---

[Category:Palm Pre](/Category:Palm_Pre "wikilink") __FORCETOC__

Palm Pre Modem Forwarding
=========================

It is possible to forward the Pre's modem to your host computer via a usb network connection.

Then you can access the Pre's modem (running WebOS) from your host computer using msmcommd and mdbus2.

Setup
-----

-   Cross-compile the serial_forward utility (git.freesmartphone.org) for the Pre (using OpenEmbedded or another cross-toolchain) and copy it over
-   Enable usbnet on the Pre:
        usbnet enable

-   Connect to the Pre using novaterm:
        novaterm

-   Stop the TelephonyInterfaceLayer:
        stop TelephonyInterfaceLayer

-   Reset the modem:
        pmmodempower cycle

-   Run serial_forward, to forward the modem to you host computer:
        ./serial_forward -n /dev/modemuart -p 3001 -t hsuart

-   On your host computer configure the usbnet interface:
        ifconfig usb0 192.168.0.1

-   Install libmsmcomm, msmcomm-specs and msmcommd
-   Change the connection settings in msmcommds config (/etc/msmcommd.conf) to look like this:

<!-- -->

    [connection]
    # Which type of connection we should use to connect to the modem: network, serial
    type = serial
    path = /dev/modemuart
    # If you want to connect to the modem over a network link you should use the
    # configuration below
    type = network
    ip = 192.168.0.202
    port = 3001

-   Start msmcommd:
        msmcommd

-   Install mdbus2 or any other DBus debugging tool
-   Issue the following DBus commands, to setup the modem:

<!-- -->

    org.msmcomm /org/msmcomm org.msmcomm.Management.Reset
    org.msmcomm /org/msmcomm org.msmcomm.Management.Initialize
    org.msmcomm /org/msmcomm org.msmcomm.Misc.TestAlive
    org.msmcomm /org/msmcomm org.msmcomm.SIM.VerifyPin "PIN1" "1234"
    org.msmcomm /org/msmcomm org.msmcomm.State.ChangeOperationMode "ONLINE"

Sources
-------

<http://mm.gravedo.de/blog/?p=23>

<http://blog.slyon.de/2011/05/08/hppalm-pre2-developer-device/>
---
title: Tutorials sms
permalink: /Tutorials/sms/
---

Sending SMS
===========

-   with mdbus:

` mdbus -s org.freesmartphone.ogsmd /org/freesmartphone/GSM/Device org.freesmartphone.GSM.SMS.SendMessage 0049987654321 "test message"  []`

-   with python:

<!-- -->

    #!/usr/bin/python

    import sys
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    gsm_device_obj = bus.get_object( 'org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device' )
    gsm_sms_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.SMS')
    gsm_sms_iface.SendMessage( sys.argv[1], sys.argv[2], [] )

Reading SMS (from the sim card)
===============================

-   with mdbus:

` mdbus -s org.freesmartphone.ogsmd /org/freesmartphone/GSM/Device org.freesmartphone.GSM.SIM.RetrieveMessagebook unread`

i tried here as parameter unread, but this doesn't work here. i must provide "read" or "all", but that may be version dependent.

-   with python:

<!-- -->

    #!/usr/bin/python

    import sys
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()
    device = bus.get_object( 'org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device' )
    iface = dbus.Interface(device, 'org.freesmartphone.GSM.SIM')
    for i in iface.RetrieveMessagebook("all"):
        print repr(i)

[Category:Tutorial](/Category:Tutorial "wikilink")
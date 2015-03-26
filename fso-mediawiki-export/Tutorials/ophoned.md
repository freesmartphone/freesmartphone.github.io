---
title: Tutorials ophoned
permalink: /Tutorials/ophoned/
---

In this tutorial we are going to learn how to use [ophoned dbus interface](/Standards/PhoneAPI "wikilink") to make a simple phone applications

Like in the other tutorials, we are going to use python, but of course any language with dbus client support could be used as well.

The application
---------------

The application we are going to do is very simple (and would be quite stupid as a real application) : The application waits for incoming phone calls, then if the caller is a contacts in our SIM card phonebook, we answer it, otherwise we don't.

Initialization
--------------

The first thing our application needs to do is to get the dbux proxy object. I won't enter into the details here, see [This other tutorial](/Tutorials/GSM_python "wikilink") for more information.

    import dbus
    import gobject

    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    # First, we get the dbus proxy object
    bus = dbus.SystemBus()
    gsm = bus.get_object('org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device')
    phone = bus.get_object('org.freesmartphone.ophoned', '/org/freesmartphone/Phone')

Next thing is to turn on the antenna power and register into a GSM network :

    print "Set antenna power on"
    gsm.SetAntennaPower(True)
    print "register on the network"
    gsm.Register()

Getting the contacts
--------------------

We want to get the list of contacts in the sim, for that we use the [SIM API](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=otapi/xhtml/docbook-org.freesmartphone.GSM.SIM.xhtml;hb=HEAD)

One thing to note is that the RetrievePhonebook method return a list of structure containing the fields : index, name, number. To access a field of a DBus structure instance in python we use __getitem__ ( [] ) operator

    numbers = []

    # Then we get the contact book
    contacts = gsm.RetrievePhonebook()
    for contact in contacts:
        print "index: %d, name: %s, number: %s" % (contact[0], contact[1], contact[2])
        numbers.append(str(contact[2]))

Initialization of the all the available phone protocols
-------------------------------------------------------

The ophoned service provides a interface to several voice communication protocol. Because some of those protocols may need to be initialized before being used, we are going to call the InitProtocols method.

    print "Init phone protocols"
    phone.InitProtocols()

Waiting for an incoming call
----------------------------

We are going to set up a callback function that will be called every time we have an incoming call. The function get the call DBus object path as an argument, we can retrieve the DBus Call object proxy from this path.

Also, To be able to get the DBus signals, we need to start the main loop (here we are using gobject.MainLoop() )

    def on_incoming(call_path):
        print "incoming: %s" % call_path
        call = bus.get_object('org.freesmartphone.ophoned', call_path)
        peer = str(call.GetPeer())
        print "peer = %s" % peer

    phone.connect_to_signal('Incoming', on_incoming)

    print "starting the main loop"
    loop = gobject.MainLoop()
    loop.run()

Answering the call
------------------

Even though we have the incoming call object, we still haven't answered it. To answer a call we use the Activate method of the call object. We have to carefully note that even after we called the Activate method, the call will need some time before being in the 'activated' state. In between it will be in the 'activating' state.

To release a call, we can call the Release method.

Here is the new version of our **on_incoming** method :

    def on_incoming(call_path):
        print "incoming: %s" % call_path
        call = bus.get_object('org.freesmartphone.ophoned', call_path)
        peer = str(call.GetPeer())
        print "peer = %s" % peer
        if peer in numbers:
            print "Hey, I know this person !"

            def on_activated():
                print 'call activated'

            def on_released():
                print 'call released'

            call.connect_to_signal('Activated', on_activated)
            call.connect_to_signal('Released', on_released)
            call.Activate()
        else:
            print "I don't know this person !"
            call.Release()
            print 'call releasing'

[Category:Tutorial](/Category:Tutorial "wikilink")
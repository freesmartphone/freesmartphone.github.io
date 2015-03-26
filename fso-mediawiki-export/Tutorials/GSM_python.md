---
title: Tutorials GSM python
permalink: /Tutorials/GSM_python/
---

This tutorial is for people who want to use the org.freesmartphone.GSM DBus API from python. The goal is not to give a complete implementation (for that it is better to refer to the zhone application), but just to give an introduction to the concepts used.

First of all, two pieces of software use this interface already:

-   [zhone](http://git.freesmartphone.org/?p=zhone.git;a=summary), the official client application developed in parallel to the framework. This is the best place to see a working implementation using the framework.
-   Tichy. A python applets manager. You can get the code by typing

`svn checkout `[`https://svn.projects.openmoko.org/svnroot/tichy`](https://svn.projects.openmoko.org/svnroot/tichy)

Setting up the system
---------------------

In order to use the framework, you need to have it installed on your machine (presumably a Openmoko cell phone). You can either install it by yourself, or use the pre-build images from [there](http://downloads.freesmartphone.org/fso-stable/).

Using DBus
----------

All the framework functionalities are exposed via DBus call. So the first thing you have to do in your application is to create proxies to the DBus interfaces. With python it is rather simple:

    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SystemBus()

    usage_obj = bus.get_object('org.freesmartphone.ousaged', '/org/freesmartphone/Usage')
    usage_iface = dbus.Interface(usage_obj, 'org.freesmartphone.Usage')

    gsm_device_obj = bus.get_object( 'org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device' )
    gsm_call_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Call')
    gsm_device_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Device')
    gsm_network_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Network')

Here gsm_device_obj is a proxy object referencing the DBus object at /org/freesmartphone/GSM/Device in the service org.freesmartphone.ogsmd.

We also create one proxy interface for each freesmartphone interface that the object implements: org.freesmartphone.GSM.Call, org.freesmartphone.GSM.Device and org.freesmartphone.GSM.Network.

So now we can use the interface like python object, the DBus calls will be done transparently.

Requesting the resource
-----------------------

Before we can use the GSM subsystem, we need to request it :

    usage_iface.RequestResource("GSM")

When we are done using GSM, we can tell the framework so :

    usage_iface.ReleaseResource("GSM")

Turning the antenna on
----------------------

    gsm_device_iface.SetAntennaPower(True)
    gsm_network_iface.Register()

[Note : In fact things can get more complicated if those methods fail, see zhone for the real way of doing things...]

Initiating a call
-----------------

Now we can actually start using the call interface. The API can be found [here](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.GSM.Call.html;hb=HEAD).

One thing to note is that the interface doesn't provide one object per call, but instead lets you use an 'id' parameter to specify the call you want to work on. So every calls has an assigned id. In our example (inspired by the zhone application code), we are going to create a class for the calls, so that we have better control over individual calls. We can do it by having a Call class, and a CallManager class :

    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    class CallManager(object):
        def __init__(self):
            self.calls = {}

            bus = dbus.SystemBus()
            gsm_device_obj = bus.get_object( 'org.freesmartphone.ogsmd', '/org/freesmartphone/GSM/Device' )
            self.gsm_call_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Call')
            self.gsm_device_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Device')
            self.gsm_network_iface = dbus.Interface(gsm_device_obj, 'org.freesmartphone.GSM.Network')

            try:
                self.gsm_device_iface.SetAntennaPower(True)
                self.gsm_network_iface.Register()
            except Exception, e:
                print e

        def initiate(self, number):
            call_id = self.gsm_call_iface.Initiate(number, "voice")
            return Call(self, call_id)


    class Call(object):
        def __init__(self, manager, id):
            self.manager = manager
            self.id = id
            self.state = 'initiated'

First we create a CallManager class, that will be used to initialize the system and also dispatch the org.freesmartphone.GSM.Call signals to the right Call instance. the dictionary **calls** contains all the created calls.

Then we have a class 'Call', that represents a single call. It may be important to keep track of the state of a call, so we use a **state** attribute for that.

The CallManager.initiate method is used to actually start a new outgoing call. It calls the org.freesmartphone.GSM.Call.Initiate method. After you do that, the framework will return you a call id, and initiate the outgoing call.

The Call session
----------------

A call can be seen as a state machine. When you use the org.freesmartphone.GSM.Call.Initiate method, your created call is in the 'initiate' state. When it starts to ring, it will be in the 'outgoing' state, later if your correspondent hang up, the call will be in the 'release' state.

But of course things can get more complicated if you decide to hang up, hold the call, or cancel the outgoing call. [ TODO: find mickey drawing of the complete state machine ]

When the call goes into a new state, the framework will emit a 'CallStatus' signal, with the id of the call as first argument. We have to handle this signal in our CallManager instance:

    def on_call_status(self, id, status, properties ):
        print "CALL STATUS=", id, status, properties
        self.calls[id].on_call_status(status, property)

And we also need to connect this method to the signal, in the **__init__** method :

        self.gsm_call_iface.connect_to_signal("CallStatus", self.on_call_status)

So for the moment all the **on_call_status** does is to dispatch the Status changing signal to the right Call instance. Now we need to actually handle the signal. In the Call class, we add :

    def on_call_status(self, status, properties ):
        self.state = status

So here we just update the status of the call. But of course in a real software what we want to do is to trigger some actions on specific state change (For example change the GUI). The best way to do so is to let the Call object emit a signal, that can then be caught by any part of the software that needs to react to a specific state change. How can we do that ? One solution (used in zhone), is to have a list of callback handlers in the Call class. When the state changes you can then trigger all the callback. Parts of the code that need to react to a state change can add their call backs to the list.

An other way would be to simply let the Call class inherits for gobject.GObject, because then, the whole callback system is already there. If we do so we can then use the **emit** method.

If we decide to use the gobject.GObject, the Call class now looks like this :

    class Call(gobject.GObject):
        __gsignals__ = {
            'outgoing' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
            'active' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ()),
            'release' : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, ())
        }
        def __init__(self, manager, id):
            super(Call, self).__init__()
            self.manager = manager
            self.id = id
            self.state = 'initiated'

        def on_call_status(self, status, properties ):
            if status == 'outgoing':
                self.emit('outgoing')
            elif status == 'active':
                self.emit('active')
            elif status == 'release':
                self.emit('release')
            self.state = status

Our Call class can react to the 'outgoing', 'active', and 'release' status (In fact there are other status, but I won't talk about it there). Also any parts of the code that want to be signaled of a state change can directly connect to the Call signals.

One thing we have to remember is to make the CallManager remove a call from its call list when the call is released. Since we can now connect to the signal we do it very simply, by rewriting the initiate method like this :

    def intitiate(self, number):
        call_id = self.gsm_call_iface.Initiate(number, "voice")
        ret = Call(call_id)
        def on_call_release(call):
            del self.calls[call.id]
        ret.connect('release', on_call_release)
        return ret

Last but not least, since the Call class is the actual class that will be used by our application, we need to add a **release** method to it, that will call the org.freesmartphone.GSM.Call.Release method :

    def release(self):
        self.manager.gsm_call_iface.Release(self.id)

Using the Call class from the application
-----------------------------------------

Ok finally, the application can use our CallManager and Call class this way :

    manager = CallManager()
    call = manager.initiate(the_number)

    def on_outgoing(call):
        # do stuffs
        return

    def on_active(call):
        # do stuffs
        return

    def on_release(call):
        # do stuffs
        return

    call.connect('outgoing', on_outgoing)
    call.connect('active', on_active)
    call.connect('release', on_release)

[Category:Tutorial](/Category:Tutorial "wikilink")
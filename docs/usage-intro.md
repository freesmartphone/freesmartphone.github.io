# Resource Handling

One of the most important aspects of middleware for mobile devices is saving energy. To do this, the system needs to make sure that peripherals are only powered when they are actually in use by at least one application. In order to support multiple concurrent applications, it is not possible to leave peripheral control up to individual applications — otherwise one application could shut down e.g. a GPS receiver, while another application still wants to access it.

One solution to this is a centralized registry, where applications announce when they need access to peripherals. The registry can then perform the necessary actions and grant or deny access. It can also keep track of a usage counter so that resources are only started up when the first client arrives, likewise only shutdown once the last client leaves the sytem. Keep in mind though that once such a registry is being used, it is most undesirable for clients to bypass this facility by controlling power directly — doing so can severly disturb the system.

FSO introduces the concept of resources. A *resource* is a high-level entity with a *name* and a *state*. The name is used to identify a resource (e.g. **WiFi**), the state is describing its condition (e.g. **enabled**). It is important to understand that a resource not necessarily correlates to a peripheral device. Although enabling a resource such as **Bluetooth** most likely has the consequence of powering up a device, there may as well be more to it, such as launching a low level device handling services or allocating related resources.

## Client-side resource handling

As a client, FSO resource handling works by accessing [`org.freesmartphone.Usage`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html). A typical usage pattern is defined through the following four steps:

1.   Checking resource availability
2.   Requesting the resource
3.   Accessing the resource
4.   Releasing the resource

### Checking resource availability

Resources can be dynamic, i.e. they may not always be available. Although not strictly necessary, it is recommended that clients check whether a resource is available before requesting it. To check for availability, call [`ListResources`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#ListResources). The result is a list of available resource names that can to be used to identify resources when requesting or releasing.

Since a resource is not necessarily present throughout the whole life-cycle of an application, it may enter or leave the system at any time. The resource system will notify clients, when a resource has been made available by broadcasting the signal [`ResourceAvailable`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#ResourceAvailable). Subscribe to this signal to stay informed about resources becoming available or unavailable.

### Requesting the resource

A client that wants to access the resource can call [`RequestResource`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#RequestResource). This call does not need parameters, since the system will keep track about the identification of the client. If the resource system can not grant access, the client will be sent an error. This can happen if the resource is not available, has been explicitly disabled, or is in a state that otherwise prohibits access. Depending on the actual error, a client may or may not retry the call after a while.

### Accessing the resource

Once [`RequestResource`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#RequestResource) returned without an error, a client may access the resource. The actual way of accessing a resource is specific to the resource hence out of scope of this document. In certain conditions, resources may become unavailable while clients are still accessing them. In this case, a client is requested to immediately stop accessing the resource. Some resources may enforce this through access control, some may not — to handle that case, it is recommended that clients listen for [`ResourceAvailable`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#ResourceAvailable) announcements throughout their life cycle.

### Releasing the resource

When a client is finished accessing a resource, it calls [`ReleaseResource`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#ReleaseResource) to inform the system. After issuing this call, clients must no longer access the resource through whatever means. Note that due to the way the dbus interprocess communication works, the system can detect a client leaving the bus, no matter whether this has been a regular detach or happened due to unforseen circumstances, such as a crash. In that case, the system will automatically release all resources the client has previously requested. It is important to remember that resource requests are *not* persistent over the clients life cycle. Once a client starts up again, it has to treat all resources as being released and need to request them again.

Note that the automatic release behaviour especially affects dbus command line tools such as **dbus-send** or **mdbus**, which usually only stay on the bus for very short periods. If a client can not stay on the bus while it wants to access a resource, you need to resort to the policy interface (see next section).

## Resource Policies

Once in a while, reference counted handling of resources gets in your way, for example when you are running legacy applications or want to configure or debug peripherals. In that case it may become necessary for a resource to be always enabled or always disabled. While not recommended, it is possible to switch from automatic resource control to manual control by calling [`SetResourcePolicy`](http://docs.freesmartphone.org/org.freesmartphone.Usage.html#SetResourcePolicy). Valid values are **auto** (which is the default on system startup), **enabled**, and **disabled**.

## Server-side resource handling

*** TO BE WRITTEN *** ... using org.freesmartphone.Resource, best practices, hardware abstraction, ...


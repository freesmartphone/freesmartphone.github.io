# Implementations

– *Cornucopia* – *Cor\`nu\*co"pi\*a (k[^o]r`n[-u]\*k[=o]"p[i^]\*[.a]), n.;*

> pl. Cornucopias (-[.a]z). [L. cornu copiae horn of plenty. See Horn, and Copious.]
> 1. The horn of plenty, from which fruits and flowers are
> represented as issuing. It is an emblem of abundance.
> [1913 Webster]

## Overview

This describes the Vala/C reference implementation of the freesmartphone.org APIs, codename 'Cornucopia'.

We describe only the big picture here – see the documentation for the individual projects for details.

## Source code

Note for packagers: The canonical source code location for all our software is at [http://sourceforge.net/projects/freesmartphone/files/sources/](http://sourceforge.net/projects/freesmartphone/files/sources/). For release tarballs, you don't need to have Vala installed on the build host.

## Tools

To support our middleware framework, we have created a number of tools, many of those which are not freesmartphone-specific. Feel free to adopt them for your project.

### vala-dbus-binding-tool

```vala-dbus-binding-tool``` is a way to create calling stubs (gobject interfaces) from DBus interface description.

[vala-dbus-binding-tool](https://www.github.com/freesmartphone/vala-dbus-binding-tool) is a seperate project at github.

### mdbus2

```mdbus2``` is an interactive DBus introspection and interaction utility.

[mdbus2](https://www.github.com/freesmartphone/mdbus2) is a seperate project at github.

### More tools

The following tools reside in the [tools](https://github.com/freesmartphone/cornucopia/tree/master/tools/) subdirectory of Cornucopia:

* ```apm2``` emulates the apm binary, but sends the equivalent dbus commands.
* ```fso-abyss``` is a GSM 07.10 multiplexing helper, exposes a multiplexed line via pseudo-tty.
* ```fso-alsa``` is an ALSA mixer scenario helper utility.
* ```fso-raw``` is the fsousaged resource aquisition wrapper for integrating legacy tools.
* ```mioctl``` is a simple command line utility to issue ioctls.
* ```mkdump``` dumps kernel messages (kobject, netlink).
* ```mterm2``` is a muxer-aware terminal emulator.
* ```serial_forward``` forwards a serial port over a network connection.

## Libraries

Although these libraries have been created for the use with the FSO daemons, they have few dependencies and might as well be used in many other projects.

If there is sufficient interest, we can easily factor them out as standalone projects – for now they reside in the [libfsoframework](https://github.com/freesmartphone/cornucopia/tree/master/libfsoframework) subdirectory of Cornucopia:

#### libfso-glib

A gobject-based FSO DBus-API library.

This library supports writing applications that communicate via dbus using the FSO APIs. Vala-bindings are available.

#### libfsobasics

A general purpose utility C-library based on glib-2.0.

libfsobasics provides classes and functions for

* smart keyfile handling (.ini style),
* debug logging,
* string and file handling convenience,
* process control,
* kobject notifications,
* netlink notifications,
* inotify notifications,
* sync/async handling.

Vala bindings are available.

#### libfsotransport

A gobject-based transport library.

This library supports writing applications that read and write data from files, serial ports, and ptys, including glib-mainloop integration.

Vala-bindings are available.

#### libfsoframework

A gobject-based FSO subsystem implementation library.

This library supports writing FSO subsystems. It contains utility classes for subsystems, plugins, kobject dispatchers, netlink dispatchers, and more.

Vala-bindings are available.

#### libfsoresource

A gobject-based FSO Resource C-library.

libfsoresource provides convenience classes to integrate with the FSO Resource System.

Vala bindings are available.

## Daemons

#### fsousaged

A resource manager.

fsousaged implements the FSO Usage DBus API. This API is concerned with coordinating application I/O requirements (think reference counting for resources).

Applications are not supposed to turn on or off devices, since they do not have any knowledge about concurrent applications that may also be using the device.

It also ensures proper high-level suspend and resume preparation for available resources. Although it might be tempting, preparing a GSM modem for suspend can't sanely be handled in kernelspace, since you need to send several AT commands to it in order to prevent bogus wakeups. 

Which commands exactly is very device and situation specific, hence should be handled by userspace. fsousaged compiles to C and is very lightweight. It needs less than 100 KB of disk space and typically operates with a RES segment of about 2 MB.

#### fsodatad

A (constant) data lookup manager.

fsodatad implements the FSO Data DBus API. This API allows querying constant data about the world, such as geographic timezones, mobile broadband network providers, etc.

fsodatad compiles to C and is very lightweight.

#### fsodeviced

A device abstraction manager.

fsodeviced implements the FSO Device DBus API. This API allows peripheral control, such as managing audio, backlight brightness, LEDs, Vibrator, Accelerometer, and power control for devices without dedicated controlling daemon. It can deal with charging notification and RTC, forwarding button events and notifying about the system's idleness status.

It also ensures proper high-level suspend and resume preparation for available resources. Although it might be tempting, preparing a GSM modem for suspend can't sanely be handled in kernelspace, since you need to send several AT commands to it in order to prevent bogus wakeups. Which commands exactly is very device and situation specific, hence should be handled by userspace.

fsodeviced compiles to C and is very lightweight. It has been written to superseed all the device-specific control daemons Linux-based mobile systems have used in the past, such as the Zaurus' ```zaurusd```, the Neo's ```neod```, Kernel Concepts' ```deviced```, etc. It also superseeds the non-customizable ```hald```. It features a plugin-architecture, so you only pay for the features you really need.

#### fsotdld

A time, data, and location manager.

fsotdld implements the FSO Device Time, Data, and Location APIs.

fsotdld compiles to C and is very lightweight. It features a plugin-architecture, so you only pay for the features you really need.

#### fsonetworkd

A simple network service manager.

#### fsogsmd

A GSM Communications manager.

fsogsmd implements the FSO GSM DBus API. This API delivers a simple way to handle voice and data communication with GSM modems.

fsogsmd compiles to C and is very lightweight.

#### fsoaudiod

An audio scenario manager.

fsoaudiod implements the FSO Audio DBus API.

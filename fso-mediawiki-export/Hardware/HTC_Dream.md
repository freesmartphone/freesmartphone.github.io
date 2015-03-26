---
title: Hardware HTC Dream
permalink: /Hardware/HTC_Dream/
---

[200px|left](/Image:Htcdream.JPG "wikilink")

Presentation
============

The Htc Dream, also known as G1 or ADP1 was the first Android phone: It runs a Linux kernel, which doesn't have standard kernel\<-\>userland interfaces, which makes the port difficult and problematic, not to count that some drivers only work only under certain conditions, lacks some standard Linux features. Most of the hardware now work but some rough edges remains(wifi PSM, and bad alsa driver(some applications work fine, some other don't), refer to the [HardwareComparison](/HardwareComparison "wikilink") for more details.

Status updates
==============

Here is a brief table about the [status of the project](http://www.htc-linux.org/wiki/index.php?title=Dream#Status) that we will try to keep update. Here is a video showing SHR on the HTC Dream: [part 1](http://www.youtube.com/watch?v=5ZpbWc0vFlc) [part 2](http://www.youtube.com/watch?v=zs4Z0It7mA4) [part 3](http://www.youtube.com/watch?v=0VnbG2uTHT4)

TODO
====

Here is a [TODO list](/Hardware/HTC_Dream/TODO "wikilink")

Free the HTC Dream (G1)
=======================

This page is to document efforts to liberate the HTC Dream from nonfree software.

We would prefer a standard GNU/Linux distribution rather than an Android/Linux.

Most of Android is licensed freely under the Apache License 2.0. The Linux core is mostly Free Software under the GPLv2. However, there are numerous components of the default software stack on the HTC Dream that are proprietary software. Most notably, nearly any component that touches the hardware directly is proprietary software.

We believe that freedom is an important end in itself -- that software developers should respect the rights of users to share and modify the software they use. But the importance of freedom is made particularly evident by the example of Google G1/ADP1 (the first commercial Android phone). While most of the software running on the phone is free, and can be distributed by anyone, some components are proprietary. In addition to the dispensable "Google Experience" applications, such as GMail and Google Maps, these components include several libraries and drivers necessary for interfacing with the phone's hardware. Since these components are not free software, the user community cannot redistribute them. And since some of them are necessary to make the phone work, the user community can't share working firmwares.

HTC Dream preinstalled non free software components
---------------------------------------------------

This is a list of proprietary components essential to some functionality of the HTC Dream device. Descriptions are our best guess -- please let us know if yours is better.

Components essential to basic phone functionality:

`   * libhtc_ril (the GSM radio interface library)`
`   * libhtc_acoustic.so (the basic audio library)`
`   * libaudioeq.so (presumably a library related to audio levels) `

Components necessary to make non-phone hardware work:

`   * libgps.so (the GPS library)`
`   * lights.goldfish.so (screen & keyboard backlights and other LEDs)`
`   * sensors.trout.so (accelerometer & compass)`
`   * system/bin/akmd (sensor daemon?) (also stores settings in /data/misc/akmd_set.txt)`
`   * brf6300.bin (bluetooth firmware)`
`   * libqcamera.so (camera) `

Media encoding & decoding:

`   * libOmxCore.so`
`   * libOmxVidEnc.so`
`   * libOmxH264Dec.so`
`   * libOmxMpeg4Dec.so`
`   * libmm-adspsvc.so`
`   * libopencorehw.so `

Other:

`   * libhgl.so (3D rendering)`
`   * libjni_pinyinime.so (Pinyin character entry)`
`   * libspeech.so (Speech recognition)`
`   * libpvasf.so (Streaming Pocket Video Windows Media Decoder Library)`
`   * libpvasfreg.so (ASF parser for libpvasf) `

Building SHR for the HTC Dream
==============================

Here are the instructions about [how to build SHR](/Hardware/HTC_Dream/SHR "wikilink")
And here's how to [how to build The kernel(and compat wireless)](/Hardware/HTC_Dream/KBUILD "wikilink")

Communications
==============

You can find us on IRC:

Server: irc.freenode.net Channel: \#lp-it

people: gnutoo, graziano

[Category:Hardware](/Category:Hardware "wikilink")
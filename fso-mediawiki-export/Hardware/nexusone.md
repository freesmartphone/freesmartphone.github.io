---
title: Hardware nexusone
permalink: /Hardware/nexusone/
---

TODO
----

### Wifi

-   make bcm4329 wifi work(htc leo got it working) or(better) import a standard kernel driver for the bcm4329 chip from mainline.
-   make bcm4329 bluetooth work(htc leo got it working)

### Sound

-   add microphone support in the kernel instead of userland
-   handle sound volume(or migrate it in /etc/asound.conf or modify the kernel driver)

### Other

-   integrate the GPS into fso
-   add ondemand in the kenrel
-   update the kernel revision in oe
-   make a better rules.yaml
-   migrate the machine configs to oe-core

quirks
------

### Wifi

The wifi chip is a bcm4329

-   replace -DCSCAN by -DWL_IW_USE_ISCAN in the bcm4329 Makefile
-   scan for wireless network like that:

`iwlist eth0 scan essid ""`

### suspend-resume

Android phones uses wakelocks: to make resume work press on the power button and run that:

`chvt 1;chvt 2`

Alsa
----

There is an alsa driver:

-   compile the htcleo as a module
-   Put the "firmware"(calibration data) in /lib/firmware/
-   Add this to .asoundrc:

`# Device for playing media audio`
`pcm.softvol {`
`    type softvol`
`    slave.pcm "plughw:0"`
`    control.name "PCM"`
`    control.card 0`
`}`
`pcm.!default {`
`        type plug`
`        slave.pcm "softvol"`
`}`

-   load the modules

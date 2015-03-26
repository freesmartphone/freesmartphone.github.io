---
title: N900 Old overview
permalink: /N900_Old_overview/
---

Overview
--------

-   Audio/Power Management Chip is TWL4030 (same as [Palm Pre](/Palm_Pre "wikilink"))
    -   /sys/class/i2c-adapter/i2c-1/1-0048
-   Accelerometer is LIS302DL (same as [Freerunner](http://wiki.openmoko.org/wiki/Neo_FreeRunner))
    -   /sys/class/i2c-adapter/i2c-3/3-001d
-   Vibrator is controlled via led interface
    -   /sys/class/leds/twl4030\\:vibrator/
-   Proximity Sensor
    -   /sys/devices/platform/gpio-switch/proximity/
    -   state will return open/closed, so just 0% or 100%
-   Ambient Light Sensor
    -   /sys/class/i2c-adapter/i2c-2/2-0029
    -   lux file will return the brightness
-   Power Button: /dev/input/event0
-   Keyboard: /dev/input/event1
-   Touchscreen: /dev/input/event3
-   Video Cable Detection
    -   /sys/devices/platform/nokia-av

<!-- -->

-   What to do about different special buttons?
    -   /sys/devices/platform/gpio-switch/cam_shutter/state -\> open/closed
        -   camera LEDS should be available only if cam_shutter is opened
    -   /sys/devices/platform/gpio-switch/headphone/state -\> connected/disconnected
        -   We need to reroute audio when somebody inserts a headphone
    -   /sys/devices/platform/gpio-switch/slide/state -\> open/closed
        -   We should enable and disable keyboard leds according to state

<!-- -->

-   GPS is connected via gsm modem - I haven't checked the details yet
-   What to do about the cameras (video/photo)? What about tagging photos (geotag, time, whatever)? Cameras are Video4Linux devices on N900 btw.
-   There's an FM receiver, but I guess we can ignore this one for now. We need a multimedia daemon for this, which could also handle DVB-H on other devices.
-   There's an FM transmitter. There should be audio routing support for it in the new audio manager. It is available as /dev/radio0 on n900.
-   Keyboard LEDs, status LED (exported via led interface on sysfs)
-   different Buttons - I did not check this yet

LEDs
----

### sysfs

-   /sys/bus/i2c/drivers/lp5523/2-0032
    -   selftest
    -   engine1_mode
    -   engine2_mode
    -   engine3_mode
    -   leds:lp5523:r
    -   leds:lp5523:g
    -   leds:lp5523:b
    -   leds:lp5523:kb1
    -   leds:lp5523:kb2
    -   leds:lp5523:kb3
    -   leds:lp5523:kb4
    -   leds:lp5523:kb5
    -   leds:lp5523:kb6

### engineX_mode: disabled

This pattern mode is not used.

### engineX_mode: load

You can setup a pattern by writing into engineX_load and engineX_leds. engineX_leds takes a string which led's should be lighten by this pattern in form of bits ("0000rgb00"). The 0's are the 6 LEDs below the keyboard and the rgb are the colored LEDs from the status LED. The file engineX_load takes the pattern in which the LEDs should be lightend. Check [LED patterns from maemo wiki](http://wiki.maemo.org/LED_patterns)

### engineX_mode: run

The pattern configured in load mode will run until mode is changed again.

### warning

Do not try to use trigger on LEDs while an engine is running on this LED. My N900 restarted due to this.

Free/Nonfree parts of Maemo5
----------------------------

<http://wiki.maemo.org/Free_Maemo>

As you can see basically the part FSO handles and parts of the UI are closed source, but the drivers in the kernel are free!

/proc/cpuinfo
-------------

`Processor  : ARMv7 Processor rev 3 (v7l)`
`BogoMIPS   : 499.92`
`Features   : swp half thumb fastmult vfp edsp neon vfpv3 `
`CPU implementer    : 0x41`
`CPU architecture: 7`
`CPU variant    : 0x1`
`CPU part   : 0xc08`
`CPU revision   : 3`
`Hardware   : Nokia RX-51 board`
`Revision   : 2101`
`Serial     : 0000000000000000`

GSM
===

phonet0 is the control interface for the modem

`phonet0   Link encap:UNSPEC  HWaddr 15-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  `
`          UP POINTOPOINT RUNNING NOARP  MTU:4000  Metric:1`
`          RX packets:60703 errors:0 dropped:0 overruns:0 frame:0`
`          TX packets:11579 errors:0 dropped:0 overruns:0 carrier:0`
`          collisions:0 txqueuelen:100 `
`          RX bytes:9155288 (8.7 MiB)  TX bytes:631392 (616.5 KiB)`

gprs0 is the data interface for the modem (ignore the name - it's also for umts)

`gprs0     Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  `
`          inet addr:XXX.XXX.XXX.XXX  P-t-P:XXX.XXX.XXX.XXX  Mask:255.255.255.255`
`          UP POINTOPOINT RUNNING NOARP  MTU:1400  Metric:1`
`          RX packets:310 errors:0 dropped:0 overruns:0 frame:0`
`          TX packets:313 errors:0 dropped:0 overruns:0 carrier:0`
`          collisions:0 txqueuelen:10 `
`          RX bytes:98693 (96.3 KiB)  TX bytes:29560 (28.8 KiB)`

-   SIM access, Network Registration, Initiating calls work, 3G works
-   Here are the [Phonet Implementation](/Phonet_Implementation "wikilink") details

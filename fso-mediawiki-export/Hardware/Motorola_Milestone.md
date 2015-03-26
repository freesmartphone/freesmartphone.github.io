---
title: Hardware Motorola Milestone
permalink: /Hardware/Motorola_Milestone/
---

General
=======

Original OSs
------------

Android 2.0

Product Pages
-------------

-   on motorola.com: [1](http://www.motorola.com/Consumers/XW-EN/Consumer-Products-and-Services/Mobile-Phones/Motorola-MILESTONE-XW-EN)

Sources
-------

-   milestone's opensource page: <https://opensource.motorola.com/sf/sfmain/do/viewProject/projects.milestone>
-   git tree: <git://android.git.kernel.org/kernel/omap.git> branch android-omap-2.6.29-eclair

Useful links
------------

-   Special Keys while Booting: <http://wiki.droid-devs.com/index.php?title=Software:Firmware>

Connect to the bootloader using EZXFlash
----------------------------------------

-   download ezxflash:

`wget `[`http://inhex.net/dion/ezxflash.tar.bz2`](http://inhex.net/dion/ezxflash.tar.bz2)

-   unpack and change into dir:

`tar -xf ezxflash.tar.bz2 && cd ezxflash`

-   patch the source to detect milestone or droid:

` patch -p 1`

and copy this into the terminal:

    --- ezxflash.orig/p2kmoto/src/p2kmoto.c 2010-02-15 22:15:47.800850045 +0100
    +++ ezxflash/p2kmoto/src/p2kmoto.c  2010-02-15 22:17:38.450862618 +0100
    @@ -1529,7 +1529,7 @@
            {
                int tmp=dev->descriptor.idProduct%16;
     //             printf("%d %d\n",tmp,tmp%16);
    -           if (dev->descriptor.idVendor==0x22b8 && (tmp==3 || tmp==8))
    +           if (dev->descriptor.idVendor==0x22b8 && (tmp==3 || tmp==8 || dev->descriptor.idProduct==0x41e0 || dev->descriptor.idProduct==0x41d0)) //for droid and milestone
                {
                    //Searching for interfaces with 2 bulk endpoints
                    if (dev->descriptor.bNumConfigurations==1 && dev->config)

press Ctrl+d to finish

-   build p2moko library (needs libusb-dev and libqt4-dev):

`cd p2kmoto && ./configure --prefix=/usr && make && sudo make install && cd ..`

-   build ezxflash:

`cd ezxflash && qmake && make`

-   start ezxflash as root
-   start your milestone into bootloader mode (press dpad up while powering up)
-   connect you stone to your PC using USB and you should see:

`Device is opened and ready`

-   play a little bit, but **remember _you are in the bootloader_ your mouse shouldn't even cross the bottom right corner with the flash box, until you know what you are doing. I'm not responsible, if you brick your device.**
-   Incomplete command overview:

<http://wiki.droid-devs.com/index.php?title=Connect_to_Droid_Bootloader>

-   usage page on moto4lin

<http://moto4lin.sourceforge.net/wiki/FlashingEZX>

Hardware
========

General
-------

-   CPU: ARMv7 Processor rev 3 (v7l) @ 550MHz
-   RAM: 256MB
-   Flash: Toshiba NAND 512MiB
-   SD-card: 8 GB microSD included; supports up to 32 GB microSD expandable
-   Form factor: slider
-   Dedicated Keys: Volume up/down, Camera, Power/Lock
-   Touch Keys: Back, Home, Back, Home, Menu

Modem
-----

-   Type: Qualcomm QSC 6085
-   Features: GSM 850/900/1800/1900, HSPA, GPRS Class 12
-   Kernel support: unknown
-   FSO support: no
-   Serial port: /dev/ttyGS0 /dev/acm0

Wifi
----

-   Type: Texas Instruments WiLink™ 6.0 Wi-Fi
-   Features: 802.11 b/g
-   Kernel support: yes

Sensors
-------

-   Accelerometer
    -   Type: STMicroelecronics LIS331DLH
    -   Features
    -   Kernel support: yes
    -   device node: /dev/lis331dlh
    -   URL: <http://www.st.com/stonline/products/literature/ds/15094.htm>

<!-- -->

-   Ambient light sensor
    -   Type
    -   Features
    -   Kernel support: unknown

<!-- -->

-   Proximity sensor
    -   Type: Osram SFH 7743
    -   URL: <http://catalog.osram-os.com/catalogue/catalogue.do?act=showBookmark&favOid=0000000600015dea00a8003a>
    -   Kernel support: yes

GPS
---

-   Type: integrated in the modem
-   Features
-   Kernel support: unknown

Bluetooth
---------

-   Type
-   Features
-   Kernel support: unknown

Camera
------

-   Type: omap34xx cam / mt9p012 / hplens
-   Features: 5MP
-   Kernel support: in motorola's kernel
-   device node: /dev/hp3a-omap /dev/video0

Useful Logs
===========

-   dmesg

<!-- -->

    [    0.000000] Initializing cgroup subsys cpu
    [    0.000000] Linux version 2.6.29-omap1 (a21146@ca25rhe53) (gcc version 4.4.0 (GCC) ) #1 PREEMPT Thu Nov 5 17:24:53 PST 2009
    [    0.000000] CPU: ARMv7 Processor [411fc083] revision 3 (ARMv7), cr=10c5387f
    [    0.000000] CPU: VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
    [    0.000000] Machine: mapphone_
    ...
    [    0.000000] Kernel command line: console=/dev/null console=ttyMTD10 rw mem=244M@0x80C00000 init=/init ip=off brdrev=P2A androidboot.bootloader=0x0000 mtdparts=omap2-nand.0:1536k@2176k(pds),384k@4480k(cid),384k@7424k(misc),3584k(boot)ro,4608k@15232k(recovery),8960k(cdrom),179840k@29184k(system),106m@209408k(cache),201856k(userdata),1536k(cust),2m@521728k(kpanic)
    [    0.000000] Unknown boot option `androidboot.bootloader=0x0000': ignoring
    ...
    [    0.000000] GPIO mapping write: pin = 28, name = akm8973_reset
    [    0.000000] GPIO mapping write: pin = 92, name = als_int
    [    0.000000] GPIO mapping write: pin = 175, name = akm8973_int
    [    0.000000] GPIO mapping write: pin = 179, name = bt_reset_b
    [    0.000000] GPIO mapping write: pin = 8, name = bt_wake_b
    [    0.000000] GPIO mapping write: pin = 178, name = bt_host_wake_b
    [    0.000000] GPIO mapping write: pin = 186, name = wlan_reset
    [    0.000000] GPIO mapping write: pin = 100, name = silence_data
    [    0.000000] GPIO mapping write: pin = 181, name = vib_control_en
    [    0.000000] GPIO mapping write: pin = 176, name = power_off
    [    0.000000] GPIO mapping write: pin = 99, name = touch_panel_int
    [    0.000000] GPIO mapping write: pin = 42, name = fm_enable
    [    0.000000] DT overwrite GPIO Mapping done!
    ...
    [    7.027191] Invalid Console Name
    [    7.027221] Invalid console paramter. UART Library Init Failed!
    [    7.027221] !!!!!!!! Unable to recongnize Console UART........
    [    7.027252] omap-uart.1: ttyS0 at MMIO 0x4806a000 (irq = 72) is a OMAP UART1
    [    7.027648] Invalid Console Name
    [    7.027679] Invalid console paramter. UART Library Init Failed!
    [    7.027679] !!!!!!!! Unable to recongnize Console UART........
    [    7.027709] omap-uart.2: ttyS1 at MMIO 0x4806c000 (irq = 73) is a OMAP UART2
    [    7.028045] Invalid Console Name
    [    7.028045] Invalid console paramter. UART Library Init Failed!
    [    7.028076] !!!!!!!! Unable to recongnize Console UART........
    [    7.028076] omap-uart.3: ttyS2 at MMIO 0x49020000 (irq = 74) is a OMAP UART3
    ...
    [    7.291412] input: compass as /devices/virtual/input/input0
    [    7.292327] LIS331DLH accelerometer driver
    [    7.294647] input: accelerometer as /devices/virtual/input/input1
    [    7.295135] lis331dlh 2-0019: lis331dlh probed
    [    7.300323] ts27010 mux registered
    [    7.300933] Loaded SysPanic device driver
    [    7.358367] Android kernel panic handler initialized (bind=kpanic)
    [    7.359039] input: cpcap-key as /devices/virtual/input/input2
    [    7.359039] cpcap_key cpcap_key: CPCAP key device probed
    [    7.359710] regulator_check_voltage: operation not allowed for vusb
    [    7.360076] cpcap_usb_det cpcap_usb_det: CPCAP USB detection device probed
    [    7.373382] regulator_check_voltage: operation not allowed for vaudio
    [    7.373931] cpcap spi1.0: Headset key event: old=0, new=0
    [    7.373962] cpcap spi1.0: New headset state: 0
    ...
    [    7.429138] Creating 11 MTD partitions on "omap2-nand.0":
    [    7.429168] 0x000000220000-0x0000003a0000 : "pds"
    [    7.431518] 0x000000460000-0x0000004c0000 : "cid"
    [    7.432830] 0x000000740000-0x0000007a0000 : "misc"
    [    7.434112] 0x0000007a0000-0x000000b20000 : "boot"
    [    7.436401] 0x000000ee0000-0x000001360000 : "recovery"
    [    7.438751] 0x000001360000-0x000001c20000 : "cdrom"
    [    7.442108] 0x000001c80000-0x00000cc20000 : "system"
    [    7.486358] cpcap spi1.0: notify_accy: accy=0
    [    7.489135] 0x00000cc80000-0x000013680000 : "cache"
    [    7.517028] 0x000013680000-0x00001fba0000 : "userdata"
    [    7.567077] 0x00001fba0000-0x00001fd20000 : "cust"
    [    7.568756] 0x00001fd80000-0x00001ff80000 : "kpanic"
    ...
    [   12.610595] init: service 'console' requires console
    [   12.615997] init: cannot find '/system/bin/telnetd', disabling 'telnet'
    [   12.620178] init: cannot find '/system/bin/catcommands', disabling 'catcommands'
    [   12.636718] warning: `adbd' uses 32-bit capabilities (legacy support in use)
    [   12.646881] adb_open
    [   12.648284] init: cannot find '/system/bin/playmp3', disabling 'bootsound'
    [   12.687164] init: cannot find '/system/etc/install-recovery.sh', disabling 'flash_recovery'
    [   12.704040] cpcap spi1.0: CPCAP uC: open status:0
    [   13.170532] rmnet0 (): not using net_device_ops yet
    [   13.246246] cpcap spi1.0: CPCAP uC: open status:0
    [   13.275634] rmnet0: Disabled Privacy Extensions
    [   13.276184] psd_data6 (): not using net_device_ops yet
    [   13.297637] psd_data6: Disabled Privacy Extensions
    [   13.298095] psd_data7 (): not using net_device_ops yet
    [   13.355407] psd_data7: Disabled Privacy Extensions
    [   13.355895] psd_data8 (): not using net_device_ops yet
    [   13.415039] psd_data8: Disabled Privacy Extensions
    [   13.415405] psd_data9 (): not using net_device_ops yet
    [   13.453155] psd_data9: Disabled Privacy Extensions
    [   13.453552] psd_data10 (): not using net_device_ops yet
    [   13.466827] psd_data10: Disabled Privacy Extensions
    [   13.467193] muxtest_net (): not using net_device_ops yet
    [   13.510437] muxtest_net: Disabled Privacy Extensions

[Category:Hardware](/Category:Hardware "wikilink")
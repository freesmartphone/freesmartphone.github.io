---
title: Palm Pre Challenge: Sep - Dec 2009
permalink: /Palm_Pre_Challenge:_Sep_-_Dec_2009/
---

|-------------|
| __TOC__ |

This page may be of historical interest; for current activity, see [Palm Pre: Jan 2010 - ?](/Palm_Pre:_Jan_2010_-_? "wikilink")

**What:** Working voice call with FSO on the Palm Pre within one month.

**When:** As soon as the Palm Pre GSM is available in Germany. (**2009-10-13**)

**Who:** Daniel, Jan, Mickey, Simon, Harald (for kernel bits), Hunz and Stefan. Who else?

Timetable
---------

**2009-09-17** First draft for Challenge.

**2009-09-24** Palm an O2 announced the 2009-10-13 as Palm Pre launch date in Germany. That means our challenge has a start date now.

**2009-09-25** Kick off some OE work for kernel and rootfs images.

**2009-10-12** Some of us got their Pres. Hacking starts now.

**2009-10-13** LVM resize script is ready. See below. Research pages moved to the research area of the webos-internals.org wiki <http://www.webos-internals.org/wiki/Portal:Research>

**2009-10-15** Running the Palm system with a selfcompiled kernel is possible without any problems

**2009-10-19** The baseband firmware provides a binary protocol (default on the call channel) and an AT protocol (default on the data channel). ogsmd can talk AT w/ the data channel protocol; which is a pretty complete and almost standard 07.07 implementation, however no VOICE call indicators arrive there.

**2009-12-01** Booting own rootfs with ssh

Tasks
-----

<table>
<colgroup>
<col width="5%" />
<col width="5%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><div style="margin: 0; margin-right:10px; margin-top:10px; border: 1px solid #dfdfdf; padding: 0em 1em 1em 1em; background-color:#ffffff; align:left;">
<h3 id="oe">OE</h3>
<p>Machine support in OE. That includes a working machine file, a kernel recipe and the whole way up to a basic tar.gz rootfs. We will use the beagleboard machine as example and adjust as needed. The kernel we will build is the 2.6.24 plus Palms patch that is already used on the device. [Stefan]</p>
<h3 id="lvm">LVM</h3>
<p>Adjust the eMMC LVM layout to allow a second rootfs patition. Ext3 bootloader partition stays as is, but the media partition gets shrinked about 100 - 200MB to make space for the new LVM volume we will use. Our rootfs partition should use a standard linux filesystem like ext3. [Jan]</p>
<h3 id="audio">Audio</h3>
<p>Understand the audio routing the system uses for GSM voice calls. Maybe just dump the alsa states in the original Palm Pre system. We only need the minimal setup for voice routed to the GSM modem and back. Optional switch betwenn speaker ringtone and handset mode.</p>
<h3 id="httpwww.webos-internals.orgwikiresearch_pre_gsm_modem-gsm"><a href="/http://www.webos-internals.org/wiki/Research_Pre_GSM_Modem_GSM" title="wikilink"><a href="http://www.webos-internals.org/wiki/Research_Pre_GSM_Modem" class="uri">http://www.webos-internals.org/wiki/Research_Pre_GSM_Modem</a> GSM</a></h3>
<p>Understand how the modem has to be driven from ogsmd. That includes finding the device nodes and research about AT comands etc. Everything until we can do a successful ATD with the modem. We already have msm7k support in ogsmd from HTC devices. More important is how the modem has to be driven. [Mickey, Simon]</p></td>
<td align="left"><div style="margin: 0; margin-right:10px; margin-top:10px; border: 1px solid #dfdfdf; padding: 0em 1em 1em 1em; background-color:#ffffff; align:left;">
<h3 id="fso">FSO</h3>
<p>Get fsodeviced and fsousaged running up to the state where the voice call is possible. The work here may be in some parts of fsodeviced. Hopefully most cases are already covered with our kernel26 plugin.</p>
<h3 id="gps">GPS</h3>
<p>Find the GPS device and evaluate how we need to drive it and what data we get from it. strace the Palm system should help us here to find the device nodes. If it is plain NMEA a ogpsd integration should be easy. (Optional) [Daniel]</p>
<h3 id="ui">UI</h3>
<p>Booting into an SHR image and use the UI dialer for the actual call. This may needs fixes in the UI for the different screen size of the Pre. We also need to investigate if XFBdev runs without problems on the framebuffer as Palms UI uses directfb. (Optional) [Simon]</p>
<h3 id="kboot">Kboot</h3>
<p>Use kexec infrastructure in OE to build a 1stage kernel that boots into a small intramfs which plays the role of a bootloader for us to decide in which system we want to boot. Decision is made by a hold key or optional by a shiny UI. (Optional)</p></td>
</tr>
</tbody>
</table>

Time Budget and Status
----------------------

Some of the tasks can be done in parallel but still we list them in the budget in a serial form.

| Task     | Time Budget  | Status | Comment                                                       |
|----------|--------------|--------|---------------------------------------------------------------|
| OE       | 2 days       | 90%    | OE build kernel can boot up the normal system                 |
| LVM      | 1 day        | 100%   | Done, the script below gives us space for our own rootfs.     |
| Plumbing | 2 days       | 0%     | Not yet started.                                              |
| Audio    | 3 days       | 20%    | audiod with some special scripts for telephony                |
| GSM      | 4 days       | 20%    | Modem ports found, HDLC based protocol, some packets known.   |
| FSO      | 3 days       | 0%     | Not yet started.                                              |
| Plumbing | 2 days       | 0%     | Not yet started.                                              |
| (GPS)    | 2 days       | 0%     | Not yet started.                                              |
| (UI)     | 3 days       | 0%     | Not yet started.                                              |
| (Kboot)  | 3 days       | 20%    | Own rootfs is booting. Working now on a graphical bootloader. |
| Total    | 17 (25) days | 0%     | Not yet started.                                              |
||

Meeting
-------

### Attendees

-   Simon Busch (morphis)
-   Stefan Schmidt
-   Michael Lauer
-   Jan Lübbe

### Date

Just enter a new date or put your name behind one.

-   01.11: Simon Busch, Stefan Schmidt, Michael Lauer, Jan Lübbe

### Location

-   Braunschweig

LVM Resize Script
-----------------

This gives us 200MB room for our FSO rootfs:

    root@castle:/var/home/root# cat pre-resize.sh
    #!/bin/sh
    # Modified version of http://kitenet.net/~joey/blog/entry/palm_pre/, thanks Joey
    cp -a /media/internal /opt
    umount /media/internal
    lvresize -L 6.5G /dev/mapper/store-media
    mkdosfs -F 32 /dev/mapper/store-media
    mount /media/internal
    mv /opt/internal/* /opt/internal/.* /media/internal
    rmdir /opt/internal
    lvcreate -l 100%FREE -n fso store
    mkfs.ext3 /dev/store/fso
    mkdir /media/fso
    echo "/dev/mapper/store-fso /media/fso auto noatime 0 0" >> /etc/fstab
    mount /media/fso

Eventually the whole root filesystem is mounted read-only, then simply remount it with

    mount -o remount,rw /

[Category:Palm Pre](/Category:Palm_Pre "wikilink")
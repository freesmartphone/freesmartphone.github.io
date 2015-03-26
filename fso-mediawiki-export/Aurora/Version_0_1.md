---
title: Aurora Version 0 1
permalink: /Aurora/Version_0_1/
---

General
-------

Release Date: 01-08-2011

Selected Users-Stories
----------------------

**Basic Telephony**

-   I want to be able to call someone by typing in his phone number
-   I want to be alerted for an incoming phone call
-   I want to reject an incoming call
-   I want to accept an incoming call

**System**

-   ~~I want the device to show a lock screen when it was idle for a decent part of time~~ (scheduled for a later version cause of missing time)

Tasks
-----

See the [tasks page](/Aurora/Version_0_1/Tasks "wikilink") for this version.

Supported devices
-----------------

-   Palm Pre/Pre Plus/Pre 2

Installation
------------

### Needed things

-   a computer with linux installed
-   an active internet connection
-   your device
-   the webos doctor corresponding to your device (see [WebOS Internals' wiki](http://www.webos-internals.org/wiki/Webos_Doctor_Versions))
-   novacom, [and just novacom!](https://developer.palm.com/content/resources/develop/sdk_pdk_download.html#linux)(at the bottom of the page)

The following three steps are the basic steps you need to use the fso-installer.

1. Create a "downloads" directory and put in there the webos version you have downloaded, something like webosxxxxx.jar .

2. In our working directory (not in "downloads/" !), download the fso-installer :

`wget '`[`http://git.freesmartphone.org/?p=utilities.git;a=blob_plain;f=palmpre/fso-installer/Makefile;hb=HEAD`](http://git.freesmartphone.org/?p=utilities.git;a=blob_plain;f=palmpre/fso-installer/Makefile;hb=HEAD)`' -O Makefile`

3. You have then to modify only two things in the Makefile : TARGET and CONFIG_WEBOS_MEDIA_TARGET_SIZE as explained at the top of the Makefile

Note: You will need a kernel and an image to flash, you can find them here: <http://amethyst.openembedded.net/~morphis/aurora-development/images/> (pick the one for the palmpre or palmpre2 device). You have to put both kernel and image file into your downloads directory.

### Reboot your device into 'flash' mode

Power your device off, hold the volume up key and plug a usb cable in (the other end should be in your computer). Wait until the usb logo is on the screen, then run the following command:

`make memload`

### Backup up everything

Before we execute any of the steps below we will backup every data from your device to be able to restore it later. You do that with entering the command while the device is connected:

`make backup`

### Resize internal flash disk of your device

To flash a Aurora image to your device we first need to get some free space for it. As of the initial state with webOS installed there is all space required by webOS. Some parts are used for the webOS system and the biggest part ist used for the media partition. This one we need to resize in the following steps to get some free space for Aurora.

First you have to decided how many space you want for the webOS media partition left. You specify this in the Makefile with adjusting the CONFIG_WEBOS_MEDIA_TARGET_SIZE variable.

As next step we start the resize process by entering the command. It will resize the internal lvm partitions and create a new one for Aurora which will be used for flashing later.

`make lvm-resize`

### Restore your data

After having resized your internal flash disk you should want to restore your data back to your device's data partition:

`make restore-media`

### Intall the bootloader

To be able to boot the system and to switch between webOS and Aurora on boot you need to install the bootloader called bootr with

`make install-bootr`

### Flash the kernel

Flashing a kernel is very simple. You just need to download or build a kernel for the device and flash it with the following command to the device:

`make KERNEL=downloads/uImage-palmpre.bin flash-kernel`

NOTE: For the Pre2 the kernel file is named: uImage-palmpre2.bin!

### Flash the image

Flashing the image to the device is as simple as flashing the kernel to the device.

`make IMAGE=downloads/aurora-fb-image.tar.gz flash-image`

### Finished!

You got it. You have now flashed aurora to your pre device. Next step is rebooting the device and starting aurora the first time. To do so use this command:

`make reboot`
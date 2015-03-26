---
title: Palm Pre: Install FSO
permalink: /Palm_Pre:_Install_FSO/
---

This page is deprecated. Follow this guide instead <http://trac.shr-project.org/trac/wiki/PalmPreInstall>

WARNING: Before you do any of the steps below just backup all our data from the device! The Freesmartphone team provides this as is without warranty of any kind, either expressed or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of this program is with you. Should this program prove defective, you assume the cost of all necessary servicing, repair or correction. In no event will the Freesmartphone team or any other party be liable to you for damages, including any general, special, incidental or consequential damages arising out of the use or inability to use this program (including but not limited to loss of data or data being rendered inaccurate or losses sustained by you or third parties or a failure of this program to operate with any other programs).

First you have to setup Open Embedded and build the fso2-preview-image (take a look at the openembedded wiki [1](http://wiki.openembedded.net/index.php/Getting_started) about how to setup a openembedde environment).

NOTE: If something in the process described below failed you have the option to reinstall webOS through the webOS doctor on your device and restart installing FSO afterwards.

### 1. Build the FSO image

NOTE: You don't have to compile your own image, but if you want to develop on the FSO framework for the Palm Pre it is the best way.

We assume that everything will be installed in /home/john/oe

`cd /home/john/oe`
`git clone `[`http://git.openembedded.org/cgit.cgi/bitbake/`](http://git.openembedded.org/cgit.cgi/bitbake/)
`mkdir -p palmpre/conf sources`
`git clone `[`git://git.freesmartphone.org/openembedded.git`](git://git.freesmartphone.org/openembedded.git)` openembedded-fso`

Create a new file **openembedded-fso/conf/site.conf** with this content (you can have a look at openembedded-fso/conf/local.conf.sample file if you want some explanations about options, you will need certainly to adjust options PARALLEL_MAKE and BB_NUMBER_THREADS according to your processor):

`BBFILES = "/home/john/oe/openembedded-fso/recipes/*/*.bb"`
`DL_DIR = "/home/john/oe/sources"`
`PARALLEL_MAKE = "-j3"`
`BBINCLUDELOGS = "yes"`
`BB_NUMBER_THREADS = "3"`
`ENABLE_BINARY_LOCALE_GENERATION = "0"`
`ASSUME_PROVIDED += "gcc3-native"`
`INHERIT += "devshell"`
`OE_ALLOW_INSECURE_DOWNLOADS = 1`
`OE_STRICT_CHECKSUMS = ""`
`IMAGE_KEEPROOTFS = 1`
`IMAGE_FSTYPES = "ext3 jffs2 tar.gz"`

Create a new file **palmpre/setup-env** with this content:

`#!/bin/sh`
`BASEDIR=/home/john/oe`
`export OEDIR="${BASEDIR}/openembedded-fso"`
`export BBPATH=${BASEDIR}/palmpre:${OEDIR}`
`export PYTHONPATH="${BASEDIR}/bitbake/lib"`
`export PATH=${BASEDIR}/bitbake/bin:$PATH`

Create a new file **palmpre/conf/local.conf** with this content:

`MACHINE = "palmpre"`
`DISTRO = "minimal"`
`require conf/distro/include/fso-autorev.inc`

Start compilation of image:

`source palmpre/setup-env`
`cd openembedded-fso`
`bitbake fso2-demo-image && bitbake linux-palmpre`

After that you have an image prepared for you Palm Pre + a modified kernel (patches from Palm + some little modifications). The next steps will install the fso2-demo-image beside webOS. Just note that maybe every webOS update will break your device (you just have to reinstall webOS through the webOS doctor).

### 2. Create a new lvm partition for FSO

To install the FSO image on your Pre we have to create some space on the internal flash. Please take care that you backup all the data you have on the internal flash (even the hidden directories, which holds informations about the installed applications etc.). Everything will be lost this step!

First, you must install novacomd and novaterm utilities on your local PC to access Palm Pre Linux. You can find a complete procedure [here](http://www.webos-internals.org/wiki/Accessing_Linux_Using_Novaterm).

    local# novaterm
    pre# cd /
    pre# mount / -o remount,rw
    pre# mv /sbin/init /sbin/init.old
    pre# ln -s /etc/miniboot.sh /sbin/init
    pre# tellbootie

Now the device reboots and you can login again with novaterm. Now we create the lvm partition for FSO.

    local# novaterm
    pre# cd /
    pre# cp -a /media/internal /opt (backup everything, but be carefull /opt is very small! just backup essential application data)
    pre# umount /media/internal
    pre# lvresize -L 6.5G /dev/mapper/store-media
    pre# mkdosfs -F 32 /dev/mapper/store-media
    pre# mount /media/internal
    pre# mv /opt/internal/* /opt/internal/.* /media/internal
    pre# rmdir /opt/internal
    pre# lvcreate -l 100%FREE -n fso store
    pre# mkfs.ext3 /dev/store/fso
    pre# mkdir /media/fso
    pre# echo "/dev/mapper/store-fso /media/fso auto noatime 0 0" >> /etc/fstab
    pre# mount /media/fso

### 3. Download and install the FSO demo image

Now you should download the FSO image and our modified kernel. Copy both on the device and put them into /media/internal. You will find the image and kernel here [2](http://amethyst.openembedded.net/~morphis/oe/palmpre/deploy/images/palmpre/) (download the fso2-demo-image-palmpre.ext3 image and the uImage-palmpre.bin kernel).

I assume for the next step that the image and kernel will be in the directory /media/internal.

    pre# umount /media/fso
    pre# dd if=/media/internal/fso2-demo-image-palmpre.ext3 of=/dev/mapper/store-fso
    pre# resize2fs /dev/mapper/store-fso
    pre# mount /media/fso (take a look into it, if everything is there)

As next step we have to copy the kernel on the boot partition and make it the default one

    pre# mount -o remount,rw /boot
    pre# cp /media/internal/uImage-palmpre.bin /boot
    pre# rm /boot/uImage (removes the symbolic link to the default kernel)
    pre# ln -s /boot/uImage-palmpre.bin /boot/uImage

### 4. Prepare for booting

In the next step we have to change the boot setup from webOS. This step you have to do everytime you want boot FSO instead of webOS and vice versa.

    pre# mount /boot -o remount,rw
    pre# cp /boot/sbin/init /boot/sbin/init.fso
    pre# vi /boot/sbin/init.fso

Now search the line with

    lvm.static lvchange -ay --ignorelockingfailure /dev/mapper/store-root

and comment it like

    #lvm.static lvchange -ay --ignorelockingfailure /dev/mapper/store-root

After this line you add the following line

    lvm.static lvchange -ay --ignorelockingfailure /dev/mapper/store-fso

This will open the FSO lvm partition on startup instead of the webOS one. Right after this line there is another one you have to comment

    mount -o ro /dev/mapper/store-root /realroot

After this line you add the following one

    mount -o rw /dev/mapper/store-fso /realroot

To shutdown your device type:

    pre# shutdown -h now

To boot your device press volume up button and connect the usbcable. Use novaterm to talk to the bootloader and type the following commands:


    setenv bootfile uImage-palmpre.bin
    setenv bootargs "root=/dev/mmcblk0p2 rootwait ro init=/sbin/init.fso"
    printenv
    fsboot

and your device will start immediately.

### 5. Network setup and ssh

On the next start of the device, the FSO demo image will boot and you should configure the usb0 network interface on your local PC with

    local# ifconfig usb0 192.168.0.1

You now find the Pre device on 192.168.0.202 and can login via ssh (user = root, no password):

    local# ssh root@192.168.0.202

### 6. Next steps

Currently nothing is ready for daily use. We working on mostly everything. See the other Wiki pages or ask people on IRC/ML about current status and where do you can help to improve FSO on the Palm Pre.
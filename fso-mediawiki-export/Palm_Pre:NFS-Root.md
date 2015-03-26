---
title: Palm Pre:NFS-Root
permalink: /Palm_Pre:NFS-Root/
---

This page describes shortly how to run an own uImage with custom rootfs without any changes on your Palm Pre's flash. If you are interested in installing a custom linux to Pre's flash follow the instructions on [this](/Palm_Pre:_Install_FSO "wikilink") page.

1. Build an Image
-----------------

We assume that you have already build or downloaded a rootfs and uImage. You can build an Image following the instructions on [Palm_Pre:_Install_FSO\#1._Build_the_FSO_image](/Palm_Pre:_Install_FSO#1._Build_the_FSO_image "wikilink")

2. Boot from NFS without Changing anything on your Pre
------------------------------------------------------

### 2.1. preparations

Our preparations are based on three steps:

-   install **NFS and novaterm** on your host
-   extract and **export the rootfs**
-   **set up networking** on the host system

#### 2.1.1. NFS and novaterm

You can get novaterm from [1](http://developer.palm.com/). To install NFS on Debian-like systems it only takes the following command as *root*

`apt-get install nfs-kernel-server`

now extract the image you have build to some folder *e.g. to /foo/bar*

`cd /foo/bar
 tar xfz yourImage.tar.gz .`

This is your root-directory into which the Pre will boot and we need to tell our NFS-server to export this directory. With your favorite text editor edit `/etc/exports` and add the line

`/foo/bar 192.168.0.0/24(rw,fsid=0,insecure,no_subtree_check,async,no_root_squash)`

btw this assumes that you will use 192.168.0.0 network range with the *server-ip* 192.168.0.200 and *192.168.0.202* as your *Pre-ip*

Now you need to restart the NFS service to apply the changes.

#### 2.1.2 set up networking

On your host (if it is using hotplug) put the following lines to */etc/network/interfaces*'

` allow-hotplug usb0
        iface usb0 inet static
        address 192.168.0.200
        netmask 255.255.255.0 `

### 2.2. boot from NFS

*' a) connect the Pre via USB to your local machine. Go into recover mode*'

either by powering on the Pre and holding the *volume-up key* or via novaterm

`tellbootie recover`

''' b) change bootargs '''

Now you are in the recover mode and should see a large USB logo on Pre's screen. Via novaterm you can now talk to *bootie* the Pre bootloader

`novaterm`

press *enter* and you see booties prompt **]** here type

`setenv bootargs "root=/dev/nfs nfsroot=192.168.0.200:/foo/bar,v3 ip=192.168.0.202:192.168.0.200:192.168.0.200:255.255.255.0::usb0:"`

These *bootargs* tell the Kernel to boot from nfs and set the ip address of your pre's *usb0* interface.

''' c) boot your Kernel '''

tell bootie to boot your kernel

` novaterm boot mem:// < uImage.bin `

This should boot into your image with your kernel.

Have fun testing and developing.
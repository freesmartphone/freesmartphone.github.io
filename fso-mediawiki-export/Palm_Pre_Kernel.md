---
title: Palm Pre Kernel
permalink: /Palm_Pre_Kernel/
---

[Category:Palm Pre](/Category:Palm_Pre "wikilink")

Palm Pre Kernel
===============

We have different branches for the Palm Pre devices. The following will focus on the kernel versions you get from the different branches.

palmpre/master
--------------

Current version used by OE to compile a kernel for the palm pre device. It mostly the kernel you get when installing webOS on the device with some additional features:

-   Based on the webOS 2.0 submission-48 patchset (http://opensource.palm.com/2.0.0/index.html)
-   Enable framebuffer console
-   WiFi Activator module (is needed to activate the WiFi chip inside the device)
-   SDIO patches for libertas_sdio
-   USB gadget provides as default usbnet and novacom functions

Supported devices: Palm Pre / Pre Plus / Pre 2

palmpre/webos20-devtmpfs
------------------------

Kernel based on the same patch as the palmpre/master with mostly the same features but many additional patches to get a working devtmpfs. This kernel version is quite unstable as it crashes X11 and has some stability issues with power management.

Supported devices: Palm Pre / Pre Plus / Pre 2

palmpre/webos14-devtmpfs
------------------------

Based on the webOS 1.4.5 kernel patch with the same devtmpfs patches as palmpre/webos20-devtmpfs.

Supported devices: Palm Pre / Pre Plus
---
title: Tutorials development env
permalink: /Tutorials/development_env/
---

Getting FSO Image
-----------------

First you need to get and flash the FSO image. The images can be found [there](http://downloads.freesmartphone.org/fso-stable/). To flash it on the neo, refer to [this page](http://wiki.openmoko.org/wiki/Flashing_openmoko)

Once the image has been flashed you can reboot your neo and already play with the installed framework and zhone.

Getting the last framework and zhone sources
--------------------------------------------

In my example I will put all the sources on my host computer, under /home/charlie/freesmartphone/ The git repositories are [there](http://git.freesmartphone.org/).

To get the last version :

`cd /home/charlie/freesmartphone`
`git clone `[`git://git.freesmartphone.org/framework.git`](git://git.freesmartphone.org/framework.git)
`git clone `[`git://git.freesmartphone.org/zhone.git`](git://git.freesmartphone.org/zhone.git)

Note : there are many other projects in the repository, but we don't need them here.

To update the code you can just type:

`git pull`

Accessing the host file from neo using nfs
------------------------------------------

This is probably the easiest way to try the framework without having to copy the files every times you make changes.

Still assuming everything has been put into /home/charlie/freesmartphone/ (in the host)

-   First, allow the directory to be accessed by nfs. At least on ubuntu it is possible to do it just by right clicking on the directory -\> share folder,

then choosing nfs, and allowing ip 192.168.0.202 (The neo ip)

-   Then ssh into the neo, and edit your /etc/fstab. In this example I will add the following line :

`192.168.0.200:/home/charlie/freesmartphone /home/root/freesmartphone nfs noauto,nolock,soft,rsize=32768,wsize=32768 0 0`

-   If you don't have nfs set up already, you may need to run

`/etc/init.d/mountnfs.sh retart`

-   Finally you can mount the directory

`mount /home/root/freesmartphone/`

After this steps you should be able to edit the files from your host machine, and run it from your neo.

Running the framework
---------------------

Note : Before running the last verison of the framework make sure to kill any other running version. You may also want to kill gsm0710muxd

from your neo :

`cd /home/root/freesmartphone/framework/`
`` export PYTHONPATH=`pwd`   # this is important because we don't want to use the installed version of the framework ``
`cd framework`
`./framework`

It is possible to start only a single subsystem of the framework by using the -s <system> option, for example :

`./framework -s ogsmd `

Will only start ogsmd subsystem

Running the tests
-----------------

in the directory framework/tests, there are a few test script that can be used to test the framework.

Setting debug logging
---------------------

You can export FRAMEWORK_DEBUG=1 before running the framework daemon to have more debug output

You can also edit the file framework/config.py to turn debug and info log on or off.

More problems ?
---------------

Try to kill the framework daemon AND gsm0710muxd.

If you have other problems, ask for help on this mailing list : smartphones-standards@linuxtogo.org

[Category:Tutorial](/Category:Tutorial "wikilink")
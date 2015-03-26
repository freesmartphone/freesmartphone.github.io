---
title: Implementations GSMD2
permalink: /Implementations/GSMD2/
---

gsmd2
=====

The gsm daemon works as a centralized software application to modem hardware and provides [D-bus](/specifications "wikilink") IPC mechanism to other applications. gsmd2 started as an internal project at [Ixonos Plc](http://www.ixonos.com/en) and is currently developed by Vesa Pikki (spyre in irc.freenode.org) and Heikki Paajanen (hepaajan in irc.freenode.org) from Ixonos.

gsmd2 is alpha level software

GSMD2 is in freesmartphone's GIT repository. You can checkout gsmd2 project with:

`git clone `[`git://git.freesmartphone.org/gsmd2.git`](git://git.freesmartphone.org/gsmd2.git)

Compilation and installation
============================

In order to compile gsmd2 you need following software packages:

-   GNU build tools
-   D-Bus library
-   glib

Additionally self tests using DBUS interface require python (\>= 2.5), dbus python bindings and gobject python bindings. Self tests for libfreesmartphone API wrapper require cython.

To generate configure script:

`./autogen.sh`

To configure run (for example):

`./configure --prefix=/opt/freesmartphone`

Configure automatically searches for all required components and packages.

To compile and install run:

`make && make install`

Refer to INSTALL file for more information.

Running gsmd2
=============

You need supported modem device.

gsmd2 uses DBus system bus so you need to allow that by placing res/freesmartphone.conf to your dbus system configuration directory (e.g. /etc/dbus-1/system.d/) and restart dbus service (e.g. /etc/init.d/dbus restart)

Run "gsmd2 --help" for information about command line options.

Supported modems
================

Telit:

-   862-GPS
-   UC864-E

Openmoko:

-   Neo 1973 (TI calypso based)

Libfreesmartphone
=================

GSMD2 includes a C library to ease implementation. Python library is also planned.

PyUnit test cases and simple Testing UIS for gsmd2
==================================================

These testing scripts are meant to support development of the gsm daemon and related applications. They are currently far from done.

pyUnit test cases (\*_unit.py)
-------------------------------

Running all tests:

`make check`

Followign scripts assume that gsmd2's directory is set to PATH and GSMD2PLUGINDIR points to plugin directory, if "make install" has not been run. Example:

`export PATH=$PATH:~/gsmd2/src`
`export GSMD2PLUGINDIR=~/gsmd2/vendor/.libs/`

Running a single test suite:

`python2.5 `<test case's filename>

Example:

`python2.5 call_unit.py`

Running a single test inside a suite:

`python2.5 `<test case's filename>` `<test class>`.`<test's name>

Example:

`python2.5 call_unit.py CallTests.test_Accept`

DBus user interface (ui.py)
---------------------------

This testing UI sends dbus commands do gsmd2 and therefore assumes that gsmd2 is running. It also prints out all signals (configured to the ui) sent by gsmd2.

Running the testing UI:

`python2.5 ui.py`

Executing commands: Type in the command plus additional parameters. For example:

`"SMS_RetrieveMessage 12"`

Getting a list of available commands:

`help`

Getting information about spesific command

`help `<command>

Quitting the UI

`quit`

Virtual modem with a user interface (modem_ui.py)
--------------------------------------------------

This testing ui starts gsmd2, creates a virtual terminal for it and mimics a modem. It can be used to simulate modem behavior, for example initiating an incoming call.

This script assumes that gsmd2's directory is set to PATH. Example: export PATH=$PATH:~/gsmd2/src

Running the testing UI:

`python2.5 modem_ui.py`

Executing commands: Type in the command plus additional parameters. For example:

`incoming_call 040124468`

Getting a list of available commands:

`help`

Getting information about spesific command

`help `<command>

Quitting the UI:

`quit`

This test script has commands in three categories: general commands, commands that affect/generate data written to gsmd2 and commands that are sent to gsmd2 through dbus.

General commands

-   help - prints help
-   init_defaults - Initializes default values
-   list_operators - Lists all operators that are supposedly available
-   print_at_commands - Should at commands (both read and written) be printed
-   print_signal_strength - Should signal strenght signals and at commands be printed
-   print_signals - Should d-bus signals be printed
-   quit - Quit

Commands that affect/generate data written to gsmd2

-   accept - Remote end accepted the phone call
-   busy - Send busy to gsmd2
-   set_sms - This virtual modem has a list of sms' in it's memory, you can add new and modify old ones with this command
-   creg_reply_set - Set the reply for creq (network registration status query) command
-   dial_reply_set - Set the reply for dial command
-   dial_reply_write - Write a dial reply to gsmd2
-   hangup - Hangup a phonecall
-   incoming_call - Initiate an incoming call to the modem
-   incoming_sms - Initiate an incoming sms message to the modem
-   no_carrier - Send NO CARRIER message to gsmd2
-   set_current_operator - Set the index of current operator in use
-   pin_reply_set - Set the reply for pin query
-   set_operator - Modify specific operator in virtual modem's list
-   set_signal - Set signal strength

Commands that are sent to gsmd2 through dbus

`TODO add them`

Usage example

This example consists of making a simple phone call with the other end being busy for a while, accepts the call and then hangs up:

-   dial_reply_set busy - set that the reply to dials will be busy
-   -   initiate the phonecall from some other user interface or enter command Call_Initiate <number>\*
-   accept - Accept the phonecall (can also be accomplished via dial_reply_write active)
-   hangup - Hangup the phonecall

Listing available operators, modifying existing operator, setting current operator:

-   list_operators - Show a list of all operators available
-   set_operator 1 3 DnaFinland 35810 - Modify Operator number 1. Change it's state forbidden (3), change the name to DnaFinland and change operator code to 35810
-   list_operators - Check that operator was modified correctly
-   set_current_operator 1 - Set DnaFinland our current operator

Creating a new incoming sms message:

-   set_sms 10 044000000 1 example message - Create a new message with index 10, sender's number is 044000000, message is read (1) and contents are "example message"
-   incoming_sms SM 10 - Tell gsmd2 that a new message has arrived, it's index is 10 and it is stored in sim's memory (SM)

Tips
----

-   AT commands can disturb usage, displaying them can be disabled with command "print_at_commands 0"
-   To stop displaying all commands/signal messages related to signal strength "print_signal_strength 0"
-   To stop displaying signals type "signals 0"

[Category:System Developers](/Category:System_Developers "wikilink")
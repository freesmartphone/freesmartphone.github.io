---
title: Aurora Documentation
permalink: /Aurora/Documentation/
---

Overview
========

Aurora's technology is based in Qt's QML,we use also Vala and C++ to do hardware handling part. Our applications are based using aurora's qml components,provided by aurora-components part of aurora framework.At this time,we have the following components:

-   StatusBar
-   NavigationBar
-   Window - Provides a lot of functions,for example.pushPage() and popPage(),that functions are made by PageStack
-   Theme - Adding this in your code you'll be able to use themeing functions like,use default text font sizes,and default colors
-   PageStack - Provides all QML functions necessary by others Aurora components
-   AppPage - You need this each time you start a new application,it's an part from Window component
-   LockScreen - Call this when device is idle,or if you want to create a *magic* application to test your hardware :)
-   Button - A simple and very-configurable button
-   Dialpad - Call this when you need the user type something into the screen if the hardware doesn't have an keyboard
-   Dialog - Opens up a dialog,can be an simple/questionable/yes-no dialog

You can write your own application using the Aurora Framework following tutorials [here](/Aurora/WritingAnApp "wikilink")

Settings
========

**Enable Wifi** - Open Wireless Settings by going to **Menu -\> Settings -\> Wireless** and activate Wifi by enabling **Wireless** checkbox
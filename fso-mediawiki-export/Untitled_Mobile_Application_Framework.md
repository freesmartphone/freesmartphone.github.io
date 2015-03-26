---
title: Untitled Mobile Application Framework
permalink: /Untitled_Mobile_Application_Framework/
---

*For the german version, see [Untitled Mobile Application Framework/de](/Untitled_Mobile_Application_Framework/de "wikilink")*

Introduction
============

-   Do you appreciate consistency?
-   Do you adore integrated systems that feel polished and like being designed with a vision in mind?
-   Do you love standard UI controls being used by most day-to-day-applications on your mobile device?
-   Did you see the iPhone, fell in love with the UI, and wondered why the free software community could not get their act together in producing something slick like that?
-   Do you enjoy concentrating on your application business logic, while all the itchy details are being covered by a strong framework?
-   Are you willing to compromise on the number of mediocre alternatives in order to make one thing really good?

If you said 'yes' for at least two times, then we have good news for you:

1.  The free software community has all the technology necessary to make it happen,
2.  There are people sharing the same views and there's a project starting to realize these goals.

For now we call it the:

Untitled Mobile Application Framework (UMAF)
============================================

UMAF is about developing an integrated system, specifically targetted at the mobile device space, where the user is presented with a rich set of common metaphors and controls. Everything should look and feel as it would have been designed by a single mind with a strong vision. New users should be able to learn how to operate the system with maximum efficiency. New "applications" will fit into the existing set of services and will provide additional features to existing "applications".

Metaphors
---------

### Feature

People are caring about features, not application. They want to **write a letter**, not **open the text editor**.

...

Concrete Goals
--------------

-   A widget set optimized for mobile environments. This will be based on the Enlightenment Foundation Libraries.
-   A services framework for mobile application services.
-   A set of applications using the services framework.

Requirements
------------

### UI

-   the UI should operate with and without touchscreen
-   the UI should support portrait and landscape
-   the UI should support different resolution (QVGA, VGA, etc.)
-   the UI should not use small popups, but fullscreen windows only

Prior Art
---------

-   Classic-style UI-Toolkits such as Qt or Gtk+ are not suitable for mobile environments. They are optimized for complex user interfaces featuring a huge screen real estate and a rich set of buttons, switches, etc. You can try stripping such toolkits down to fit a mobile device (Maemo did that), but the outcome is disputable (many people are not satisfied with the standard Maemo UI, but instead love the simplified Canola and Carman UIs).

<!-- -->

-   Classic-style UI-Toolkits are mostly static toolkits. Adding dynamics such as animations and alphablending is almost impossible. Note that devices like animations and alphablending are not to facilityte eyecandy, but rather to ease users memorizing the application structures and help constructing a mental model of the user interface.

<!-- -->

-   Pure UI-Toolkits do not include application semantics. They are defined in categories such as a TreeView or a ScrollableWindow, but they do not suggest any behaviour to make applications consistent. We rather need widgets such as a "ContactsView", "PhonePad", "ConnectivityChooser", etc.

Development Plans
-----------------

To reach the goal of UMAF, the following steps are planned:

1.  Development of a UI Usability Concept
2.  Define a rough development model
3.  Prototye Design of the UI Elements
4.  Framework Subsystem Design
5.  Development of the base framework with rudimental functions
6.  Development of the base features and auxilliary functions in the framework

### Development of a UI Usability Concept

-   The UI should use the Unicode Charset
-   Use (modified) Illume as the window manager.
-   No small popups! Applications should always use the whole screen (minus the small part of illume).
-   Only show UI elements, which are absolutely neccesary to use the application.
-   Our Usability and Interface Concept will based on the GNOME Human Interface Guidline.

New Wiki-Page: [UMAF Interface Guidelines](/UMAF_Interface_Guidelines "wikilink")

### Define a rough development model

-   Collect and elaborate multiple mockups or concepts at a time and merge the good aspects. Then continue with the thereby achieved state.
-   We will meet once in a week in irc.freenode.net/neo1973-germany on Saturday 18:00, if no other date and time was announced on the mailing list

### Prototype Design of the UI Elements

-   A toolbar with the most important features (like 'fetch mail' or 'zoom in') is placed on the bottom.

### Framework Subsystem Design

-   Use a compiled programming language (most likely C or C++)
-   Use Elementary to develop the UIs
-   Build upon the FSO \`frameworkd\` stack
-   Use GPLv2 or later as the license for the source code
-   Expand Elementary if necessary

### Development of the base framework with rudimental functions

-   ... to be defined ...

### Development of the base features and auxilliary functions in the framework

-   ... to be defined ...

Base Features
-------------

The base features serve two purposes:

1.  Showcase, real-world testing and requirements engineering for the service level framework,
2.  Ready-to-use set of mobile companion features.

The following base features would make sense for a 1.0 version:

-   Phone Dialer
-   Short Message Service
-   Contacts List
-   Calendar
-   Media Player (audio, photo, video)
-   Memo (text, paint, speech, camera)
-   World Time Clock, Alarm Clock
-   Package Manager
-   Preferences

FAQs
----

Q: It's UMAF only for Device X?

A: No, UMAF is for all devices they can execute the freesmartphone stack.

Q: What is the service framework?

A: The service framework is a "high-level FSO stack". It should provide services like "search a contact", "send data to a peer", "select network connection", etc. and "common dialogs" (file chooser etc.).

Questions for Discussion
========================

-   programming language for the framework
-   how do we want to use gestures? as keyboard? application or framework level interaction?
-   fennec[1] looks interesting. some inspiration?
-   accel gestures? too cpu intensive? only some applications?
-   how should we use gestures in application, when we use it in the application lauchner (see illume ideas)
-   Abstraction of the filesystem structure to ease browsing through pictures, movies or music?

Discussion Summaries
====================

Short Term ToDo Items
---------------------

-   Develop Python bindings for Elementary (morphis)
-   Develop small applications to demonstrate some basic ideas and to ease discussion about basic concepts.
-   Contact OpenUsability

Ideas for Illume
----------------

-   Three windows

`   * main screen (like Qtopia + messages, date view, ..., will be replaced when a new application starts)`
`   * icon menu (12 icons - define categories?)`
`   * Running applications (switch between them)`
`   `
`   Switch between windows with gestures (from the left to right or the other way around).`
`   `
`   * Example for the three window idea with gestures:`
`     You start the phone => The Homescreen appears`
`     You slide left => The Menu with 12 icons appears`
`     You slide left => The running-application window appears (no running application)`
`     You slide right => Menu-Window => you starts a application`
`     You see the application`
`     You slide left => The Menu with 12 icons appears`
`     You slide left => Running-Applications => Home and your started application`
`     You activate home and you get back to the home-screen`
`   `
`   A modified idea of mine by bumbl `[`http://img119.imageshack.us/my.php?image=mockupab8.jpg`](http://img119.imageshack.us/my.php?image=mockupab8.jpg)
`    - But i think an up or down gesture should scroll through all active applications (a other option to switch an application, without the running-application-window)`
`    - Gestures should be usable without to pushing an extra hardware-button => how could we use gestures in the global menu and in an application?`
`   `
`   New Mockup by Patrick => `[`http://yourse.de/tmp/illume_konzept.png`](http://yourse.de/tmp/illume_konzept.png)
`   The svg-file is under => `[`http://yourse.de/tmp/illume_konzept.svg`](http://yourse.de/tmp/illume_konzept.svg)

-   illume modified idea with hardware buttons by sleipnir <http://www.bilder-space.de/show.php?file=roSiwuZSzoFtL0L.jpg>

<!-- -->

-   Key-Bindungs: AUX and Power

`   * Press AUX-Key short - open menu with the following content`
`       - create screenshot`
`       - rotate screen (do we really need this? we have an accel-based rotate program now.)`
`       - lock screen`
`       - mute ringtones, alarms, ...`
`       - more?`
`       `
`   * Press Power-Key short`
`       - close current program`

`   * Make the keybindings configurable and ship with defaults for the average user? (the opinions about keybindings differ a lot!)`
`       `
`  (How should we activate suspend or how to exit applications?)`
`  => Add a close button for every application?`

Ideas for UMAF
--------------

Also see the 'Development Plans' section

-   consistend MVC
    -   own layout description language (similiar to edje) to design applications (View)
    -   data loading etc. should be done in background processes, so the application is as far as possible on the screen (Model)

General UI Ideas
----------------

-   Buttons with the same functionality should be on the same place in **all** programs (like forward, backward or delete)
    -   Trigger forward and backward per left/right gesture?
-   Find a better way to close applications
-   The illume launcher is evil
-   Use gestures in the UI, but not too much as they can get annoying pretty fast
-   Allow the use of other keyboards to support innovation in this area

### Ideas for the menu prompt

1st idea

`   `[`http://media.cream-project.org/mockup.png`](http://media.cream-project.org/mockup.png)
`   With toolbar: Always show three or four icons. The other ones should be available through a seperate window, which is accessable through an arrow (more or less illume like)`
`   `
`   Cons:`
`       * Due to the 3 mm border around the display, the toolbar would be hard to use.`

2nd idea

`   Just two buttons: "Options" and "Call" (options can be changed in a seperate window with scrollbar or tabs (??)).`
`   `
`   Cons:`
`   `
`       * Do we really need "Options" visible all the time? Most Users will change them once and never touch them again.`

3rd idea

`   Two toolbars - on top and on the bottom`

User contributed mockups

`   `[**`wp:`**](http://lists.openmoko.org/nabble.html#nabble-td1113867|a1113867)
`   `
`       `[`http://server6.theimagehosting.com/image.php?img=structure.png`](http://server6.theimagehosting.com/image.php?img=structure.png)` (general structure)`
`       `[`http://server6.theimagehosting.com/image.php?img=artconcept1.png`](http://server6.theimagehosting.com/image.php?img=artconcept1.png)
`       `[`http://server6.theimagehosting.com/image.php?img=artconcept2.png`](http://server6.theimagehosting.com/image.php?img=artconcept2.png)
`       `[`http://server6.theimagehosting.com/image.php?img=artconcept3.png`](http://server6.theimagehosting.com/image.php?img=artconcept3.png)

### Ideas for general layout

dialog proposition: layout of date and time dialogs (to set system time, to get time for a calendar entry...) <http://server6.theimagehosting.com/image.php?img=layout_time.png>

Generize Layout:

`  * create a page widget and a selection Widget`
`  * the page widget shows the possible pages on top`
`  * selection widget can embed arbitary widgets`
`    it will automatically add page switch buttons if necessary`
`  * based on user settings the selection widget might hide the page switch widgets and use left right gestures,`
`    this will then be inicated by small arrows on left and right side`
`  * same with page widget, but with up/down gesture`

Layout could then look like this (layout, not design): <http://server6.theimagehosting.com/image.php?img=layout_illume.png>

Ideas for Applications
----------------------

-   Every window of a application is subdivided by zones. There are ZoneLayouts which specify how big the zones are and where they are on the screen. In every zones the application can embeded their content or navigation.

<!-- -->

-   Templates for different application.

`  * only text information (one window?)`
`  * tabs (with more windows)`
`  * ???`

`=> So we can create four or five templats thats should fit all needs - zones are the base of the templates.`

Idea for a application layout engine: <http://rafb.net/p/e4iSPD56.html> (broken link!)

Staff members
=============

[**Michael 'Mickey' Lauer**](/User:Mickey "wikilink")

Mail: *mlauer(at)vanille-media(dot)de*

[**morphis**](/User:morphis "wikilink")

Mail: *morphis(at)gravedo.de(dot)net*

Jabber: morphis(at)jabber(dot)ccc(dot)de

[**stein**](/User:stein "wikilink")

Mail: *sebbil(at)gmx(dot)de*

Jabber: ''stein(at)jabber(dot)cream-project(dot)org

[**Flyser**](/User:Flyser "wikilink")

Mail: *CC.Fan(at)gmx(dot)de*

Jabber: flyser(at)jabber(dot)ccc(dot)de

[**Patrick Beck**](/User:PatrickBeck "wikilink")

Mail: *pbeck(at)yourse(dot)de*

Jabber: pbeck(at)unixboard(dot)de

Source Control
==============

UMAF has a Subversion (SVN) Repository: <http://projects.linuxtogo.org/scm/?group_id=11>

To checkout use: svn checkout <svn://projects.linuxtogo.org/svn/smartphones>

Register a account
------------------

1.  To become a account, register on <http://projects.linuxtogo.org/>.
2.  Then ask Mickey or seeseekey to add you to project.
3.  After this you must create a key with ssh-keygen.

Useful Links
============

-   <http://www.openusability.org/>
-   <http://humanized.com/weblog/2007/10/05/make_oss_humane/>
-   A GTA02 Image with elementary: <http://download.enlightenment.org/misc/Illume/>
-   please add more

Discussion
==========

-   Please use smartphones-standards (at) linuxtogo (dot) org for now.
-   To subscribe/unsubscribe/visit archives: <http://lists.linuxtogo.org/cgi-bin/mailman/listinfo/smartphones-standards>
-   For IRC discussion visit the Channel \#neo1973-germany in irc.freenode.net.

[UMAF](/Category:UMAF "wikilink")
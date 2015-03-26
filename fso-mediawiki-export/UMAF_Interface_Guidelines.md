---
title: UMAF Interface Guidelines
permalink: /UMAF_Interface_Guidelines/
---

Preliminary Remark
==================

Please note: Our work on a interface guideline for our untiled mobile application framework will base on the Human Interface Guidelines of the GNOME Usability Project. So we can start our guideline easily and know what we have to care about.

The GNOME Human Interface Guideline is published unter GNU Free Documentation License so our work will be published under the same license.

REMARK: Currently I am copying the whole guideline to this wiki page.

This page is based on the GHIG 2.24.0 that you can find under <http://library.gnome.org/devel/hig-book/stable/>

Introduction
============

This document tells you how to create applications that look right, behave properly, and fit into the GNOME user interface as a whole. It is written for interface designers, graphic artists and software developers who will be creating software for the GNOME environment. Both specific advice on making effective use of interface elements, and the philosophy and general design principles behind the GNOME interface are covered.

These guidelines are meant to help you design and write applications that are easy to use and consistent with the GNOME desktop. Following these guidelines will have many benefits:

-   Users will learn to use your program faster, because interface elements will look and behave the way they are used to.
-   Novice and advanced users alike will be able accomplish tasks quickly and easily, because the interface won't be confusing or make things difficult.
-   Your application will have an attractive look that fits in with the rest of the desktop.
-   Your application will continue to look good when users change desktop themes, fonts and colors.
-   Your application will be accessible to all users, including those with disabilities or special needs.

To help you achieve these goals, these guidelines will cover basic interface elements, how to use them and put them together effectively, and how to make your application integrate well with the desktop.

The recommendations here build on design aspects that have worked well in other systems, including Mac OS, Windows, Java and KDE. At the same time they retain a uniquely GNOME flavor.

Remember... Following the guidelines will make your job easier, not harder!

Usability Principles
====================

This section explains some of the basic principles behind the more specific technical guidelines recommended in this document. We believe that these principles are important for all application development.

Design for People
-----------------

Remember that the purpose of any software application is to enable some group of people to accomplish a specific set of tasks. So, the first things to establish when designing your application are:

-   who your users are
-   what you want to enable them to do

For example, you may be designing an application that will enable engineers (software, electrical, or mechanical) to create diagrams. You may be designing an application that will enable system administrators to configure and monitor a web server. You may be designing an application that will help elementary school students to learn math.

The important thing is that you know your audience, and you understand both their goals and the tasks necessary to achieve those goals. There are a large number of professional interaction designers who write books and teach courses on design methods that can help with this process, many of which are extremely useful— see the Bibliography for a selection. Most of these methods, however, boil down to specific ways of understanding your users, understanding the tasks you want to help them accomplish, and finding ways to support those tasks in your application.

Don't Limit Your User Base
--------------------------

If you are designing an application for use by engineers, or by children, or by system administrators, be sure to create an application that can be used by all engineers, children, or system administrators, including those with disabilities or those who are native speakers of a language different from yours. Be aware of accessibility issues and internationalization and localization issues, many of which are addressed by the guidelines in this document.

### Accessibility

Accessibility (sometimes called a11y) means enabling people with disabilities of some kind to participate in life's activities: in this case, specifically to use your software. For example:

-   Color-blind users may not be able to use your application if you rely only on color-coding to distinguish different types of information
-   Users with hearing impairments may not be able to use your application if you rely on sounds to indicate critical information
-   Users with limited movement may not be able to use your application if you don't provide keyboard equivalents for commands

Your software should also be usable with voice interfaces, screen readers such as Gnopernicus, alternate input devices, and other assistive technologies. The standard GNOME libraries do most of this work for you, but with a little extra effort you can make your application every bit as useful to users who rely on those technologies as to those who don't.

GNOME has excellent inbuilt support for accessibility by means of the ATK and GAIL libraries, which in many cases can do most of the work for you. More information on accessibility in GNOME can be found at the GNOME Accessibility Project.

### Internationalization and Localization

Internationalization means designing software so that it can function in different language environments. Localization is the process of actually translating the messages, labels, and other interface elements of an application into another language.

GNOME has excellent support for both internationalization (also referred to as i18n) and localization (also referred to as l10n). In most cases, simply using standard GNOME APIs for displaying text and messages will allow you or others to localize your application for other locales. For more information on how to make your application localizable, see the Pango project home page (Pango is the GNOME library for rendering internationalized text), the GNOME Translations page, and the GNOME Translation Project page.

Sensitivity to cultural and political issues is also an important consideration. Designing icons and sounds, and even choosing colors requires some understanding of the connotations they might have to a user from a different part of the world.

Examples of elements it is best to avoid for these reasons include:

-   Pictures of flags or money
-   Maps showing political boundaries or contentious location names
-   Lists of countries or cities in non-alphabetical order (unless specifically requested or required by the context)
-   Icons depicting animals
-   Icons depicting only hands or feet

Create a Match Between Your Application and the Real World
----------------------------------------------------------

Always use words, phrases, and concepts that are familiar to the user rather than terms from the underlying system. Use terms that relate to the user's knowledge of the tasks your application supports. For example, in medicine, the paper folder that contains all information about a specific patient is called a "chart." Hence, a medical application might refer to a patient record that contains the same information as a paper chart as a "patient chart" rather than as a "patient database record."

You can often take advantage of your users' knowledge of the real world by using metaphor— that is, a familiar concept from the outside world— to represent elements within your application. For example:

-   an image of a file folder suggests a container into which documents can be placed
-   a waste basket suggests a container into which items can be placed when they are no longer needed

When using metaphors, however, it is important to neither take the metaphor too literally, nor to extend the metaphor beyond its reasonable use. For example, the capacity of a file folder should not be limited to the capacity of a physical file folder, which presumably could contain only a few documents before becoming unwieldy. On the other hand, a waste basket should not be used for anything other than holding discarded files. It should not be used, for example, to eject a removable disk such as a floppy or CD.

Make Your Application Consistent
--------------------------------

Make your application consistent with itself and with other applications, in both its appearance and its behavior. This is one of the most important design principles, and probably the most famous, but it is also frequently ignored. While this document serves as the basis for consistency between GNOME applications, you are encouraged to look at and follow other application's conventions where this document provides no guidelines.

Consistency enables users to apply their existing knowledge of their computing environment and other applications to understanding a new application. This not only allows users to become familiar with new applications more quickly, but also helps create a sense of comfort and trust in the overall environment. Most of the recommendations in the GNOME HI Guidelines are designed to help you create applications that are consistent with the GNOME environment and other GNOME applications.

A word of caution: a mis-applied or incomplete consistency is often worse than inconsistency. If your application includes an Undo menu item for consistency, but it is always disabled because your application does not actually support Undo, this will reduce the user's trust in the availability of Undo in other applications on their desktop. Either make your application support Undo, or eliminate the Undo menu item.

Keep the User Informed
----------------------

Always let the user know what is happening in your application by using appropriate feedback at an appropriate time. The user should never have to guess about the status of the system or of your application. When the user performs an action, provide feedback to indicate that the system has received the input and is operating on it. Feedback can be visual, audio, or both. If the system will take a long time to process the request, provide as much feedback as possible about how lengthy the operation will be. Types of helpful feedback include but are not limited to: cursor changes, animated "throbbers", progress indicators, audio feedback such as a beep, and error messages. Error messages should use simple language, clearly state the problem, and provide solutions or tell the user how to get out of the current situation if possible.

It is critical that feedback be accurate and precise. If you display a determinate progress indicator to display the state of completion of a task and it is inaccurate, the user will lose faith in progress indicators, and they will find the environment less usable. If you display a generic error message that indicates that there is a problem but fails to provide enough information to diagnose or solve the problem, your users will be unable to continue with their task.

See Chapter 7 ― Feedback and Section 3.4 ― Alerts for more information on feedback.

Keep It Simple and Pretty
-------------------------

Your application should enable the user to concentrate on the task at hand. So, design your application to show only useful and relevant information and interface elements. Every extra piece of information or interface control competes with the truly relevant bits of information and distracts the user from important information. Hence, don't clutter your interface, and don't overload the user with buttons, menu options, icons, or irrelevant information. Instead, use progressive disclosure and other techniques to limit what the user sees at any given moment.

Finally, present your information and interface elements in an aesthetically pleasing manner. A disorganized, cluttered-looking interface with a few elements can be just as distracting as an organized interface with too much information. Make sure that dialog elements are cleanly-aligned, and do not overuse or misuse color or graphics. If you know a graphic designer, seek their advice if possible— the guidelines in this document will help you with the basics, but there is no substitute for a trained eye.

See Chapter 8 ― Visual Design and Chapter 9 ― Icons for more information on designing the visual appearance of your application.

Put the User in Control
-----------------------

Remember that computers exist to serve humans. A user should always feel in control, able to do what they want when they want. This means you should generally avoid modes; users should be able to switch between different tasks (and specifically, different windows) at any time. See Section 3.1.3 ― Modality for more information on modes.

The user should also be able to tailor aspects of their environment to fit personal preferences. It is very important, however, to avoid the trap of allowing too much configuration, or allowing the configuration of parameters that most users will not understand or find useful to modify. Wherever possible, inherit visual and behavioral parameters from global preferences and settings such as the current GTK+ theme.

Forgive the User
----------------

We all make mistakes. Whether we're exploring and learning how to use the system, or we're experts who just hit the wrong key, we are only human. Your application should therefore allow users to quickly undo the results of their actions.

If an action is very dangerous, and there is no way to undo the result, warn the user and ask for confirmation. Only do this in extreme cases, though; if frequently faced with such confirmation messages, users begin to ignore them, making them worse than useless.

In all cases, the user's work is sacrosanct. Nothing your application does should lose or destroy user's work without explicit user action. Among other techniques, this can be achieved by auto-saving backups of documents, and allowing multiple levels of undo.

Provide Direct Manipulation
---------------------------

Wherever possible, allow users to act on objects and data directly, rather than through dialogs or explicit commands. For example, it is more intuitive to drag a circle object around in a diagram rather than selecting a "Move" command from a menu while the circle is selected. Simlarly, in an email application, allow the user to attach files by dragging them from the file manager and dropping them onto the message composition window if they wish.

See Chapter 10 ― User Input for more information on direct manipulation.

Desktop Integration
===================

There are two elements to basic integration with the user environment of the GNOME Desktop.

1.  Place an entry for your application in the Applications menu. This is the primary mechanism by which users discover and run applications.
2.  If your application can open and save files, place entries for those file types in the application database and the document type (MIME) database. This allows the file manager and other applications to automatically launch your application when they encounter files your application can handle.

Do not add launchers or other icons to the desktop when your application is installed. The desktop is the user's space, and is reserved for icons that they explicitly request or add themselves.

Placing Entries in the Applications Menu
----------------------------------------

The Applications menu, which appears on the panel at the top of the screen by default, is the primary mechanism by which users discover and run applications. You place entries in this menu by installing an appropriate .desktop file.

The menu is arranged into a set of categories, such as Accessories and Games. Applications are placed in particular categories by the set of keywords they include in their .desktop file. Guidelines

-   Assign your application to only one category on the Applications menu
-   For application suites that wrap a number of smaller sub-applications into a single window, such as Evolution or OpenOffice.org, add a menu item for each sub-application. For example, the mail, calendar, and tasklist in Evolution should each have their own menu item.

Technical details can be found in the freedesktop.org menu and desktop entry specifications.

### Menu Item Names

#### Include a functional description in the menu name

In the menu item name, include a description of functionality in addition to the proper name of the application. This is especially useful novice users, and to users of systems where numerous applications are installed by default. Users are more likely to find your application if the name that appears in the menu includes a description of its functionality.

For example, user testing of MIT's Athena system revealed that users had difficulty finding the file manager because they were unfamiliar with the name "Nautilus". Because users did not associate the word "Nautilus" with the concept "file manager" the menu item did not help them. This is an example of not using the user's language. See Section 1.3 ― Create a Match Between Your Application and the Real World for more on this topic.


Example 2-1 Including functional description in menu names

:{| class="wikitable" border=1 ! Original menu item !! Revised menu item |- | Epiphany || Epiphany Web Browser |}

#### Only put useful information in the menu name

Do not include words like "GNOME", "X Window System", "GTK+" or other platform details in Application menu names. The user probably already knows what platform they are using, and if they don't, then application names are not the right place to inform them.


Example 2-2 Removing non-essential information from menu names

:{| class="wikitable" border=1 ! Original menu item !! Revised menu item |- | GNOME Image Viewer || Image Viewer |- | GTK Blog Editor || Blog Editor |}

Do not include technical details when the user does not need to know them, or can infer them from context. Avoid technical jargon unless the application is to be used only by a technical audience.

For example, when both a client and a server for something are listed in the menus, remove the word "Client" from the menu name for the client.


Example 2-3 Removing technical jargon from menu names

:{| class="wikitable" border=1 ! Original menu item !! Revised menu item |- | Gnome Batalla Naval Client || Batalla Naval |- | Gnome Batalla Naval Server || Batalla Naval Multiplayer Server |- | Gnome VideoLAN Client || VideoLAN Movie Player |}

`   `**`Providing` `the` `right` `information`**
`   Try to imagine what words users will be looking for when they select your application from the Applications menu. That is the information that should be in the menu       name. For example, a user wanting to play a movie will probably not be looking for the word "Client". On the other hand, a user wanting to transmit movies from their   computer may well look for the word "Server". Avoid thinking of the applications menu as an ontology!`

#### Menu name formats

-   If your application's proper name is already descriptive of its functionality, and not just suggestive, use the format: Application Name


Example 2-4 Using application's name as menu name

:{| class="wikitable" border=1 ! Application name !! Menu name |- | Dictionary || Dictionary |- | Search Tool || Search Tool |}

-   If there is a succinct functional description of your application, use the format: ApplicationName FunctionalDescription


Example 2-5 Using functional description in menu names

:{| class="wikitable" border=1 ! Application name !! Menu item name |- | The GIMP || GIMP Image Editor |- | Evolution email sub-application || Evolution Email |- | AbiWord || AbiWord Word Processor |- | Galeon || Galeon Web Browser |- | Gramps || Gramps Genealogy |- | AisleRiot || AisleRiot Solitaire |}

-   A few applications, particularly games, do not have appropriate functional descriptions (but note that many games do). In this case, use Application Name as the menu name.


Example 2-6 Using applicaton's name as menu name where no functional description exists

:{| class="wikitable" border=1 ! Application name !! Menu item name |- | Bomber Maze || Bomber Maze |}

#### Menu Item Tooltips

Tooltips help provide users with enough information to run the right application. Many users use tooltips to explore a new environment.

Provide a tooltip for each Application menu item you add, following these guidelines: Guidelines

-   Phrase the tooltip as an imperative verb, for example "design", "write" or "check".
-   Describe the most important tasks users can accomplish with your application.
-   While tooltips should not be verbose, they should be longer and more descriptive than the item's name.


Example 2-7 Example tooltips for GNOME applications

:{| class="wikitable" border=1 ! Application !! Menu item tooltip |- | Character Map || Insert special characters into documents |- | Memprof || Check your applications for memory leaks |- | Same Gnome || Arrange long chains of similarly-colored balls to eliminate them |- | Gnome Batalla Naval Client || Find and sink enemy ships in this networked version of Battleship |}

GConf Keys
----------

GConf keys are required to have long and short descriptions for each key. Many keys have no interface through the application, so for someone administering the key values from another application each description field will be the only interface available to them. Guidelines

-   Short Descriptions should be short, less than 8 words, describing the purpose of the key
-   Long Description should be complete in describing the possible values of the key and the effects that those values have on the application


Example 2-8 Example descriptions for GConf Keys from gnome-terminal

:{| class="wikitable" border=1 ! Key !! Short Description !! Long Description |- | background_type || Background type || Type of terminal background. May be "solid" for a solid color, "image" for an image, or "transparent" for pseudo-transparency. |- | delete_binding || Effect of the Delete key || Sets what code the delete key generates. Possible values are "ascii-del" for the ASCII DEL character, "control-h" for Control-H (AKA the ASCII BS character), "escape-sequence" for the escape sequence typically bound to backspace or delete. "escape-sequence" is normally considered the correct setting for the Delete key. |}

Mapping Document Types to Applications
--------------------------------------

The document type (MIME) database allows users to specify their preferred applications for opening different types of document. This is the mechanism by which Nautilus, Evolution and other applications decide which application to run when they encounter a document they cannot open themselves.

It is important for users to be able to double-click on documents they see on the desktop, such as files and email messages, and have them launch in their favorite application. Therefore, your GNOME application should associate itself at install-time with all the document types it can handle. Technical details on doing this can be found in the GnomeVFS API reference.

Using the Status Notification Area
----------------------------------

The status notification area on the panel is used to notify the user of non-critical events, such as the arrival of new email, and to monitor the status of background activities, such as a laptop battery charging. Recent versions of the GNOME desktop (2.12 or newer) can also pop up a small transient "balloon" attached to a notification icon, to give additional information and interaction choices related to an event.

WARNING: The utility of the notification area decreases rapidly when more than four icons are displayed at the same time. Icons that appear only temporarily, in response to specific events, are therefore preferable.

Following the guidelines in this section will help to clarify the difference in the user's mind between information presented in the notification area, and controls and information presented on other parts of the panel.

### Appropriate Uses for the Notification Area

There are three acceptable uses for the notification area:

-   Displaying a transient icon in response to an event (e.g. arrival of new mail in a monitored folder). Clicking the icon opens the most appropriate window to deal with the event (e.g. Inbox). The icon is removed when the state prior to the event is restored (e.g. no more unread mail in monitored folders).
-   Displaying an icon for the duration of a background activity (e.g. while a document is being printed). The icon is removed when the activity successfully completes, or replaced with a suitable error icon if the activity fails (optional tooltip or balloon to explain problem). Clicking the error icon (or balloon) opens the most appropriate window for the user to rectify the problem.
-   Displaying an ever-present icon to monitor a continuous background activity, such as a laptop battery being charged. Continous notification icon presence should always be controllable by a user preference. Only core GNOME applications may have this preference turned on by default; other applications should turn it off by default.

Standard way of presenting this option would be nice.

In particular, you should probably use an applet instead of using a notification icon if:

-   your notification icon would need to be shown all the time, or would benefit from being shown all the time

and:

-   clicking your notification icon would do anything other than opening a window or dialog box directly associated with the icon or the event that caused it to appear

`     (example?)`
`     , or`

-   multiple instances of the icon would either be required, or could be considered useful (for example, a clock-- a user might want to display a separate clock for each of multiple timezones)

Because the notification area is itself a panel applet, remember that the user may not have it on their desktop at all. Above all, therefore, only use notification icons to provide redundant, non-critical information.

### Icon Appearance

Guidelines Need some examples here. There have been suggestions in the past that notification icons should have a more muted colour scheme (possibly just B&W) than other objects on the panel-- good idea?

-   Use table perspective for icons representing physical devices, for example a printer icon shown during printing, with the light source above and to the left of the represented object. See Section 9.1.1 ― Perspective for more about table perspective.
-   Use a flat, unshaded image for status monitors that take the form of a chart or graph, such as a CPU usage monitor. Clearly delimit the borders of the chart area.
-   Use shelf perspective, with overhead lighting, for all other icons. For example, an envelope shown when new mail arrives. See Section 9.1.1 ― Perspective for more about shelf perspective.

### Icon Animation

As with any part of the desktop, animation must be used sparingly to be effective, and redundantly to be accessible. Guidelines

-   To avoid distracting the user, do not update notification icons that are monitoring a background activity any more than once per second by default. For any such icons that are perpetually shown, make the exact update frequency a user preference.
-   Do not animate notification icons that are not monitoring the status of a background activity.
-   Do not rely on animation, or any other change of appearance within a notification icon, as a means of alerting the user to a particular event.

### Interaction

All notification icons should respond to user interaction in a consistent way, similar to that for panel applets. Guidelines

-   Perform the icon's default action when the user clicks the icon, or presses the Space key when it is focused. In general, an icon's default action should be to open a relevant window or dialog box, or to raise and focus that window or dialog box if it is already open but not focused. Examples of such windows and dialogs include:

o the printer queue window, for a "printing in progress" icon o the default mail application's Inbox window, for an incoming email icon o the message window, for an incoming instant message icon

If the icon's associated window or dialog box is already raised and focused, close it when the user clicks the icon, or presses the Space key when the icon is focused. All windows associated with notification icons should be dismissable in this way, except for explicit apply dialog boxes. Those should always be dismissed by clicking their action or cancel buttons.

-   Present a context menu, containing at least the icon's default action, when the user right clicks the icon or presses Shift+F10 when the icon is focused.
-   If the icon's properties, or the properties of its associated application or document may be altered, include a Properties menu item in its context menu, and show its property panel in response to Alt+Enter when the icon is focused.

### Notification Ballons

FIXME: guidelines for appearance and interaction with libnotify-type balloons. All the guidelines shown here now are very early thoughts.

Random Thoughts

-   If an icon has displayed a balloon that is no longer visible, subsequently mousing over the icon should perhaps cause the last message to appear as a tooltip?
-   Need to think about notifications in the context of accessibility. The notification spec allows for notifications to be shown in different ways, perhaps we need to do something different for users relying on screenreaders or desktop magnification?
-   An icon may show a balloon to indicate an error in deference to showing an alert. For example, a printing-in-progress icon may show a balloon when there is a paper jam, but not when the printer is on fire - that should show an alert.
-   A balloon may be show when the icon is first displayed, if the icon's appearance is not the direct result of a user action. For example, the icon for an incoming email or instant message may be accompanied by a balloon. However, the appearance of a printing-in-progress icon would not be accompanied by a balloon, because its appearance was caused by the user choosing to print a document.
-   An icon may show a balloon if it has previously shown a balloon, and the condition recurs. For example, an incoming email icon which has remained visible, and was originally accompanied by a transient balloon, may show another balloon when another message arrives.

Windows
=======

Parts of Windows and System Interaction
---------------------------------------

### Titles

Give every window a title (with the exception of alerts and toolboxes). A good window title contains information that is relevant to the user, and distinguishes a particular window from other open windows. Omit information that does not assist in this selection, for example the application's version number or vendor name.

Figure 3-1 Example of a window title

See the description of each particular window type for title formats.

### Borders and Window Commands

Most windows have borders, except certain shaped windows and some torn-off windows. Do not attempt to draw your own window borders, but instead provide hints to the window manager for the desired border type.

Different window commands are appropriate to different types of window. See the description of each particular window type for a list of appropriate window commands. These are the possible window commands:

-   Close: Closes the window. Always draw this as a button on the window border when relevant to the window type.
-   Maximize: Causes the window to use all unused screen space.
-   Minimize:Causes the window to be temporarily hidden. It will continue to appear on the desktop window list.
-   Roll-up/Unroll: Shows only the title bar of the window, as if it has been "rolled up".

### Modality

A non-modal window does not restrict the user's interaction with other open windows on the desktop in any way. Using non-modal windows gives the user maximum flexibility to perform tasks within your application in any order and by whichever means they choose.

An application modal window, while it is open, prevents the user from interacting with other windows in the same application.

A system modal window, while it is open, prevents the user from interacting with any other window in any application, including the desktop itself. Guidelines

-   Use an application modal window only if allowing interaction with other parts of the application while the window is open could cause data loss or some other serious problem. Provide a clear way of leaving the modal window, such as a Cancel button in an alert.
-   Do not use system modal windows.

### Focus

Focus is the means by which the user designates which window should receive data from the keyboard, mouse or other input device. If using a screen reader or similar assistive technology, focus may also designate the window that the user wants to receive information about. The focused window is considered the window the user is currently "working with".

Ensure your application functions properly with the three different mechanisms by which windows can receive focus in GNOME:

-   Click-to-focus: A window is focused by clicking in it.
-   Point-to-focus: A window is focused by moving the mouse pointer into it. Sometimes known as "sloppy focus".
-   Keyboard focus: A window is focused by using a keyboard shortcut such as Alt+Tab.

NOTE: Special restrictions for point to focus

Note that point-to-focus places a number of restrictions on GNOME applications that are not present in environments such as MacOS or Windows. For example, utility windows shared between multiple document windows, like the toolbox in the GIMP Image Editor, cannot be context-sensitive— that is, they cannot initiate an action such as Save on the current document. This is because while moving the mouse from the current document to the utility window, the user could inadvertently pass the pointer over a different document window, thus changing the focus and possibly saving the wrong document.

### Showing and Hiding Windows

How your application shows and hides windows can greatly affect the user's perception of your application, particularly its performance. Guidelines

-   Always show a window as soon as possible, but make sure your window is the correct size before displaying it. Resizing a window after it is visible is disorienting and gives an unpolished look to your application.
-   If a window contains information that takes a few seconds to compute or display, it is often better not to fill it in completely before displaying the window. For example, a window containing a large text area can be shown quickly, and then the text can be filled in afterwards (provided this does not result in the window resizing). This will make your application feel more responsive than if you had not shown the window until its content was complete.
-   Hide a window as soon as possible after it is closed. Unless an alert might be shown, immediately hide a window that the user has closed by clicking the Close button in the window border-- your application can still perform any internal clean-up operations afterwards. Besides making the system appear slow, not doing this can cause the window manager to think the application is not responding, and display an unnecessary alert to the user.

Primary Windows
---------------

A primary window usually presents a view of the user's data, such as a text document in a word processor application, an image in a drawing program, or calculations in a calculator or spreadsheet application. It may also be a view of something more abstract, like a game. A single instance of an application may have more than one primary window, and more than one kind of primary window.

A primary window is always shown on the panel window list. Figure 3-2 A typical primary window (gedit)

A primary application window normally has a border, a menubar and a statusbar, and may also contain one or more toolbars.

### Title

The most important element of a document-based application's window title is the name of the open document. For other applications, it usually the name of the application. Guidelines

-   Use Filename as the window title for document-based applications. Do not use the full pathname, as the filename alone is easier to distinguish amongst other open window titles, for example on the window list.

`     Example 3-1 Using document names as window titles`
`     Application   Example window title`
`     AbiWord   My Report.abw`
`     Evolution Inbox`
`     Music player  U2 - Better Than the Real Thing`

If the pathname is important, for example the user has opened two documents with the same name from different directories in the same application, show the full pathname in the statusbar.

-   Before a new document has been saved for the first time, set the window title to Unsaved <document type>. For example, Unsaved Drawing, Unsaved Spreadsheet, or the more generic Unsaved Document.
-   When a document has pending changes, insert an asterisk (\*) at the beginning of the window title. For example, \*Unsaved Drawing, \*AnnualReport.
-   For non-document-based applications, use Application Name as the window title.

`     Example 3-2 Using application names as window titles`
`     Application   Window title`
`     Dictionary    Dictionary`
`     Calculator    Calculator`
`   `

-   Do not place version numbers, company names, or other information that is of no immediate use to the user in the window title. These consume space, making titles in limited spaces such as the system window list less useful, and add more text the user has to scan to find useful information. In a "beta" product, where version numbers are critical for bug information, placing version numbers can be useful, but remove them from stable releases. Place version information in the about box instead.

While document names are most pertinent to users, we understand that application developers may want to increase recognition of their application. If you plan to include your application's name in the title of a primary window, use the following format: Document Name - Application Name. This will ensure that the document name appears in limited space situations such as the system window list.

Including the application name in the title of a document-based application is not recommended.

Think about naming windows in the context of the panel window list. On a typical screen with a relatively small number of windows open, a window will have 20-30 characters of text and an icon. Consider which text will provide the most immediately obvious clues to a user looking for a particular window.

### Window Commands

Close, Maximize/Restore, Minimize, Roll-up/Unroll

### Relation between Documents and Windows

#### Single Document Interface (SDI)

A single document interface places each document in its own primary window. Toolboxes and other utility windows may be shared between multiple SDI documents, but closing them should have no effect on the document windows. Use SDI for your GNOME application unless there is a compelling reason not to. Figure 3-3 A typical SDI application (Eye of GNOME)

#### Multiple Document Interface (MDI)

A multiple document interface presents a paned, tabbed or similar presentation of two documents within a single window. Figure 3-4 A typical MDI application (gedit) showing three open documents on tabbed pages

MDI has several inherent usability problems, so its use is discouraged in applications. It is better to open each document in a new primary window, with its own menubar, toolbars and statusbar, or allow multiple instances of your application to be run simultaneously. In either case, this leaves it for the window manager (acting on the user's preferences) rather than your application to decide how to group and present document windows from the same application.

#### Controlled Single Document Interface (CSDI)

In a typical SDI application, document windows are treated as primary. For example, when all document windows have been closed, the application (including utility windows) exits as well. In CSDI a utility window is treated as the primary window. For example, closing this utility window will close all document windows and exit the application.

Using CSDI is not recommended

CSDI is sometimes used because document windows might be too small to have menu bars. Typically this is not the normal use case for the application, but does represent a significant minority use case. For example, an image editor being used to edit small web page elements will often result in very small document windows that cannot accomodate a title bar.

A better way to address this problem is to allow menu bars to "collapse" into an overflow button, in much the same way toolbars operate when the window shrinks to below the toolbar width. This allows for small windows, but also provides an opportunity for people to figure out where their menus have gone.

Note that if very small documents are the primary use case for your application, you should consider finding a means to avoid windows altogether. Windows are not an effective interface for dealing with large numbers of small items. Consider looking for a fixed/automated layout system for presenting the "documents". Also consider if the "documents" will be primarily used in a higher level grouping, in which case that grouping could become the document instead.

Utility Windows
---------------

Utility windows, such as palettes and toolboxes, normally have borders. They do not contain a menu bar, a toolbar, or a statusbar.

A utility window should not appear in the panel window list unless it is, or may be, the only window shown by an application. Otherwise, the utility window should be raised above the application when the application window itself is selected from the window list.

### Instant apply windows

For windows that allow the user to change values or settings, such as property and preference windows, update those values or settings immediately to reflect the changes made in the window. This is known as "instant apply". Do not make the user press an OK or Apply button to make the changes happen, unless either:

-   the change will take more than about one second to apply, in which case applying the change immediately could make the system feel slow or unresponsive, or
-   the changes in the window have to be applied simultaneously to prevent the system entering a potentially unstable state. For example, the hostname and proxy fields in a network properties window.

If either these conditions affect only a few of the controls in your window, arrange those controls together into one or more groups, each with its own Apply button. Leave the rest of the controls as instant apply. Guidelines

-   Do not attempt to validate or apply changes caused by editing a text field control until the user has moved focus to a different control in the window, or the window is closed. Validating after each keypress is usually annoying and unnecessary. Exception: if the field accepts only a fixed number of characters, such as a hexadecimal color code, validate and apply the change as soon as that number of characters have been entered.
-   When the user moves focus to a different control, do not indicate an invalid entry by displaying an alert or undoing the change the user made. Both of these methods are particularly disruptive for focus-follows-mouse users, for whom focus may leave the control more often than it does for a click-to-focus user.

### Explicit apply windows

If most of the controls in your window are not suitable for instant apply, consider making the whole window "explicit apply". An explicit apply window has these three buttons in its button box, plus an optional Help button:

-   Apply

`     Applies all the settings in the window, but does not close the window in case the user wishes to change their mind.`

-   Cancel

`     Resets all settings in the window to those that were in force when the window was opened. Note: this must undo the effects of all applications of the Apply since the window was opened, not just the most recent one.`

-   OK

`     Applies all settings in the window, and closes the window.`

Figure 3-5 Buttons in an explicit apply window

### Default Buttons

When designing a dialog or utility window, you can assign the Return key to activate a particular button in the window. GNOME indicates this button to the user by drawing a different border around it. For example, the OK button in Figure 3-5.

Choose the default button to be the most likely action, such as a confirmation action or an action that applies changes in a utility window. Do not make a button the default if its action is irreversible, destructive or otherwise inconvenient to the user. If there is no appropriate button in your window, to designate as the default button, do not set one.

In particular, it is currently not recommended to make the Close button the default in an instant apply window, as this can lead to users closing the window accidentally before they have finished using it.

### Property Windows

Property windows allow the user to view and change the characteristics of an object such as a document, file, drawing, or application launcher. Figure 3-6 Example of a property window Title Format:

Object Name Properties Window Commands:

Close, Minimize, Roll-up/Unroll Buttons:

Place a Close button in the lower right corner. A Help may be placed in the lower left corner.

### Preferences Windows

Preferences windows allow the user to change the way an application looks or behaves. Figure 3-7 Example of a preferences window Title Format:

Application Name Preferences Window Commands:

Close, Minimize, Roll-up/Unroll Buttons:

Place a Close button in the lower right corner. A Help may be placed in the lower left corner.

#### Customizing Fonts and Colors

If your preferences window allows the user to customize fonts or colors, use the following wording and layout as a guide for these controls: Example 3-3 Recommended wording for overriding theme elements- replace with screenshot

`   (o) Use font from theme`
`   (o) Use this font: [ Font selector ]`

`   (o) Use colors from theme`
`   (o) Use these colors:`
`       Background: [ color selector ]`
`       Foreground: [ color selector ]`
`       `

The wording of the radio buttons may be more specific where required, for example, "Use monspace font from theme", or "Use background color from theme". 3.3.6. Toolboxes

A toolbox provides convenient access to a set of actions and toggles through a set of small toolbar-like buttons. Toolboxes can be used to provide a specialized group of tools to augment a toolbar containing more universal items such as Save and open. A single toolbox can be shared between multiple documents to save screen space. Figure 3-8 An example of a toolbox Title Format:

Toolboxes have no title Window Commands:

Close, Roll-up/Unroll Buttons:

Toolboxes have no buttons Resizing:

Make toolboxes resizable, but only resize by discrete toolbox item widths. In other words, the user can resize the toolbox to be one item wide, two items wide, three items wide, etc. but not one and a half items wide. Guidelines

-   Only place buttons in a toolbox that do not open another window.
-   Toolboxes are best used for modal toggle buttons that affect the operation of the mouse on the document, such as a set of buttons for choosing between paintbrush, eraser, and fill modes in a drawing application. Buttons that initiate actions upon clicking (such as a save button) are better placed in toolbars.
-   Ensure that closing a toolbox does not close or otherwise alter any primary window with which it is associated.
-   Do not place toolboxes in the system window list. Toolboxes should always remain above all primary windows with which they are associated.
-   If all primary windows associated with a toolbox are closed or minimized, hide the toolbox as well. Show the toolbox again when one of the primary windows is opened or restored.
-   Make a toolbox two items wide by default, unless it is broken into categories. Make categorized toolboxes four items wide by default.

#### Toolbox Categories

While categories may not be as visually appealing as a toolbox homogenously filled with beautiful icons, they make an unwieldy large toolbox more managable. Picking a small icon from more than fifteen other items is a difficult task. Additionally, categories allow users to hide sets of tool items that are not relevant to their current task. Figure 3-9 A large toolbox broken into categories Guidelines

-   Break toolboxes with more than sixteen items into categories. The best size for a category is between four and ten items.
-   Give each category a label (in title caps) and a collapsing arrow. Clicking the label or the arrow toggles the category between a collapsed and uncollapsed state.

Alerts
------

An alert provides information about the state of the application system, or asks for essential information about how to proceed with a particular task. It is distinct from other types of window in that it is not directly requested by the user, and usually contains a message or a question rather than editable controls. Since alerts are an unwelcome intrusion into the user's work, do not use them except where necessary to avoid potential data loss or other serious problems.

An alert has a border similar to that of a dialog, and is object modal.

An alert should not appear in the panel window list unless it is, or may be, the only window shown by an application. For example, an appointment reminder alert may be shown after the main calendar application window has been closed.

Otherwise, an alert should be raised above the application when the application window itself is selected from the window list. Figure 3-10 An example of an alert Title Format

Alert windows have no titles, as the title would usually unnecessarily duplicate the alert's primary text. This way, users can read and respond to alerts more quickly as there is less visual noise and confounding text. Resizing

Alert windows are not resizable. If the user needs to resize your alert, the text is probably not concise enough. Window Commands:

None Alerts must stay above their parent

Alerts do not appear in the system window list. Consequently, take care to ensure that alerts stay above their parent window. Otherwise, users will be likely to lose the alert and find your application unresponsive for no apparent reason. Modal windows should always stay above the window(s) they block.

### Alert Text

An alert may contain both primary and secondary text. The primary text briefly summarizes the situation. The secondary text provides additional information.

Make both the primary and secondary text selectable. This makes it easy for the user to copy and paste the text to another window, such as an email message. Figure 3-11 Primary and Secondary Text Placement Primary Text

The primary text provides the user with a one sentence summary of the information or suggested action. This summary should concisely contain the essential details of the problem or suggestion. Every alert has primary text, displayed in a bold font slightly larger than the default. The primary text is punctuated in 'newspaper headline' style, that is, it has no terminating period, but it may have a terminating question mark.

Denote primary text with the pango markup:

<span weight="bold"
      size="larger">Primary Text</span>

Secondary Text

Secondary text provides a more in-depth description of the problem and suggested action, including possible side effects. Secondary text can also provide information that may be helpful in allowing the user to make an informed decision. In most situations the user should only need the primary text to make a quick decision, but they may read the secondary text if they are unsure of the proper course of action, or require extra details. Secondary text is optional, but if used, place it one text line height beneath the primary text using the default font size and weight.

### Alert Buttons

Give all alerts an affirmative button that dismisses the alert and performs the action suggested in the primary text. Provide a Cancel button for all alerts displayed in response to a user actions, such as Quit. If the alert warns of a technical problem or other situation that could result in data loss, provide a Help button that provides more information on the particular situation and explains the user's options. You may also provide buttons to perform alternate actions that provide another possible solution, fix potential problems, or launch related dialogs or programs. Figure 3-12 Button ordering and placement for alerts Button Phrasing

Write button labels as imperative verbs, for example Save, Print. This allows users to select an action with less hesitation. An active phrase also fits best with the button's role in initiating actions, as contrasted with a more passive phrase. For example Find and Log In are better buttons than than Yes and OK.

-   Affirmative Button

`     Place the affirmative button in the lower right corner of the alert. The affirmative button accepts the action proposed by the alert, or simply dismisses the alert if no action is suggested (as is the case with an information alert).`

-   Cancel Button

`     If the alert was produced in response to a user action, place a Cancel button immediately to the left of the affirmative button. This provides an escape route for users to stop an action in response to new information, or just if they clicked accidentally. Clicking the Cancel button reverts the application to its state prior to the user action.`

-   Help Button

`     A Help button may be used to clarify alerts that present potentially destructive options. Place the Help button in the lower left corner of the alert. When clicked, launch a help window clarifying the situation, detailing the actions performed by the other buttons, and explaining any side-effects that each action may have.`

-   Alternate Buttons

`     Extra buttons may be used to provide alternates to the primary action proposed by the alert text. Place these buttons to the left of the Cancel button, or the affirmative button if Cancel is not present. An example of a common alternate action would be a Quit without Saving button in a save confirmation alert. This is an alternative to the primary suggested action Save and the Cancel button.`

### Spacing and Positioning Inside Alerts

Using clear, consistent spacing in alerts makes the message easier to digest and the available responses more obvious. Figure 3-13 Spacing inside an alert Guidelines

-   The border around all edges of the alert, and the space between the icon and the text, is 12 pixels.
-   The horizontal spacing between the buttons is 6 pixels.
-   Add one line break at the standard font size below both the primary and secondary text, or 24 pixels if you are using Glade.
-   Align the top of the icon with the top of the primary text.
-   Left-align the message text, for western locales.

Technical Details for Proper Layout

Create a new GtkDialog window specifying the number of buttons you wish the alert to contain (and a help button if appropriate). The GtkDialog will contain a GtkVBox with an empty upper row, and a lower row containing a GtkButtonBox with buttons in it. In the empty upper row, place a new GtkHBox. In the left column of the GtkHBox place a GtkImage. In the right column of the GtkHBox place a GtkLabel. Inside the GtkLabel place Primary Text first (using the appropriate Pango markup, see Section 3.4.1 ― Alert Text), then put two linebreaks (return), then place Secondary Text. Now change the properties for each control according to these tables: Table 3-1 Properties for the GtkDialog Property Value Title (none) Border Width 6 Type Top Level Resizable No Has Seperator No Table 3-2 Properties for the GtkVBox (included in the dialog by default) Property Value Spacing 12 Table 3-3 Properties for the GtkHBox Property Value Spacing 12 Border Width 6 Table 3-4 Properties for the GtkImage Property Value Y Align 0.00 Icon Size Dialog Table 3-5 Properties for the GtkLabel Property Value Use Markup Yes Wrap Text Yes Y Align 0.00 3.4.4. Information Alerts

Use an information alert when the user must know the information presented before continuing, or has specifically requested the information. Present less important information by other means such as a statusbar message. Figure 3-14 An information alert An information alert...

-   uses the stock information icon.
-   presents a selectable message and an OK button. The button is placed in the bottom right corner of the alert. Pressing Enter or Escape dismisses the alert.
-   may present a convenience button to give access to a relevant object. For example, a Details button in an appointment reminder alert that opens the appointment's property window. Place this button to the left of the affirmative button.

Window Commands:

Roll-up/Unroll, Minimize (if the alert has no parent window), Close

### Error Alerts

Display an error alert when a user-requested operation cannot be sucessfully completed. Present errors caused by operations not requested by the user by another means, unless the error could result in data loss or other serious problems. For example, an error encountered during an email check initiated by the user clicking a toolbar button should present an error alert. However, an error encountered in an automated periodic email check would more appropriately report failure with a statusbar message. Figure 3-15 An error alert An error alert...

-   uses the stock error icon.
-   presents a selectable message and an OK button. The button is placed in the bottom-right corner of the alert. Pressing Enter may dismiss the error alert.
-   may present a convenience button to allow immediate handling of the error. For example, a Format... button in a "This disk is not formatted" alert. Place this button to the left of the affirmative button.

Window Commands:

Roll-up/Unroll

### Confirmation Alerts

Present a confirmation alert when the user's command may destroy their data, create a security risk, or take more than 30 seconds of user effort to recover from if it was selected in error. Figure 3-16 A confirmation alert A confirmation alert...

-   uses the stock warning icon.
-   presents a selectable message and a button labelled with a verb or verb phrase describing the action to be confirmed, or labelled OK if such a phrase would be longer than three words. This button is placed in the bottom right corner of the alert.
-   presents a Cancel button that will prevent execution of the user's command. This button is placed to the immediate left of the OK or equivalent button.
-   may present an alternate action button or a convenience button. Place this button to the left of the Cancel button.

Window Commands:

Roll-up/Unroll

#### Save Confirmation Alerts

Save confirmation alerts help ensure that users do not lose document changes when they close applications. This makes closing applications a less dangerous operation. Figure 3-17 A save confirmation alert Primary Text

Save changes to document Document Name before closing?

You may replace “document” with a more appropriate description, for example “image” or “diagram” if the document in question is not primarily text. Secondary Text

If you close without saving, changes from the last Time Period will be discarded

The secondary text provides the user with some context about the number of changes that might be unsaved. Buttons

Close without Saving, Cancel, Save

When a confirmation alert is needed, present it immediately. If the user confirms closing without saving, hide the alert and the document or application window immediately, before doing any necessary internal clean-up. If the user chooses to save before closing, hide the alert immediately but show the document window until the document is saved, in case an error occurs. Then hide the document window immediately after it has been saved successfuly.

### Authentication Alerts

Authentication alerts prompt the user for information necessary to gain access to protected resources, such as their username or password. Authentication alerts are a special kind of alert because they are both routine and largely unavoidable. Every attempt should be made to retain information entered into an authentication alert as long as is possible within security constraints. Figure 3-18 An authentication alert

Guidelines

-   Use the stock authentication icon.
-   Show a labelled field for each required item of information. Suggested fields are Username and Password (in that order) where appropriate.
-   If it is secure to retain the username longer than the password, pre-fill the username field and give focus to the password field when the alert is displayed.
-   Show a button labelled with a verb or verb phrase describing the authentication action, or OK if there is no appropriate phrase or such a phrase would be longer than three words. Place this button in the bottom right corner of the alert.
-   Do not enable the OK or equivalent button until all fields that require input have been attended to by the user. Remember that not all fields may require input however, for example an empty password may be acceptable in some applications.
-   Show a Cancel button that will prevent authentication and close the alert. Place this button to the immediate left of the OK or equivalent button.
-   Place any alternative action or convenience button to the left of the Cancel button.
-   When the user presses Return in the last field, activate the default button. When the user presses Return in any other field, move focus to the next field.

Window Commands:

Roll-up/Unroll

Progress Windows
----------------

A progress window can be used to provide feedback during an operation that takes more than a few seconds. See Section 6.17 ― Progress Bars for more details about proper use of progress bars.

A progress window may appear in the panel window list if it is, or may be, the only window shown by an application. For example, the file download progress window of a web browser may remain after all the browser windows have been closed.

Otherwise, a progress window should be raised above the application when the application window itself is selected from the window list. Figure 3-19 An example of a progress window Title Format

Progress windows should have the same title as their primary text. Unlike alerts, it is expected that progress windows will be present in the window list and may be active for extended periods. Resizing

Progress windows should be resizable if they contain non-static information the user may want to copy (for example, the source URL in a download progress window). Otherwise they should not be resizable. Guidelines

-   It is often better to use the progress bar contained in many primary windows' statusbar rather than a progress window. See Section 7.4.2.1.1 ― Progress Windows vs. the Statusbar for details on choosing between the two.
-   Progress windows should use primary and secondary text like an alert. See Section 3.4.1 ― Alert Text
-   The progress bar text should provide an idea of how much work has been completed. It is better to provide specific information rather than a unitless percentage. For example, "13 of 19 images rotated" or "12.1 of 30 MB downloaded" rather than "13% complete".
-   If possible, an estimate of the time left until the operation is complete should also be included in the progress bar text. Indicate that the "time left" is an estimate using the word "about".
-   Immediately beneath the progress bar, place italicized text indicating the current sub-operation being performed. This might be a step in a sequence, "Contacting control tower for permission to land", or it could be the current object being operated on in a bulk operation, "Rotating MonaLisa.png", "Rotating StarryNight.png".
-   If the operation in progress is potentially hazardous (destructive, costly, etc) or heavily taxes a limited resource for more than ten seconds (network bandwidth, hard disk, CPU, etc), consider placing a Pause toggle button to the right of the Cancel button. When paused, the italicized current sub-operation text should have " (Paused)" appended. This will allow users to perform important tasks requiring that resource, or give them time to think whether they want to procede with a dangerous operation they inadvertantly triggered.

Figure 3-20 A progress window for a file copy operation

### Checklist Windows

Occasionally a procedure is comprised of a series of user performable actions. In these cases, particularly when it is desirable that the user acquire some familiarity with the actions involved in a procedure, checklist windows may be used. Example 3-4 Firewall Setup Wizard

A personal firewall setup wizard might install the firewall package, add entries for the firewall to /etc/xinetd.conf, restart the internet super-daemon, and configure the user's web browser to operate through the firewall. It may be desirable that the user is exposed the series of actions involved in setting up the firewall to increase the chances that they will be sucessful in making modifications later, if they so desire. Figure 3-21 An example checklist window (Ready to Start) Figure 3-22 An example checklist window (In Progress) Figure 3-23 An example checklist window (Completed) Guidelines

-   If knowing the series of steps in an operation isn't that useful to the user, just use a regular progress window. Remember that you are probably more interested in the information than most users, many of whom will find the technical steps confusing rather than helpful.
-   Unlike regular progress windows, checklist windows should not close automatically when the operation is complete and should require explicit user input before they begin. This is because one of their purposes is to inform the user concerning an operation's contingent steps.
-   The progress bar indicates progress in the overall operation, not each step. While this is more difficult to program, it is the information most useful to the user. Just estimate how long each of the steps takes relative to each other and assign each step a fixed ratio of the progress bar's progress accordingly.
-   Do not use a checklist window for a series of internal programmatic steps, use a regular progress window. For example "Connect to mail server", "Authenticate with mail server", "Download messages", "Disconnect" would not be an appropriate series of steps for a checklist window, but would be appropriate sub-operation steps for a regular progress window.

Dialogs
-------

A dialog provides an exchange of information, or dialog, between the user and the application. Use a dialog to obtain additional information from the user that is needed to carry out a particular command or task.

A dialog should not appear in the panel window list. Any open dialogs should be raised above the application when the application window itself is selected from the window list. Figure 3-24 An example of a dialog Title Format:

Name of command that opened the dialog (without any trailing ellipsis) Window Commands:

Minimize, Roll-up/Unroll Buttons:

Follow the guidelines for Alert buttons, see Section 3.4.2 ― Alert Buttons.

Your dialog may specify a default button, that is activated when the user presses the Return key. See Section 3.3.3 ― Default Buttons for guidance on choosing an appropriate default button.

### Additional Buttons

You can include other buttons in a dialog's main button area in addition to the affirmative button and Cancel, but any more than one or two such buttons will make the dialog appear complicated and difficult to use. As with any other button, keep the labels as concise as possible to minimize this effect. Guidelines

-   Place buttons that apply to the dialog as a whole in the main button area row at the bottom of the dialog, to the left of the Cancel button.
-   Place buttons that apply to one or a few controls next to their associated controls. For instance, place a Browse... button at the trailing edge of the text field it fills in.

### Layout

A clean, logical dialog layout helps the user to quickly understand what information is required from them. Guidelines

-   Arrange controls in your dialog in the direction that people read. In western locales, this is generally left-to-right, top-to-bottom. Position the main controls with which the user will interact as close to the upper left corner as possible. Follow similar guidelines for arranging controls within groups in the dialog, and for specifying the order in which controls are traversed using the Tab key.
-   When opening a dialog, provide initial keyboard focus to the component that you expect users to operate first. This focus is especially important for users who must use a keyboard to navigate your application.
-   Provide and show sensible default values for as many of the controls in your dialog as possible when it is opened, so the user does not have to generate the information from scratch. These defaults may come from system settings (for example, hostname or IP address), or from information that the user has previously entered in this or another application (for example, email address or network proxy).

See Chapter 8 ― Visual Design for more detailed information on arranging controls in dialogs.

See Section 6.16 ― Tabbed Notebooks for information on using tabbed notebook controls in dialogs.

### Common Dialogs

The gtk and GNOME libraries provide standard dialogs for many common tasks, including opening and saving files, choosing fonts and colors, and printing. Always use these when the user is performing one of these tasks. You may modify the dialogs to reflect the needs of your particular application (for example, adding preview Play and Stop buttons to the Open File dialog in an audio application), but do not change or remove features so much as to make them unrecognizable.

Assistants
----------

An assistant is a secondary window that guides the user through an operation by breaking it into sequential steps. Assistants are useful for making complex operations less intimidating, as they restrict the information visible to the user at any given moment.

Because assistants provide a relatively small number of controls on the screen at any given time, they have sufficient space for inline documentation. Therefore, do not include a Help button in an assistant window. If you cannot make an operation sufficiently clear in an assistant without resorting to a Help button, you need to simplify it further.

Assistants do have major downsides. After using an assistant it is often hard to figure out where the individual settings aggregated into the assistant are stored. Often people will resort to re-running the assistant, re-entering many settings that they don't want to change.

Assistants are often used in situations where a better solution would be to simplify, or even better automate, the process. Before using an assistant to step people through a complex operation, consider if the operation can be fundamentally simplified so an assistant is unnecessary. Window Commands:

Close, Minimize/Unminimize, Roll-up/Unroll

### Introductory Page

The first page provides the user with the "big picture". Place the title of the assistant in the window's title bar and the assistant's title area, along with an optional picture. Beneath this, state the goal of the assistant, and, if it is not obvious, where the user can find the information the assistant will be asking for. Title Format:

Assistant Title Buttons:

Cancel, Forward Figure 3-25 Example of the first page of an assistant

### Content Pages

Content pages contain the actual settings of the assistant. Summarize the type of setting present on each content page in its title area. For example, Mail Server. Title Format:

Assistant Title - (Current Page of Total Pages) Buttons:

Cancel, Back, Forward

### Last Page

The last page should summarize the settings that will be changed by the assistant, and how the user can modify them later. Title Format:

Finish Assistant Title Buttons:

Cancel, Back, Finish

Menus
=====

Menus present the whole range of an application's commands to the user, and often a subset of its preferences. When designing a new application, place common menu items in the same locations as they appear in other applications, as this makes it much easier for the user to learn.

In most applications, only primary windows should have a menubar. Utility windows and dialogs should be simple enough that their functions can be provided by controls such as buttons placed within the window.

Occasionally, however, a utility window or dialog is so complex that there would be too many such controls. In this case, you may use a menubar provided that:

-   the menus follow the same standard layout as described in Section 4.4 ― Standard Menus
-   the window does not include a dialog button area or any buttons that dismiss it, such as OK, Close or Cancel. Place these commands on the File menu or equivalent instead.

Guidelines

-   Label menu items with verbs for commands and adjectives for settings, according to the rules in Section 8.3.2 ― Capitalization.
-   Make a menu item insensitive when its command is unavailable. For example, the Edit ▸ Copy item, which issues the command to copy selected data to the clipboard, should not be active when there is no data selected.
-   Provide an access key for every menu item. You may use the same access key on different menus in your application, but avoid duplicating access keys on the same menu. Note that unlike other controls, once a menu is displayed, its access keys may be used by just typing the letter; it is not necessary to press the Alt key at the same time.
-   Design your menu structure to avoid more than one level of submenus. Deep menu hierarchies are harder to memorize and physically difficult to navigate.
-   Do not have menus with less than three items on them (except the standard Help menu, which has only two items by default). If you have a submenu with fewer than three items on it, move them into their parent menu. If you have a top-level menu with fewer than three items on it, find another suitable menu to add them to, or find suitable items from other menus to add to it.

The Menubar
-----------

Figure 4-1 A typical menubar

The menubar provides a number of drop-down menus. Only the menu titles are displayed, until the user clicks on one of them.

The menubar is normally visible at all times and is always accessible from the keyboard, so make all the commands available in your application available on the menubar. Full screen mode

When your application is running in full screen mode, hide the menubar by default. However, make its menus and items accessible from the keyboard as usual. Pressing ESC should cause the application to leave full screen mode. A Leave Fullscreen button should be placed in the upper right hand corner of the window. The button should disappear after the mouse is unused for 5 seconds, and should appear again when the moused is moved. Alternately, in applications where the mouse is used frequently in full screen mode, all but a two pixel row of the button may be slid off the top of the screen. The button should slide back on the screen when the mouse moves near it. Guidelines

-   Provide a menubar in each primary application window, containing at least a File and a Help menu.
-   Organize menu titles in the standard order— see Section 4.4 ― Standard Menus
-   Do not disable menu titles. Allow the user to explore the menu, even though there might be no available items on it at that time.
-   Menu titles on a menubar are single words with their first letter capitalized. Do not use spaces in menu titles, as this makes them easily-mistaken for two separate menu titles. Do not use compound words (such as WindowOptions) or hyphens (such as Window-Options) to circumvent this guideline.
-   Do not provide a mechanism for hiding the menubar, as this may be activated accidentally. Some users will not be able to figure out how to get the menu bar back in this case.

Types of Menu
-------------

### Drop-down Menus

Figure 4-2 A typical drop-down menu

A drop-down menu appears when the user clicks on its title in a menubar, or focuses the title and presses Return. Guidelines

-   Only place items on a menu that relate to that menu's title.
-   Organize menu items in the standard order— see Section 4.4 ― Standard Menus. For application-specific items where there is no standard order, arrange in numerical or other logical order (for example, 50%, 100%, 200%), task order (for example, Compile followed by Debug) or by expected frequency of use.
-   Limit top-level menus to a maximum of about 15 items. If you have any more items than this, consider moving a functionally-related subset of the items into a submenu or a new top-level menu.
-   Do not add or remove individual menu items while the application is running, make them insensitive instead. Entire menus may be added or removed from the menubar at runtime, however, for example in component-based applications.
-   Immediately update menu items that are edited directly or indirectly by the user, such as those on the Open Recent submenu and the Bookmarks menu.

### Submenus

Figure 4-3 A drop-down menu with a submenu

A submenu appears when the user clicks its title, which is indicated by a small arrow symbol beside its label. You can save space on long menus by grouping related commands onto a single submenu. Guidelines

-   Use submenus sparingly, as they are physically difficult to navigate and make it harder to find and reach the items they contain.
-   Do not create submenus with fewer than three items, unless the items are added dynamically (for example the File ▸ New Tab submenu in gnome-terminal).
-   Do not nest submenus within submenus. More than two levels of hierarchy are difficult to memorize and navigate.

### Popup Menus

Figure 4-4 A popup menu for a mail folder

Popup menus provide shortcuts to those menu items that are applicable only to the currently selected object. As such, they are sometimes known as "context menus" or "shortcut menus". A popup menu is shown when the user right-clicks on an object, or selects the object and presses Shift+F10.

Be aware that popup menus are used primarily by intermediate and advanced users. Even some users who have used graphical desktops for many years do not know about popup menus until somebody shows them. Guidelines

-   Provide a popup menu for every object, selectable part, and text input target such as entry fields.
-   Provide an access key for each item. However, to enhance their spatial efficiency and readability, do not show keyboard shortcuts in popup menus.
-   Since the user may not be aware of their presence, do not provide functions that are only accessible from popup menus unless you are confident that your target users will know how to use popup menus.
-   Order items on a popup menu as follows:

`         o the double-click action for object, when it exists`
`         o other commands and settings in expected frequency-of-use order`
`         o transfer commands such as Cut, Copy, and Paste`
`         o Input Methods, where applicable. Input Methods is provided by GTK+ for supporting alternatives to the keyboard for input (such as used for Japanese, Chinese, and some accessibility technologies).`

-   Popup menus need to be as simple as possible to maximize their efficiency. Do not place more than about ten items on a popup menu, and do avoid submenus.

Designing a Menu
----------------

### Grouping Menu Items

Figure 4-5 Items grouped on a menu with separators

Menu separators are the horizontal dividing lines that visually separate groups of related items on a drop-down menu, submenu, or popup menu. For example, the separators in Figure 4-5 divide the menu into five functionally-related groups. Good use of separators helps to "chunk" the information on a menu and make it easier to scan and memorize. Guidelines

-   The best size for a group is around 2-5 items. Single-item groups are best placed at the top or bottom of a menu, otherwise try to group them with other single items of the same type on the same menu.
-   Order items within a group logically, numerically, in task order or by expected frequency of use, as appropriate.
-   Only place one type of menu item in each group— command, mutable, check box or radio button. For example, do not place commands (such as View ▸ Reload) and settings (such as. View ▸ Toolbar) in the same group.

### Types of menu item

#### Command Items

Figure 4-6 A group of command items on a menu

Command items are menu items that initiate a command or perform an action, such as Save, Print or Quit. They may act on the currently active document in a document based application, or on the application itself. Guidelines

-   Provide a keyboard shortcut for standard or frequently used command items. See Section 10.2.3 ― Choosing Shortcut Keys for more information on choosing shortcut keys.
-   Do not remove command items from the menu when they are unavailable, make them insensitive instead. This allows the user to infer what functionality the application provides even if it is not currently available, and keeping the menu structure static makes it easier to memorize.
-   Label the menu item with a trailing ellipsis ("...") only if the command requires further input from the user before it can be performed. Do not add an ellipsis to items that only present a confirmation dialog (such as Delete), or that do not require further input (such as Properties, Preferences or About).

#### Mutable Command Items

A mutable command item changes its label when selected. For example, View ▸ Reload in a browser may change to Stop to allow the user to interrupt the operation if it is taking a long time.

Note that mutable menu items can be problematic because the user never sees the menu item changing, so it is not obvious that a different function has become available. Guidelines

-   If your mutable menu items are command items, and you have sufficient space on your menu, consider providing two adjacent menu items for the commands instead. Then make the items sensitive or insensitive as the situation demands. This also makes it easier for the user to tell when different shortcuts are available for each of the commands, for example Ctrl+R for Reload, and Esc for Stop.
-   Do not use mutable menu items to toggle a two-state setting (for example, Show Toolbar and Hide Toolbar). Present such items as a single check box item instead.

#### Checkbox Items

Figure 4-7 A group of check box items on a menu

A check box menu item shows the current state of a two-state setting, and allows the user to toggle it by selecting the menu item. Guidelines

-   Use a check box menu item only when it is obvious from the label what the set and unset states mean. This usually means that the two states are logical or natural opposites, such as "on" and "off". If this is not the case, use two radio button items instead.
-   Never change the label of a check box menu item in response to the user selecting the item.

#### Radio Button Items

Figure 4-8 A group of radiobutton items on a menu

Radio button menu items show which of two or more mutually-exclusive settings are currently selected, and allow the user to choose a different setting by selecting its menu item.

-   If you need to offer a choice of two mutually-exclusive settings to the user, use a group of two radio button items instead of a single check box menu item if the settings are not clearly opposites. For example, represent View as Icons and View as List as two radio button items.
-   Never change the label of a radio button menu item in response to the user selecting or deselecting the item.

Standard Menus
--------------

Most applications have many functions in common, such as Cut, Copy, Paste and Quit. To aid learning and memorability, these menu items, and the menus on which they appear, must appear with the same labels and in the same order in every application. The same commands must also behave the same way in different applications, to avoid surprising the user.

This section details the most common menus, menu items and their behaviors. You will not need all of these menus or menu items in every application you write, but do preserve the order of the menu titles and of the menu items that you do use. Guidelines

-   Place application-specific menus after the Format menu and before the Go menu
-   Place application-specific menu items towards the middle of a standard menu, unless they logically fit with one of the standard groups already on the menu.

Figure 4-9 A menubar showing all the standard menu titles in their correct order

### File

The File menu contains commands that operate on the current document. It is the left-most item in the menubar because of its importance and frequency of use, and because it is a relevant menu in many applications. Historically, because most applications already had this menu, and because the distinction between closing documents and closing windows became blurred over time, the File menu has also become the standard location for Quit.

The items on the File menu are generally ordered by locality, closest first. That is, items to save or load from file, followed by printing, followed by sending to a remote user. Try to maintain this ordering if you have to add new items to the menu.

If your application does not operate on documents, name this item for the type of object it displays. For example, many games should have a Game instead of a File menu. However, place the Quit menu item last on this menu nonetheless. Figure 4-10 A generic File menu

#### Creation and Opening Operations

Table 4-1 Creation and Opening operation menu items Label Shortcut Description New Ctrl+N Creates a new document. Open a new primary window, with the title Document name, containing a blank document. How this window is displayed, e.g. as a tab or a separate window, is up to the window manager.

If your application can create a number of different types of document, you can make the New item a submenu, containing a menu item for each type. Label these items New document type, make the first entry in the submenu the most commonly used document type, and give it the Ctrl+N shortcut.

Note: A blank document will not necessarily be completely blank. For example, a document created from a template may already contain some data. Open... Ctrl+O Opens an existing document in a new window. Present the user with a standard Open File dialog from which they can choose an existing file. If the chosen file is already open in the application, raise that window instead of opening a new one.

#### Saved State Operations

Table 4-2 Saved State Operation menu items Label Shortcut Description Save Ctrl+S Saves the document with its current filename. If the document already has a filename associated with it, save the document immediately without any further interaction from the user. If there are any additional options involved in saving a file (eg. DOS or UNIX-style line endings in a text file), prompt for these first time the document is saved, but subsequently use the same values each time until the user changes them. If the document has no current filename or is read-only, selecting this item should be the same as selecting Save As. Save As... Shift+Ctrl+S Saves the document with a new filename. Present the user with the standard Save As dialog, and save the file with the chosen file name. Save a Copy... None Prompts the user to enter a filename, with which a copy of the document is then saved. Do not alter either the view or the filename of the original document. All subsequent changes are still made to the original document until the user specifies otherwise, for example by choosing the Save As command.

Like the Save As dialog, the Save a Copy dialog may present different ways to save the data. For example, an image may be saved in a native format or as a PNG. Revert None Reverts the document to the last saved state. Present the user with a warning that all changes will be lost, and offer the option of cancelling before reloading the file. Save Version... None An alternative to the Save a Copy command. Only use this item in conjunction with the Restore Version. command. Restore Version... None Prompts the user for a version of the current document to be restored. Present the user with with a warning that all changes will be lost, and offer the option of cancelling before restoring the version. Only use this item in conjunction with the Save Version command. Versions... None An alternative to the Save Version and Restore Version commands. Use this when more utilities, such as a diff, are available.

#### Export Operations

Table 4-3 Export Operation menu items Label Shortcut Description Page Setup None Allows the user to control print-related settings. Present the user with a dialog allowing the user to set such options as portrait or landscape format, margins, and so on. Print Preview Shift+Ctrl+P Shows the user what the printed document will look like. Present a new window containing an accruate represenation of the appearance of the document as it would be printed. The libgnomeprintui library provides a standard Print Preview window that you should use if possible. Print... Ctrl+P Prints the current document. Present the user with a dialog allowing them to set options like the page range to be printed, the printer to be used, and so on. The dialog must contain a button labelled Print that starts printing and closes the dialog. The libgnomeprintui library provides a standard Print dialog that you should use if possible. Send To... Ctrl+M Provides the user a means to attach or send the current document as an email or email attachment, depending on its format. You may provide more than one Send item depending on which options are available. If there are more than two such items, move them into a submenu. For example, if only Send by Email and Send by Fax are available, leave them on the top-level menu If there is a third option, such as Send by FTP, place all the options in a Send submenu.

#### File Properties

Table 4-4 Properties menu items Label Shortcut Description Properties Alt+Return Opens the document's Properties window. This may contain editable information, such as the document author's name, or read-only information, such as the number of words in the document, or a combination of both. The Alt+Return shortcut should not be provided where Return is most frequently used to insert a new line.

#### Closing Operations

Table 4-5 Closing Operation menu items Label Shortcut Description Close Ctrl+W Closes the current document. If it has unsaved changes, present the user with a confirmation alert giving the option to save changes, discard them, or cancel the action without closing or saving the document.

If the window you are closing is the last open document in the application, the correct action depends on your application type:

-   Single document interface: close the application
-   Controlled single document interface: leave only the control window open
-   Multiple document interface: close the current document and create a new blank document

Quit Ctrl+Q

Closes the application. If there are unsaved changes in any open documents, present the user with a confirmation alert for each affected document, giving the option to save the changes, discard them, or cancel. If there are no unsaved changes, close the application immediately without presenting any further messages or dialogs.

In particular, non-document based applications, for example a game or a calculator, should save their state and exit immediately. This state should be restored the next time the application is started.

### Edit

The Edit menu contains items relating to editing both the document (clipboard handling, search and replace, and inserting special objects) and the user's preferences. Preferences are edited here rather than on a Settings menu, because:

-   most applications' preferences windows are accessed via a single menu tem, and single-item menus offer poor usability
-   most applications already contain a suitable Edit menu.

Figure 4-11 A generic Edit menu

#### Modification History

Document-based applications should maintain a history of modifications to a document and the state of the document between each action. The Undo and Redo commands move backwards and forwards through this history. Table 4-6 Modification History menu items Label Shortcut Description Undo action Ctrl+Z Undoes the effect of the previous action in the undo history list. Revert the document to its state before the previous action was performed. If your application supports undo, and the user undoes all changes since it was last saved, treat the document as unmodified. Note: provide a separate Undo and Redo menu item even if your application only supports one level of undo. Redo action Shift+Ctrl+Z Performs the next action in the undo history list, after the user has moved backwards through the list with the Undo command. Move the user one step forwards again, restoring the document to the state it was in after that action was originally performed.

Note: provide a separate Undo and Redo menu item even if your application only supports one level of undo.

#### Manipulating Selected Data

Table 4-7 Selected Data Manipulation menu items Label Shortcut Description Cut Ctrl+X Removes the selected content and places it onto the clipboard. Visually, remove the content from the document in the same manner as Delete. Copy Ctrl+C Copies the selected content onto the clipboard. Paste Ctrl+V Inserts the contents of the clipboard into the document. If there is no current selection, use the caret as the insertion point. If there is a current selection, replace it with the clipboard contents. Paste Special... Shift+Ctrl+V Inserts a non-default representation of the clipboard contents into the document. Open a dialog presenting a list of the available formats from which the user can select. For example, if the clipboard contains a PNG file copied from a file manager, the image may be embedded in the document, or a link to the file inserted so that changes to the image on disk are always reflected in the document. Duplicate Ctrl+U Creates a duplicate copy of the selected object. Do not prompt for a name for the duplicate object, but give it a sensible default (for example, Copy of ShoppingList.abw) and allow the user to change it later. Place the duplicate copy as near the original as possible without overlapping it, even if this means breaking the current sort order within the container, so the user sees it immediately. Delete Delete Removes the selected content without placing it on the clipboard. Select All Ctrl+A Selects all content in the current document. Deselect All Shift+Ctrl+A Deselects all content in the current document. Only provide this item in situations when no other method of undoing selection is possible or apparent to the user. For example, in complex graphics applications where selection and deselection is not usually possible simply by using the cursor keys. Note: Do not provide Deselect All in text entry fields, as Shift+Ctrl+hex digit is used to enter unicode characters so its shortcut will not work.

#### Searching and Replacing

Table 4-8 Search and Replace menu items Label Shortcut Description Find... Ctrl+F Opens a window or dialog allowing the user to search for specific content in the current document. Highlight each match in-place. If the command allows the user to search for content in places other than the current document, for example other open documents, other documents on disk, or a remote network location, label this item Search instead of Find. Find Next Ctrl+G Selects the next instance of the last Find term in the current document. Find Previous Shift+Ctrl+G Selects the previous instance of the last Find term in the current document. Replace... Ctrl+H Opens a window or dialog allowing the user to search for specific content in the current document, and replace each occurrence with new content.

#### Inserting Special Objects

Where applicable, provide items on the Edit menu that insert special objects such as images, links, GUI controls or the current date and time.

If you have up to three types of object that can be inserted, add them as individual items to this menu, for example Insert Image, or Insert External Link. If you have between three and six types, place them on an Edit ▸ Insert submenu. If you have more than six, add a separate Insert menu to the menubar.

#### User Preferences

Table 4-9 User Preferences menu items Label Shortcut Description Preferences None Opens a preferences window allowing the user to change preferences for the whole application. Changes will apply to all running and subsequent instances of the application.

### View

The View menu contains only items that affect the user's view of the current document. Do not place any items on the View menu that affect the the content of the current document. (Exception: View ▸ Reload may change the current contents if, for example, the document is a webpage that has been recently updated on the server). Figure 4-12 A generic View menu

#### Toolbar and Statusbar

Table 4-10 Toolbar and Statusbar menu items Label Shortcut Description Toolbar None Shows or hides the application's toolbar. This is a check box menu item. Include this item in every application that has a single toolbar. See Section 5.2 ― Controlling Display and Appearance for information on how to deal with multiple toolbars.

#### Content Presentation

Table 4-11 Content Presentation menu items Label Shortcut Description Icons None Shows the contents of the selected container as rows and columns of large icons, each with its name underneath. This is a radio button menu item. List None Shows the contents of the selected container as a list of small icons, possibly in multiple columns, each with its name on its right-hand side. This is a radio button menu item. Details None Shows the contents of the selected container as single column of small icons, each with its name on its right-hand side. Additional columns give extra information about the object each icon represents, for example the size and modification date of files in a file manager. This is a radio button menu item.

If your application has no need for both List and Details modes, use the List item for whichever of the two modes you support. Sort By... None Sorts the contents of an container by user-specified criteria. Open a dialog allowing the user to choose from pre-defined sort keys (for example, Name, Size, or Modification Date in a file manager), or to specify their own if applicable. Filter... None Hides objects that are not of interest to the user. Open a dialog allowing the user to choose from a list of types of object they want to display, or to enter their own criteria (for example, a regular expression matched against a particular property of the objects). Zoom In Ctrl++ Zooms into the document. Make the center of the new view the same as the center of the previous view. Zoom Out Ctrl+- Zooms out of the document. Make the center of the new view the same as the center of the previous view. Normal Size Ctrl+0 Resets the zoom level back to the default value, normally 100%. Make the center of the new view the same as the center of the previous view. Best Fit None Makes the document fill the window. Show the document, or the current page of the document, at as high a zoom level as will fit in the window whilst allowing the whole document or page to be visible without scrolling. Refresh Ctrl+R Redraws the current view of the document from local storage. For example, in a web browser application, this would redraw the page from the browser page cache. Reload Ctrl+R Redraws the current view of the document, checking the data source for changes first. For example, checks the web server for updates to the page before redrawing it. If your application requires both Reload and Refresh, use Shift+Ctrl+R as the shortcut for Reload.

### Insert

The Insert menu lists the type of special objects that can be inserted into the document at the current caret position, for example images, links, page breaks or GUI objects. Only provide this menu if you have more than about six types of object that can be inserted, otherwise place individual items for each type on the Edit menu. Figure 4-13 A generic Insert menu

The types of object will vary between applications, but the table below shows some common types that may be applicable. Table 4-12 Insert menu items Label Shortcut Description Page Break None Inserts a page break at the caret position. Show the page break visually, for example as a dotted line across the page, unless the user has specifically requested not to see them. Date and Time... None Inserts the current date and/or time at the caret position. Open a dialog giving a choice of date and time formats. If applicable, also offer the choice to insert either as plain text, so the specified date and time will always appear in the document, or as a special field that will updated every time the document is opened, refreshed or printed. Symbol... None Inserts a special symbol, such as a mathematical symbol or foreign character, at the caret position. Open a dialog showing all the available symbols as a table, from which the user can choose. The user must be able to add multiple symbols to the document at one time without having to close and re-open the dialog. Sheet... None Adds a new sheet to the current workbook. Do not prompt for a name, but choose a sensible default (such as Sheet-2) and allow the user to change it later. Rows... None Adds new rows to a table in which one or more rows or cells are currently selected. Open a dialog asking whether to insert rows above or below the current selection, and for any other required information. Copy the row format from the last or first row of the current selection respectively, unless the user specifies otherwise. Columns... None Adds new columns to a table in which one or more columns or cells are currently selected. Open a dialog asking whether to insert columns to the left or right of the current selection, and for any other required information. Copy the column format from the right- or left-most column of the current selection respectively, unless the user specifies otherwise. Image... None Inserts an image into the document from a file. Present a standard Open File dialog filtered on acceptable file types, from which the user can choose an image file to insert. Graph... None Inserts a graph into the document. Open a dialog or assistant that allows the user to build (or open from a file) a graph of their choice, using the current selection as an indication of which values, axis labels and data labels to use. From FIle... None Inserts an object from any acceptable file type, for example plain text, formatted text, or an image. Present a standard Open File dialog filtered on acceptable file types, from which the user can choose a file to insert. External Link... None Inserts a link to an object stored in a different file, or on a remote system. The object is not embedded in or saved with the document, only a link to it. Open a dialog in which the user can type or choose the name of the object, for example a filename or a webpage URL. Show the link in the document in as informative way as possible. For example, show a link to an image as a thumbnail of that image, unless the user specifies otherwise.

### Format

A Format menu contains commands to change the visual appearance of the document. For example, changing the font, color, or line spacing of a text selection.

The difference between these commands and those on the View menu is that changes made with Format commands are persistent and saved as part of the document, for example as HTML or RTF tags. Figure 4-14 A generic Format menu

Items found on the Format will be very application-specific, but some common items are listed in the table below. Table 4-13 Format menu items Label Shortcut Description Style... None Sets the style attributes of the selected text or objects either individually or to a named, predefined style. Open a dialog allowing the user to set attributes such as bold, italic, size and spacing individually, and to create their own named styles where applicable. Font... None Sets the font properties of the selected text or objects. Open a dialog allowing the user to choose font, size, style, color, or whatever other attributes are applicable. Paragraph... None Sets the properties of the selected paragraph. Open a dialog allowing the user to choose style, line spacing, tabulation, or whatever other attributes are applicable. Bold Ctrl+B Toggles the boldness of the current text selection on or off. If some of the selection is currently bold and some is not, this command should bolden the selected text. Italic Ctrl+I Toggles the italicisation of the current text selection on or off. If some of the selection is currently italicised and some is not, this command should italicise the selected text. Underline Ctrl+U Toggles underlining of the current text selection. If some of the selection is currently underlined and some is not, this command should underline the selected text. Cells... None Sets the properties of the selected table cells. Open a dialog allowing the user to choose alignment, borders, shading, text style, number format, or whatever other attributes are applicable. List... None Sets the properties of the selected list, or turns the selected paragraphs into a list if they are not already formatted as such. Open a dialog allowing the user to choose number or bullet style, spacing, tabulation, or whatever other attributes are applicable. Layer... None Sets the properties of all or selected layers of a multi-layered document. Open a dialog allowing the user to choose name, size, visibility, opacity, z-ordering, or whatever other attributes are applicable. Page... None Sets the properties of all or selected pages of the document. Open a dialog allowing the user to choose paper size, orientation, columns, margins, or whatever other attributes are applicable.

### Bookmarks

Provide a Bookmarks menu in any application that allows the user to browse files and folders, help documents, web pages or any other large information space. Icons

Show icons for bookmark entries on the Bookmarks menu that indicate the type of the bookmark, even if the user has globally turned off icons for other menu items on the desktop. Figure 4-15 A generic Bookmarks menu Table 4-14 Bookmark menu items Label Shortcut Description Add Bookmark Ctrl+D Adds a bookmark for the current document to the default bookmark list. Do not pop up a dialog asking for a title or location for the bookmark, instead choose sensible defaults (such as the document's title or filename as the bookmark name) and allow the user to change them later using the Edit Bookmarks feature. Edit Bookmarks Ctrl+B Allows the user to edit the application's bookmark list. Open a window in which the user can arrange bookmarks into a hierarchy, move, copy, and delete bookmarks, and change their properties. Bookmark List None The user's current list of bookmarks for the application.

### Go

A Go menu provides commands for quickly navigating around a document or collection of documents, or an information space such as a directory structure or the web.

The contents of the menu will vary depending on the type of application. Different standard menus are presented here for browser-based and document-based applications , but your application may require a combination of both. Figure 4-16 A generic Go menu for a browser application Table 4-15 Go menu items for a browser application Label Shortcut Description Back Alt+Left Navigates to the previous document in the browser's history list. Forward Alt+Right Navigates to the next document in the browser's history list. Up Alt+Up Navigates to the current document's (or folder's) parent document (or folder). For a document browser, such as an online help viewer, this usually means navigating to the enclosing sub-section, section, chapter or contents page. Home Alt+Home Navigates to a starting page defined by the user or the application. Location... Ctrl+L Navigates to a user-specified URI. Open a dialog into which the user can type a suitable URI, or select one from a list where applicable (for example, a file selection dialog for applications that can handle <file://> URIs). Figure 4-17 A generic Go menu for document-based applications Table 4-16 Go menu items for a document-based application Label Shortcut Description Previous Page PageUp Navigates to the previous page in the document. Next Page PageDown Navigates to the next page in the document. Go to Page... None Navigates to a user-specified page number. Open a dialog into which the user can type a page number. Text-based applications may also include a Go to Line... menu item, which allows the user to jump to a specified line number. First Page Ctrl+Home Navigates to the first page in the document. Last Page Ctrl+End Navigates to the last page in the document. 4.4.8. Windows

The Windows menu contains commands that apply to all of the application's open windows. Only use a Windows menu in multiple document interface (MDI) applications. MDI Applications

The use of MDI is discouraged, as they have a number of inherent usability problems.

You may also label this menu Documents, Buffers, or similar according to the type of document handled by your application.

The last items on this menu are a numbered list of the application's primary windows, for example 1shoppinglist.abw. Selecting one of these items raises the corresponding window. Figure 4-18 A generic Windows menu Table 4-17 Windows menu items Label Shortcut Description Save All None Saves all open documents. If any documents have no current filename, prompt for a filename for each one in turn using the standard Save dialog. Close All None Closes all open documents. If there are any unsaved changes in any documents, post a confirmation alert for each one in turn. 1. first open window title

2. second open window title

etc.

`   None    Raises the corresponding window to the top of the window stack.`

### Help

The Help menu provides access to all online documentation for your application. This includes both the user guide, and the About window which includes a brief description of your application's functionality. Figure 4-19 A generic Help menu Table 4-18 Help menu items Label Shortcut Description Contents F1 Opens the default help browser on the contents page for the application. About None Opens the About dialog for the application. Use the standard dialog provided by the GNOME libraries, which contains the name and version number of the application, a short description of the application's functionality, author contact details, copyright message and a pointer to the licence under which the application is made available.

Toolbars
========

Appearance and Content
----------------------

Controlling Display and Appearance
----------------------------------

Labels and Tooltips
-------------------

Controls
========

Using Controls Effectively
--------------------------

Terminology
-----------

Sensitivity
-----------

Text Entry Fields
-----------------

Spin Boxes
----------

Sliders
-------

Buttons
-------

Check Boxes
-----------

Radio Buttons
-------------

Toggle Buttons
--------------

Drop-down Lists
---------------

Drop-down Combination Boxes
---------------------------

Scrollbars
----------

Lists
-----

Trees
-----

Tabbed Notebooks
----------------

Progress Bars
-------------

Statusbars
----------

Frames and Separators
---------------------

Feedback
========

Characteristics of Responsive Applications
------------------------------------------

Acceptable Response Times
-------------------------

Responding to User Requests
---------------------------

Types of Visual Feedback
------------------------

Choosing Appropriate Feedback
-----------------------------

Allowing Interruptions
----------------------

Visual Design
=============

Color
-----

Window Layout
-------------

Text Labels
-----------

Fonts
-----

Icons
=====

Style
-----

Kinds of Icons
--------------

Designing Effective Icons
-------------------------

Designing Accessible Icons
--------------------------

User Input
==========

Mouse Interaction
-----------------

Keyboard Interaction
--------------------

Language
========

Labels
------

Warning and Error Messages
--------------------------

Online Help
-----------

Checklists
==========

Things You Can Do Yourself
--------------------------

Things You Can Do With Other People
-----------------------------------

[Category:UMAF](/Category:UMAF "wikilink")
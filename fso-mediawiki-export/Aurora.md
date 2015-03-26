---
title: Aurora
permalink: /Aurora/
---

*Light at the end of the tunnel...* [200px|thumb|right|Aurora 0.1](/File:aurora.png "wikilink")

Description
-----------

The aim of aurora is to replace zhone and zhone2 as development UIs for FSO. From the viewpoint of a middleware architect, it's essential to have clients available that use the various features of the FSO services. In the past, FSO has been too much developed without considering how the features will actually be used by the API consumers. Zhone (and its successor Zhone2) is currently an oversimplified approach based on a non-maintainable Edje file. We have now decided to develop a new testing/demonstrator for FSO named Aurora.

User Stories
------------

At the top of every stack is the user. Pleasing him or her is the topmost priority. Technology should not stand in the way, but rather support the user. Aurora releases will be done as user milestones. The user stories for every milestone are specified [here](/Aurora/UserStories "wikilink").

Documentation
-------------

If you want to learn how aurora works,or create your own application to it,you can visit our [Documentation](/Aurora/Documentation "wikilink") page.

Technology
----------

-   The UI components of Aurora will be based on Qt's [QML](/Aurora/QML "wikilink") (Qt Markup Language) and will have parts written in C++ and Vala – It's even an interesting way to find out how to combine C++/Qt best. (Qt on Linux already bases its mainloop on the GLib mainloop, so at least that part is already solved.)
-   We will support both Qt/X11 and Qt/Embedded, the latter being useful on smaller systems, such as the OpenEZX family of devices (48MB RAM, no GFX acceleration, etc.)
-   Our flashable images will be based on [OpenEmbedded](http://www.openembedded.org), however we'd welcome people taking care of creating releases based on Debian, Gentoo, etc.

Development
-----------

-   [Architecture Overview](/Aurora/Architecture "wikilink")
-   [Information about QML](/Aurora/QML "wikilink")
-   [OpenEmbedded](/Aurora/OpenEmbedded "wikilink")
-   [How to build the Aurora distribution](/Aurora/OpenEmbedded/HowToBuild "wikilink")
-   [Announcement](/Aurora/Announcement "wikilink")
-   [Code Style](/Aurora/CodeStyle "wikilink")

Participiants
-------------

-   Simon Busch (morphis)
-   Michael Lauer (mickeyl)
-   Angelo S. Mavridis Bartolome (angelox)

How to help
-----------

-   We wrote a "formal" [announcement](/Aurora/Announcement "wikilink") to the linuxtogo mailing list smartphones-userland. For now,we are using \#openmoko-cdevel on freenode, to coordinate the project.

Roadmap
-------

-   [Version 2011.12](/Aurora/Version_2011_12 "wikilink"): Release Date: xx-12-2011
-   [Version 0.1](/Aurora/Version_0_1 "wikilink"): Release Date: 22-08-2011

Screenshots
-----------

-   We are always taking screenshots from the development of Aurora,you can check them [here](/Aurora/Screenshots "wikilink").

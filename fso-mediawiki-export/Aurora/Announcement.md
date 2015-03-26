---
title: Aurora Announcement
permalink: /Aurora/Announcement/
---

Overview
========

This page contains the annoucement text we want to publish to tell all people out there about the Aurora project and what it's about.

Target Audience
---------------

Mailinglists:

-   smartphones-userland@linuxtogo.org
-   shr-user@lists.shr-project.org
-   community@lists.openmoko.org

Text
----

    Dear FOSS-Telephony lovers,

    today we want to announce something that has been brewing in our minds for quite a while
    and will change the way we develop the freesmartphone.org middleware.

    In the past, FSO has been too much developed without considering how the features will actually be used by the API consumers.
    Apart from the great work our friends from SHR did, there has only been a handful of special purpose FSO clients, such as
    the Emacs client, Zhone, and Zhone2. Zhone (and its successor Zhone2) is currently an oversimplified approach based on a
    non-maintainable Edje file. We have therefore decided to develop a new testing/demonstrator for FSO named Aurora that
    is supposed to be the driving force for further development.

    AURORA

    The aim of Aurora is to replace zhone and zhone2 as development UIs for FSO. From the viewpoint of a middleware architect,
    it's essential to have clients available that use the various features of the FSO services. On the other hand though, this
    time we want to create something that is also suitable for day to day use. Aurora is supposed to be something we call
    a "featurephone client" – featurephones being those things we used for telephony before smartphones were invented.

    Aurora being a featurephone client does not necessarily mean it will never get the "smartphone features" Android or iOS
    are popular for, it rather describes our approach as being as-simple-as-possible. So for now you will not be able to
    install additional apps or features. Everything (you need) is part of the Aurora client.

    DEVELOPMENT PROCESS

    At the top of every application stack is the user. Pleasing him or her is the topmost priority. Technology should not stand in the
     way, but rather support the user. Hence, Aurora releases will be done as user milestones. For every user milestone, we will
    pick a number of user stories to be implemented. We will then split a user story into tasks and distribute among the contributors.

    SUPPORTED DEVICES

    We decided to only support the Palm Pre devices (Pre/Pre Plus/Pre 2) for the first to-be-released version of Aurora. More
    supported devices will join after the 0.1 release. This decision has been forced by the fact that we are only very few people
    working both on FSO and Aurora (and also on OpenEmbedded). Later on, we expect to see the OpenEZX family of devices,
    the Openmoko devices, the Nokia N900, and possibly also a bunch of HTC smartphones supported.

    TECHNOLOGY

    Some words about the technology choices we have made for Aurora. The UI components of Aurora will be based on Qt's QML
    (Qt Markup Language) and will have parts written in C++ and Vala (although we're going to use Python for prototyping as well).
    We will support both Qt/X11 and Qt/Embedded, the latter being useful on smaller systems, such as the OpenEZX family of devices
    (48MB RAM, no GFX acceleration, etc.)
    For the first release we will only provide Qt/Embedded based images for the Palm Pre devices;
    those flashable images will be based on OpenEmbedded, however we'd welcome people taking care
    of creating releases based on Debian, Gentoo, etc.

    HOW TO HELP

    Speaking about welcoming people, the major aim of this announcement is to find people who want to share this vision
    and give us a bit of a hand. We are especially lacking artists and folks who can improve our user interaction.
    Apart from the technical reasons, we chose QML to have a very low barrier of entry. QML is easy to understand
    and it also comes with a GUI design tool.

    If you are interested and share our vision, please feel free to contact us. We can then see how you can help
    us to get to the end goal (see roadmap) even faster.

    There are several possibilities to make us aware of you:

    - IRC: irc.freenode.net; channel: #openmoko-cdevel
    - Mail: smartphones-userland@linuxtogo.org
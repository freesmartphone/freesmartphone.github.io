---
title: Feb11PRDraft ES
permalink: /Feb11PRDraft/ES/
---

Comunidades de desarrolladores decididas a seguir proveyendo plataformas de software libre para sistemas empotrados.
--------------------------------------------------------------------------------------------------------------------

13 de febrero, 2011

Dado el reciente comunicado oficial del gran fabricante de dispositivos móviles que posiblemente dejará de lado sus estrategias relacionadas con el software libre y que dificultará el objetivo de una plataforma libre con una comunidad viva, los equipos de SHR/FSO/QtMoko/Replicant/Android con sus desarrolladores y usuarios están, de hecho... más vivos que nunca. Buscando seguir con nuestro objetivo a largo plazo de tener sistemas para plataformas empotradas lo más mlibres posibles, nosotros, los usuarios y desarrolladores, nos gustaria invitar a otros usuarios y desarrolladores para unirse y participen en un proyecto que no se deja arrastrar por el impredecible capricho de una administración empresarial.

Nuestra comunidad de desarrolladores ha hecho progresos firmes a lo largo de los años. El único requerimiento ha sido un hardware sólido con soporte para Linux. Y lo tenemos ahora: los teléfonos Openmoko, las nuevas Palm Pre, el Nokia N900, las HTC. Todos estos dispositivos nos proveen ahora de plataformas para el desarrollo y el aprendizaje para aquellos que buscan sistemas independientes y libres para aprender, programar o usarlos profesional y comercialmente.

Cuando un nuevo jugador aparece, puede ser una ventaja por algun tiempo, especialmente si el código se da libre y abierto, o cuando se decide financiar algun equipo que desarrolla código libre por sus creencies. Por ejemplo, la compañia Openmoko,otorgando hardware libre y abierto y financiando el desarrollo del kernel de Linux y el framework FSO, o Nokia con la plataforma Maemo/MeeGo. Pero al final, si el impulso no viene de la comunidad, cuando la financiación desaparece y el código no es lo suficiente abierto ni es bien acogido por la comunidad, o depende de parches cerrados y no libres, la plataforma cae con el fin de ese impulso.

Creemos en otro modelo que está demostrado que es sostenible y satisfactorio. Un modelo donde todos pueden contribudir con su conocimiento y aprender al mismo tiempo, sin parches propietarios, sin reuniones administrativas a puerta cerrada. Un modelo que nos permite usar hardware existente que ya tenemos incluso cuando el creador decidió abandonarlo o no piensa crear más actualitzaciones. Un modelo que permite a todos comprometerse, leer, comentar o descargar el código fuente.

Te invitamos a que mires las páginas de los proyectos de cada uno de nuestros equipos, sus resultados actuales, motivaciones y necesidad i si te inspiran, sientente libre de unirte a las listas de correo, wikis, foros, salas de IRC y, porque no, a hablar, escuchar y eventualmente contribuir para crear una plataforma empotrada libre y abierta para tus dispositivos.

### What is SHR?

SHR is a community driven distribution focusing on embedded and mobile systems. While utilizing many existing free and open source projects for the heavy lifting, such are Xorg, Enlightenement, Vala, Bluez, OpenEmbedded and others, SHR specializes in integration of these underlying architectural blocks onto existing hardware, for example the Nokia N900, Palm Pre, HTC Dream or Openmoko Neo Freerunner and Neo 1973 phones. SHR's main focus is a flexible and adoptable system with integrated FSO middleware framework for telephony, networking and other hardware management. As one of the main consumers of the FSO framework at the moment, the SHR distribution is already including basic user interface for phone calls, messaging or user settings and while fully operating telephony has been a work in progress, SHR has been enjoying a slow but steady flow of applications designed especially for embedded and mobile systems, offering web browsers, microblogging clients, games and other utilities. The SHR telephony applications, Settings application and full FSO have been included in Debian operating system.

SHR provides unstable and testing branches of it's distribution. Some people use it as their daily phone, some use it as tablets or PDAs. While we have some basic phone apps and support written in an extendable and themeable way, there certainly is a room for extending, more themes, contact sync, testing... you name it.

### freesmartphone.org, the gray eminence

Undividable part of SHR is FSO - freesmartphone.org Framework, modern and service-based middleware platform, providing extendable and customizable middleware interface. Written in a modular way it utilizes the power of D-Bus communication for plugin integration. Due to its open nature and liberal license – being mostly a community driven project – FSO is the perfect choice for research, education and also for commercial vendors with special requirements that can benefit from professional support for FSO, including, but not limited to consulting and development.

There is a long list of devices with FSO support under way, so to name a few - HTC Dream/Magic and many other HTC phones including Magician, Kaiser, Raphael, Diamond, Blackstone; the Palm Pre (Plus(2)) phones, Nokia N900, iPhone 3g, or OpenEZX family of devices with E680(i), A780, A910, A1200, ROKR E2 or ROKR E6. The Openmoko phones Freerunner and Neo 1973 have a fully working FSO support.

### QtMoko

QtMoko is a Debian-based distribution for the Openmoko Neo Freerunner and Neo 1973 cellular phones, with the user interface based on Qt Extended, formerly known as Qtopia. It's telephony subsystem has been largely utilizing the qtopiacomm library, but QtMoko is currently starting to work on a move towards FSO. This will allow integration on greater number of FSO supported devices and will also address wider developer/consumer group.

QtMoko can be used as a daily phone on the Openmoko devices with it's many applications, great themes and amazing speed.

### Replicant

Replicant is an Android-based distribution for the HTC Dream and the Nexus One that focuses on freedom: its goal is to replace the proprietary components that are usually present on the Android phones. It's now based on Cyanogen mod, but it goes further: instead of replacing the system and keeping some proprietary low level libraries (that interface with the hardware) and some proprietary higher level applications such as the market, it replaces them:

-   While Cyanogen mod like distribution replace most of the software by improved free software version, the user ends up with proprietary libraries in his images, such as the RIL (Radio Interface Library, the library which talks to the modem), or the audio libraries (dlopend libraries) in the case of the HTC Dream. Replicant replaces these libraries.
-   The user, if he chooses to, also usually end up with proprietary Google applications such as the Market, that we replaced too (with FDroid)

Replicant is now functional enough to be used in Europe (the RIL has some issues in USA and Australia).

### Android on Freerunner

Android on Freerunner is the continuation of the work initiated by Koolu. The AoF project is community driven port of Android for the Openmoko Neo Freerunner device. AoF has produced stable and fully functioning releases for Cupcake and continues to improve the quality of that distribution on the Freerunner. Cupcake on the Freerunner can be used as a daily phone. At the same time, Froyo is being ported. It is functional, but considered more experimental and less stable compared to Cupcake.

The AoF builds come with all advantages of the standard Android OS functionality, look and feel, ease of use and its prepackaged applications.

### Contacts and links

-   [The SHR Project](http://shr-project.org), \#openmoko-cdevel on irc.freenode.net, [SHR users mailing-list](http://lists.shr-project.org/mailman/listinfo/shr-user), [SHR developers mailing-list](http://lists.shr-project.org/mailman/listinfo/shr-devel)

<!-- -->

-   [freesmartphone.org](http://freesmartphone.org), coreteam (at) freesmartphone (dot) org

<!-- -->

-   [QtMoko](http://qtmoko.org/), \#qtmoko on irc.freenode.net

<!-- -->

-   [Replicant](http://replicant.us/), \#replicant on irc.freenode.net, [Identi.ca microblog](http://identi.ca/group/replicant)

<!-- -->

-   [Android on Freerunner](http://code.google.com/p/android-on-freerunner/), \#android-on-freerunner on irc.freenode.net, [mailing list](http://groups.google.com/group/android-on-freerunner)

<!-- -->

-   [GTA04](http://www.gta04.org), a new hardware platform utilizing FSO/SHR etc.

<!-- -->

-   [Debian](http://wiki.debian.org/DebianOnFreeRunner/) on Freerunner

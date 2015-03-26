---
title: Untitled Mobile Application Framework de
permalink: /Untitled_Mobile_Application_Framework/de/
---

*For the english version, see [Untitled Mobile Application Framework](/Untitled_Mobile_Application_Framework "wikilink")*

Einleitung
==========

-   Schätzen Sie Konsistenz?
-   Mögen Sie integrierte Systeme die sich stimming anfühlen und nach einer Vision entworfen sind?
-   Mögen Sie Standard UI Widgets welche von allen Applikationen auf ihrem mobilen Gerät benutzt werden?
-   Sahen Sie die iPhone Oberfläche und verliebten sich in die UI, wundern sich aber warum die freie Softwaregemeinde so etwas nicht hinbekommt?
-   Möchten Sie sich auf ihre Anwendungslogik konzentrieren und alle Dinge welche das Gerät bereitstellt von einem mächtigen Framework abstahieren lassen?
-   Sind Sie bereit einen die Sache richtig gut zu machen?

Wenn sie mindestens zwei mal Ja auf diese Fragen geantwortet haben, dann haben wir eine gute Nachricht für Sie:

1.  The freie Softwaregemeinde hat alle Technologien um dies möglich zu machen
2.  Es gibt Leute, welche dieselben Ansichten teilen und es gibt ein Projekt was dies realisieren will

Das zu entwickelnde Framework und das Projekt hört auf den Namen:

Untitled Mobile Application Framework (UMAF)
============================================

UMAF befasst sich mit der Entwicklung eines einheitlichen Systems, welches auf mobile Geräte abziehlt und dem Benutzer ein großen Satz an Anwendungsverhalten und Widgets liefert. Dabei soll das ganze System wie aus einem Guss wirken. Neue Nutzer sollten im Stande sein zu erlernen wie man das System mit maximaler Effizienz bedienen kann. Neue Applikation sollen sich in den vorhandenen Satz von Services einfügen und weitere Funktion bereitstellen.

Metaphern
---------

### Features

Der Benutzer möchte Features, keine Anwendungen. Er möchte einen Brief schreiben und nicht einen Texteditor öffnen.

...

Konkrete Ziele
--------------

-   Ein Widget Set optimiert für mobile Umgebungen. Dieses soll auf den Enlightenment Foundation Libraries basieren.
-   Ein Service Framework für mobile Anwendungsservices
-   Ein Reihe von Anwendungen welche das Service Framework benutzen

Anforderungen
-------------

### UI

-   die Oberfläche sollte mit und ohne Touchscreen bedienbar sein
-   die Oberfläche sollte Portrait und Landscape unterstützen
-   die Oberfläche sollte unterschiedliche Aufgaben unterstützen (QVGA, VGA, etc.)

Bestehende Frameworks/Toolkits
------------------------------

-   Klassische UI Toolkits wie Qt oder Gtk+ sind für mobile Umgebungen nicht wirklich brauchbar. Sie sind meist optimiert für komplexe Benutzerinterfaces welches auf einem großen Bildschirm und einer Unzahl von Buttons, Schaltern, etc. basieren. Natürlich kann man versuchen diese Toolkits auf mobile Geräte zu bringen (Maemo tut dies), aber das Ergebnis ist zwiespältig (viele Leute sind mit der Standard Maemo UI nicht zufrieden und nutzen stattdessen lieber Systeme wie z.B. die vereinfachten Canola und Carmen UI's).

<!-- -->

-   Klassische UI Toolkits sind meist statisch. Das hinzufügen von dynamischen Dingen wie Animationen oder Alphablending ist meist ein Ding der Unmöglichkeit. Dabei ist zu beachten das Solche Dinge nicht nur Eyecandy sein sollen, sondern dem Benutzer dabei helfen sollen die Anwendungsstrukturen zu verstehen so das er in seinem Geist ein Modell des User Interfaces entwerfen kann.

<!-- -->

-   Reine UI Toolkit verfügen über keine Anwendungsverhalten. In diesen Toolkits wird natürlich definiert wie ein Treeview oder ein ScrollableWindow funktioniert, aber es gibt halt keine Anwendungsverhalten welche die Anwendung konsistent machen. Wir benötigen eher Dinge wie eine "ContacsView", "PhonePad" oder einen "ConnectivityChooser".

Entwicklungsplan
----------------

Um die Ziele von UMAF zu erreichen sind folgende Schritte angedacht:

1.  Entwicklung einen UI Usability Konzeptes
2.  Prototypisches Design der UI Elemente
3.  Design der Framework Subsysteme
4.  Entwicklung des Basis Framworks (die rudimentären Funktionen)
5.  Entwicklung der grundlegenden Anwendungen und gleichzeitige Verbesserung des Basis Frameworks

### Entwicklung einen UI Usability Konzeptes

-   ... muss definiert werden
-   OpenUsability Integration?

### Prototypisches Design der UI Elemente

-   ... muss definiert werden

### Design der Framework Subsysteme

-   ... muss definiert werden

### Entwicklung des Basis Framworks (die rudimentären Funktionen)

-   ... muss definiert werden

### Entwicklung der grundlegenden Anwendungen und gleichzeitige Verbesserung des Basis Frameworks

-   ... muss definiert werden

Basisfeatures
-------------

Die Basisfeatures sollen zwei Zwecke erfüllen

1.  Die Anwendungen sollen als Vorzeigeprojekt dienen welches dann von den Anwendern getestet werden kann, sowie zur Bestimmung der benötigten Services im Service Framework
2.  Ein gebrauchsfertiges System mit dem man arbeiten kann.

Die folgenden Anwendungen sollen in Version 1.0 bereitstehen:

-   einen Dailer
-   eine SMS Anwendung
-   eine Kontakte Anwendung
-   eine Kalender Anwendung
-   Media Player (Audio, Photo, Video)
-   Memo (Text, Zeichnen, Sprechen, Kamera)
-   Weltzeituhr mit Alarmfunktion
-   Paketverwaltung
-   Einstellungen

FAQs
----

Q: Ist UMAF nur für das Gerät X?

A: Nein, UMAF soll für alle Geräte sein welche den freesmartphone Stack unterstützen.

Q: Was ist das Service Framework in UMAF?

A: Das Service Framwork ist ein High Level FSO Stack. Er soll Services bereitstellen wie z.B. "Suche einen Kontakt", "Sende Daten", "Wähle Netzwerkverbindungen", "Common Dialogs" etc.

Mitarbeiter
===========

[**Michael 'Mickey' Lauer**](/User:Mickey "wikilink")

Mail: *mlauer(at)vanille-media(dot)de*

Diskussion
==========

-   Bitte nutzt die Mailingliste smartphones-standards (at) linuxtogo (dot) org dafür
-   Zum Anmelden, Abmelden und dem einsehen der Archive besucht <http://lists.linuxtogo.org/cgi-bin/mailman/listinfo/smartphones-standards>

<!-- -->

-   Für Diskussionen im IRC besucht den Channel \#neo1973-germany im irc.freenode.net.

[UMAF](/Category:UMAF "wikilink")
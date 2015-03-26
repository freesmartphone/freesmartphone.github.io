---
title: Feb11PRDraft PL
permalink: /Feb11PRDraft/PL/
---

Projekty społeczności skupionych wokół Wolnego Oprogramowania nadal tworzą istotne platformy dla urządzeń wbudowanych.
----------------------------------------------------------------------------------------------------------------------

13 lutego 2011

Ostatnie zapowiedzi giganta telefonii komórkowej, dotyczące ewentualnego odwrócenia się od strategii wykorzystywania Wolnego Oprogramowania, dają coraz mniejsze nadzieje na osiągnięcie w pełni otwartej i wolnej platformy mobilnej dla urządzeń wbudowanych z uwzględnieniem ekosystemu i społeczności skupionej wokół niej. Mimo to, zespoły projektów SHR/FSO/QtMoko/Replicant/Android on Freerunner oraz ich użytkownicy... szczęśliwie pracują dalej. Usiłując osiągnąć nasz długoterminowy cel, jakim jest w pełni (lub "jak tylko się da") wolna platforma dla systemów wbudowanych, my, użytkownicy i deweloperzy, chcielibyśmy zaprosić innych użytkowników i deweloperów do przystąpienia i uczestniczenia w projekcie, który nie jest szarpany na lewo i prawo przez nieprzewidywalne zachowanie managementu korporacyjnego.

Nasza społeczność rozwijała się na przestrzeni ostatnich lat. Jedynym wymaganiem są porządne urządzenia, obsługiwane przez Linuksa. Nasze wymaganie zostało osiągnięte. Telefony Openmoko, Palm Pre, Nokia N900, telefony HTC - każde z tych urządzeń jest doskonałą platformą do uczenia się i rozwoju dla tych, którzy szukają prawdziwie otwartego i niezależnego systemu dla potrzeb ich edukacji, hobby, a także profesjonalnego i komercyjnego zastosowania.

Gdy tylko pojawia się jeden z dużych graczy, szczególnie gdy jego kod jest otwarty i dostępny dla każdego, lub gdy decyduje się na finansowanie jakiegoś zespołu tworzącego oprogramowanie FLOSS, może to przynieść jakieś korzyści. Tak było w przypadku Openmoko, które dostarczyło wolny i otwarty sprzęt oraz finansowało pracę nad rozwijaniem jądra Linuksa i frameworku FSO. Identyczna sytuacja miała miejsce w przypadku Nokii i jej platformy Maemo/MeeGo. Jednak po jakimś czasie, jeśli impuls nie pojawił się od strony społeczności, kiedy dofinansowanie się skończyło, a kod okazał się nie być wystarczająco otwarty, by być otoczonym przez konstruktywną społeczność która może przejąć inicjatywę, platforma zaczyna tonąć.

My wierzymy w inny model, który okazał się być zarówno zrównoważony, jak i satysfakcjonujący. Model, w którym każdy może przyczynić się swoją wiedzą i uczyć się w tym samym czasie, bez własnościowych sterowników, bez spotkań zarządu za zamkniętymi drzwiami. Model, który pozwala na wykorzystywanie istniejącego sprzętu nawet wtedy, gdy producent zdecydował się go porzucić lub nie ma zamiaru dostarczać dla niego żadnych aktualizacji. Model, który pozwala każdemu tworzyć, czytać, komentować i pobierać kod źródłowy.

Zapraszamy do przyjrzenia się naszym projektom, ich stronom internetowym, aktualnym osiągnięciom, motywacjom i potrzebom, a jeśli któryś okaże się inspirujący, polecamy nasze listy dyskusyjne, wiki, fora, pokoje IRC, aby porozmawiać, posłuchać, a także wnieść swój wkład w celu stworzenia otwartej i wolnej platformy mobilnej dla Twojego urządzenia.

### Czym jest SHR?

SHR to dystrybucja społecznościowa, koncentrująca się na systemach wbudowanych i mobilnych. Wykorzystując wiele istniejących projektów wolnego oprogramowania, takich jak Xorg, Enlightenment, Vala, Blues, OpenEmbedded i inne, SHR specjalnizuje się w integracji tych poszczególnych części architektury z istniejącymi urządzeniami, takimi jak Nokia N900, Palm Pre, HTC Dream, Openmoko Neo Freerunner i Neo 1973. Głównym zadaniem projektu jest stworzenie elastycznego i adaptowalnego systemu ze zintegrowanym frameworkiem FSO do obsługi telefonii, sieci i zarządzania peryferiami. Jako jeden z obecnie największych użytkowników middleware od FSO, SHR zawiera w sobie podstawowe interfejsy użytkownika, m.in. do prowadzenia rozmów telefonicznych, przesyłania wiadomości i zarządzania ustawieniami; a kiedy prace nad funkcjami telefonicznymi pozostawały w toku, SHR cieszył się powolnym, ale stałym napływem aplikacji zaprojektowanych specjalnie dla systemów wbudowanych i mobilnych, oferując przeglądarki internetowe, aplikacje mikroblogowe, gry oraz inne narzędzia. Aplikacje telefoniczne SHR wraz z aplikacją do ustawień oraz pełnym FSO zostały dodane do repozytoriów Debiana.

Projekt SHR aktualnie dostarcza użytkownikowi dwie gałęzie swojej dystrybucji - testową i niestabilną. Niektórzy z powodzeniem wykorzystują je nich na swoim głównym telefonie, z kolei inni wykorzystują telefony z SHR jako małe tablety i PDA. Nasze aplikacje pisane są w sposob ułatwiający ich rozbudowę i dostosowywanie do własnych potrzeb, nadal pozostaje również spore pole do popisu dla przyszłych deweloperów - więcej motywów, dodatkowych funkcji, poprawianie błędów... to, czym się zajmiesz, zależy tylko od Ciebie i Twoich zainteresowań.

### Szara eminencja, freesmartphone.org

Niepodzielną częścią SHR jest FSO - framework freesmartphone.org, nowoczesna platforma middleware, dostarczająca rozszerzalny i konfigurowalny interfejs dla aplikacji. Napisany w sposób modularny, wykorzystuje komunikację D-Bus dla integracji wtyczek. Ze względu na otwarty charakter i liberalną licencję - będąc głównie projektem społecznościowym - FSO jest doskonałym wyborem do badań, edukacji, a także dla komercyjnych zastosowań ze szczególnymi wymaganiami, które mogą wykorzystać profesjonalne wsparcie dla FSO, zawierające w sobie, ale nie ograniczające się do konsultacji i dalszego rozwijania platformy.

FSO pracuje nad wsparciem dla długiej listy urządzeń, między innymi HTC Dream / Magic i wiele innych telefonów HTC, w tym Magician, Kaiser, Raphael, Diamond i Blackstone; telefony Palm Pre (Plus (2)), Nokia N900, iPhone 3G oraz urządzenia z OpenEZX - E680(i), A780, A910, A1200, ROKR E2 or ROKR E6. Telefony Openmoko Neo Freerunner i Neo 1973 posiadają pełne wsparcie ze strony FSO.

### QtMoko

QtMoko to oparta na Debianie dystrybucja dla telefonów Openmoko Neo Freerunner oraz Neo 1973, z interfejsem użytkownika opartym na Qt Extended, dawniej znanym jako Qtopia. Jej podsystem telefoniczny w dużej mierze wykorzystuje bibliotekę qtopiacomm, ale QtMoko pracuje obecnie nad wykorzystaniem FSO. Pomoże to w integracji z większą ilością urządzeń obsługiwanych przez FSO oraz w dotarciu do większej grupy użytkowników i deweloperów.

Urządzenie z QtMoko może być z powodzeniem wykorzystywane jako główny telefon dzięki wielu dostępnym aplikacjom, wspaniałym motywom i niesamowitą prędkością działania.

### Replicant

Replicant to dystrybucja oparta na systemie Android dla telefonów HTC Dream i Nexus One, która koncentruje się na wolności: jej celem jest zastąpienie własnościowych modułów, które są zwykle obecnie na telefonach z Androidem.

Replicant jest obecnie oparty na modyfikacji Cyanogen, jednak idzie dalej, niż jej autor - własnościowe komponenty i biblioteki, które odpowiadają za komunikacje ze sprzętem, oraz zamknięte aplikacje, takie jak Android Market, są zastępowane:

-   Mimo, że Cyanogen mod, tak jak i Replicant, zastępuje większość aplikacji ich ulepszonymi, wolnymi odpowiednikami, użytkownik nadal pozostaje z własnościowymi bibliotekami, takimi jak RIL (Radio Interface Library, biblioteka, ktora komunikuje się z modemem), albo biblioteki dźwiękowe (dlopend) w przypadku HTC Dream. Replicant zastępuje te biblioteki.
-   Użytkownik, jeśli tak wybierze, pozostaje również z własnościowymi aplikacjami Google, takimi jak Market; my je również zastąpiliśmy (w tym przypadku przez FDroid).

Replicant jest obecnie wystarczająco funkcjonalny, aby być używanym w Europie (w USA i Australii występują jeszcze problemy z siecią).

### Android on Freerunner

Android on Freerunner jest kontynuacją prac podjętych oryginalnie przez Koolu. Projekt AoF jest społecznościowym portem systemu Android na telefon Openmoko Neo Freerunner. AoF dostarcza stabilne i w pełni funkcjonalne wydania Android Cupcake i kontynuuje prace związane z poprawą jakości tej dystrybucji na Freerunnerze. W tym samym czasie trwają prace nad wersją Froyo. Jest ona obecnie funkcjonalna, ale uważana za bardziej eksperymentalną i mniej stabilną w porównaniu do Cupcake.

Obrazy AoF dostarczają standardową funkcjonalność systemu Android, jego wygląd, łatwość użytkowania oraz dostępne aplikacje.

### Kontakty i linki

-   [Projekt SHR](http://shr-project.org), \#openmoko-cdevel na irc.freenode.net, [mailista użytkowników SHR](http://lists.shr-project.org/mailman/listinfo/shr-user), [mailista deweloperów SHR](http://lists.shr-project.org/mailman/listinfo/shr-devel)

<!-- -->

-   [freesmartphone.org](http://freesmartphone.org), coreteam (at) freesmartphone (dot) org

<!-- -->

-   [QtMoko](http://qtmoko.org/), \#qtmoko na irc.freenode.net

<!-- -->

-   [Replicant](http://replicant.us/), \#replicant na irc.freenode.net, [profil Identi.ca](http://identi.ca/group/replicant)

<!-- -->

-   [Android on Freerunner](http://code.google.com/p/android-on-freerunner/), \#android-on-freerunner na irc.freenode.net, [mailista](http://groups.google.com/group/android-on-freerunner)

<!-- -->

-   [GTA04](http://www.gta04.org), nowa platforma korzystająca z FSO/SHR itp.

<!-- -->

-   [Debian](http://wiki.debian.org/DebianOnFreeRunner/) na Freerunnerze

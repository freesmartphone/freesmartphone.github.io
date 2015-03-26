---
title: Feb11PRDraft CZ
permalink: /Feb11PRDraft/CZ/
---

Odhodlané skupiny vývojářů pokračují ve vývoji FLOSS softwaru pro mobilní zařízení.
-----------------------------------------------------------------------------------

13. únor 2011

I přes nedávné prohlášení velkovýrobce mobilních telefonů o možném odklonu od strategie založené na FLOSS, které ještě více snížilo šance na vytvoření svobodné a otevřené platformy pro mobilní zařízení s vývojářskou a uživatelskou komunitou, skupiny SHR/FSO/QtMoko/Replicant/Android on Freerunner vývojářů a uživatelů... kódují vesele dále. Pracující na naplnění dlouhodobého cíle o vytvoření plně, nebo "jak jen to bude možné" FLOSS svoboodné platformy pro mobilní zařízení, my uživatelé a vývojáři, bychom rádi pozvali další uživatele a vývojáře k účasti na projektu, který není zmítán nepředvídatelnou pošetilostí korporátních manažerů.

Úsilí našich týmů rok od roku postupuje.Jedininým požadavkem byl solidní, Linuxem podporovaný hardware a ten nyní máme - Openmoko telefony, nové Palm Pré telefony, linuxový tank Nokia N900, HTC přístroje - každý z nich nyní poskytuje výtečnou živnou půdu pro výzkum a vývoj pro ty, kteří vyžadují opravdu otevřený a nezávislý systém pro své učení, programování či dokonce profesionální nebo komerční využití.

Každý příchod nového velkého hráče na scénu se zdá být výtečným počinem, tedy alespoň ze začátku, obzvláště pokud je výsledný kód zpracováván a distribuován svobodně a otevřeně, nebo pokud dokonce dojde k financování některého z týmů programujících FLOSS kód ze svého přesvědčení. Tak to bylo například v případě společnosti Openmoko, která přinesla svobodný a otevřený hardware a sponzorovala vývoj Linuxového kernelu a FSO frameworku. Nebo v případě společnosti Nokia s Maemo/Meego platformou. Nicméně, bohužel je to tak, že, pokud impuls nepochází přímo z řad uživatelů a vývojářů, v okamžiku odlivu peněz a v případě kódu, který nebyl dostatečně otevřený, nebo podporovaný dostatečně silnou komunitou, jde výsledek ke dnu spolu s financováním.

My věříme v jiný model - v model, který je vyzkoušený, udržitelný a uspokojující, model, kde každý může přispět své vědomosti a zároveň se učit od ostatních, bez proprietálních kusů ovladačů, bez porad manažerů za zavřenými dveřmi. Model, který nám umožňuje využívat existující zařízení, ta která již vlastníme a to i poté, co se výrobce rozhodl, že je již nebude podporovat, nebo není ochoten vydat pro ně žádné další aktualizace. Model, u kterého může kdokoliv vytvořit, číst, komentovat nebo stáhnout zdrojový kód.

Rádi bychom vás tímto pozvali k prohlédnutí stránek jednotlivých týmů, kde se dozvíte více o dosažených výsledích, motivaci i potřebách a pokud vás to bude inspirovat, připojte se do diskuzních skupin, wiki webů nebo irc kanálů k diskuzi, případně i k přispění v díle na svobodném a otevřeném systému pro vaše zařízení.

### Co je SHR?

SHR komunitní linuxová distribuce zaměřená na mobilní zařízení. V základu SHR je využito mnoho existujících svobodných a otevřených projektů jako jsou Xorg, Enlightenement, Vala, Bluez, OpenEmbedded a další s tím, že SHR se specializuje na integraci těchto komponent do existujícího hardware, například pro Nokia N900, Palm Pré, HTC Dream nebo Openmoko Neo Freerunner a Neo 1973. Hlavním cílem SHR je flexibilní a adaptovatelný systém s integrovaným FSO frameworkem pro telefonii, síťování a správu dalšího hardware. Jako jeden z hlavních uživatelů FSO frameworku, zahrnuje SHR základní uživatelské programy pro telefonii jako je dialer, SMS aplikace nebo manažer uživatelských nastavení. A přesto, že plně fungující telefonie je ve stádiu vývoje, SHR se pomalu, ale jistě, naplňuje novými aplikacemi vyvinutými speciálně pro mobilní systému, jako jsou webové prohlížeče, klienti pro mikroblogování, různé utility, hry a podobně.

SHR nabízí dvě verze své distribuce - testovací a nestabilní. Někteří lidé využívají SHR k dennímu používání na svém telefonu, jiní ji využívají jako webové tablety nebo PDA. A protože základní aplikace jsou vytvořeny v modulárním a témovatelném stylu, je zde rozhodně spousta místa pro rozšíření, nová témata, moduly synchronizace, testování a podobně.

=== freesmartphone.org - šedá eminence

Neoddělitelnou součástí SHR je FSO - freesmartphone.org Framework, moderní middleware platforma založená na službách, poskytující rozšiřitelné a konpletně nastavitelné rozhraní mezi vrstavmi aplikací a hardware. FSO je od základu postaven mudulárně s D-Bus propojením jednotlivýcxh komponent. Díky své otevřené nátuře a liberální licenci (s tím, že se jedná převážně o komunitní projekt) je FSO perfektní volbou pro výzkum, vzdělávání a je velmi vhodný také pro nasazení komerčních subjektů se speciálními požadavky, které mohou benefitovat s poskytovanho proferionálního podpory, zahrnující, ale ne-limitované, na konzultace a vývoj.

Dlouhý seznam zařízení s FSO podporou ve vývoji zahrnuje například HTC Dream/Magic a mnoho dalších HTC přístrojů včetně Magician, Kaiser, Raphael, Diamond, Blackstone, dále pak Palm Pre (Plus(2)) telefony, Nokia N900, iPhone 3g, nebo skupinu zařízení OpenEZX - E680(i), A780, A910, A1200, ROKR E2 or ROKR E6. Openmoko telefony Freerunner a Neo 1973 mají plně funkční FSO podporu.

### QtMoko

QtMoko - distribuce založena na Debianu, je určená pro Openmoko Neo Freerunner a Neo 1973 telefony, s uživatelským rozhraním postaveným na Qt Extended, dříve známé jako Qtopia. Telefonní subsystém využívá z většiny knihovnu qtopiacomm, ale QtMoko momentálně začíná práce na přesunu směrem k FSO. To umožní integraci na větším množství zařízeních, která FSO podporují a také širší uživatelskou a vývojářskou základnu.

QtMoko je možno používat jako každodenní telefon na Openmoko zařízeních, a nabízí množství aplikací, výborná témata a úžasnou rychlost.

### Replicant

Replicant je distribuce založená na Androidu, v tomto okamžiku pro HTC Dream a Nexus One, s jedním hlavním záměrem - veškeré komponenty musí být pod svobodnou licencí. Postupně se pracuje na náhradě jednotlivých uzavřených částí, které jsou momentálně v Androidu přítomny. Replicant je založen na Cyanogen mod, ale jde dále - namísto záměny systému s využívání proprietálních nízkoúrovňových knihoven, které komunikují s hardwerem, spolu s proprietálními uzavřenými vysokoúrovňovými aplikacemi jako je např Market, je Replicant nahrazuje:

-   tam, kde distribuce založené na Cyanogen mod doplní původní software o vylepšenou svobodbou verzi, uživateli zůstanou v systému proprietální knihovny jako je napříkůlad RIL (Radio interface library, knihovna pro komunikaci s modemem), nebo Audio (dlopend) knihovny, v případě HTC Dream. Replicant tyto nihovny nahrazuje.
-   Replicant nahrazuje i Market pomocí svobodné aplikace FDroid a je na uživateli, zda si proprietální Market v systému ponechá, nebo ne.

Replicant je nyní plně funkční pro použití v Europe (RIL knihovna má ještě problémy v USA a Australii).

### Android na Freerunneru

Android na Freerunneru je pokračování práce započaté kanadskou společností Koolu a jedná se komunitou řízený port Androidu pro Openmoko Neo Freerunner. Podařilo se vytvořit stabilní a plně funkční vydání pro Cupcake a nadále se pokračuje ve zkvalitňování tohoto systému na Freerunneru. Cupcake na Freerunneru je možno použít jako každodenní telefon.Ve stejnou dobu probíhají i práce na portování Froyo. I ti je již také funkční, ale zatím je stále považováno spíše za experimentální a méně stabilní, než Cupcake.

AoF vydání poskytují všechny možnosti standardní Android funkcionality, se vzhledem, funkcemi a jednoduchostí používání předinstalovaných aplikací.

### Kontakty a odkazy

[The SHR Project](http://shr-project.org), \#openmoko-cdevel na irc.freenode.net, [SHR mailing-list uživatelů](http://lists.shr-project.org/mailman/listinfo/shr-user), [SHR mailing-list vývojářů](http://lists.shr-project.org/mailman/listinfo/shr-devel)

[freesmartphone.org](http://freesmartphone.org), coreteam (at) freesmartphone (dot) org

[QtMoko](http://qtmoko.org/), \#qtmoko na irc.freenode.net

[Replicant](http://replicant.us/), \#replicant na irc.freenode.net, [Identi.ca mikroblog](http://identi.ca/group/replicant)

[GTA04](http://www.gta04.org), prorotyp nového zařízení, které využívá FSO/SHR atd.

[Android na Freerunner](http://code.google.com/p/android-on-freerunner/) a jeho [mailing list](http://groups.google.com/group/android-on-freerunner) , \#android-on-freerunner na irc.freenode.net
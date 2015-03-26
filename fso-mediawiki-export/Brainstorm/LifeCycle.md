---
title: Brainstorm LifeCycle
permalink: /Brainstorm/LifeCycle/
---

Propose
=======

This service is proposed to manage the lifecycle of an application. From starting, over suspending if necessary to stoping if it's not required anymore. Maybe this should also care about unique instances?

Android describes the lifecycle of an app as follows: [1](http://developer.android.com/guide/topics/fundamentals.html?q=lifecycle#lcycles)

Ideas
=====

-   Applications can provide several features like rejecting/answer calls, show SMS,... , and we don't want to lose the current screen during the call.
-   Apps should suspend e.g. the system shuts down/ memory is low
-   TODO

Server side
===========

-   AddProvider( ObjectPath apppath, string provider )
-   SetPreferredProvider( string provide, string app )
-   SetProviderUsage( string provide, string app, string usage ) //never, always, prefer_current
-   RegisterApplication( Object Path )
-   ShowProvider( string provide )
-   Shutdown(string reason)
-   string[] ListApplications()
-   StartApplication( string name )
-   ShowApplication( ObjectPath path )

Application side
================

-   void Start()
-   void Stop()
-   string[] Provides()
-   signal Finished( string provide )
-   bool Suspend( string filename ) //write current state to a file to resume later
-   bool Resume( string filename )
-   void LeaveForeground(string reason)
-   bool GoToForeground()
-   void Pause()
-   void Continue()
-   bool Show( string provide )
-   string ApplicationName()

Interaction
===========

None preferred provider is on top
---------------------------------

In this case navit is starting, registers to the lifecycle service. Meanwhile a consumer (e.g. fsoeventsd) wants to show the call window, because of an incoming call. [Image:Navit_answers.png](/Image:Navit_answers.png "wikilink")

Open preferred provider
-----------------------

In this case the application on top does provide the requiered provider, and fsolifecycle pops up the prefered provider. [Image:Shr_answers.png](/Image:Shr_answers.png "wikilink")

Use cases
=========

-   Trucker Joe is on the road and gets a phone call, but he's lost in $(TOWN) without navit, and navit supports answering calls. instead of bringing navit to background, it show OSD buttons to answer the call.

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
---
title: Brainstorm fsoeventsd
permalink: /Brainstorm/fsoeventsd/
---

Purpose
=======

The purpose of this daemon is to connect the different FSO daemons in a flexible, configureable and (lazy) way.

Requirements
============

-   Modules Support
-   Easy way to add own rules
-   lightweight
-   Easy to maintain system rules

Namespaces / Subsystems
=======================

TODO

Proposals to evaluate
=====================

-   Reimplement current API in vala. Docs are here: <http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.Events.html;hb=HEAD>
    -   Minimal interface (only 2 methods and 1 test method)
    -   If you want to add a new rule you need to know YAMl
    -   doesn't use modules yet
-   My (playya) GSoC 2008 project has a slightly different approach and could be adopted (source: <http://code.google.com/p/robgsoc/source/checkout> )
    -   every rule has an own dbus path
    -   And,Or,Not, Xor (one out of n) is implemented as a ComplexRule
    -   Every Rule keeps several Actions to trigger/untrigger
    -   Basic interfaces are quite minimal
-   TaSN wrote a similar daemon, too: <https://projects.openmoko.org/projects/siglaunchd/>
    -   TODO
    -   even more todo

How to save/write Rules?
========================

| Name                | flexibility | complexity | parsebility | human rw-able | Vala/C-integration | Comment                  | Link                                                            |
|---------------------|-------------|------------|-------------|---------------|--------------------|--------------------------|-----------------------------------------------------------------|
| YAML                | 2           | 4          | 4           | 5             | 2(?)               | used by frameworkd       | <http://www.yaml.org/>                                          |
| JSON/libpersistence | 5           | 3          | 4           | 3             | 5                  | A project by mickey/jürg | <http://git.freesmartphone.org/?p=libpersistence.git;a=summary> |
| LUA                 | 5           | 3          | 4           | 4             | 4                  |                          | <http://www.lua.org/>                                           |

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
---
title: Implementations OpenPreferencesDaemon
permalink: /Implementations/OpenPreferencesDaemon/
---

The Preferences daemon can be used to store configuration values, in a way similar to GConf.

About
=====

The preferences service offer an easy way to share configuration parameters between applications. Several configuration service already exist (the most famous being gconf.) Here I (Charlie) decided not to use any existing software, but create one from scratch. The reason being that I wanted the service to be :

-   Simple.
-   fully aware of profiles configuration.

The service is simple : all the configuration and schema file (files that describe the preferences offered by a service) are stored in [YAML](http://www.yaml.org/) files. So we don't have the burden of XML editing.

The service is fully aware of profiles : It means that an application can specify which of its configuration parameters can be redefined in different profiles. This way, an application using the preferences server, when trying to access a parameter, will automatically receive the one corresponding to the current profile.

installation
============

The daemon is part of frameworkd, so there is no need to install it.

API
===

The current DBus API is there : [Standards/PreferencesAPI](/Standards/PreferencesAPI "wikilink")

Files format
============

The Schema files, describing the configuration of a service, look like this :

    vibration:          # The name of the parameter
      type: bool        # The type
      default: yes      # default value
      profilable: yes   # set to yes if the parameter depends of the profile

    ring-volume:
      type: int
      default: 10
      profilable: yes

The configuration files, storing the configuration parameter, look like this :

    vibration: Yes
    ring-volume: 9

There is one configuration file per service per profile

[Category:System Developers](/Category:System_Developers "wikilink")
---
title: Standards PreferencesAPI
permalink: /Standards/PreferencesAPI/
---

Purpose
=======

The preferences service can be used to get and set configuration attributes. It is also in charge of the profiles.

All the attributes are grouped into services.

Each service has to declare its configuration attribute in a schema file placed into :

`/etc/freesmartphone/opreferences/schema/`

See [Standards/PreferencesSchema](/Standards/PreferencesSchema "wikilink")

The actual values of the configuration attributes are stored into the files

`/etc/freesmartphone/opreferences/conf/${service}/${profile}.yaml`

where **service** is the name of the service and **profile** is the name of the profile

### Preference

See [org.freesmartphone.Preferences](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.Preferences.html;hb=HEAD)

### Service

See [org.freesmartphone.Preferences.Service](http://git.freesmartphone.org/?p=specs.git;a=blob_plain;f=html/org.freesmartphone.Preferences.Service.html;hb=HEAD)

[Category:Developer resources](/Category:Developer_resources "wikilink")
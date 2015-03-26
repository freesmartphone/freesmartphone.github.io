---
title: AlsaScenarios
permalink: /AlsaScenarios/
---

Introduction
------------

This article assume that the porter is familiar with fso config files. We will take the gta04 hardware as an example. We will make the stereoout scenario.

Manual Howto
------------

-   let's go [at the gta04 documentation page](http://projects.goldelico.com/p/gta04-kernel/page/Sound/)

we see some amixer commands:

`#Basic`
`amixer set 'DAC1 Analog' off`
`amixer set 'DAC2 Analog' on`
`amixer set 'Codec Operation Mode' 'Option 1 (audio)'`

And:

`#Handsfree`
`amixer set HandsfreeL on`
`amixer set HandsfreeR on`
`amixer set 'HandsfreeL Mux' AudioL2`
`amixer set 'HandsfreeR Mux' AudioR2`
`aplay /usr/share/sounds/alsa/Front_Center.wav `
`amixer set HandsfreeL off`
`amixer set HandsfreeR off`

-   let's make some dump:

`alsactl -f dump.state store`

-   looking into Basic we see:

`amixer set 'Codec Operation Mode' 'Option 1 (audio)'`

-   we then look into our dump of the alsa states and find that:

`        control.1 {                        `
`                iface MIXER         `
`                name 'Codec Operation Mode'`
`                value 'Option 2 (voice/audio)'`
`                comment {             `
`                        access 'read write'`
`                        type ENUMERATED`
`                        count 1`
`                        item.0 'Option 2 (voice/audio)'`
`                        item.1 'Option 1 (audio)'`
`                }`
`        }`

-   the rest is the understanding of the fsodeviced states format:

`1:'Codec Operation Mode':1:1`
`|              \          \ \`
` \              \          \ \->that correspond to the control value(here 'Option 1 (audio)' )`
`  \              \          \->that correspond to the numbers of controls, if there were 2 controls it would look like that: :2:1,1"`
`   \              \->that corresponds to the name of the control`
`    \->that correspond to the control number (control.1)`

More automatized howto
----------------------

The following command saves \*all\* controls of the current scenario to the respective configuration directory(/etc/freesmartphone/conf/$machine/alsa-default). It doesn't touch controls, which aren't listed in the current scenario.

`mdbus2 -s org.freesmartphone.odeviced /org/freesmartphone/Device/Audio org.freesmartphone.Device.Audio.SaveScenario stereoout`

To create a **new scenario**, use one of the tools from here (alsa2fso.py or fso-alsa):

[<http://git.freesmartphone.org/?p=cornucopia.git;a=tree;f=tools>](http://git.freesmartphone.org/?p=cornucopia.git;a=tree;f=tools)
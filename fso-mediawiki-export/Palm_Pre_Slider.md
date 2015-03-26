---
title: Palm Pre Slider
permalink: /Palm_Pre_Slider/
---

This page is just a little mockup on which events the slider of the Palm Pre sends.

Device
------

The Slider sends its events (at least on WebOS) to /dev/input/event1

Signals
-------

Two different Signals are send: EV_SW and EV_SYN

EV_SW contains values, EV_SYN is just send after each EV_SW

EV_SW has two keys: 06 and 07

Key "07" defines adjusting. Value "0" = adjusting, value "1" = adjusted. Key "06" is send when Sliders position is somewhere around the center (in fact it is a little deeper than that but does not matter). Value "1" indicates that the Slider is closing, value "0" indicates opening.

So an openingslide performs these events:

EV_SW code: 07 value: 0 (adjusting = true)

EV_SYN code: 00 value: 0

EV_SW code: 06 value: 0 (Slider is opening)

EV_SYN code: 00 value: 0

EV_SW code: 07 value: 1 (adjusting = false)

EV_SYN code: 00 value: 0

Analogue, closing looks like that:

EV_SW code: 07 value: 0 (adjusting = true)

EV_SYN code: 00 value: 0

EV_SW code: 07 value: 1 (Slider is closing)

EV_SYN code: 00 value: 0

EV_SW code: 06 value: 1 (adjusting = false)

EV_SYN code: 00 value: 0

Hint: If the Slider is NOT moved constantly (moved to centre and back) this set of events is incomplete.

The eventpositions look something like this: |--1-------2----------------------1--|

The room from an end to (1) is the room where adjusting = false. At point (2) code "06" is send.
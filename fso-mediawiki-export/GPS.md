---
title: GPS
permalink: /GPS/
---

| Device                  | Working?        | Formats  | AGPS?                 | Comments                           | Protocol Implementation                   | Resource Plugin                                                          |
|-------------------------|-----------------|----------|-----------------------|------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|
| GTA02                   |                 | -   NMEA
                                             -   UBX   | ,trough UBX           | -   Has an external antenna switch | -   Before: UBX trough frameworkd's ogpsd
                                                                                                                     -   Now: to check                          | To check                                                                 |
| GTA04                   |                 | -   NMEA
                                             -   SIRF  | ?                     |                                    | Trough gpsd                               | -   sysfs
                                                                                                                                                                 -   rfkill
                                                                                                                                                                 -   handled Trough fsodeviced's plugins
                                                                                                                                                                 -   handled trough oeventsd in rules.yaml                                 |
| HTC Dream(unmaintained) |                 | -   NMEA | , need to be reversed |                                    | -   trough ogpsd                          | -   trough ogpsd which calls the program named 'gps' which activates GPS

                                                                                                                                                                 Or:

                                                                                                                                                                 -   Trough an fsodtldt plugin which conflict with gpsd.                   |
| Other devices           | **Not working** |


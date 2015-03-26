---
title: Licensing proposal
permalink: /Licensing_proposal/
---

Licensing
---------

Perhaps the first order of business should be a discussion on how various components in this effort should be licensed.

My own view is that this layer sits immediately above the kernel, and its services are accessible generally through IPC methods, primarily D-Bus. As such, the designer of the layers that make use of these services should have the freedom to utilize these services from anything from GPL to Proprietary code.
 The software components that provide these services, however, should IMHO be licensed under the GPL where they export services through IPC mechanisms and under the LGPL only in cases where they provide services that must be linked with external programs (e.g. libraries).
 I think this makes more sense than bsd, apache2, or similar licenses because adoption of one of these may loose too much support from the FOSS side and any license that does not permit distribution of proprietary code utilizing these services would likely loose too much support from the proprietary side.
 So I propose that:

Kernel Space Modules (like drivers) be GPL2

</ul>

User Space Daemons exporting service via IPC be GPL2

</ul>

Libraries be LGPL2

</ul>

Wiki content and specifications be GNU FDL

</ul>

------------------------------------------------------------------------

Other thoughts? --[Writchie](/User:Writchie "wikilink") 03:19, 27 November 2007 (CET)

------------------------------------------------------------------------

I([Mudyc](/User:Mudyc "wikilink")) agree with few minor points:

The kernel space modules should follow the licensing terms of the kernel. With Linux it's GPL2 at the moment.

</ul>

It might be good motion to support GPL3 too with user space applications, i.e. GPL2+.

</ul>
[Category:Community](/Category:Community "wikilink")
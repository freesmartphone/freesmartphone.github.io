---
title: Tutorials Example FSO plugin
permalink: /Tutorials/Example_FSO_plugin/
---

This tutorial shows yout how to write a minimal example plugin for fsodeviced. You can use it as a base for every subsystem if you change some small bits.

Creating base file structure
----------------------------

go to src/plugins in your fsodeviced directory and add an example dir:

`mkdir example`

create a Makefile.am in this directory and copy with the following into it:

`include $(top_srcdir)/Makefile.decl`
`NULL =`
`#the flags passed to gcc`
`AM_CPPFLAGS = \`
`   -I$(top_srcdir) \`
`   $(FSO_CFLAGS) \`
`   $(DBUS_CFLAGS) \`
`   $(NULL)`
`noinst_PROGRAMS = $(TEST_PROGS)`
`progs_ldadd = $(FSO_LIBS) $(DBUS_LIBS) $(top_srcdir)/src/lib/libfsodevice.la`
`#flags passed to valac`
`VALAC_ARGS = \`
`   --basedir $(top_srcdir) \`
`   --vapidir $(top_srcdir)/fsoframework \`
`   --pkg glib-2.0 \`
`   --pkg dbus-glib-1 \`
`   --pkg fso-glib-1.0 \`
`   --pkg fsoframework-2.0`
`#`
`# plugin`
`#`
`modlibexecdir = $(libdir)/cornucopia/modules/fsodevice`
`#all libraries to build`
`modlibexec_LTLIBRARIES = example.la`
`#c files for your plugins`
`example_la_SOURCES = plugin.c`
`#vala sources for the plugin`
`example_la_VALASOURCES = plugin.vala`
`$(example_la_SOURCES): $(example_la_VALASOURCES)`
`   $(VALAC) -C $(VALAC_ARGS) $^`
`   touch $@`
`example_la_LIBADD = $(progs_ldadd)`
`example_la_LDFLAGS = -no-undefined -module -avoid-version`
`example_la_LIBTOOLFLAGS = --tag=disable-static`
`CLEANFILES = \`
`   *.c \`
`   *.h \`
`   *.la \`
`   *.lo \`
`   $(NULL)`
`MAINTAINERCLEANFILES = \`
` Makefile.in \`
` $(NULL)`

Add to the configure script
---------------------------

To create your Makefile from a Makefile.am you have to add it to the AC_CONFIG_FILES macro at the bottom of the configure.ac in the project's root directory. You have to add a path, relative to the project's root like:

`src/plugins/example/Makefile`

To compile your plugin you have to add your plugin to src/plugins/Makefile.am SUBDIRS variable. Don't forget the \\ at the end of the line, or it'll break compilation of other plugins.

At the end you have to regenerate everything type

`./autogen.sh --prefix=${your_prefix}`

in the project's root

Write the plugin
----------------

Add a plugin.vala in src/plugins/example/ and add the following code:

`
 using GLib;

 //Normally generated from specs and in fso-glib
 [DBus (name="org.freesmartphone.Device.Example")]
 public interface IExample: Object
 {
     public abstract string hello(string text) throws DBus.Error;
 }
 class Example: IExample, FsoFramework.AbstractObject
 {
     //the module name
     public const string MODULE_NAME = "fsodevice.example";

    //In libfsoframework
    public const  string ExampleServiceFace = FsoFramework.Device.ServiceFacePrefix + ".Example";
    public const  string ExampleServicePath = FsoFramework.Device.ServicePathPrefix + "/Example";

    //private members
    private string my_name;

    public Example( FsoFramework.Subsystem subsystem)
    {
        //register plugin
        subsystem.registerServiceName( FsoFramework.Device.ServiceDBusName );
        subsystem.registerServiceObject( FsoFramework.Device.ServiceDBusName,
                                         ExampleServicePath, this );
        //get something out of the config
        my_name = config.stringValue(MODULE_NAME, "my_name", "Example");
    }

    //org.freesmartphone.Device.Example implementation
    public string hello(string text)
    {
        //write an info into the log
        logger.info(@"sending hello with '$text'");
        return "hello " + text + " from " + my_name;
    }
    //representation of the object
    public override string repr()
    {
        return @"<$my_name>";
    }
 }

 internal Example instance = null;

 //this is called on loading the plugin into the daemon
 //create your objects here
 public static string fso_factory_function( FsoFramework.Subsystem subsystem ) throws Error
 {
    instance = new Example( subsystem );
    return Example.MODULE_NAME;
 }
 //this is called on loading the shared object
 [ModuleInit]
 public static void fso_register_function( TypeModule module )
 {
    FsoFramework.theLogger.debug( "fsodevice.example fso_register_function()" );
 }
`

Load the plugin
---------------

To load your plugin just add a section with the name of your plugin to your /etc/freesmartphone/fsodevice.conf. For the example plugin it's the following:

`[fsodevice.example]`
`my_name=my first fsodevice plugin`

Test your plugin
----------------

install fsodevice:

`make install`

start fsodeviced and you should see the following line in your logs:

`2010-02-13T12:44:44.616978Z [DEBUG] fsodeviced : fsodevice.example fso_register_function()`

to call the function you can use mdbus, which is in the python-helpers repository:

`mdbus -s org.freesmartphone.odeviced /org/freesmartphone/Device/Example org.freesmartphone.Device.Example.Hello FOOBAR`
`'hello FOOBAR from my first fsodevice plugin'`

[Category:Tutorial](/Category:Tutorial "wikilink")
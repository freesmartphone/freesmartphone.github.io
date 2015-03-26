---
title: Tutorials Using FSO glib for resource handling
permalink: /Tutorials/Using_FSO_glib_for_resource_handling/
---

To make live easy for C devolopers and have a contract between client and server, we are creating [libfso-glib](/Implementations/libfso-glib "wikilink") from the specs. This example shows how to list all available resource and request a resource including (some) error handling from C. Because we're using asynchronous DBus calls, it needs some callbacks and knowledge of the gio-2.0 library.

The Code
--------

`#include `<freesmartphone.h>
`#include `<fsoframework.h>
`//The GLib mainloop`
`GMainLoop* ml;`
`//Callback to list resources`
`static void list_resources_ready(GObject* source, GAsyncResult* res, gpointer user_data)`
`{`
`  FreeSmartphoneUsage* usage = FREE_SMARTPHONE_USAGE(user_data);`
`  int nr_resources;`
`  int i;`
`  GError* error = NULL;`
`  //Get results`
`  char** resources = free_smartphone_usage_list_resources_finish(`
`          usage, res, &nr_resources, &error);`
`  //Handle error case`
`  if(error)`
`  {`
`      g_debug("list resources: %s", error->message);`
`  }`
`  //if no error occured print resources`
`  else`
`  {`
`      for(i=0;i`<nr_resources; i++)
       {
           g_debug("resource: %s",resources[i]);
       }
   }
 }

 //Callback to request a resource
 static void request_resource_ready(GObject* source, GAsyncResult* res, gpointer user_data)
 {
   FreeSmartphoneUsage* usage = FREE_SMARTPHONE_USAGE(user_data);
   GError* e = NULL;
   free_smartphone_usage_request_resource_finish(
           usage, res, &e);
   //Handle error case
   if(e)
   {
       g_debug("request resource: %s", e->`message);`
`  }`
`  else`
`       g_debug("success!");`
`}`
`//Callback to release a resource`
`static void release_resource_ready(GObject* source, GAsyncResult* res, gpointer user_data)`
`{`
`  FreeSmartphoneUsage* usage = FREE_SMARTPHONE_USAGE(user_data);`
`  GError* e = NULL;`
`  free_smartphone_usage_release_resource_finish(`
`          usage, res, &e);`
`  //Handle error case`
`  if(e)`
`  {`
`      g_debug("release resource: %s", e->message);`
`  }`
`  else`
`       g_debug("success!");`
`}`
`//Signal callback`
`static gboolean on_resource_changed(GObject* source, char* name, gboolean state, GHashTable* prop, gpointer user_data)`
`{`
`  //print state`
`  g_debug("resource changed: %s %s", name, state ? "true": "false");`
`  //quit the mainloop to get a clean exit`
`  if(!state)`
`       g_main_loop_quit(ml);`
`  return FALSE;`
`}`
`int main(int argc, char* argv[])`
`{`
`  //get the mainloop`
`  ml = g_main_loop_new(NULL, FALSE);`
`  GError* error = NULL;`
`  //Get the dbus connection. ATM everything lives on system bus`
`  DBusGConnection* con = dbus_g_bus_get(DBUS_BUS_SYSTEM, &error);`
`  if(error)`
`  {`
`  }`
`  //Get the usage object`
`  FreeSmartphoneUsage* usage = free_smartphone_get_usage_proxy(con,`
`              FSO_FRAMEWORK_USAGE_ServiceDBusName,`
`              FSO_FRAMEWORK_USAGE_ServicePathPrefix);`
`   //connect a signal handle to "resource-changed"-signal`
`   g_signal_connect(usage, "resource-changed", G_CALLBACK(on_resource_changed), usage);`
`   //start the async call to list resources`
`   free_smartphone_usage_list_resources(usage, (GAsyncReadyCallback)list_resources_ready, usage); `
`   //request the Display resource`
`   free_smartphone_usage_request_resource(usage, "Display", (GAsyncReadyCallback)request_resource_ready, usage);`
`   //request a bogus resource to force the error case`
`   free_smartphone_usage_request_resource(usage, "BOGUS", (GAsyncReadyCallback)request_resource_ready, usage);`
`   //release the Display resource`
`   free_smartphone_usage_release_resource(usage, "Display", (GAsyncReadyCallback)release_resource_ready, usage);`
`   //start the mainloop`
`   g_main_loop_run(ml); `
`   g_debug("returned from mainloop");`
`   //free memory`
`   dbus_g_connection_unref(con);`
`   g_object_unref(G_OBJECT(usage));`
`   g_main_loop_unref(ml); `
`   return 0;`
`}`

How to compile
--------------

`gcc -Wall $(pkg-config --cflags --libs fso-glib-1.0 fsoframework-2.0) -o fsoresource fsoresource.c`

[Category:Tutorial](/Category:Tutorial "wikilink")
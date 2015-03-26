---
title: Tutorials glibcall
permalink: /Tutorials/glibcall/
---

Calling dbus with C and glib
============================

this example calls method GetStatus on interface org.freesmartphone.GSM.Network specially for the property "provider"

    /* author: Matze Huber matthias.huber [AT] wollishausen.de */
    /* License: GPL Latest */
    /* less than half of the time could be necessary, if dbus-calls and result-types and their usage were better documented */

    #include <stdio.h>
    #include <stdlib.h>
    #include <unistd.h>
    #include <string.h>

    #include <dbus/dbus-glib.h>
    #include <glib-object.h>
    #include <glib.h>

    static char provider[40];
    static char netstring[128];


    static DBusGConnection *connection = NULL;
    DBusGProxy *proxy_dbus = NULL;
    GError *error = NULL;

    int main( int argc, char *argv[] ) {
    static DBusGProxyCall *id;
    GHashTable *hash = NULL;
    int i;

        g_type_init ();

        connection = dbus_g_bus_get(DBUS_BUS_SYSTEM, &error);
        if (!connection) {
            fprintf(stderr, "Failed to open connection to system bus: %s", error->message);
            exit(1);
        }
        proxy_dbus = dbus_g_proxy_new_for_name(connection, "org.freesmartphone.ogsmd", "/org/freesmartphone/GSM/Device", "org.freesmartphone.GSM.Network");

        hash = g_hash_table_new(NULL, NULL);

        if ( !dbus_g_proxy_call( proxy_dbus, "GetStatus", &error,
            G_TYPE_INVALID,
            dbus_g_type_get_map ("GHashTable", G_TYPE_STRING, G_TYPE_VALUE), &hash, G_TYPE_INVALID ) ) {
            if ( error && error->message )
                        fprintf(stderr, "error at line %d: %s\n", __LINE__, error->message);
            else if ( error )
                        fprintf(stderr, "error at line %d\n", __LINE__);
            else
                fprintf(stderr, "error at line: %d\n", __LINE__);
        }
        else {
            fprintf(stderr, "provider: %s\n", g_value_get_string(g_hash_table_lookup(hash, "provider")));
        }
        return 0;
    }

[Category:Tutorial](/Category:Tutorial "wikilink")
---
title: Tutorials glibcsignalx
permalink: /Tutorials/glibcsignalx/
---

Receiving Signals with C
========================

this example listens on a status change (registration to a net provider) and also to changes ot signal strength

    /* author: Matze Huber matthias.huber [AT] wollishausen.de */
    /* License: GPL Latest */
    /* less than half of the time could be necessary, if dbus-calls and result-types and their usage were better documented */

    #include <stdio.h>
    #include <stdlib.h>

    #include <dbus/dbus-glib.h>
    #include <glib-object.h>
    #include <glib.h>


    static DBusGConnection *connection = NULL;
    DBusGProxy *proxy_dbus = NULL;
    GError *error = NULL;


    GCallback strength_handler( DBusGProxy *proxy, gint lstrength, gpointer data ) {

        fprintf(stderr, "Strength: %d\n", lstrength);
    }


    GCallback status_handler( DBusGProxy *proxy, GHashTable *hash, gpointer data ) {

        fprintf(stderr, "status_handler: %s\n", g_value_get_string(g_hash_table_lookup(hash, "provider")));
    }


    void *getdbus( void *arg ) {
    GMainLoop *loop = NULL;

        while ( 1 ) {
            g_type_init();
            loop = g_main_loop_new(NULL, FALSE);
            connection = dbus_g_bus_get(DBUS_BUS_SYSTEM, &error);
            if (!connection) {
                fprintf(stderr, "Failed to open connection to system bus: %s", error->message);
                exit(1);
            }
            proxy_dbus = dbus_g_proxy_new_for_name(connection, "org.freesmartphone.ogsmd", "/org/freesmartphone/GSM/Device", "org.freesmartphone.GSM.Network");

            dbus_g_proxy_add_signal( proxy_dbus, "SignalStrength", G_TYPE_INT, G_TYPE_INVALID, G_TYPE_INVALID );
            dbus_g_proxy_connect_signal( proxy_dbus, "SignalStrength", (GCallback)strength_handler, NULL, NULL );

            dbus_g_proxy_add_signal( proxy_dbus, "Status", dbus_g_type_get_map("GHashTable", G_TYPE_STRING, G_TYPE_VALUE), G_TYPE_INVALID, G_TYPE_INVALID );
            dbus_g_proxy_connect_signal( proxy_dbus, "Status", (GCallback)status_handler, NULL, NULL );
            g_main_loop_run(loop);
            sleep(5);
        }
    }



    int main( int argc, char *argv[] ) {

        getdbus( NULL );

    }

[Category:Tutorial](/Category:Tutorial "wikilink")
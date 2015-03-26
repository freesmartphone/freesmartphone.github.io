---
title: Aurora WritingAnApp
permalink: /Aurora/WritingAnApp/
---

Making a simple application
---------------------------

Using Aurora's components,it's easy to start an aurora application,first you'll create your main.qml,each shortcut in the main screen will call, you can even call it another name,but main.qml is the better way. You'll have almost nothing in your main.qml,it'll only be a switcher.

    /*
     * (C) 2011 John Doe No One <something@likethis.com>
     *
     * This program is free software; you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation; either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program; if not, write to the Free Software
     * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
     */

    import Qt 4.7
    import Aurora.Components 1.0 // This one will help we to call Window component

    Window {
        id: application

        //
        // private
        //

        Component { id: firstPage; SomePage { } } // This makes a component from your next Page(in this case,your first page)

        initialPage: firstPage
    }

After that,you'll create your own page,in this case,it'll be called "SomePage.qml" (without quotes),inside that,you'll add:

-   An identifier (id)
-   Define which area it will take from the screen (anchors.fill: parent)
-   An Rectangle component to do the background
-   A title area
-   (optional) A field area

Basically,your first app sketch will look like:

    /*
     * (C) 2011 John Doe No One <something@likethis.com>
     *
     * This program is free software; you can redistribute it and/or modify
     * it under the terms of the GNU General Public License as published by
     * the Free Software Foundation; either version 2 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU General Public License for more details.
     *
     * You should have received a copy of the GNU General Public License
     * along with this program; if not, write to the Free Software
     * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
     */
    import Qt 4.7
    import Aurora.Components 1.0

    Page {
        id: first_page
        anchors.fill: parent

        Rectangle {
            id: background
            anchors.fill: parent
            color: "black"
        }

        Item {
            id: app_title
            anchors.top: parent.top
            width: parent.width
            height: 70

            Text {
                id: title
                anchors.centerIn: parent
                text: "My First App"
                color: "white"
                font.pixelSize: 26
            }
         }
        Item {
            id: field
            anchors.top: app_title.bottom
            anchors.bottom: parent.bottom
            width:  first_page.width
       }
     }

Now you can implement anything in your code,also switch between pages function,you'll be able to do this like in the first main.qml file,create a Component and call it using **pushPage(component_id);** .
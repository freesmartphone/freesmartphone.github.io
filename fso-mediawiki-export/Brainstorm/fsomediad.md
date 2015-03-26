---
title: Brainstorm fsomediad
permalink: /Brainstorm/fsomediad/
---

Purpose
=======

This service should provide easy and generic way to consume media and fit into the FSO framework (e.g. pause playing on calls)

Current Status
==============

-   Playlists handling
-   Playing http/mms/file streams with ogg,mp3,flac
-   Low memory footprint because constructing pipeline instead of using playbin
-   TODO

What should change
==================

-   split the interfaces to get a higher granularity
-   support more stream/file formats
-   support video playing
-   support viewing pictures
-   support more web services
-   support more playlist formats
-   remote other players
-   zeroconf support?
-   Searching
-   use restricted playbin
-   _use plugin architecture_
-   (run on session bus)
-   ...

Idea
----

Add a new interface to control the different MediaPlayers (MediaPlayerManager?):

-   [s] GetSupported()
-   o GetNewForType( s: type )
-   signal New( o:path, s:type )
-   signal NewType( s: type ) //necessary?

Split interfaces:

-   MusicPlayer
    -   [s] GetInterface() //or use dbus-hlid
    -   s GetType()
    -   [s] GetSupportedPlaylistTypes
    -   TODO
-   Sub interfaces
    -   Control: Play,Pause,Stop,Next,Previous, Get/SetPlaying signals: State, PlayingChanged, Progress
    -   Seek: Forward, Backward, Jump
    -   PlaylistManager: Get/SetCurrentPlaylist, New, ListPlaylists,
    -   Volume: Get/set, Up/Down
    -   Info: Current, ForUri
    -   Video: RequestVideo signals: Available
    -   Equalizer ListChannels, Get/SetChannels
    -   EPG: TODO
    -   Query/Query.Result: TODO
    -   Record: TODO
    -   Sync: TODO
    -   Radio: Scan, TODO
    -   Cam: TakePicture, Start/StopRecording
    -   Share: TODO

<!-- -->

-   Playlist
    -   [s] GetInterface() //or use dbus-hlid
    -   s GetType()
    -   Name()
    -   Files: the old playlist format
    -   Podcast: GetMetadata, TODO
    -

Plugins
=======

-   local Files
-   avahi
-   jamendo
-   youtube
-   seeqpod
-   dreambox?
-   rygel
-   Social Networks?
-   try to get blocked by iTunes :P
-   myspace
-   mpd
-   [xkcd](http://xkcd.com)
-   dilbert
-   facebook
-   ...

Gstreamer Pipeline
==================

To connect your device to other service we have to modify the normal gstreamer pipe. This is my first idea:

[thumb|none|500px|fsomediad Gstreamer pipeline](/image:fsomedia_gstreamer.png "wikilink")

[Category:Maturity Level](/Category:Maturity_Level "wikilink")
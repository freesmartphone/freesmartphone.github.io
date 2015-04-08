
# freesmartphone.org PIM.NoteQuery Interface
            
##Description


This interface gives access to a note query.


##Namespace


```org.freesmartphone.PIM.NoteQuery```


##Methods

* [GetResultCount](#GetResultCount)
* [Rewind](#Rewind)
* [Skip](#Skip)
* [GetNotePath](#GetNotePath)
* [GetResult](#GetResult)
* [GetMultipleResults](#GetMultipleResults)
* [Dispose](#Dispose)


##Signals

* [NoteAdded](#NoteAdded)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

***Returns:***

<i>i: count</i>
Amount of notes in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first note (for this dbus client only). 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n notes in the result cursor (for this dbus client only). 

***Parameters:****

<i>i: count</i>
Amount of notes to skip. 



###<a name="GetNotePath">GetNotePath</a> ( ) &rarr; s


**Description:** Path for the note the result cursor points to. 

***Returns:***

<i>s: note_path</i>
The path to the note. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next note in the query result, and move the query to the next note. 

***Returns:***

<i>a{sv}: item</i>
fields of the result. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple notes from the result set at once. 

***Parameters:****

<i>i: count</i>
The number of notes to get from the result set. A negative value means all. 


***Returns:***

<i>aa{sv}: resultset</i>
The list of the returned notes data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 


#Signals

###
###<a name="NoteAdded">NoteAdded</a> ( s )

**Description:** Sent when a new note which matches this query is loaded. 

***Parameters:***

<i>s: note_path</i>
The path of the newly loaded note. 





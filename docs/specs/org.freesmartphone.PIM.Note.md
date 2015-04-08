
# freesmartphone.org PIM.Note Interface
            
##Description


This interface provides access to one PIM note.


##Namespace


```org.freesmartphone.PIM.Note```


##Methods

* [GetContent](#GetContent)
* [GetMultipleFields](#GetMultipleFields)
* [GetUsedBackends](#GetUsedBackends)
* [Update](#Update)
* [Delete](#Delete)


##Signals

* [NoteDeleted](#NoteDeleted)
* [NoteUpdated](#NoteUpdated)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the fields of one note. 

***Returns:***

<i>a{sv}: note_data</i>
The note's data. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get a specified field list of the note's data. 

***Parameters:****

<i>s: field_list</i>
The list of fields to get, split by "," (coma) char. 


***Returns:***

<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="GetUsedBackends">GetUsedBackends</a> ( ) &rarr; as


**Description:** Get used backends in note. 

***Returns:***

<i>as: backends</i>
The list of backends used in this note. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this note. 

***Parameters:****

<i>a{sv}: note_data</i>
The list of fields/values to update for this note. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this note. 


#Signals

###<a name="NoteDeleted">NoteDeleted</a> ( )


###
###<a name="NoteUpdated">NoteUpdated</a> ( a{sv} )

**Description:** Sent when note is updated. 

***Parameters:***

<i>a{sv}: data</i>
Data used to update note. 





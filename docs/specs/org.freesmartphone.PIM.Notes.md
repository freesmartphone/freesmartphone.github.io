
# freesmartphone.org: freesmartphone.org PIM.Notes Interface
            

#org.freesmartphone.PIM.Notes

##Description


This interface provides access to the collection of PIM notes.


##Namespace


```org.freesmartphone.PIM.Notes```


##Methods

* [Add](Add)
* [GetUsedTags](GetUsedTags)
* [GetSingleEntrySingleField](GetSingleEntrySingleField)
* [Query](Query)


##Signals

* [NewNote](NewNote)
* [NewTag](NewTag)
* [TagRemoved](TagRemoved)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new note to the default backend for notes. 

####Parameters
<i>a{sv}: note_data</i>
The new notes data. 


####Returns
<i>s: note_path</i>
The path of the added note. 



###<a name="GetUsedTags">GetUsedTags</a> ( ) &rarr; as


**Description:** Returns list of all tags used in loaded notes. 

####Returns
<i>as: used_tags</i>
List of tags. 



###<a name="GetSingleEntrySingleField">GetSingleEntrySingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of one field of one note. 

####Parameters
<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to query. 


####Returns
<i>s: value</i>
The content of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Start a query for notes. 

####Parameters
<i>a{sv}: query</i>
The query. 


####Returns
<i>s: query_path</i>
The path for the started query. 



#Signals

###
###<a name="NewNote">NewNote</a> ( s )

**Description:** Sent when a new note is loaded. 

####Parameters
<i>s: note_path</i>
The path of the newly loaded note. 




###
###<a name="NewTag">NewTag</a> ( s )

**Description:** Sent when a newly loaded or updated note has some unused before tag. 

####Parameters
<i>s: tag</i>
The name of new tag. 




###
###<a name="TagRemoved">TagRemoved</a> ( s )

**Description:** Sent when last instance of tag in notes is removed. 

####Parameters
<i>s: tag</i>
The name of removed tag. 



the footer here

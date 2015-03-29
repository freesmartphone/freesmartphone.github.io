
# freesmartphone.org: freesmartphone.org PIM.ContactQuery Interface
            

#org.freesmartphone.PIM.ContactQuery

##Description


This interface gives access to a contact query.


##Namespace


```org.freesmartphone.PIM.ContactQuery```


##Methods

* [GetResultCount](GetResultCount)
* [Rewind](Rewind)
* [Skip](Skip)
* [GetContactPath](GetContactPath)
* [GetResult](GetResult)
* [GetMultipleResults](GetMultipleResults)
* [Dispose](Dispose)


##Signals

* [ContactAdded](ContactAdded)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

####Returns
<i>i: count</i>
Amount of contacts in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first contact (for this dbus client only). 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n contacts in the result cursor (for this dbus client only). 

####Parameters
<i>i: count</i>
Amount of contacts to skip. 



###<a name="GetContactPath">GetContactPath</a> ( ) &rarr; s


**Description:** Path for the contact the result cursor points to. 

####Returns
<i>s: contact_path</i>
The path to the contact. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next contact in the query result, and move the query to the next contact. 

####Returns
<i>a{sv}: item</i>
fields of the result. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple contacts from the result set at once. 

####Parameters
<i>i: count</i>
The number of contacts to get from the result set. A negative value means all. 


####Returns
<i>aa{sv}: resultset</i>
The list of the returned contacts data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 


#Signals

###
###<a name="ContactAdded">ContactAdded</a> ( s )

**Description:** Sent when a new contact which matches this query is loaded. 

####Parameters
<i>s: contact_path</i>
The path of the newly loaded contact. 



the footer here


# freesmartphone.org: freesmartphone.org PIM.Contact Interface
            

#org.freesmartphone.PIM.Contact

##Description


This interface provides access to one PIM contact.


##Namespace


```org.freesmartphone.PIM.Contact```


##Methods

* [GetContent](GetContent)
* [GetMultipleFields](GetMultipleFields)
* [GetUsedBackends](GetUsedBackends)
* [Update](Update)
* [Delete](Delete)


##Signals

* [ContactDeleted](ContactDeleted)
* [ContactUpdated](ContactUpdated)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the fields of one contact. 

####Returns
<i>a{sv}: contact_data</i>
The contact's data. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get a specified field list of the contact's data. 

####Parameters
<i>s: field_list</i>
The list of fields to get, split by "," (coma) char. 


####Returns
<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="GetUsedBackends">GetUsedBackends</a> ( ) &rarr; as


**Description:** Get used backends in contact. 

####Returns
<i>as: backends</i>
The list of backends used in this contact. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this contact. 

####Parameters
<i>a{sv}: contact_data</i>
The list of fields/values to update for this contact. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this contact. 


#Signals

###<a name="ContactDeleted">ContactDeleted</a> ( )


###
###<a name="ContactUpdated">ContactUpdated</a> ( a{sv} )

**Description:** Sent when contact is updated. 

####Parameters
<i>a{sv}: data</i>
Data used to update contact. 



the footer here

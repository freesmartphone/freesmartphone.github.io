
# freesmartphone.org PIM.Date Interface
            
##Description


This interface provides access to one PIM date.


##Namespace


```org.freesmartphone.PIM.Date```


##Methods

* [GetContent](#GetContent)
* [GetMultipleFields](#GetMultipleFields)
* [GetUsedBackends](#GetUsedBackends)
* [Update](#Update)
* [Delete](#Delete)


##Signals

* [DateDeleted](#DateDeleted)
* [DateUpdated](#DateUpdated)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the fields of one date. 

***Returns:***

<i>a{sv}: date_data</i>
The date's data. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get a specified field list of the date's data. 

***Parameters:****

<i>s: field_list</i>
The list of fields to get, split by "," (coma) char. 


***Returns:***

<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="GetUsedBackends">GetUsedBackends</a> ( ) &rarr; as


**Description:** Get used backends in date. 

***Returns:***

<i>as: backends</i>
The list of backends used in this date. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this date. 

***Parameters:****

<i>a{sv}: date_data</i>
The list of fields/values to update for this date. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this date. 


#Signals

###<a name="DateDeleted">DateDeleted</a> ( )


###
###<a name="DateUpdated">DateUpdated</a> ( a{sv} )

**Description:** Sent when date is updated. 

***Parameters:***

<i>a{sv}: data</i>
Data used to update date. 





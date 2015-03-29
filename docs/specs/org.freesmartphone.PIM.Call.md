
# freesmartphone.org: freesmartphone.org PIM.Call Interface
            

#org.freesmartphone.PIM.Call

##Description


This interface provides access to one PIM call.


##Namespace


```org.freesmartphone.PIM.Call```


##Methods

* [GetContent](GetContent)
* [GetMultipleFields](GetMultipleFields)
* [GetUsedBackends](GetUsedBackends)
* [Update](Update)
* [Delete](Delete)


##Signals

* [CallDeleted](CallDeleted)
* [CallUpdated](CallUpdated)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the fields of one call. 

####Returns
<i>a{sv}: call_data</i>
The call's data. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get a specified field list of the call's data. 

####Parameters
<i>s: field_list</i>
The list of fields to get, split by "," (coma) char. 


####Returns
<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="GetUsedBackends">GetUsedBackends</a> ( ) &rarr; as


**Description:** Get used backends in call. 

####Returns
<i>as: backends</i>
The list of backends used in this call. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this call. 

####Parameters
<i>a{sv}: call_data</i>
The list of fields/values to update for this call. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this call. 


#Signals

###<a name="CallDeleted">CallDeleted</a> ( )


###
###<a name="CallUpdated">CallUpdated</a> ( a{sv} )

**Description:** Sent when call is updated. 

####Parameters
<i>a{sv}: data</i>
Data used to update call. 



the footer here


# freesmartphone.org PIM.Calls Interface
            
##Description


This interface provides access to the collection of PIM calls.


##Namespace


```org.freesmartphone.PIM.Calls```


##Methods

* [Add](Add)
* [GetSingleEntrySingleField](GetSingleEntrySingleField)
* [Query](Query)
* [GetNewMissedCalls](GetNewMissedCalls)


##Signals

* [NewCall](NewCall)
* [IncomingCall](IncomingCall)
* [NewMissedCalls](NewMissedCalls)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new call to the default backend for calls. 

***Parameters:****

<i>a{sv}: call_data</i>
The new calls data. 


***Returns:***

<i>s: call_path</i>
The contact path of the added call. 



###<a name="GetSingleEntrySingleField">GetSingleEntrySingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of one field of one call. 

***Parameters:****

<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to query. 


***Returns:***

<i>s: value</i>
The content of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Start a query for calls. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



###<a name="GetNewMissedCalls">GetNewMissedCalls</a> ( ) &rarr; i


**Description:** Get the amount of new missed calls. 

***Returns:***

<i>i: amount</i>
Amount of new missed calls 



#Signals

###
###<a name="NewCall">NewCall</a> ( s )

**Description:** Sent when a new call is loaded. 

***Parameters:***

<i>s: call_path</i>
The path of the newly loaded call. 




###
###<a name="IncomingCall">IncomingCall</a> ( s )

**Description:** Sent when a new missed call is registered. 

***Parameters:***

<i>s: call_path</i>
The path of the newly registered missed call. 




###
###<a name="NewMissedCalls">NewMissedCalls</a> ( i )

**Description:** Sent when amount of new missed calls changes. 

***Parameters:***

<i>i: amount</i>
Amount of new missed calls. 





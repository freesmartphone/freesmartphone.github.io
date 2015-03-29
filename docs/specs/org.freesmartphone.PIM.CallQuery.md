
# freesmartphone.org: freesmartphone.org PIM.CallQuery Interface
            

#org.freesmartphone.PIM.CallQuery

##Description


This interface gives access to a call query.


##Namespace


```org.freesmartphone.PIM.CallQuery```


##Methods

* [GetResultCount](GetResultCount)
* [Rewind](Rewind)
* [Skip](Skip)
* [GetCallPath](GetCallPath)
* [GetResult](GetResult)
* [GetMultipleResults](GetMultipleResults)
* [Dispose](Dispose)


##Signals

* [CallAdded](CallAdded)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

####Returns
<i>i: count</i>
Amount of calls in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first call (for this dbus client only). 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n calls in the result cursor (for this dbus client only). 

####Parameters
<i>i: count</i>
Amount of calls to skip. 



###<a name="GetCallPath">GetCallPath</a> ( ) &rarr; s


**Description:** Path for the call the result cursor points to. 

####Returns
<i>s: call_path</i>
The path to the call. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next call in the query result, and move the query to the next call. 

####Returns
<i>a{sv}: item</i>
fields of the result. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple calls from the result set at once. 

####Parameters
<i>i: count</i>
The number of calls to get from the result set. A negative value means all. 


####Returns
<i>aa{sv}: resultset</i>
The list of the returned calls data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 


#Signals

###
###<a name="CallAdded">CallAdded</a> ( s )

**Description:** Sent when a new call which matches this query is loaded. 

####Parameters
<i>s: call_path</i>
The path of the newly loaded call. 



the footer here

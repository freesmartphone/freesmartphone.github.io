
# freesmartphone.org: freesmartphone.org PIM.MessageQuery Interface
            

#org.freesmartphone.PIM.MessageQuery

##Description


Represent the result of a Query


##Namespace


```org.freesmartphone.PIM.MessageQuery```


##Methods

* [GetResultCount](GetResultCount)
* [Rewind](Rewind)
* [Skip](Skip)
* [GetMessagePath](GetMessagePath)
* [GetResult](GetResult)
* [GetMultipleResults](GetMultipleResults)
* [Dispose](Dispose)


##Signals

* [MessageAdded](MessageAdded)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

####Returns
<i>i: count</i>
Number of contacts in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first message (for this dbus client only) 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n messages in the result cursor (for this dbus client only) 

####Parameters
<i>i: count</i>
Amount of messages to skip 



###<a name="GetMessagePath">GetMessagePath</a> ( ) &rarr; s


**Description:** Path for the message the result cursor points to. 

####Returns
<i>s: message_path</i>
The path to the message. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next message in the query result, and move the query to the next message. 

####Returns
<i>a{sv}: item</i>
Fields of the message. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple message from the result set at once. 

####Parameters
<i>i: count</i>
The amount of messages to get from the result set. A negative value means all. 


####Returns
<i>aa{sv}: resultset</i>
The list of the returned messages data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 


#Signals

###
###<a name="MessageAdded">MessageAdded</a> ( s )

**Description:** Sent when a new message which matches this query is loaded. 

####Parameters
<i>s: message_path</i>
The path of the newly loaded message. 



the footer here

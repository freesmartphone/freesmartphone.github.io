
# freesmartphone.org PIM.Messages Interface
            
##Description


This interface provides access to the list of messages.


##Namespace


```org.freesmartphone.PIM.Messages```


##Methods

* [Add](Add)
* [AddIncoming](AddIncoming)
* [GetSingleEntrySingleField](GetSingleEntrySingleField)
* [Query](Query)
* [QueryThreads](QueryThreads)
* [GetUnreadMessages](GetUnreadMessages)


##Signals

* [NewMessage](NewMessage)
* [IncomingMessage](IncomingMessage)
* [UnreadMessages](UnreadMessages)
* [UpdatedMessage](UpdatedMessage)
* [DeletedMessage](DeletedMessage)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new message to the default message backend. 

***Parameters:****

<i>a{sv}: message_data</i>
The data of the message. 


***Returns:***

<i>s: message_path</i>
The path of the newly added message. 



###<a name="AddIncoming">AddIncoming</a> ( a{sv} ) &rarr; s


**Description:** Add a new message to the default message backend and notify client about incoming message. 

***Parameters:****

<i>a{sv}: message_data</i>
The data of the message. 


***Returns:***

<i>s: message_path</i>
The path of the newly added message. 



###<a name="GetSingleEntrySingleField">GetSingleEntrySingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of a single field of one message. 

***Parameters:****

<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to return the value for. 


***Returns:***

<i>s: value</i>
The value of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Query a list of messages. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



###<a name="QueryThreads">QueryThreads</a> ( a{sv} ) &rarr; s


**Description:** Query a list of message threads. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



###<a name="GetUnreadMessages">GetUnreadMessages</a> ( ) &rarr; i


**Description:** Get the amount of unread incoming messages. 

***Returns:***

<i>i: amount</i>
Amount of unread messages 



#Signals

###
###<a name="NewMessage">NewMessage</a> ( s )

**Description:** Sent when a new message is loaded. 

***Parameters:***

<i>s: message_path</i>
The path of the newly loaded message. 




###
###<a name="IncomingMessage">IncomingMessage</a> ( s )

**Description:** Sent when a incoming message arrives. 

***Parameters:***

<i>s: message_path</i>
The path of the newly arrived incoming message. 




###
###<a name="UnreadMessages">UnreadMessages</a> ( i )

**Description:** Sent when amount of unread incoming messages changes. 

***Parameters:***

<i>i: amount</i>
Amount of unread incoming messages. 




###
###<a name="UpdatedMessage">UpdatedMessage</a> ( sa{sv} )

**Description:** Sent whenever a message has been updated. 

***Parameters:***

<i>s: message_path</i>
The DBus path of the message that was updated. 

<i>a{sv}: message_data</i>
The data that was changed for the message. 




###
###<a name="DeletedMessage">DeletedMessage</a> ( s )

**Description:** Sent whenever a message has been deleted. 

***Parameters:***

<i>s: message_path</i>
The DBus path of the message that has been deleted. 





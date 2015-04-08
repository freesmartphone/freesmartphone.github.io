
# freesmartphone.org PIM.Message Interface
            
##Description


This interface provides access to one message.


##Namespace


```org.freesmartphone.PIM.Message```


##Methods

* [GetContent](#GetContent)
* [GetMultipleFields](#GetMultipleFields)
* [MoveToFolder](#MoveToFolder)
* [Update](#Update)
* [Delete](#Delete)


##Signals

* [MessageDeleted](#MessageDeleted)
* [MessageUpdated](#MessageUpdated)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the content of one message. 

***Returns:***

<i>a{sv}: content</i>
The content of the message. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get the content for a list of fields from the message. 

***Parameters:****

<i>s: field_list</i>
The list of fields to get the content for. 


***Returns:***

<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="MoveToFolder">MoveToFolder</a> ( s )


**Description:** Move this message to a different folder. 

***Parameters:****

<i>s: folder_name</i>
The name of the folder to move the message to. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this message. 

***Parameters:****

<i>a{sv}: message_data</i>
The list of fields/values to update for this message. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this message. 


#Signals

###<a name="MessageDeleted">MessageDeleted</a> ( )


###
###<a name="MessageUpdated">MessageUpdated</a> ( a{sv} )

**Description:** Sent when message is updated. 

***Parameters:***

<i>a{sv}: data</i>
Data used to update message. 





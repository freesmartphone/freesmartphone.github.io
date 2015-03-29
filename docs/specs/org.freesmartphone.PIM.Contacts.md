
# freesmartphone.org PIM.Contacts Interface
            
##Description


This interface provides access to the collection of PIM contacts.


##Namespace


```org.freesmartphone.PIM.Contacts```


##Methods

* [Add](Add)
* [GetSingleEntrySingleField](GetSingleEntrySingleField)
* [Query](Query)


##Signals

* [NewContact](NewContact)
* [UpdatedContact](UpdatedContact)
* [DeletedContact](DeletedContact)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new contact to the default backend for contacts. 

***Parameters:****

<i>a{sv}: contact_data</i>
The new contacts data. 


***Returns:***

<i>s: contact_path</i>
The contact path of the added contact. 



###<a name="GetSingleEntrySingleField">GetSingleEntrySingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of one field of one contact. 

***Parameters:****

<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to query. 


***Returns:***

<i>s: value</i>
The content of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Start a query for contacts. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



#Signals

###
###<a name="NewContact">NewContact</a> ( s )

**Description:** Sent when a new contact is loaded. 

***Parameters:***

<i>s: contact_path</i>
The path of the newly loaded contact. 




###
###<a name="UpdatedContact">UpdatedContact</a> ( sa{sv} )

**Description:** Sent when an existing contact got updated. 

***Parameters:***

<i>s: contact_path</i>
The path of the updated contact. 

<i>a{sv}: contact_data</i>
The part of the contacts data that got changed. 




###
###<a name="DeletedContact">DeletedContact</a> ( s )

**Description:** Sent when a contact got deleted. 

***Parameters:***

<i>s: contact_path</i>
The path of that deleted contact. 





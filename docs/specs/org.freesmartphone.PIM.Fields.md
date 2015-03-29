
# freesmartphone.org PIM.Fields Interface
            
##Description


This interface provides access to field types in domains.


##Namespace


```org.freesmartphone.PIM.Fields```


##Methods

* [AddField](AddField)
* [DeleteField](DeleteField)
* [GetType](GetType)
* [ListFields](ListFields)
* [ListFieldsWithType](ListFieldsWithType)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="AddField">AddField</a> ( ss )


**Description:** Add new field to the list. 

***Parameters:****

<i>s: name</i>
The field's name. 

<i>s: type</i>
The field's type. 



###<a name="DeleteField">DeleteField</a> ( s )


**Description:** Delete field from list. 

***Parameters:****

<i>s: name</i>
The field's name. 



###<a name="GetType">GetType</a> ( s ) &rarr; s


**Description:** Get type of specified field. 

***Parameters:****

<i>s: name</i>
The field's name. 


***Returns:***

<i>s: type</i>
The field's type. 



###<a name="ListFields">ListFields</a> ( ) &rarr; a{ss}


**Description:** List all specified fields and their types. 

***Returns:***

<i>a{ss}: fields</i>
A dictionary with field names and types. 



###<a name="ListFieldsWithType">ListFieldsWithType</a> ( s ) &rarr; as


**Description:** List all fields with specified type. 

***Parameters:****

<i>s: type</i>
Field type. 


***Returns:***

<i>as: fields</i>
A list with field names. 




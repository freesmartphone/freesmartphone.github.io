
# freesmartphone.org PIM.Dates Interface
            
##Description


This interface provides access to the collection of PIM dates.


##Namespace


```org.freesmartphone.PIM.Dates```


##Methods

* [Add](#Add)
* [GetSingleEntrySingleField](#GetSingleEntrySingleField)
* [Query](#Query)


##Signals

* [NewDate](#NewDate)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new date to the default backend for dates. 

***Parameters:****

<i>a{sv}: date_data</i>
The new dates data. 


***Returns:***

<i>s: date_path</i>
The contact path of the added date. 



###<a name="GetSingleEntrySingleField">GetSingleEntrySingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of one field of one date. 

***Parameters:****

<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to query. 


***Returns:***

<i>s: value</i>
The content of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Start a query for dates. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



#Signals

###
###<a name="NewDate">NewDate</a> ( s )

**Description:** Sent when a new date is loaded. 

***Parameters:***

<i>s: date_path</i>
The path of the newly loaded date. 





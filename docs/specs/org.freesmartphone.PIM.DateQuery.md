
# freesmartphone.org PIM.DateQuery Interface
            
##Description


This interface gives access to a date query.


##Namespace


```org.freesmartphone.PIM.DateQuery```


##Methods

* [GetResultCount](GetResultCount)
* [Rewind](Rewind)
* [Skip](Skip)
* [GetDatePath](GetDatePath)
* [GetResult](GetResult)
* [GetMultipleResults](GetMultipleResults)
* [Dispose](Dispose)


##Signals

* [DateAdded](DateAdded)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

***Returns:***

<i>i: count</i>
Amount of dates in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first date (for this dbus client only). 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n dates in the result cursor (for this dbus client only). 

***Parameters:****

<i>i: count</i>
Amount of dates to skip. 



###<a name="GetDatePath">GetDatePath</a> ( ) &rarr; s


**Description:** Path for the date the result cursor points to. 

***Returns:***

<i>s: date_path</i>
The path to the date. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next date in the query result, and move the query to the next date. 

***Returns:***

<i>a{sv}: item</i>
fields of the result. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple dates from the result set at once. 

***Parameters:****

<i>i: count</i>
The number of dates to get from the result set. A negative value means all. 


***Returns:***

<i>aa{sv}: resultset</i>
The list of the returned dates data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 


#Signals

###
###<a name="DateAdded">DateAdded</a> ( s )

**Description:** Sent when a new date which matches this query is loaded. 

***Parameters:***

<i>s: date_path</i>
The path of the newly loaded date. 





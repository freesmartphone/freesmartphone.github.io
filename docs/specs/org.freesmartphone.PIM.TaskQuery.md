
# freesmartphone.org PIM.TaskQuery Interface
            
##Description


This interface gives access to a task query.


##Namespace


```org.freesmartphone.PIM.TaskQuery```


##Methods

* [GetResultCount](GetResultCount)
* [Rewind](Rewind)
* [Skip](Skip)
* [GetTaskPath](GetTaskPath)
* [GetResult](GetResult)
* [GetMultipleResults](GetMultipleResults)
* [Dispose](Dispose)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetResultCount">GetResultCount</a> ( ) &rarr; i


**Description:** Return the number of items in the query result 

***Returns:***

<i>i: count</i>
Amount of tasks in the query result. 



###<a name="Rewind">Rewind</a> ( )

**Description:** Rewind the result cursor to the first task (for this dbus client only). 


###<a name="Skip">Skip</a> ( i )


**Description:** Skip n tasks in the result cursor (for this dbus client only). 

***Parameters:****

<i>i: count</i>
Amount of tasks to skip. 



###<a name="GetTaskPath">GetTaskPath</a> ( ) &rarr; s


**Description:** Path for the task the result cursor points to. 

***Returns:***

<i>s: task_path</i>
The path to the task. 



###<a name="GetResult">GetResult</a> ( ) &rarr; a{sv}


**Description:** Return the next task in the query result, and move the query to the next task. 

***Returns:***

<i>a{sv}: item</i>
fields of the result. 



###<a name="GetMultipleResults">GetMultipleResults</a> ( i ) &rarr; aa{sv}


**Description:** Get multiple tasks from the result set at once. 

***Parameters:****

<i>i: count</i>
The number of tasks to get from the result set. A negative value means all. 


***Returns:***

<i>aa{sv}: resultset</i>
The list of the returned tasks data. 



###<a name="Dispose">Dispose</a> ( )

**Description:** Delete the query result object. 



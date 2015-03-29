
# freesmartphone.org PIM.Tasks Interface
            
##Description


This interface provides access to the collection of PIM tasks.


##Namespace


```org.freesmartphone.PIM.Tasks```


##Methods

* [Add](Add)
* [GetSingleTaskSingleField](GetSingleTaskSingleField)
* [Query](Query)


##Signals

* [NewTask](NewTask)
* [UnfinishedTasks](UnfinishedTasks)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Add">Add</a> ( a{sv} ) &rarr; s


**Description:** Add a new task to the default backend for tasks. 

***Parameters:****

<i>a{sv}: task_data</i>
The new tasks data. 


***Returns:***

<i>s: task_path</i>
The path of the added task. 



###<a name="GetSingleTaskSingleField">GetSingleTaskSingleField</a> ( a{sv}s ) &rarr; s


**Description:** Query the content of one field of one task. 

***Parameters:****

<i>a{sv}: query</i>
The query. 

<i>s: field</i>
The name of the field to query. 


***Returns:***

<i>s: value</i>
The content of the queried field. 



###<a name="Query">Query</a> ( a{sv} ) &rarr; s


**Description:** Start a query for tasks. 

***Parameters:****

<i>a{sv}: query</i>
The query. 


***Returns:***

<i>s: query_path</i>
The path for the started query. 



#Signals

###
###<a name="NewTask">NewTask</a> ( s )

**Description:** Sent when a new task is loaded. 

***Parameters:***

<i>s: task_path</i>
The path of the newly loaded task. 




###
###<a name="UnfinishedTasks">UnfinishedTasks</a> ( i )

**Description:** Sent when amount of unfinished tasks changes. 

***Parameters:***

<i>i: amount</i>
Amount of unfinished tasks. 





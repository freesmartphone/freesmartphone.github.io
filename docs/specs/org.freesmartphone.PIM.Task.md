
# freesmartphone.org: freesmartphone.org PIM.Task Interface
            

#org.freesmartphone.PIM.Task

##Description


This interface provides access to one PIM task.


##Namespace


```org.freesmartphone.PIM.Task```


##Methods

* [GetContent](GetContent)
* [GetMultipleFields](GetMultipleFields)
* [GetUsedBackends](GetUsedBackends)
* [Update](Update)
* [Delete](Delete)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetContent">GetContent</a> ( ) &rarr; a{sv}


**Description:** Get the fields of one task. 

####Returns
<i>a{sv}: task_data</i>
The task's data. 



###<a name="GetMultipleFields">GetMultipleFields</a> ( s ) &rarr; a{sv}


**Description:** Get a specified field list of the task's data. 

####Parameters
<i>s: field_list</i>
The list of fields to get, split by "," (coma) char. 


####Returns
<i>a{sv}: field_data</i>
The data of the requested fields. 



###<a name="GetUsedBackends">GetUsedBackends</a> ( ) &rarr; as


**Description:** Get used backends in task. 

####Returns
<i>as: backends</i>
The list of backends used in this task. 



###<a name="Update">Update</a> ( a{sv} )


**Description:** Update one or more fields of this task. 

####Parameters
<i>a{sv}: task_data</i>
The list of fields/values to update for this task. 



###<a name="Delete">Delete</a> ( )

**Description:** Delete this task. 

the footer here

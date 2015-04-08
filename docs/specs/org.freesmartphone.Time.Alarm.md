
# freesmartphone.org Time Alarm Interface
            
##Description


The Alarm interface is used to register wakeup alarms. Alarm notifications  will be submitted as dbus method calls, hence alarm receivers need to  implement the interface org.freesmartphone.Notification on the root object.  Alarm receivers need to be running dbus system services or dbus system-activatible.  If the system features a suspend mode, the framework will ensure that the  system is awake at the time the alarm triggers.   Multiple alarms per bus name can be registered. If you want to register  named alarm (e.g. agenda items, birthdays, etc.), consider using the PIM  services instead.


##Namespace


```org.freesmartphone.Time.Alarm```


##Methods

* [ClearAlarms](#ClearAlarms)
* [ListAlarms](#ListAlarms)
* [RemoveAlarm](#RemoveAlarm)
* [AddAlarm](#AddAlarm)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="ClearAlarms">ClearAlarms</a> ( s )


**Description:** Clear all scheduled alarms for a given dbus service name. 

***Parameters:****

<i>s: busname</i>
The dbus service bus name to clear all alarms for. 



###<a name="ListAlarms">ListAlarms</a> ( ) &rarr; a(si)


**Description:** List all currently scheduled alarms. 

***Returns:***

<i>a(si): alarms</i>
All currently scheduled alarms. 



###<a name="RemoveAlarm">RemoveAlarm</a> ( si )


**Description:** Removes a scheduled alarm. 

***Parameters:****

<i>s: busname</i>
The dbus service bus name to clear the alarm for. 

<i>i: timestamp</i>
When to call in seconds since 1970 (epoch). 



###<a name="AddAlarm">AddAlarm</a> ( si )


**Description:** Schedules an alarm for a given dbus service name.  The alarm will be triggered by calling the service's  [Alarm](specs/org.freesmartphone.Notification.Alarm)</a> method on the root (/) object. 

***Implementation Note***

Make sure to specify a dbus system service configuration file for  the services that use this interface. This way, you can  receive alarm notifications even when your service is not  running at the time the alarm fires. 



***Parameters:****

<i>s: busname</i>
The dbus service name to call. 

<i>i: timestamp</i>
When to call in seconds since 1970 (epoch). 




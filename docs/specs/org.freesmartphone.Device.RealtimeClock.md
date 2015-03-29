
# freesmartphone.org RealtimeClock Interface
            
##Description


This interface provides access to a Realtime Clock device.


##Namespace


```org.freesmartphone.Device.RealtimeClock```


##Methods

* [GetCurrentTime](GetCurrentTime)
* [SetCurrentTime](SetCurrentTime)
* [GetWakeupTime](GetWakeupTime)
* [SetWakeupTime](SetWakeupTime)


##Signals

* [WakeupTimeChanged](WakeupTimeChanged)
* [Alarm](Alarm)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetCurrentTime">GetCurrentTime</a> ( ) &rarr; i


**Description:** Retrieve the current time from the RTC. 

***Returns:***

<i>i: time</i>
The current time in seconds since epoch. 



###<a name="SetCurrentTime">SetCurrentTime</a> ( i )


**Description:** Set the current time in the RTC. 

***Parameters:****

<i>i: time</i>
The current time in seconds since epoch. 



###<a name="GetWakeupTime">GetWakeupTime</a> ( ) &rarr; i


**Description:** Retrieve the currently programmed wakeup time from the RTC. 

***Returns:***

<i>i: time</i>
The wakeup time in seconds since epoch, if programmed. 0, otherwise. 



###<a name="SetWakeupTime">SetWakeupTime</a> ( i )


**Description:** Program a wakeup time in the RTC. 

***Parameters:****

<i>i: time</i>
The wakeuptime in seconds since epoch. Set to 0, if you want to disable wakeup. 



#Signals

###
###<a name="WakeupTimeChanged">WakeupTimeChanged</a> ( i )

**Description:** Sent, when the programmed RTC wakeup time has been changed. 

***Parameters:***

<i>i: time</i>
The wakeup time in seconds since epoch, if programmed. 0, otherwise. 




###
###<a name="Alarm">Alarm</a> ( i )

**Description:** Sent, when the programmed RTC wakeup time has been reached. 

***Parameters:***

<i>i: time</i>
The wakeup time in seconds since epoch. 





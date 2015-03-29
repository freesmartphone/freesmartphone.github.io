
# freesmartphone.org PowerControl Interface
            
##Description


This interface provides access to a power-controllable device.


##Namespace


```org.freesmartphone.Device.PowerControl```


##Methods

* [GetPower](GetPower)
* [SetPower](SetPower)


##Signals

* [Power](Power)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetPower">GetPower</a> ( ) &rarr; b


**Description:** Get the power status. 

***Returns:***

<i>b: on</i>
True, if the device is powered on. False, otherwise. 



###<a name="SetPower">SetPower</a> ( b )


**Description:** Power the device on, or turn the device off. 

***Parameters:****

<i>b: on</i>
True, if the device should be turned on. False, otherwise. 



#Signals

###
###<a name="Power">Power</a> ( b )

**Description:** Sent, when the device has changed power status. 

***Parameters:***

<i>b: on</i>
True, if the device is now powered on. False, otherwise. 





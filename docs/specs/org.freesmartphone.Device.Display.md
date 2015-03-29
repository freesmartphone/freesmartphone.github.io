
# freesmartphone.org Display Interface
            
##Description


This interface provides access to a display device.


##Namespace


```org.freesmartphone.Device.Display```


##Methods

* [GetBrightness](GetBrightness)
* [SetBrightness](SetBrightness)
* [GetBacklightPower](GetBacklightPower)
* [SetBacklightPower](SetBacklightPower)


##Signals

* [BacklightPower](BacklightPower)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetBrightness">GetBrightness</a> ( ) &rarr; i


**Description:** Get the current brightness level. 

***Returns:***

<i>i: brightness</i>
The brightness level in percent (0-100). 



###<a name="SetBrightness">SetBrightness</a> ( i )


**Description:** Set the brightness level. 

***Implementation Note***

A brightness level of 0 does not necessarily mean that the backlight power is off. 



***Parameters:****

<i>i: brightness</i>
The brightness level in percent (0-100). 



###<a name="GetBacklightPower">GetBacklightPower</a> ( ) &rarr; b


**Description:** Get whether the backlight is powered or not. 

***Returns:***

<i>b: power</i>
True, if the backlight is powered. False, otherwise. 



###<a name="SetBacklightPower">SetBacklightPower</a> ( b )


**Description:** Set whether the backlight should be powered or not. 

***Parameters:****

<i>b: power</i>
True, if the backlight should be powered. False, otherwise. 



#Signals

###
###<a name="BacklightPower">BacklightPower</a> ( b )

**Description:** Send when the backlight brightness (or power) moves to 0 or out of 0. 

***Parameters:***

<i>b: power</i>
True, if the backlight has been turned on. False, otherwise. 





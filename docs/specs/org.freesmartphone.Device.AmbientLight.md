
# freesmartphone.org Ambient Light Interface
            
##Description


This interface provides access to an ambient light device.


##Namespace


```org.freesmartphone.Device.AmbientLight```


##Methods

* [GetAmbientLightBrightness](#GetAmbientLightBrightness)


##Signals

* [AmbientLightBrightness](#AmbientLightBrightness)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetAmbientLightBrightness">GetAmbientLightBrightness</a> ( ) &rarr; ii


**Description:** Get the last ambient light brightness, or -1 if unknown. 

***Returns:***

<i>i: brightness</i>
The last ambientlight. 

<i>i: epoch</i>
Timestamp indicating when this value has been received. 



#Signals

###
###<a name="AmbientLightBrightness">AmbientLightBrightness</a> ( i )

**Description:** Sent, when the ambient light brightness changes. 

***Parameters:***

<i>i: brightness</i>
The new ambient light brightness. 






# freesmartphone.org Input Interface
            
##Description


The Input Interface provides information about the device's buttons, switches, and similar peripheral entities.


##Namespace


```org.freesmartphone.Device.Input```


##Methods

* [GetId](GetId)
* [GetCapabilities](GetCapabilities)


##Signals

* [Event](Event)
* [DirectionalEvent](DirectionalEvent)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetId">GetId</a> ( ) &rarr; s


**Description:** Get the identification of the input device. 

***Returns:***

<i>s: id</i>
The identification. 



###<a name="GetCapabilities">GetCapabilities</a> ( ) &rarr; s


**Description:** Get the capabilities of the input device. 

***Returns:***

<i>s: id</i>
The capabilities. Valid elements are:  <ul>  <li>"keys"</li>,  <li>"relative"</li>,  <li>"absolute"</li>,  <li>"misc"</li>,  <li>"switches"</li>,  <li>"leds"</li>,  <li>"sound"</li>,  <li>"force-feedback"</li>.  </ul> 



#Signals

###
###<a name="Event">Event</a> ( ssi )

**Description:** Sent, when a button or switch input event occurs. 

***Parameters:***

<i>s: name</i>
The name of the event source. 

<i>s: action</i>
The action that triggered the event. Expected values are:  <ul>  <li>"pressed"</li>  <li>"held" (only for selected event sources)</li>  <li>"released"</li>  </ul> 

<i>i: seconds</i>
The duration for the event. Only valid for the "held" and the "released" action. 




###
###<a name="DirectionalEvent">DirectionalEvent</a> ( sii )

**Description:** Sent, when a directional input event occurs. 

***Parameters:***

<i>s: name</i>
The name of the event source. 

<i>i: axis</i>
The axis on which the event happened. 

<i>i: offset</i>
The offset. 





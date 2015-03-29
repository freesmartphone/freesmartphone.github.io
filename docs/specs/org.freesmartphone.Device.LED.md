
# freesmartphone.org LED Interface
            
##Description


This interface provides access to a LED device.


##Namespace


```org.freesmartphone.Device.LED```


##Methods

* [SetBrightness](SetBrightness)
* [SetBlinking](SetBlinking)
* [BlinkSeconds](BlinkSeconds)
* [SetNetworking](SetNetworking)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="SetBrightness">SetBrightness</a> ( i )


**Description:** Set the brightness level. 

***Parameters:****

<i>i: brightness</i>
The brightness level in percent (0-100). 



###<a name="SetBlinking">SetBlinking</a> ( ii )


**Description:** Start blinking. 

***Implementation Note***

This requires the Linux 2.6 LED class trigger 'timer' to be available. 



***Parameters:****

<i>i: on_duration</i>
Duration of being lit in milliseconds. 

<i>i: off_duration</i>
Duration of being unlit in milliseconds. 



###<a name="BlinkSeconds">BlinkSeconds</a> ( iii )


**Description:** Blink the LED for a number of seconds. 

***Implementation Note***

This requires the Linux 2.6 LED class trigger 'timer' to be available. 



***Parameters:****

<i>i: seconds</i>
The amount of time (in seconds) to blink this LED. 

<i>i: on_duration</i>
Duration of being lit in milliseconds. 

<i>i: off_duration</i>
Duration of being unlit in milliseconds. 



###<a name="SetNetworking">SetNetworking</a> ( ss )


**Description:** Start visualizing the network status. 

***Implementation Note***

This requires the Linux 2.6 LED class trigger 'netdev' to be available. 



***Parameters:****

<i>s: interface</i>
The interface to visualize. 

<i>s: mode</i>
A string combined of elements describing the visualization mode. Valid elements are:  <ul>  <li>"link": Visualizes the interface link status (up = lit),</li>  <li>"rx": Visualizes the interface receiving data,</li>  <li>"tx": Visualizes the interface transmitting data.</li>  </ul> 




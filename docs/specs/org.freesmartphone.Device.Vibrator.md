
# freesmartphone.org Vibrator Interface
            
##Description


This interface provides access to a Vibrator device.


##Namespace


```org.freesmartphone.Device.Vibrator```


##Methods

* [VibratePattern](#VibratePattern)
* [Vibrate](#Vibrate)
* [Stop](#Stop)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="VibratePattern">VibratePattern</a> ( iiii )


**Description:** Vibrate in an on/off pattern for a specified number of pulses. 

***Parameters:****

<i>i: pulses</i>
The amount of pulses (on+off iterations). 

<i>i: on_duration_ms</i>
Duration of vibrating in milliseconds. 

<i>i: off_duration_ms</i>
Duration of not vibrating in milliseconds. 

<i>i: strength_percentage</i>
Strength of vibration in percent (0-100). Note that not all vibrators honor this parameter. 



###<a name="Vibrate">Vibrate</a> ( ii )


**Description:** Pulse the vibrator for a specified number of seconds. 

***Parameters:****

<i>i: duration_ms</i>
The amount of time (in milliseconds) to vibrate. 

<i>i: strength_percentage</i>
Strength of vibration in percent (0-100). Note that not all vibrators honor this parameter. 



###<a name="Stop">Stop</a> ( )

**Description:** Cancel any previous commands and stop the vibrator immediately. 



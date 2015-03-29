
# freesmartphone.org GSM Device Interface
            
##Description


The Device interface is used to give information about the GSM  or CDMA device and its capabilities. Use it also to enable or  disable the RF subsystem (which is mandatory for implementing  a flight mode).


##Namespace


```org.freesmartphone.GSM.Device```


##Methods

* [GetFunctionality](GetFunctionality)
* [SetFunctionality](SetFunctionality)
* [GetFeatures](GetFeatures)
* [GetDeviceStatus](GetDeviceStatus)
* [GetSpeakerVolume](GetSpeakerVolume)
* [SetSpeakerVolume](SetSpeakerVolume)
* [GetMicrophoneMuted](GetMicrophoneMuted)
* [SetMicrophoneMuted](SetMicrophoneMuted)


##Signals

* [DeviceStatus](DeviceStatus)
* [KeypadEvent](KeypadEvent)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetFunctionality">GetFunctionality</a> ( ) &rarr; sbs


**Description:** Retrieve the current functionality status of the device. 

***Returns:***

<i>s: level</i>
The functionality level. Expected values are:  <ul>  <li>"minimal": The device is in maximum powersave mode, SIM access is not possible</li>  <li>"airplane": The device is in airplane mode (RF receivers and transmitters have been turned off), SIM access is possible</li>  <li>"full": The device operates with maximum functionality (all units are powered up).</li>  </ul> 

<i>b: autoregister</i>
Whether the device tries to maintain registration with a provider.  This parameter is only valid, if level = "full". 

<i>s: pin</i>
The SIM PIN being used to authenticate if necessary, or an empty string.  This parameter is only valid, if level = "full" or "airplane". 



###<a name="SetFunctionality">SetFunctionality</a> ( sbs )


**Description:** Set the functionality status for this device. 

***Parameters:****

<i>s: level</i>
See <a href="specs/org.freesmartphone.GSM.Device/#GetFunctionality">GetFunctionality</a> 

<i>b: autoregister</i>
Whether the device should try to maintain registration with a provider.  This parameter is only valid, if level = "full". 

<i>s: pin</i>
The SIM PIN being used to authenticate if necessary, or an empty string.  This parameter is only valid, if level = "full" or "airplane". 



###<a name="GetFeatures">GetFeatures</a> ( ) &rarr; a{sv}


**Description:** Get information about the telephony features supported by this device. 

***Returns:***

<i>a{sv}: features</i>
The telephony features supported by this device. Valid tuples are:  <ul>  <li>("voice", bool) = true, if the device supports voice calls,</li>  <li>("csd", bool) = true, if the device supports circuit-switched (data) calls,</li>  <li>("gsm", bool) = true, if the device can operate in a GSM network,</li>  <li>("cdma", bool) = true, if the device can operate in a CDMA network,</li>  <li>("pdp", string) = supported pdp classes, if the device supports packet data communication,</li>  <li>("fax", string) = supported fax classes, if the device supports fax communication,</li>  <li>("facilities", string) = supported security facilities.</li>  </ul> 



###<a name="GetDeviceStatus">GetDeviceStatus</a> ( ) &rarr; s


**Description:** Retrieve the current device status. SIM commands, such as  <a href="specs/org.freesmartphone.GSM.SIM/#ListPhonebooks">ListPhonebooks</a> can not be performed  before the device is in the status 'alive-sim-ready'. 

***Returns:***

<i>s: status</i>
The device status. Expected values are:  <ul>  <li>"unknown" = Device status could not be found,</li>  <li>"closed" = Device is present, but not opened,</li>  <li>"initializing" = Device is being opened,</li>  <li>"alive-no-sim" = Device is operating without a SIM card,</li>  <li>"alive-sim-locked" = Device is operating, SIM card is locked,</li>  <li>"alive-sim-unlocked" = Device is operating, SIM card unlocked,</li>  <li>"alive-sim-ready" = Device is operating, SIM card is ready for access,</li>  <li>"alive-registered" = Device is operating and camped to the network,</li>  <li>"suspending" = Device is suspending,</li>  <li>"suspended" = Device is suspended,</li>  <li>"resuming" = Device is resuming,</li>  <li>"closing" = Device is closing.</li>  </ul> 



###<a name="GetSpeakerVolume">GetSpeakerVolume</a> ( ) &rarr; i


**Description:** Retrieve the current loudspeaker volume. 

***Returns:***

<i>i: volume</i>
The volume in percent (0-100). 



###<a name="SetSpeakerVolume">SetSpeakerVolume</a> ( i )


**Description:** Set the current loudspeaker volume. 

***Implementation Note***

This maps to the GSM 07.07 command +CLVL=... see 3GPP TS 07.07 Chapter 8.2.3. 



***Parameters:****

<i>i: volume</i>
The volume in percent (0-100). 



###<a name="GetMicrophoneMuted">GetMicrophoneMuted</a> ( ) &rarr; b


**Description:** Retrieve whether the microphone is currently muted. 

***Implementation Note***

This maps to the GSM 07.07 command +CMUT?, see 3GPP TS 07.07 Chapter 8.2.4. 



***Returns:***

<i>b: muted</i>
True, if the microphone is muted. False, otherwise. 



###<a name="SetMicrophoneMuted">SetMicrophoneMuted</a> ( b )


**Description:** Mute or unmute the microphone. 

***Implementation Note***

This maps to the GSM 07.07 command +CMUT=... see 3GPP TS 07.07 Chapter 8.2.4. 



***Parameters:****

<i>b: muted</i>
True, to mute the microphone. False, otherwise. 



#Signals

###
###<a name="DeviceStatus">DeviceStatus</a> ( s )

**Description:** Sent on a change in device status. 

***Parameters:***

<i>s: status</i>
The device status. See <a href="specs/org.freesmartphone.GSM.Device/#GetDeviceStatus">GetDeviceStatus</a> for expected values. 




###
###<a name="KeypadEvent">KeypadEvent</a> ( sb )

**Description:** Sent, when a keypad input event occurs. 

***Parameters:***

<i>s: name</i>
The name of the event source. 

<i>b: pressed</i>
True, if the keypad key has been pressed. False, otherwise. 





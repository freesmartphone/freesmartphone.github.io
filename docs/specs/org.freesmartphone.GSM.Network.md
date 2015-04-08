
# freesmartphone.org GSM Network Interface
            
##Description


The Network interface is used to give information about the GSM  service providers and this device's status with regards to  to network registration and connectivity.   Taxonomy note: We think in terms of (service) providers  rather than (network) operators, since multiple (service)  providers can use the networks from operators, however  what actually matters most is the provider name, not the  actual network operator the provider is using.


##Namespace


```org.freesmartphone.GSM.Network```


##Methods

* [Register](#Register)
* [Unregister](#Unregister)
* [GetStatus](#GetStatus)
* [GetSignalStrength](#GetSignalStrength)
* [GetTimeReport](#GetTimeReport)
* [ListProviders](#ListProviders)
* [RegisterWithProvider](#RegisterWithProvider)
* [SetCallingIdentification](#SetCallingIdentification)
* [GetCallingIdentification](#GetCallingIdentification)
* [SendUssdRequest](#SendUssdRequest)


##Signals

* [Status](#Status)
* [SignalStrength](#SignalStrength)
* [TimeReport](#TimeReport)
* [IncomingUssd](#IncomingUssd)
* [CipherStatus](#CipherStatus)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Register">Register</a> ( )

**Description:** Register with any available service provider. 

***Implementation Note***

This maps to the GSM 07.07 command +COPS=0, see 3GPP TS 07.07 Chapter 7.3. 




###<a name="Unregister">Unregister</a> ( )

**Description:** Unregister from service provider. 


###<a name="GetStatus">GetStatus</a> ( ) &rarr; a{sv}


**Description:** Get Network Status. 

***Returns:***

<i>a{sv}: status</i>
Network status information. Mandatory tuples are:  <ul>  <li>( "registration", string ):  <ul> The telephony registration status. Expected values are:  <li>"unregistered" = not registered, not trying,</li>  <li>"home" = registered to home network,</li>  <li>"busy" = not registered, but currently trying,</li>  <li>"denied" = no permitted network available,</li>  <li>"unknown" = no idea,</li>  <li>"roaming" = registered to foreign network.</li>  </ul></li>  <li>( "mode", string ):  <ul>  The registration mode. Expected values are:  <li>"automatic" = automatic selection,</li>  <li>"manual" = manual selection,</li>  <li>"manual;automatic" = manual first, then automatic,</li>  <li>"unregister" = manual unregister,</li>  <li>"unknown" = unknown (this should never occur in production).</li>  </ul></li>  <li>( "act", string ):  <ul>  The network access type. Will default to "GSM" if a modem doesn't support reporting. Expected values are:  <li>"GSM" = GPRS access</li>  <li>"Compact GSM" = </li>  <li>"UMTS" = UMTS access</li>  <li>"EDGE" = Enhanced Data Rates for GSM Evolution </li>  <li>"HSDPA" = High Speed Downlink Packet Access</li>  <li>"HSUPA" = High Speed Uplink Packet Access</li>  <li>"HSDPA/HSUPA" = High Speed Packet Access (both downlink and uplink)</li>  </ul></li>  </ul>  Optional tuples are:  <ul>  <li>( "display", string ): The display name of the network provider (if registered or roaming).</li>  <li>( "provider", string ): The full name of the network provider (if registered or roaming).</li>  <li>( "code", string ): MCC and MNC of the network provider (if registered or roaming).</li>  <ul>  <li>MCC: first three characters starting from the left.</li>  <li>MNC: remaining characters.</li>  </ul>  <li>( "strength", int ): The signal strength in percentage (0-100).</li>  <li>( "lac", string ): The location area code string (if available).</li>  <li>( "cid", string ): The cell id string (if available).</li>  <li>( "pdp.registration", string ): The PDP access registration; values same as telephony registration.  <li>( "pdp.lac", string ): The PDP location area code string (if available).</li>  <li>( "pdp.cid", string ): The PDP cell id string (if available).</li>  </ul> 



###<a name="GetSignalStrength">GetSignalStrength</a> ( ) &rarr; i


**Description:** Query the current signal strength, if registered with a service provider. 

***Returns:***

<i>i: signal_strength</i>
The signal strength in percent (0-100). 



###<a name="GetTimeReport">GetTimeReport</a> ( ) &rarr; iiii


**Description:** Query the last received time report. 

***Returns:***

<i>i: time</i>
The current time in seconds since UNIX epoch.  0, if no time has been received. 

<i>i: timestamp</i>
Timestamp indicating when the time report has been received from the network. 

<i>i: zone</i>
The time zone offset in minutes based on UTC.  This value is only valid, if within the interval ( -1440, 1440 ). 

<i>i: zonestamp</i>
Timestamp indicating when the time report has been received from the network. 



###<a name="ListProviders">ListProviders</a> ( ) &rarr; a(sssss)


**Description:** List available service providers. 

***Returns:***

<i>a(sssss): providers</i>
An array of four-tuples with the following structure:  <ul>  <li>Unique operator code,</li>  <li>Status ("unknown", "available", "current", "forbidden"),</li>  <li>Long Name,</li>  <li>Short Name (optional, may be empty).</li>  <li>Network access type (defaults to "GSM").</li>  </ul> 



###<a name="RegisterWithProvider">RegisterWithProvider</a> ( s )


**Description:** Register to a dedicated service provider. 

***Parameters:****

<i>s: operator_code</i>
The operator code. 



###<a name="SetCallingIdentification">SetCallingIdentification</a> ( s )


**Description:** Set whether your subscriber number is visible during a call. 

***Parameters:****

<i>s: status</i>
One of the following values:  <ul>  <li>"on", if your subscriber number should always be visible to other parties.</li>  <li>"off", if your subscriber number should never be visible to other parties.</li>  <li>"network", if you want to use the network default.</li>  </ul> 



###<a name="GetCallingIdentification">GetCallingIdentification</a> ( ) &rarr; s


**Description:** Get whether your subscriber number is visible during a call. 

***Returns:***

<i>s: status</i>
One of the following values:  <ul>  <li>"on", if your subscriber number is always visible to other parties.</li>  <li>"off", if your subscriber number is never visible to other parties.</li>  <li>"network", if visibility depends on the network settings.</li>  </ul> 



###<a name="SendUssdRequest">SendUssdRequest</a> ( s )


**Description:** Send an Unstructured Supplementary Service Data (USSD) request to the network.  Responses will be delivered via the signal [IncomingUssd](specs/org.freesmartphone.GSM.Network.IncomingUssd)</a> 

***Implementation Note***

This can map to the GSM 07.07 command +CUSD=1,"(request)",(code), see 3GPP TS 07.07 Chapter 7.14. 



***Parameters:****

<i>s: request</i>
The request to be sent to the network. 



#Signals

###
###<a name="Status">Status</a> ( a{sv} )

**Description:** Sent, when the network registration status changes. 

***Parameters:***

<i>a{sv}: status</i>
The registration status. See [GetStatus](specs/org.freesmartphone.GSM.Network.GetStatus)</a> for expected values. 




###
###<a name="SignalStrength">SignalStrength</a> ( i )

**Description:** (OPTIONAL) Sent, when registered with a service provider and the network signal strength changes. 

***Parameters:***

<i>i: signal_strength</i>
The signal strength in percent (0-100). 




###
###<a name="TimeReport">TimeReport</a> ( ii )

**Description:** Sent upon receiving a network time and/or zone report. 

***Parameters:***

<i>i: time</i>
The current time in seconds since UNIX epoch.  0, if no time has been received. 

<i>i: zone</i>
The time zone offset in minutes based on UTC.  This value is only valid, if within the interval ( -1440, 1440 ). 




###
###<a name="IncomingUssd">IncomingUssd</a> ( ss )

**Description:** Sent, when an USSD result or a network initiated request arrives. This signal is usually  sent in response to the method [SendUssdRequest](specs/org.freesmartphone.GSM.Network.SendUssdRequest)</a> 

***Parameters:***

<i>s: mode</i>
The message mode. Valid values are:  <ul>  <li>"completed", if the last user-initiated request has been successfully completed,</li>  <li>"useraction", if this is a network-initiated request and further user action is necessary,</li>  <li>"terminated", if the network terminated the request,</li>  <li>"localclient", if another local client on the network has responded,</li>  <li>"unsupported", if the last user-inititated request is unsupported,</li>  <li>"timeout", if the network has not answered in time.</li>  </ul> 

<i>s: message</i>
The message. Only set if mode is "completed" or "useraction". "", otherwise. 




###
###<a name="CipherStatus">CipherStatus</a> ( ss )

**Description:** Sent, when the network reports a change in telephony or PDP cipher indication. 

***Parameters:***

<i>s: telephony</i>
The telephony cipher: "enabled", "disabled", or "unknown" 

<i>s: pdp</i>
The PDP cipher cipher: "enabled", "disabled", or "unknown" 





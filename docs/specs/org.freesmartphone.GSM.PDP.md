
# freesmartphone.org GSM Packet Data Protocol Interface
            
##Description


The Packet Data Protocol interface is used to set up  binary data connections that allow you to transfer  data over the TCP/IP protocol family routed  via IP-based provider networks.


##Namespace


```org.freesmartphone.GSM.PDP```


##Methods

* [SetCredentials](#SetCredentials)
* [GetCredentials](#GetCredentials)
* [ActivateContext](#ActivateContext)
* [DeactivateContext](#DeactivateContext)
* [GetContextStatus](#GetContextStatus)
* [InternalStatusUpdate](#InternalStatusUpdate)


##Signals

* [ContextStatus](#ContextStatus)


##Properties

* [RoamingAllowed](#RoamingAllowed)


##Errors
*None*

#Methods

###<a name="SetCredentials">SetCredentials</a> ( sss )


**Description:** Set the credentials for PDP context activation. 

***Parameters:****

<i>s: apn</i>
The access point name to connect to. 

<i>s: username</i>
The user name to identify as. 

<i>s: password</i>
The password to identify as. 



###<a name="GetCredentials">GetCredentials</a> ( ) &rarr; sss


**Description:** Get the credentials for PDP context activation. 

***Returns:***

<i>s: apn</i>
The access point name to connect to. 

<i>s: username</i>
The user name to identify as. 

<i>s: password</i>
The password to identify as. 



###<a name="ActivateContext">ActivateContext</a> ( )

**Description:** Request a PDP context activation to an IP-based network service provider. 

***Implementation Note***

Invocation of this command can change your network default route. 




###<a name="DeactivateContext">DeactivateContext</a> ( )

**Description:** Cancel an ongoing ppp session and request a PDP context deactivation. 

***Implementation Note***

This command might change your network default route. 




###<a name="GetContextStatus">GetContextStatus</a> ( ) &rarr; sa{sv}


**Description:** Retrieve the current PDP context status. 

***Returns:***

<i>s: status</i>
The context status. See [ContextStatus](specs/org.freesmartphone.GSM.PDP.ContextStatus)</a> for a list of valid values. 

<i>a{sv}: properties</i>
The context status properties.  See [ContextStatus](specs/org.freesmartphone.GSM.PDP.ContextStatus)</a> for details. 



###<a name="InternalStatusUpdate">InternalStatusUpdate</a> ( sa{sv} )


**Description:** This method is for internal use only. 

***Parameters:****

<i>s: status</i>
Internal use only. 

<i>a{sv}: properties</i>
Internal use only. 



#Signals

###
###<a name="ContextStatus">ContextStatus</a> ( sa{sv} )

**Description:** Sent whenever there is any status or property change on a pdp context in the system. 

***Parameters:***

<i>s: status</i>
The new status of the context. Expected values are:  <ul>  <li>"incoming" = The context is incoming (but not yet accepted),</li>  <li>"outgoing" = The context is outgoing (but not yet established),</li>  <li>"active" = The context is active and has offered a route,</li>  <li>"held" = The context has been interrupted,</li>  <li>"released" = The context is released.</li>  <li>  "suspended" = The context is suspended due out of network coverage or  another internal reason (for example network does not support  simultaneous packet and voice data)  </li>  </ul>  Further information can be part of the properties. 

<i>a{sv}: properties</i>
An array of property values. Note that properties are optional.  Expected tuples are:  <ul>  <li>( "reason", string ) = The reason for the status change,</li>  <li>( "apn", string ) = The number of the access point.</li>  </ul> 




#Properties

###
###<a name="RoamingAllowed">RoamingAllowed</a> - b : Read/Write


**Description:** <p>Specify wether an active PDP context is allowed while modem is roaming.</p>  <p>  If set to false and network registration state indicates that the modem  is roaming PDP context will automatically deactivated and no further  activation will be possible until modem is not roaming anymore.  </p> 
 




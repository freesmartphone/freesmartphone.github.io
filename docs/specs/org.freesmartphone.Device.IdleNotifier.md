
# freesmartphone.org Idle Notification Interface
            
##Description


The Idle Notification Interface provides information about a device's idleness state.


##Namespace


```org.freesmartphone.Device.IdleNotifier```


##Methods

* [GetState](GetState)
* [GetTimeouts](GetTimeouts)
* [SetTimeout](SetTimeout)
* [SetState](SetState)


##Signals

* [State](State)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetState">GetState</a> ( ) &rarr; s


**Description:** Get the current idleness status. 

***Returns:***

<i>s: status</i>
The idleness status. Expected values are:  <ul>  <li>"busy"</li>  <li>"idle"</li>  <li>"idle_dim"</li>  <li>"idle_prelock"</li>  <li>"lock"</li>  <li>"suspend"</li>  <li>"awake"</li>  </ul> 



###<a name="GetTimeouts">GetTimeouts</a> ( ) &rarr; a{si}


**Description:** Gets a list of all the idle states and their correspondent timeouts. 

***Returns:***

<i>a{si}: status</i>
The list of the idle states, and their correspondent timeouts. 



###<a name="SetTimeout">SetTimeout</a> ( si )


**Description:** Sets a timeout value for a given state. 

***Parameters:****

<i>s: status</i>
The idle status. See <a href="specs/org.freesmartphone.Device.IdleNotifier/#GetState">GetState</a> for a list of valid values. 

<i>i: timeout</i>
The timeout value. Set to -1 to disable the state. 



###<a name="SetState">SetState</a> ( s )


**Description:** Forces a new idleness status. 

***Parameters:****

<i>s: status</i>
The idle status. See <a href="specs/org.freesmartphone.Device.IdleNotifier/#GetState">GetState</a> for valid values. 



#Signals

###
###<a name="State">State</a> ( s )

**Description:** Sent, when the idleness status has changed. 

***Parameters:***

<i>s: status</i>
The idle status. See <a href="specs/org.freesmartphone.Device.IdleNotifier/#GetState">GetState</a> for a list of expected values. 





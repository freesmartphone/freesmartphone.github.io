
# freesmartphone.org PowerSupply Interface
            
##Description


This interface provides access to a power supply device.


##Namespace


```org.freesmartphone.Device.PowerSupply```


##Methods

* [GetCapacity](GetCapacity)
* [GetPowerStatus](GetPowerStatus)


##Signals

* [PowerStatus](PowerStatus)
* [Capacity](Capacity)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetCapacity">GetCapacity</a> ( ) &rarr; i


**Description:** Retrieve the capacity of this power supply. 

***Implementation Note***

A wall power supply will always return 100. 



***Returns:***

<i>i: energy</i>
The capacity in percent (0-100). 



###<a name="GetPowerStatus">GetPowerStatus</a> ( ) &rarr; s


**Description:** Retrieve the power status for this power supply. 

***Implementation Note***

A wall power supply will always return "full". 



***Returns:***

<i>s: status</i>
The power status. Expected values for a battery are:  <ul>  <li>"charging"</li>  <li>"discharging"</li>  <li>"full"</li>  <li>"empty"</li>  <li>"critical"</li>  <li>"removed"</li>  <li>"unknown"</li>  </ul>  Additional values for an ac adapter are:  <ul>  <li>"online"</li>  <li>"offline"</li>  </ul>  Additional values for an aggregated supply are:  <ul>  <li>"ac"</li>  </ul> 



#Signals

###
###<a name="PowerStatus">PowerStatus</a> ( s )

**Description:** Sent, when the power status changes significantly. 

***Parameters:***

<i>s: status</i>
The power status. See <a href="specs/org.freesmartphone.PowerSupply/#GetPowerStatus">GetPowerStatus</a> for a list of expected values. 




###
###<a name="Capacity">Capacity</a> ( i )

**Description:** Sent, when the capacity changes. 

***Parameters:***

<i>i: energy</i>
The capacity in percent (0-100). 





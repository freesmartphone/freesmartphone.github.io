
# freesmartphone.org GSM Home Zone Interface
            
##Description


The Home Zone interface allows you to be informed about the home zone status.   Home Zone is a marketing instrument that is used by several operators.  By defining so called 'home zones' on your SIM card, they adjust how much  they charge for your phone calls.


##Namespace


```org.freesmartphone.GSM.HZ```


##Methods

* [GetKnownHomeZones](GetKnownHomeZones)
* [GetHomeZoneStatus](GetHomeZoneStatus)


##Signals

* [HomeZoneStatus](HomeZoneStatus)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetKnownHomeZones">GetKnownHomeZones</a> ( ) &rarr; as


**Description:** Get the names of known home zones as stored on your SIM card. 

***Returns:***

<i>as: zones</i>
The home zone names. 



###<a name="GetHomeZoneStatus">GetHomeZoneStatus</a> ( ) &rarr; s


**Description:** Get current zone name. 

***Returns:***

<i>s: zone</i>
The home zone you are currently on. An empty string denotes  that you are out of all home zones. "unknown" indicates that the system  has not processed the necessary data to compute this information. 



#Signals

###
###<a name="HomeZoneStatus">HomeZoneStatus</a> ( s )

**Description:** Sent, when the home zone status has changed. 

***Parameters:***

<i>s: name</i>
The home zone you are currently on. See <a href="specs/org.freesmartphone.GSM.HZ/#GetHomeZoneStatus">GetHomeZoneStatus</a> 





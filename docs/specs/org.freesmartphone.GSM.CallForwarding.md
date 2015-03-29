
# freesmartphone.org: freesmartphone.org GSM Call Forwarding Interface
            

#org.freesmartphone.GSM.CallForwarding

##Description


The call forwarding interface allows to access the call forwarding  supplementary service according to 3GPP TS 22.082. It supports  enabling and disabling different voice related call forwarding rules  and to query their current status.


##Namespace


```org.freesmartphone.GSM.CallForwarding```


##Methods

* [DisableAll](DisableAll)
* [Enable](Enable)
* [Disable](Disable)
* [GetStatus](GetStatus)


##Signals

* [StatusChanged](StatusChanged)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="DisableAll">DisableAll</a> ( s )


**Description:** Disable all (or only conditional) call forwarding rules. 

####Parameters
<i>s: type</i>
Type of call forwarding rules to disable. Expected values are  <ul>  <li>"all": disable all rules,</li>  <li>"conditional": disable only coniditonal rules  (e.g. busy, not reachable, no reply).</li>  </ul> 



###<a name="Enable">Enable</a> ( ssi )


**Description:** Enable a call forwarding rule. The corresponding properties for the  specified rules will be populated with the values specified. 

####Parameters
<i>s: rule</i>
Call forwarding rule to assign a number and timeout for. Expected values are:  <ul>  <li>"voice unconditional",</li>  <li>"voice busy",</li>  <li>"voice no reply",</li>  <li>"voice not reachable".</li>  </ul> 

<i>s: number</i>
Number the call should be forwarded too. Should be either in national  or international format. 

<i>i: timeout</i>
Timeout after the call forwarding rule should become active. Only accepted  if rule is "voice no reply". 



###<a name="Disable">Disable</a> ( s )


**Description:** Disable a call forwarding rule. 

####Parameters
<i>s: rule</i>
Name of the call forwarding rule. See  <a href="specs/org.freesmartphone.GSM.CallForwarding/#Enable">Enable</a> for a list  of valid values.  The corresponding property for the rule will be unset. 



###<a name="GetStatus">GetStatus</a> ( s ) &rarr; a{sv}


**Description:** Retrieve the current status for a call forwarding rule. 

####Parameters
<i>s: rule</i>
Name of the call forwarding rule. See  <a href="specs/org.freesmartphone.GSM.CallForwarding/#Enable">Enable</a> for a list  of valid values. 


####Returns
<i>a{sv}: status</i>
Status of the call forwarding rule. See <a href="specs/org.freesmartphone.GSM.CallForwarding/#StatusChanged">StatusChanged</a>  for a description of the format. 



#Signals

###
###<a name="StatusChanged">StatusChanged</a> ( sa{sv} )

**Description:** Sent whenver a status of a call forwarding rule has changed. 

####Parameters
<i>s: rule</i>
Name of the call forwarding rule it's status has changed. 

<i>a{sv}: status</i>
Changed status of the call forwarding rule. Expected values are:  <ul>  <li>"active": boolean: Wether the rule is active or not</li>  <li>  "number": string: Number for the call forwarding rule; is empty  if the rule is not active.  </li>  </ul>  If the status of the rule "voice no reply has changed" there is an  additional entry:  <ul>  <li>  "timeout": uint16: Value of the voice "no reply" timeout in  seconds. Should be in a range of [1:30].  </li>  </ul> 



the footer here

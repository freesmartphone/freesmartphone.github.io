
# freesmartphone.org GSM Call Interface
            
##Description


The Call interface is used to initiate, accept, release, and otherwise deal  with voice calls. It also allows you to send DTMF tones.


##Namespace


```org.freesmartphone.GSM.Call```


##Methods

* [Emergency](#Emergency)
* [Activate](#Activate)
* [ActivateConference](#ActivateConference)
* [Release](#Release)
* [HoldActive](#HoldActive)
* [Join](#Join)
* [Transfer](#Transfer)
* [Deflect](#Deflect)
* [ReleaseHeld](#ReleaseHeld)
* [ReleaseAll](#ReleaseAll)
* [Initiate](#Initiate)
* [ListCalls](#ListCalls)
* [SendDtmf](#SendDtmf)


##Signals

* [CallStatus](#CallStatus)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="Emergency">Emergency</a> ( s )


**Description:** Initiate an emergency call. 

***Implementation Note***

This maps to ATD(number);, see v.250. 



***Parameters:****

<i>s: number</i>
The emergency number to dial. National and world-wide restrictions apply. 



###<a name="Activate">Activate</a> ( i )


**Description:** Activate a call as single active call. All previously active calls are  put on hold. No difference is made whether this is an incoming  call or a call that has been put on hold. 

***Implementation Note***

This can map to ATA, see v.250. It might also map to GSM 07.07 +CHLD=..., see 3GPP TS 07.07 Chapter 7.12. 



***Parameters:****

<i>i: id</i>
 



###<a name="ActivateConference">ActivateConference</a> ( i )


**Description:** Activate a call in addition to all previously active calls.  No difference is made whether this is an incoming  call or a call that has been put on hold. 

***Implementation Note***

This maps to GSM 07.07 +CHLD=..., see 3GPP TS 07.07 Chapter 7.12. 



***Parameters:****

<i>i: id</i>
 



###<a name="Release">Release</a> ( i )


**Description:** Release a call. 

***Implementation Note***

This can map to ATH, see v.250. It might also map to GSM 07.07 +CHLD=..., see 3GPP TS 07.07 Chapter 7.12. Some implementations might map it to GSM 07.07 +CHUP=, see 3GPP TS 07.07 Chapter 6.5. 



***Parameters:****

<i>i: id</i>
 



###<a name="HoldActive">HoldActive</a> ( )

**Description:** Hold the active call. 

***Implementation Note***

This maps to GSM 07.07 +CHLD=2, see 3GPP TS 07.07 Chapter 7.12. 




###<a name="Join">Join</a> ( )

**Description:** Join all active and held calls and release yourself from the conversation. 

***Implementation Note***

This maps to GSM 07.07 +CHLD=4, see 3GPP TS 07.07 Chapter 7.12. 




###<a name="Transfer">Transfer</a> ( )

**Description:** Join the currently active and held calls together and disconnect both calls. 

***Implementation Note***

This usually maps to the +CHLD AT command, see 3GPP TS 27.07 Chapter 7.13. 




###<a name="Deflect">Deflect</a> ( s )


**Description:** Deflect an incoming or active call to another number. 

***Implementation Note***

This maps to GSM 07.07 +CTFR=..., see 3GPP TS 27.07 Chapter 7.14. 



***Parameters:****

<i>s: number</i>
The number to transfer the call to. 



###<a name="ReleaseHeld">ReleaseHeld</a> ( )

**Description:** Release all held calls. 

***Implementation Note***

This maps to GSM 07.07 +CHLD=, see 3GPP TS 07.07 Chapter 7.12. 




###<a name="ReleaseAll">ReleaseAll</a> ( )

**Description:** Release all calls, no matter whether active or put on hold. 

***Implementation Note***

This maps to ATH, see v.250. 




###<a name="Initiate">Initiate</a> ( ss ) &rarr; i


**Description:** Initiate an outgoing call. 

***Implementation Note***

This maps to ATD(number);, see v.250. 



***Parameters:****

<i>s: number</i>
The number to call. 

<i>s: type</i>
The type of call to made. Valid values are:  <ul>  <li>"voice" - a GSM voice call,</li>  <li>"data" - a GSM data call,</li>  <li>"fax" - a FAX call.</li>  </ul> 


***Returns:***

<i>i: id</i>
The reference id for this call. It will get assigned by the system. 



###<a name="ListCalls">ListCalls</a> ( ) &rarr; a(isa{sv})


**Description:** Retrieve the status for all calls in the system. 

***Returns:***

<i>a(isa{sv}): call_details</i>
The call status. This is an array containing a call status record for every single call.  See [CallStatus](specs/org.freesmartphone.GSM.Call.CallStatus)</a> signal for a description of the format. 



###<a name="SendDtmf">SendDtmf</a> ( s )


**Description:** Send one or more Dual Tone Multiple Frequency (DTMF) signals during an active call. 

***Implementation Note***

This maps to the TIA IS 101 command +VTS=(value), see 3GPP TS 07.07 Chapter C.2.11.  Note: DTMF signals are always sent to all active calls, this is a limitation of the underlying protocols. 



***Parameters:****

<i>s: tones</i>
The tones to send. Allowed values are: (0-9,#,*,A-D) 



#Signals

###
###<a name="CallStatus">CallStatus</a> ( isa{sv} )

**Description:** Sent whenever there is any status or property change on a call in the system,  no matter whether this is an incoming, active, held, or released call. 

***Parameters:***

<i>i: id</i>
The index of the call that changed its status or properties. 

<i>s: status</i>
The new status of the call. Expected values are:  <ul>  <li>"incoming" = The call is incoming (but not yet accepted),</li>  <li>"outgoing" = The call is outgoing (but not yet established),</li>  <li>"active" = The call is the active call (you can talk),</li>  <li>"held" = The call is being held,</li>  <li>"release" = The call has been released.</li>  </ul>  Further information can be part of the properties. 

<i>a{sv}: properties</i>
An array of property values. Note that some properties are optional. Mandatory tuples are:  <ul>  <li>( "direction", string ) = "incoming" or "outgoing",</li>  <li>( "peer", string ) = The number of the peer (on incoming calls only if we received a CLIP).</li>  </ul>  Optional tuples include:  <ul>  <li>( "reason", string ) = The reason for the status change (on outgoing calls e.g. 'BUSY' or 'NO CARRIER'),</li>  <li>( "auxstatus", string ) = An auxillary connection status (if your modem supports that),</li>  <li>( "line", string ) = The GSM line (0 or 1) this call is taking place (on modems that support multiple lines).</li>  <ul> 





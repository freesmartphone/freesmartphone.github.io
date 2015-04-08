
# freesmartphone.org GSM SIM Interface
            
##Description


The SIM interface is used to access the Subscriber Identification Module (SIM)  plugged as a card into a GSM device. Use it to authenticate yourself  against the GSM network and read/store data from/to the embedded SIM card memory.  Support for accessing the on-card phonebooks and messagebook is also provided.


##Namespace


```org.freesmartphone.GSM.SIM```


##Methods

* [GetAuthStatus](#GetAuthStatus)
* [SendAuthCode](#SendAuthCode)
* [GetUnlockCounters](#GetUnlockCounters)
* [Unlock](#Unlock)
* [ChangeAuthCode](#ChangeAuthCode)
* [SetAuthCodeRequired](#SetAuthCodeRequired)
* [GetAuthCodeRequired](#GetAuthCodeRequired)
* [GetSimInfo](#GetSimInfo)
* [SendGenericSimCommand](#SendGenericSimCommand)
* [SendRestrictedSimCommand](#SendRestrictedSimCommand)
* [GetHomeZoneParameters](#GetHomeZoneParameters)
* [GetPhonebookInfo](#GetPhonebookInfo)
* [DeleteEntry](#DeleteEntry)
* [StoreEntry](#StoreEntry)
* [RetrievePhonebook](#RetrievePhonebook)
* [GetServiceCenterNumber](#GetServiceCenterNumber)
* [SetServiceCenterNumber](#SetServiceCenterNumber)
* [DeleteMessage](#DeleteMessage)
* [StoreMessage](#StoreMessage)
* [SendStoredMessage](#SendStoredMessage)
* [RetrieveMessage](#RetrieveMessage)


##Signals

* [AuthStatus](#AuthStatus)
* [IncomingMessage](#IncomingMessage)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetAuthStatus">GetAuthStatus</a> ( ) &rarr; s


**Description:** Retrieve the authentication status for the SIM card. 

***Returns:***

<i>s: status</i>
The authentication status for the SIM card. Values to expect:  <ul>  <li>"UNKNOWN" = unknown (possibly due to SIM communication error or SIM not inserted)</li>  <li>"READY" = not waiting for any PIN or PUK,</li>  <li>"SIM PIN" = waiting for SIM PIN to be given,</li>  <li>"SIM PUK" = waiting for SIM PUK to be given,</li>  <li>"SIM PIN2" = waiting for SIM PIN 2 to be given,</li>  <li>"SIM PUK2" = waiting for SIM PUK 2 to be given.</li>  </ul> 



###<a name="SendAuthCode">SendAuthCode</a> ( s )


**Description:** Send authentication code (PIN) for the SIM card. 

***Parameters:****

<i>s: pin</i>
The authentication code. 



###<a name="GetUnlockCounters">GetUnlockCounters</a> ( ) &rarr; a{sv}


**Description:** Retrieve the unlock counters for the SIM card. 

***Implementation Note***

This is outside the GSM standard and only supported on some devices. 



***Returns:***

<i>a{sv}: counters</i>
The unlock counters for the SIM card. 



###<a name="Unlock">Unlock</a> ( ss )


**Description:** Send unlock code (PUK) and new authentication code (PIN). 

***Parameters:****

<i>s: puk</i>
The unlock code. 

<i>s: new_pin</i>
The new authentication code. 



###<a name="ChangeAuthCode">ChangeAuthCode</a> ( ss )


**Description:** Change the authentication code. 

***Parameters:****

<i>s: old_pin</i>
The old authentication code. 

<i>s: new_pin</i>
The new authentication code. 



###<a name="SetAuthCodeRequired">SetAuthCodeRequired</a> ( bs )


**Description:** Enable or disable checking for the SIM card authentification on startup. 

***Parameters:****

<i>b: check</i>
True, to turn SIM card authentification on. False, to turn it off. 

<i>s: pin</i>
A valid authentication code. 



###<a name="GetAuthCodeRequired">GetAuthCodeRequired</a> ( ) &rarr; b


**Description:** Retrieve whether the SIM card checks for authentification on startup. 

***Returns:***

<i>b: check</i>
True, if SIM card authentification is turned on. False, otherwise. 



###<a name="GetSimInfo">GetSimInfo</a> ( ) &rarr; a{sv}


**Description:** Get information stored on the SIM card. 

***Returns:***

<i>a{sv}: info</i>
Information about the SIM card. Possible tuples are:  <ul>  <li>("imsi", string) = The unique subscriber identification stored on your SIM.</li>  <li>("issuer", string) = The unique subscriber identification stored on your SIM.</li>  <li>("phonebooks", space-separated string) = The phonebooks stored on this SIM.  Expected values are "contacts", "dialed", "received", "own", "missed", "emergency".  Other phonebooks are named included with their native code and prefixed "aux:".</li>  <li>("slots") = The capacity of the messagebook</li>  <li>("messages") = The messages in the messagebook</li>  </ul> 



###<a name="SendGenericSimCommand">SendGenericSimCommand</a> ( s ) &rarr; s


**Description:** Send a generic SIM command to the SIM card. 

***Parameters:****

<i>s: command</i>
The command to send, encoded as described in GSM 11.11. 


***Returns:***

<i>s: result</i>
The result of the command, encoded as described in GSM 11.11. 



###<a name="SendRestrictedSimCommand">SendRestrictedSimCommand</a> ( iiiiis ) &rarr; s


**Description:** Send a restricted SIM command to the SIM card. 

***Parameters:****

<i>i: command</i>
The command to send. Valid values are:  <ul>  <li>176 = READ BINARY,</li>  <li>178 = READ RECORD,</li>  <li>192 = GET RESPONSE,</li>  <li>214 = UPDATE BINARY,</li>  <li>220 = UPDATE RECORD,</li>  <li>242 = STATUS.</li>  </ul> 

<i>i: fileid</i>
The identifier of an elementary datafile on SIM. Mandatory for every command except STATUS. 

<i>i: p1</i>
Parameter 1 passed to the SIM. Mandatory for every command except STATUS and GET RESPONSE. 

<i>i: p2</i>
Parameter 1 passed to the SIM. Mandatory for every command except STATUS and GET RESPONSE. 

<i>i: p3</i>
Parameter 1 passed to the SIM. Mandatory for every command except STATUS and GET RESPONSE. 

<i>s: data</i>
The command data to the SIM, encoded as described in GSM 11.11. 


***Returns:***

<i>s: result</i>
The result of the command, encoded as described in GSM 11.11. 



###<a name="GetHomeZoneParameters">GetHomeZoneParameters</a> ( ) &rarr; a(siii)


**Description:** Retrieve the homezones coordinates, if stored on the SIM. 

***Returns:***

<i>a(siii): homezones</i>
An array containing up to four homezones in Gauss-Krueger coordinates. The array contains of four-tuples with the following format:  <ol>  <li>(name:string), the name of the zone,</li>  <li>(x:int), the X value of the zone center in Gauss-Krueger format,</li>  <li>(y:int), the Y value of the zone center in Gauss-Krueger format,</li>  <li>(r:radius), the R*R value of the zone dimension in meters.</li>  </ol> 



###<a name="GetPhonebookInfo">GetPhonebookInfo</a> ( s ) &rarr; iii


**Description:** Request information about a phonebook. 

***Parameters:****

<i>s: category</i>
The phonebook storage category.  See [GetSimInfo](specs/org.freesmartphone.GSM.SIM.GetSimInfo)</a> for valid categories. 


***Returns:***

<i>i: slots</i>
Capacity of the phonebook. 

<i>i: numberlength</i>
Maximum length for the phone number. 

<i>i: namelength</i>
Maximum length for the associated name. 



###<a name="DeleteEntry">DeleteEntry</a> ( si )


**Description:** Delete an entry in the SIM phonebook. 

***Parameters:****

<i>s: category</i>
The phonebook storage category. See [GetSimInfo](specs/org.freesmartphone.GSM.SIM.GetSimInfo)</a>  for a list of valid categories. 

<i>i: index</i>
Index of entry to delete. 



###<a name="StoreEntry">StoreEntry</a> ( siss )


**Description:** Store an entry in the SIM phonebook. 

***Parameters:****

<i>s: category</i>
The phonebook storage category. See [GetSimInfo](specs/org.freesmartphone.GSM.SIM.GetSimInfo)</a>  for a list of valid categories. 

<i>i: index</i>
The index of the entry to store. 

<i>s: name</i>
The name corresponding to the number. 

<i>s: number</i>
The number corresponding to the name. 



###<a name="RetrievePhonebook">RetrievePhonebook</a> ( sii ) &rarr; a(iss)


**Description:** Retrieve (parts of) a SIM phonebook. 

***Parameters:****

<i>s: category</i>
The phonebook storage category.  Use [GetSimInfo](specs/org.freesmartphone.GSM.SIM.GetSimInfo)</a> to gather the list of valid categories. 

<i>i: mindex</i>
The minimum index of the entry to retrieve. 

<i>i: maxdex</i>
The maximum index of entries to receive. 


***Returns:***

<i>a(iss): entries</i>
The phonebook entries. This is an array of three-tuples. Every entry has the following structure:  <ul>  <li>(int:index) = storage index.</li>  <li>(string:name) = name.</li>  <li>(string:number) = number.</li>  </ul> 



###<a name="GetServiceCenterNumber">GetServiceCenterNumber</a> ( ) &rarr; s


**Description:** Retrieve phone number of SMS Center. 

***Returns:***

<i>s: number</i>
The SMS Center Number. 



###<a name="SetServiceCenterNumber">SetServiceCenterNumber</a> ( s )


**Description:** Set phone number of SMS Center. 

***Parameters:****

<i>s: number</i>
The SMS Center Number. 



###<a name="DeleteMessage">DeleteMessage</a> ( i )


**Description:** Delete a message in the SIM messagebook. 

***Parameters:****

<i>i: index</i>
The storage index of the message to delete. 



###<a name="StoreMessage">StoreMessage</a> ( ssa{sv} ) &rarr; i


**Description:** Store a message in the SIM messagebook. 

***Parameters:****

<i>s: recipient_number</i>
The number of the recipient. 

<i>s: contents</i>
The contents of the message. 

<i>a{sv}: properties</i>
For a list of valid properties see [SendMessage](specs/org.freesmartphone.GSM.SMS.SendMessage)</a> 


***Returns:***

<i>i: index</i>
The index of the new message. 



###<a name="SendStoredMessage">SendStoredMessage</a> ( i ) &rarr; is


**Description:** Sends a message stored in the SIM messagebook. 

***Parameters:****

<i>i: index</i>
The index of the message. 


***Returns:***

<i>i: transaction_index</i>
The given transaction index for this message. 

<i>s: timestamp</i>
The timestamp this message was received by the SMSC 



###<a name="RetrieveMessage">RetrieveMessage</a> ( i ) &rarr; sssa{sv}


**Description:** Retrieve a message from the SIM messagebook. 

***Parameters:****

<i>i: index</i>
The index of the message to retrieve. 


***Returns:***

<i>s: status</i>
The category the message is in, one of ("read", "sent", "unread", "unsent"). 

<i>s: sender_number</i>
The number of the sender. 

<i>s: contents</i>
The contents of the message. 

<i>a{sv}: properties</i>
Additional properties (TBD). 



#Signals

###
###<a name="AuthStatus">AuthStatus</a> ( s )

**Description:** Sent, when the authentication status for the SIM card changes. 

***Parameters:***

<i>s: status</i>
The authentication status for the SIM card. See [GetAuthStatus](specs/org.freesmartphone.GSM.SIM.GetAuthStatus)</a> for a list of expected values. 




###
###<a name="IncomingMessage">IncomingMessage</a> ( i )

**Description:** Sent, when a new message has been received and stored on the SIM card. 

***Parameters:***

<i>i: index</i>
The storage index of the new message. 





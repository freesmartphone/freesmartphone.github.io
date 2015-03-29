
# freesmartphone.org: freesmartphone.org GSM SMS Interface
            

#org.freesmartphone.GSM.SMS

##Description


org.freesmartphone.GSM.SMS is a high level interface for  textual Short Message Service (SMS). If you have special  requirements or need direct access to individual messages,  you may use the corresponding SMS functions provided by  org.freesmartphone.GSM.SIM.


##Namespace


```org.freesmartphone.GSM.SMS```


##Methods

* [RetrieveTextMessages](RetrieveTextMessages)
* [GetSizeForTextMessage](GetSizeForTextMessage)
* [SendTextMessage](SendTextMessage)


##Signals

* [IncomingTextMessage](IncomingTextMessage)
* [IncomingMessageReport](IncomingMessageReport)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="RetrieveTextMessages">RetrieveTextMessages</a> ( ) &rarr; a(issssa{sv})


**Description:** Retrieve all text messages. 

####Returns
<i>a(issssa{sv}): messages</i>
Messages matching the given category. This is an array of four-tuples. Every entry has the following structure:  <ul>  <li>(int:index) = storage index,</li>  <li>(string:status) = status of message, one of ("read", "unread", "sent", "unsent"),</li>  <li>(string:number) = sender number.</li>  <li>(string:timestamp) = timestamp.</li>  <li>(string:content) = contents of the message.</li>  </ul> 



###<a name="GetSizeForTextMessage">GetSizeForTextMessage</a> ( s ) &rarr; u


**Description:** Calculates the number of GSM Short Messages necessary to deliver a given text. 

####Parameters
<i>s: contents</i>
The contents of the message. 


####Returns
<i>u: messages</i>
The number of SMS to be sent, if this message were to be delivered. 



###<a name="SendTextMessage">SendTextMessage</a> ( ssb ) &rarr; is


**Description:** Sends a text message via the GSM Short Message Service (SMS) 

***Implementation Note***

Text messages can be of unlimited length. They might get fragmented by the  underlying message transport layers though. This will happen transparently. 



####Parameters
<i>s: recipient_number</i>
The number of the recipient. 

<i>s: contents</i>
The contents of the message. 

<i>b: report</i>
If true, status reports (message receipts) will be sent by the  SMS Center, delivered via the <a href="specs/org.freesmartphone.GSM.SMS/#IncomingMessageReceipt">IncomingMessageReceipt</a> signal. 


####Returns
<i>i: reference</i>
This is the message-reference number of this message.  This can be used to identify status reports. 

<i>s: timestamp</i>
The timestamp this message was received by the SMSC. 



#Signals

###
###<a name="IncomingTextMessage">IncomingTextMessage</a> ( sss )

**Description:** Sent, when a text message has been received. 

####Parameters
<i>s: number</i>
The number of the sender. 

<i>s: timestamp</i>
The timestamp of the message. 

<i>s: contents</i>
The contents of the message. 




###
###<a name="IncomingMessageReport">IncomingMessageReport</a> ( isss )

**Description:** Sent when a status report for a message has been received. 

####Parameters
<i>i: reference</i>
The message-reference number as returned by <a href="specs/org.freesmartphone.GSM.SMS/#SendTextMessage">SendTextMessage</a> 

<i>s: status</i>
The status. Expected values are:  <ul>  <li>COMPLETED_RECEIVED</li>  <li>COMPLETED_UNABLE_TO_CONFIRM</li>  <li>COMPLETED_REPLACED</li>  <li>COMPLETED_LAST</li>  <li>TEMPORARY_CONGESTION</li>  <li>TEMPORARY_SME_BUSY</li>  <li>TEMPORARY_NO_RESPONSE</li>  <li>TEMPORARY_SERVICE_REJECTED</li>  <li>TEMPORARY_QOS_UNAVAILABLE</li>  <li>TEMPORARY_SME_ERROR</li>  <li>TEMPORARY_LAST</li>  <li>PERMANENT_RP_ERROR</li>  <li>PERMANENT_INVALID_DESTINATION</li>  <li>PERMANENT_CONNECTION_REJECTED</li>  <li>PERMANENT_NOT_OBTAINABLE</li>  <li>PERMANENT_QOS_UNAVAILABLE</li>  <li>PERMANENT_INTERWORKING_UNAVAILABLE</li>  <li>PERMANENT_VALIDITY_PERIOD_EXPIRED</li>  <li>PERMANENT_DELETED</li>  <li>PERMANENT_SC_ADMIN_DELETED</li>  <li>PERMANENT_SM_DOES_NOT_EXIST</li>  <li>PERMANENT_LAST</li>  <li>TEMPFINAL_CONGESTION</li>  <li>TEMPFINAL_SME_BUSY</li>  <li>TEMPFINAL_NO_RESPONSE</li>  <li>TEMPFINAL_SERVICE_REJECTED</li>  <li>TEMPFINAL_QOS_UNAVAILABLE</li>  <li>TEMPFINAL_SME_ERROR</li>  <li>TEMPFINAL_LAST  </ul> 

<i>s: sender_number</i>
The number of the sender. 

<i>s: contents</i>
Optional contents of the receipt. Will usually be empty. 



the footer here

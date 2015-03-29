
# freesmartphone.org: freesmartphone.org GSM Voice Mail Interface
            

#org.freesmartphone.GSM.VoiceMail

##Description


The Voice Mail interface gives access to the voice mail status.   Voice Mail is a feature provided by several operators, in which an answering  machine (voice mailbox) is provided to a caller, if the callee can't be  reached or doesn't want to be reached (i.e. by sending busy).


##Namespace


```org.freesmartphone.GSM.VoiceMail```


##Methods

* [GetVoiceMailboxNumber](GetVoiceMailboxNumber)
* [SetVoiceMailboxNumber](SetVoiceMailboxNumber)
* [GetStoredVoiceMails](GetStoredVoiceMails)


##Signals

* [IncomingVoiceMail](IncomingVoiceMail)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetVoiceMailboxNumber">GetVoiceMailboxNumber</a> ( ) &rarr; s


**Description:** Retrieve phone number of Voice Mailbox. 

####Returns
<i>s: number</i>
The Voice mailbox number. 



###<a name="SetVoiceMailboxNumber">SetVoiceMailboxNumber</a> ( s )


**Description:** Set phone number of Voice Mailbox. 

####Parameters
<i>s: number</i>
The Voice mailbox nNumber. 



###<a name="GetStoredVoiceMails">GetStoredVoiceMails</a> ( ) &rarr; as


**Description:** Retrieve the indices of stored voice mails on your voice mailbox. 

####Returns
<i>as: zones</i>
The home zone names. 



#Signals

###
###<a name="IncomingVoiceMail">IncomingVoiceMail</a> ( i )

**Description:** Sent, when a new voice mail has been stored on the voice mailbox. 

####Parameters
<i>i: index</i>
The storage index of the new message. 



the footer here


# freesmartphone.org: freesmartphone.org GSM Cell Broadcast Interface
            

#org.freesmartphone.GSM.CB

##Description


The Cell Broadcast interface allows you to manage cell broadcast subscriptions.   Cell Broadcast is a technology that allows a text or binary message to be defined  and distributed to all mobile terminals connected to a set of cells. Whereas SMS  messages are sent point-to-point, Cell Broadcast messages are sent point-to-area.  This means that one Cell Broadcast message can reach a huge number of terminals  at once.


##Namespace


```org.freesmartphone.GSM.CB```


##Methods

* [GetCellBroadcastSubscriptions](GetCellBroadcastSubscriptions)
* [SetCellBroadcastSubscriptions](SetCellBroadcastSubscriptions)


##Signals

* [IncomingCellBroadcast](IncomingCellBroadcast)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetCellBroadcastSubscriptions">GetCellBroadcastSubscriptions</a> ( ) &rarr; s


**Description:** Get current cell broadcast subscription channels. 

####Returns
<i>s: channels</i>
The channels you are subscribed to. Simple strings to expect are  "none" and "all". Also valid are compound descriptions of channel lists like  "1,2,3-5,7,234,10-5". 



###<a name="SetCellBroadcastSubscriptions">SetCellBroadcastSubscriptions</a> ( s )


**Description:** Set cell broadcast subscription channels. 

####Parameters
<i>s: channels</i>
The channels you want to subscribe. Valid simple strings are  "none" and "all". Also valid are compound descriptions of channels lists like  "1,2,3-5,7,234,10-5". 



#Signals

###
###<a name="IncomingCellBroadcast">IncomingCellBroadcast</a> ( ssa{sv} )

**Description:** Sent, when a cell broadcast message has been received. 

####Parameters
<i>s: text</i>
The text of the message. 

<i>s: language</i>
The language encoding. 

<i>a{sv}: properties</i>
Additional properties. 



the footer here


# freesmartphone.org GSM Debug Interface
            
##Description


The Debug interface is used to debug (sic!). You can ping the device,  execute test commands, inject unsolicited responses, or be updated  about the detailed modem status.


##Namespace


```org.freesmartphone.GSM.Debug```


##Methods

* [DebugCommand](DebugCommand)
* [DebugInjectResponse](DebugInjectResponse)
* [DebugPing](DebugPing)


##Signals

* [DebugStatus](DebugStatus)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="DebugCommand">DebugCommand</a> ( ss ) &rarr; s


**Description:** Sends a debug command. 

***Implementation Note***

WARNING: Only use this, if you know what you are doing.  You may crash the device or the service, if you send bogus commands. 



***Parameters:****

<i>s: command</i>
The command to send. Note that the validity of commands depends  on the actual modem channel. Not all modem channels are AT channels!  It is recommended to implement a 'help' command that returns a  list of valid commands. 

<i>s: channel</i>
The channel to send this command on. Set to "" to use the default one. 


***Returns:***

<i>s: result</i>
The result of the command 



###<a name="DebugInjectResponse">DebugInjectResponse</a> ( ss )


**Description:** Injects an unsolicited response into the command queue. 

***Implementation Note***

WARNING: Only use this, if you know what you are doing.  You may crash the device or the service, if you inject bogus responses. 



***Parameters:****

<i>s: response</i>
The response to inject. 

<i>s: channel</i>
The channel to inject this command on. Set to "" to use the default one. 



###<a name="DebugPing">DebugPing</a> ( )

**Description:** Ping the device. 


#Signals

###
###<a name="DebugStatus">DebugStatus</a> ( a{ss} )

**Description:** Sent, when the modem status changes. 

***Parameters:***

<i>a{ss}: channels</i>
 





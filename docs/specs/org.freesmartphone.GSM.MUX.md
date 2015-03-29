
# freesmartphone.org: freesmartphone.org GSM MUX Interface
            

#org.freesmartphone.GSM.MUX

##Description


The MUX interface is used to manage and control virtual serial channels  (implemented through pseudo TTYs) which are multiplexed to one serial  line as described in 3GPP TS 07.10.


##Namespace


```org.freesmartphone.GSM.MUX```


##Methods

* [OpenSession](OpenSession)
* [CloseSession](CloseSession)
* [AllocChannel](AllocChannel)
* [ReleaseChannel](ReleaseChannel)
* [SetStatus](SetStatus)


##Signals

* [Status](Status)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="OpenSession">OpenSession</a> ( bisi )


**Description:** Initiate a new multiplexing session. 

***Implementation Note***

The device needs to support the +CMUX command. 



####Parameters
<i>b: advanced</i>
True, to use 07.10 Advanced Mode multiplexing, False to use 07.10 Basic Mode multiplexing. 

<i>i: framesize</i>
The maximum framesize for 07.10 multiplexing frames. 

<i>s: portname</i>
The port name to use. 

<i>i: portspeed</i>
The port speed to use. 



###<a name="CloseSession">CloseSession</a> ( )

**Description:** Closes a multiplexing session. 

***Implementation Note***

The device will be left in AT command mode. 




###<a name="AllocChannel">AllocChannel</a> ( si ) &rarr; si


**Description:** Allocate a new virtual channel. Raises <a href="specs/org.freesmartphone.GSM.MUX/#NoChannel">NoChannel</a>  if the requested channel can not be allocated. Raises <a href="specs/org.freesmartphone.GSM.MUX/#ChannelTaken">ChannelTaken</a>  if the requested channel is already allocated. 

####Parameters
<i>s: origin</i>
A handle for channel user identification. 

<i>i: channel</i>
The requested channel. Submit 0 to request the next free channel. 


####Returns
<i>s: path</i>
The pseudo tty connected to the virtual channel. 

<i>i: allocated_channel</i>
The channel number that has been allocated. 



###<a name="ReleaseChannel">ReleaseChannel</a> ( s )


**Description:** Release all channels requested by a specified user. 

####Parameters
<i>s: origin</i>
A handle for channel user identification. 



###<a name="SetStatus">SetStatus</a> ( is )


**Description:** Modify the v24 status of a virtual channel. 

####Parameters
<i>i: channel</i>
The virtual channel you want to change the outgoing status for. 

<i>s: status</i>
The new v.24 status. See <a href="specs/org.freesmartphone.GSM.MUX/#Status">Status</a> for the format. 



#Signals

###
###<a name="Status">Status</a> ( s )

**Description:** Sent whenever there is v.24 incoming status change on a virtual channel. 

####Parameters
<i>s: status</i>
The new v.24 status, which is a string combined of elements that make up the status. Valid elements are:  <ul>  <li>...</li>  <li>...</li>  </ul> 



the footer here

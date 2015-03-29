
# freesmartphone.org: freesmartphone.org Phone Call Interface
            

#org.freesmartphone.Phone.Call

##Description


The Call Interface is used to represent a communication channel.


##Namespace


```org.freesmartphone.Phone.Call```


##Methods

* [GetPeer](GetPeer)
* [Initiate](Initiate)
* [Activate](Activate)
* [Release](Release)
* [GetStatus](GetStatus)
* [Remove](Remove)


##Signals

* [Incoming](Incoming)
* [Outgoing](Outgoing)
* [Released](Released)
* [Activated](Activated)


##Properties
*None*

##Errors

* [Unauthorized](Unauthorized)


#Methods

###<a name="GetPeer">GetPeer</a> ( ) &rarr; s


**Description:** Return the number of the peer (usually the number of the call). 

####Returns
<i>s: peer</i>
The number of the peer. 



###<a name="Initiate">Initiate</a> ( ) &rarr; s


**Description:** Initiate the call. 

####Returns
<i>s: status</i>
The new status of the Call (should be 'Initiating'). 



###<a name="Activate">Activate</a> ( ) &rarr; s


**Description:** Accept the call. 

####Returns
<i>s: status</i>
The new status of the Call (should be 'Activating'). 



###<a name="Release">Release</a> ( ) &rarr; s


**Description:** Release the call. 

####Returns
<i>s: status</i>
The new status of the Call (should be 'Releasing'). 



###<a name="GetStatus">GetStatus</a> ( ) &rarr; s


**Description:** Return the current status of the call. 

####Returns
<i>s: status</i>
The current status of the Call. 



###<a name="Remove">Remove</a> ( )

**Description:** Remove the call object when it is not needed anymore. 


#Signals

###<a name="Incoming">Incoming</a> ( )


###<a name="Outgoing">Outgoing</a> ( )


###<a name="Released">Released</a> ( )


###<a name="Activated">Activated</a> ( )


#Errors

###<a name="Unauthorized">Unauthorized</a>

**Description:** Raised, if registering with the specified network is not possible. 

the footer here

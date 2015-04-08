
# freesmartphone.org Network Interface
            
##Description


The Network interface provides access to high level networking functions.  Please see org.moblin.connman and org.bluez for low level networking functions.


##Namespace


```org.freesmartphone.Network```


##Methods

* [StartConnectionSharingWithInterface](#StartConnectionSharingWithInterface)
* [StopConnectionSharingWithInterface](#StopConnectionSharingWithInterface)
* [OfferDefaultRoute](#OfferDefaultRoute)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="StartConnectionSharingWithInterface">StartConnectionSharingWithInterface</a> ( s )


**Description:** Start sharing the internet connection of this device with any clients  connected to the specified network interface via DHCP. 

***Implementation Note***

Might launch a dhcp server process and adjust IP tables. 



***Parameters:****

<i>s: interface</i>
The network interface to start sharing the connectivity with. 



###<a name="StopConnectionSharingWithInterface">StopConnectionSharingWithInterface</a> ( s )


**Description:** Stop sharing the internet connection of this device with any clients  connected to the specified network interface via DHCP. 

***Implementation Note***

Might stop a dhcp server process and adjust IP tables. 



***Parameters:****

<i>s: interface</i>
The network interface to stop sharing the connectivity with. 



###<a name="OfferDefaultRoute">OfferDefaultRoute</a> ( sssssss )


**Description:** Offer a default route to the internet. 

***Implementation Note***

NOTE that this method is for TESTING purposes only. Eventually connman will be used for that. 



***Parameters:****

<i>s: technology</i>
The technology offering the default route. 

<i>s: interface</i>
The network interface offering the default route. 

<i>s: ipv4address</i>
The network address to configure the interface with. 

<i>s: ipv4mask</i>
The network mask to configure the interface with. 

<i>s: ipv4gateway</i>
The network gateway address for the default route. 

<i>s: dns1</i>
The first DNS address. 

<i>s: dns2</i>
The second DNS address. 




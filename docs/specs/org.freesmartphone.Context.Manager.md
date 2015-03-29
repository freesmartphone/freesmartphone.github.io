
# freesmartphone.org Context Manager Interface
            
##Description


The Context Manager interface allows you to register for environmental  context updates, such as geolocation updates, region monitoring, etc.


##Namespace


```org.freesmartphone.Context.Manager```


##Methods

* [SubscribeLocationUpdates](SubscribeLocationUpdates)
* [UnsubscribeLocationUpdates](UnsubscribeLocationUpdates)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="SubscribeLocationUpdates">SubscribeLocationUpdates</a> ( s )


**Description:** Subscribe for receiving location updates. 

***Implementation Note***

To receive location updates, clients need to implement the <a href="specs/org.freesmartphone.Context/#Client">Client</a> interface 



***Parameters:****

<i>s: desired_accuracy</i>
The desired accuracy. Valid values are: navigation, best, nearest-ten-meters, hundred-meters, one-kilometer, three-kilometers, hundred-kilometers. 



###<a name="UnsubscribeLocationUpdates">UnsubscribeLocationUpdates</a> ( )

**Description:** Unsubscribe from receiving location updates. 



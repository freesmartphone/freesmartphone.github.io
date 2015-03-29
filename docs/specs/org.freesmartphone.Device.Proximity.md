
# freesmartphone.org Proximity Interface
            
##Description


This interface provides access to a proximity device.


##Namespace


```org.freesmartphone.Device.Proximity```


##Methods

* [GetProximity](GetProximity)


##Signals

* [Proximity](Proximity)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetProximity">GetProximity</a> ( ) &rarr; ii


**Description:** Get the last percentage value of the proximity device (most probably 0 or 100), or -1 if unknown. 

***Returns:***

<i>i: proximity</i>
The last proximity. 

<i>i: epoch</i>
Timestamp indicating when this value has been received. 



#Signals

###
###<a name="Proximity">Proximity</a> ( i )

**Description:** Sent, when the proximity changes. 

***Parameters:***

<i>i: proximity</i>
The new proximity in percentage (most probably 0 or 100). 





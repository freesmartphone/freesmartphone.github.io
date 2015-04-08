
# freesmartphone.org Phone Interface
            
##Description


The Phone object is used to create Call objects using different protocols.


##Namespace


```org.freesmartphone.Phone```


##Methods

* [InitProtocols](#InitProtocols)
* [CreateCall](#CreateCall)


##Signals

* [Incoming](#Incoming)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="InitProtocols">InitProtocols</a> ( ) &rarr; as


**Description:** Initialize all the protocols. 

***Returns:***

<i>as: protocols</i>
The list of all the protocols names. 



###<a name="CreateCall">CreateCall</a> ( ssb ) &rarr; o


**Description:** Create a new Call to a given number, with an optional protocol. 

***Parameters:****

<i>s: number</i>
A string representing the number of the peer. 

<i>s: protocol</i>
The name of the protocol as returned by InitProtocols,  if None the best protocol will be used. Default to None 

<i>b: force</i>
If true, we destroy any already present call object to this number. Default to True 


***Returns:***

<i>o: call</i>
The path to the new Call object 



#Signals

###
###<a name="Incoming">Incoming</a> ( o )

**Description:** Emitted when a new call is incoming 

***Parameters:***

<i>o: call</i>
Path to the Call object. 






# freesmartphone.org Usage Interface
            
##Description


The Usage interface provides access to subsystem resource management.  The usage manager keeps track of all users per resource and will enable or disable the  associated hardware/software as requested. Before an application can make use of a subsystem,  it needs to request the resource first and is only allowed to use it if the request  has been granted.


##Namespace


```org.freesmartphone.Usage```


##Methods

* [RegisterResource](#RegisterResource)
* [UnregisterResource](#UnregisterResource)
* [ListResources](#ListResources)
* [GetResourcePolicy](#GetResourcePolicy)
* [SetResourcePolicy](#SetResourcePolicy)
* [GetResourceState](#GetResourceState)
* [GetResourceUsers](#GetResourceUsers)
* [RequestResource](#RequestResource)
* [ReleaseResource](#ReleaseResource)
* [Suspend](#Suspend)
* [Resume](#Resume)
* [Shutdown](#Shutdown)
* [Reboot](#Reboot)


##Signals

* [ResourceAvailable](#ResourceAvailable)
* [ResourceChanged](#ResourceChanged)
* [SystemAction](#SystemAction)


##Properties
*None*

##Errors

* [PolicyUnknown](#PolicyUnknown)
* [PolicyDisabled](#PolicyDisabled)
* [ResourceUnknown](#ResourceUnknown)
* [ResourceExists](#ResourceExists)
* [ResourceInUse](#ResourceInUse)
* [UserExists](#UserExists)
* [UserUnknown](#UserUnknown)


#Methods

###<a name="RegisterResource">RegisterResource</a> ( so )


**Description:** Register yourself as provider for a given resource. 

***Implementation Note***

Providers can chose the name of the resource freely, note that there are  some well known names such as:  <ul>  <li>"GSM",</li>  <li>"GPS",</li>  <li>"Bluetooth",</li>  <li>"WiFi",</li>  <li>"Display",</li>  <li>"CPU".</li>  </ul>  In any case, only one provider per resource can be registered at a given time. 



***Parameters:****

<i>s: name</i>
The resource name. 

<i>o: path</i>
The resource path. 



###<a name="UnregisterResource">UnregisterResource</a> ( s )


**Description:** Unregister yourself as provider for a given resource. 

***Implementation Note***

Leaving the bus will automatically unregister yourself for all resources you are providing. 



***Parameters:****

<i>s: name</i>
The resource name. 



###<a name="ListResources">ListResources</a> ( ) &rarr; as


**Description:** List available resources. 

***Returns:***

<i>as: resources</i>
An array of resource names. 



###<a name="GetResourcePolicy">GetResourcePolicy</a> ( s ) &rarr; s


**Description:** Get the current resource policy for a given resource. 

***Parameters:****

<i>s: name</i>
The resource name. 


***Returns:***

<i>s: policy</i>
The resource policy. Expected values are:  <ul>  <li>"disabled" - using this resource is currently not allowed,</li>  <li>"auto" - the resource is enabled as long as it is used by at least one client,</li>  <li>"enabled" - the resource is enabled even without a client.</li>  </ul> 



###<a name="SetResourcePolicy">SetResourcePolicy</a> ( ss )


**Description:** Set a new resource policy for a given resource. 

***Parameters:****

<i>s: name</i>
The resource name. 

<i>s: policy</i>
The new resource policy. See [GetResourcePolicy](specs/org.freesmartphone.Usage.GetResourcePolicy)</a> for a list of valid values. 



###<a name="GetResourceState">GetResourceState</a> ( s ) &rarr; b


**Description:** Get the current state for a given resource. 

***Parameters:****

<i>s: name</i>
The resource name. 


***Returns:***

<i>b: state</i>
The resource state. True if the resource is currently enabled. 



###<a name="GetResourceUsers">GetResourceUsers</a> ( s ) &rarr; as


**Description:** Get the users which currently use a given resource. 

***Parameters:****

<i>s: name</i>
The resource name. 


***Returns:***

<i>as: users</i>
An array of bus names using the resource. 



###<a name="RequestResource">RequestResource</a> ( s )


**Description:** Request occupation of a given resource. An error is returned if the resource was not occupied sucessfully. 

***Parameters:****

<i>s: name</i>
The resource name. 



###<a name="ReleaseResource">ReleaseResource</a> ( s )


**Description:** Release a given resource. 

***Implementation Note***

Resources in use get autoreleased when a client leaves the bus. 



***Parameters:****

<i>s: name</i>
The resource name. 



###<a name="Suspend">Suspend</a> ( )

**Description:** Triggers a suspend on all managed resources and puts the device into suspend mode.  When the device comes back from suspend, all resources are resumed.  All Resources need to implement [Suspend](specs/org.freesmartphone.Resource.Suspend)</a> and  [Resume](specs/org.freesmartphone.Resource.Resume)</a> if they have anything to prepare / recover  on suspend and resume. 


###<a name="Resume">Resume</a> ( ss )


**Description:** Triggers a resume on all managed resources and puts the device into normal mode. 

***Implementation Note***

This method is only useful on systems where a suspend does not halt the main CPU. 



***Parameters:****

<i>s: source</i>
The resume source. 

<i>s: reason</i>
The resume reason. 



###<a name="Shutdown">Shutdown</a> ( )

**Description:** Triggers a shutdown of all managed resources and powers the device down. 


###<a name="Reboot">Reboot</a> ( )

**Description:** Triggers a reboot of the device. 


#Signals

###
###<a name="ResourceAvailable">ResourceAvailable</a> ( sb )

**Description:** Sent whenever a resource is added or removed. 

***Parameters:***

<i>s: name</i>
The name of the resource. 

<i>b: availability</i>
The resource availability. True if the resource is currently available. 




###
###<a name="ResourceChanged">ResourceChanged</a> ( sba{sv} )

**Description:** Sent whenever a resource status changes. 

***Parameters:***

<i>s: name</i>
The name of the resource. 

<i>b: state</i>
The resource state. True if the resource is currently enabled. 

<i>a{sv}: attributes</i>
The new status of the resource. Expected values are:  <ul>  <li>"policy": The current resource policy</li>  <li>"refcount": The count of clients that have requested the resource</li>  </ul>  Further information can be part of the properties. 




###
###<a name="SystemAction">SystemAction</a> ( s )

**Description:** Sent whenever a system state action is performed. 

***Parameters:***

<i>s: action</i>
The name of the action. Expected values are:  <ul>  <li>"suspend": The system is suspending.</li>  <li>"resume": The system has resumed.</li>  <li>"reboot": The system is rebooting.</li>  <li>"shutdown": The system is shutting down.</li>  </ul> 




#Errors

###<a name="PolicyUnknown">PolicyUnknown</a>

**Description:** Raised, if the requested policy is unknown. 


###<a name="PolicyDisabled">PolicyDisabled</a>

**Description:** Raised, if the requested resource is set to policy "disabled". 


###<a name="ResourceUnknown">ResourceUnknown</a>

**Description:** Raised, if the requested resource is unknown. 


###<a name="ResourceExists">ResourceExists</a>

**Description:** Raised, if a (new) resource has already been registered. 


###<a name="ResourceInUse">ResourceInUse</a>

**Description:** Raised, if the to-be-disabled (by policy) resource is still in use. 


###<a name="UserExists">UserExists</a>

**Description:** Raised, if the requested resource has already been requested by the same user. 


###<a name="UserUnknown">UserUnknown</a>

**Description:** Raised, if the to-be-released resource has never been requested by the user. 



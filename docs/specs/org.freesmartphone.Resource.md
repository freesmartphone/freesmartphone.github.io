
# freesmartphone.org: freesmartphone.org Resource Interface
            

#org.freesmartphone.Resource

##Description


The Resource interface provides access to a resource as visible from the FSO usage subsystem.  Every resource provider has to implement this interface.  Applications other than FSO usage are not allowed to use this interface, they have to  use the org.freesmartphone.Usage API.


##Namespace


```org.freesmartphone.Resource```


##Methods

* [Enable](Enable)
* [Disable](Disable)
* [Suspend](Suspend)
* [Resume](Resume)
* [GetDependencies](GetDependencies)
* [GetDefaultPolicy](GetDefaultPolicy)


##Signals
*None*

##Properties
*None*

##Errors

* [NotEnabled](NotEnabled)
* [UnableToEnable](UnableToEnable)


#Methods

###<a name="Enable">Enable</a> ( )

**Description:** Enable the resource. 


###<a name="Disable">Disable</a> ( )

**Description:** Disable the resource. 


###<a name="Suspend">Suspend</a> ( )

**Description:** Suspend the resource. 


###<a name="Resume">Resume</a> ( )

**Description:** Resume the resource. 


###<a name="GetDependencies">GetDependencies</a> ( ) &rarr; a{sv}


**Description:** The resource is able to lists its dependencies.   For example a resource can depend on another resource. If this resource  is enabled the dependency resource will be enabled first. 

####Returns
<i>a{sv}: dependencies</i>
Dependencies required for resource operation. Expected values are:  <ul>  <li>"services": A comma-separated string of service names</li>  <li>"processes": A comma-separated string of process names</li>  </ul>  Dependencies are being activated / deactivated as defined by the resource lifecycle. 



###<a name="GetDefaultPolicy">GetDefaultPolicy</a> ( ) &rarr; s


**Description:** The resource is able to provide the default policy to use. 

####Returns
<i>s: policy</i>
The default policy to use for this resource. See  <a href="specs/org.freesmartphone.Usage/#GetResourcePolicy">GetResourcePolicy</a> for a list of possible values. 



#Errors

###<a name="NotEnabled">NotEnabled</a>

**Description:** Raised, if the resource is not enabled. 


###<a name="UnableToEnable">UnableToEnable</a>

**Description:** Raised, if the resource can not be enabled. 

the footer here

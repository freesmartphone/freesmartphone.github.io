
# freesmartphone.org Preferences Service Interface
            
##Description


The service object deals with configuration values of a given service   The service can set and get the value of parameters.   The services are used to group related parameters together.  Basically, every application using the config server should use its own service name.   For each service we need a schema file describing the parameters the service provides.   The configurations values are stored in yaml file.  Each conf file contains all the parameters for a given service in a given context.  The conf files are organised with the following file hierachy :  conf/$(service)/$(profile).yaml   All the parameters that are independant of the profile are stored in the 'default' profile file.   When we set or get parameters, the service server takes into account the current profile,  so the applications using the service don't need to know about the current profile.


##Namespace


```org.freesmartphone.Preferences.Service```


##Methods

* [GetKeys](#GetKeys)
* [GetValue](#GetValue)
* [SetValue](#SetValue)
* [IsProfilable](#IsProfilable)
* [GetType](#GetType)


##Signals

* [Notify](#Notify)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetKeys">GetKeys</a> ( ) &rarr; as


**Description:** Retrieve all the keys of the service.   This method should be used only for introspection purposes. 

***Returns:***

<i>as: keys</i>
The list of keys. 



###<a name="GetValue">GetValue</a> ( s ) &rarr; v


**Description:** Get a parameter value. 

***Parameters:****

<i>s: key</i>
The parameter key string. 


***Returns:***

<i>v: value</i>
The value associated with the key. 



###<a name="SetValue">SetValue</a> ( sv )


**Description:** Set a parameter value. 

***Parameters:****

<i>s: key</i>
The parameter key string. 

<i>v: value</i>
The new value associated with the key. 



###<a name="IsProfilable">IsProfilable</a> ( s ) &rarr; b


**Description:** Return true if a parameter depends on the current profile. 

***Parameters:****

<i>s: key</i>
The parameter key string. 


***Returns:***

<i>b: profileable</i>
True if a parameter depends on the current profile. 



###<a name="GetType">GetType</a> ( s ) &rarr; s


**Description:** Return a string representing the type of the parameter. 

***Parameters:****

<i>s: key</i>
The parameter key string. 


***Returns:***

<i>s: type</i>
A string representing the type of the parameter. 



#Signals

###
###<a name="Notify">Notify</a> ( sv )

**Description:** Sent whenever there is a change in a parameter value in the service 

***Parameters:***

<i>s: key</i>
The parameter key string. 

<i>v: value</i>
The new value of the parameter. 





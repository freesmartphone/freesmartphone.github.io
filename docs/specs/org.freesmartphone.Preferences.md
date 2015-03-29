
# freesmartphone.org: freesmartphone.org Preferences Interface
            

#org.freesmartphone.Preferences

##Description


All the preferences values are grouped into services.   The Preferences object is used to get the preferences Services objects.  It can also set the current profile value.


##Namespace


```org.freesmartphone.Preferences```


##Methods

* [GetServices](GetServices)
* [GetService](GetService)
* [GetProfiles](GetProfiles)
* [GetProfile](GetProfile)
* [SetProfile](SetProfile)


##Signals

* [Changed](Changed)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetServices">GetServices</a> ( ) &rarr; as


**Description:** Return the list of all available services. 

####Returns
<i>as: services</i>
The list of all available services. 



###<a name="GetService">GetService</a> ( s ) &rarr; o


**Description:** Retrieve a given service. 

####Parameters
<i>s: name</i>
the name of the service, as returned by `GetServices`. 


####Returns
<i>o: service</i>
the path to the service object 



###<a name="GetProfiles">GetProfiles</a> ( ) &rarr; as


**Description:** Return a list of all the available profiles. 

####Returns
<i>as: profile</i>
The list of all the available profiles. 



###<a name="GetProfile">GetProfile</a> ( ) &rarr; s


**Description:** Retrieve the current top profile. 

####Returns
<i>s: profile</i>
The name of the current profile. 



###<a name="SetProfile">SetProfile</a> ( s )


**Description:** Set the current top profile. 

####Parameters
<i>s: profile</i>
The name of the new current profile. 



#Signals

###
###<a name="Changed">Changed</a> ( s )

**Description:** Sent whenever there is a change of the active profile 

####Parameters
<i>s: profile</i>
The name of the new profile. 



the footer here

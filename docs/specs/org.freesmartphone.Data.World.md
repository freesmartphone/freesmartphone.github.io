
# freesmartphone.org Data World Interface
            
##Description


The World interface is used to query (more or less static) information about  the communication world, such as countries and their timezones, mobile broadband  provider apns, etc.


##Namespace


```org.freesmartphone.Data.World```


##Methods

* [GetAllCountries](#GetAllCountries)
* [GetCountryCodeForMccMnc](#GetCountryCodeForMccMnc)
* [GetTimezonesForCountryCode](#GetTimezonesForCountryCode)
* [GetApnsForMccMnc](#GetApnsForMccMnc)
* [GetProviderNameForMccMnc](#GetProviderNameForMccMnc)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetAllCountries">GetAllCountries</a> ( ) &rarr; a(ss)


**Description:** Retrieves all known country codes and their (english) name. 

***Returns:***

<i>a(ss): countries</i>
A list of country codes and their (english) names. 



###<a name="GetCountryCodeForMccMnc">GetCountryCodeForMccMnc</a> ( s ) &rarr; s


**Description:** Retrieve a country code for MCC or concatenated MCC and MNC.  Raises [InvalidParameter](specs/org.freesmartphone.Error.InvalidParameter)</a> if not found. 

***Parameters:****

<i>s: mcc_mnc</i>
MCC or concatenated MCC and MNC. 


***Returns:***

<i>s: country_code</i>
The country code that owns the specified MCC (and MNC). 



###<a name="GetTimezonesForCountryCode">GetTimezonesForCountryCode</a> ( s ) &rarr; a{ss}


**Description:** Retrieves the list of timezones given a country code.  Raises [InvalidParameter](specs/org.freesmartphone.Error.InvalidParameter)</a> if not found. 

***Parameters:****

<i>s: country_code</i>
The country code. 


***Returns:***

<i>a{ss}: timezones</i>
A dictionary of coordinates and timezone names. 



###<a name="GetApnsForMccMnc">GetApnsForMccMnc</a> ( s ) &rarr; a(ssssss)


**Description:** Retrieves a list of data connectivity (GPRS, EDGE, 3G)  access point names for MCC or concatenated MCC and MNC.  Raises [InvalidParameter](specs/org.freesmartphone.Error.InvalidParameter)</a> if not found. 

***Parameters:****

<i>s: mcc_mnc</i>
MCC or concatenated MCC and MNC. 


***Returns:***

<i>a(ssssss): apns</i>
A list of six-tuples descriping a connectivity access point. Structure is: 



###<a name="GetProviderNameForMccMnc">GetProviderNameForMccMnc</a> ( s ) &rarr; s


**Description:** Retrieves the name of a provider for a supplied concatenated MCC and MNC.  Raises [InvalidParameter](specs/org.freesmartphone.Error.InvalidParameter)</a> if not found. 

***Parameters:****

<i>s: mcc_mnc</i>
MCC or concatenated MCC and MNC. 


***Returns:***

<i>s: provider</i>
Name of the provider. 




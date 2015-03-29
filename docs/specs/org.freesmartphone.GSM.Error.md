
# freesmartphone.org GSM Errors
            
##Description


The org.freesmartphone.GSM.Error domain describes common errors clients should expect when calling FSO GSM DBus APIs.


##Namespace


```org.freesmartphone.GSM.Error0```


##Methods
*None*

##Signals
*None*

##Properties
*None*

##Errors

* [DeviceNotPresent](DeviceNotPresent)
* [DeviceTimeout](DeviceTimeout)
* [DeviceFailed](DeviceFailed)
* [AuthorizationRequired](AuthorizationRequired)
* [SimNotPresent](SimNotPresent)
* [SimAuthFailed](SimAuthFailed)
* [SimBlocked](SimBlocked)
* [SimNotFound](SimNotFound)
* [SimMemoryFull](SimMemoryFull)
* [SimInvalidIndex](SimInvalidIndex)
* [CallNotFound](CallNotFound)
* [MuxChannelTaken](MuxChannelTaken)
* [MuxNoChannel](MuxNoChannel)
* [MuxNoSession](MuxNoSession)
* [MuxSessionAlreadyOpen](MuxSessionAlreadyOpen)
* [MuxSessionOpenError](MuxSessionOpenError)
* [NetworkNotPresent](NetworkNotPresent)
* [NetworkUnauthorized](NetworkUnauthorized)
* [NetworkNotSupported](NetworkNotSupported)
* [NetworkNotFound](NetworkNotFound)
* [ContextNotFound](ContextNotFound)


#Errors

###<a name="DeviceNotPresent">DeviceNotPresent</a>

**Description:** Raised, when the device is not present. 


###<a name="DeviceTimeout">DeviceTimeout</a>

**Description:** Raised, when the device does not answer within the specified time for this operation. 


###<a name="DeviceFailed">DeviceFailed</a>

**Description:** Raised, when the device reported an unrecoverable error. 


###<a name="AuthorizationRequired">AuthorizationRequired</a>

**Description:** Raised, if an authentication code is required before this operation can succeed. 


###<a name="SimNotPresent">SimNotPresent</a>

**Description:** Raised, if there is no SIM card present. 


###<a name="SimAuthFailed">SimAuthFailed</a>

**Description:** Raised, if the SIM authentication code is not accepted. 


###<a name="SimBlocked">SimBlocked</a>

**Description:** Raised, if the SIM has been deactivated or is otherwise not allowed to join a network. 


###<a name="SimNotFound">SimNotFound</a>

**Description:** Raised, if a data record on the SIM is not present. 


###<a name="SimMemoryFull">SimMemoryFull</a>

**Description:** Raised, if there is not enough space for a data record on the SIM. 


###<a name="SimInvalidIndex">SimInvalidIndex</a>

**Description:** Raised, if the requested messagebook or phonebook entry is out of bounds. 


###<a name="CallNotFound">CallNotFound</a>

**Description:** Raised, if the specified call is not present. 


###<a name="MuxChannelTaken">MuxChannelTaken</a>

**Description:** Raised, when the requested channel is already allocated. 


###<a name="MuxNoChannel">MuxNoChannel</a>

**Description:** Raised, when the device can't allocate the requested channel. 


###<a name="MuxNoSession">MuxNoSession</a>

**Description:** Raised, when there is no active session. 


###<a name="MuxSessionAlreadyOpen">MuxSessionAlreadyOpen</a>

**Description:** Raised, when a session has already been opened. 


###<a name="MuxSessionOpenError">MuxSessionOpenError</a>

**Description:** Raised, when the session can not be opened. 


###<a name="NetworkNotPresent">NetworkNotPresent</a>

**Description:** Raised, if no network service is available. 


###<a name="NetworkUnauthorized">NetworkUnauthorized</a>

**Description:** Raised, if registering with the specified network is not possible. 


###<a name="NetworkNotSupported">NetworkNotSupported</a>

**Description:** Raised, if the requested network operation is not supported. 


###<a name="NetworkNotFound">NetworkNotFound</a>

**Description:** Raised, if a requested network provider is not present. 


###<a name="ContextNotFound">ContextNotFound</a>

**Description:** Raised, if the specified PDP context is not present. 



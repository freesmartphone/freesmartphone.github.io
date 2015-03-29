
# freesmartphone.org Audio Interface
            
##Description


This interface provides access to notification sounds, sound scenarios, and mixer controls.


##Namespace


```org.freesmartphone.Device.Audio```


##Methods

* [PlaySound](PlaySound)
* [StopSound](StopSound)
* [StopAllSounds](StopAllSounds)
* [GetAvailableScenarios](GetAvailableScenarios)
* [GetScenario](GetScenario)
* [SetScenario](SetScenario)
* [PushScenario](PushScenario)
* [PullScenario](PullScenario)
* [SaveScenario](SaveScenario)
* [GetVolume](GetVolume)
* [SetVolume](SetVolume)


##Signals

* [SoundStatus](SoundStatus)
* [Scenario](Scenario)


##Properties
*None*

##Errors

* [UnknownFormat](UnknownFormat)
* [PlayerError](PlayerError)
* [NotPlaying](NotPlaying)
* [AlreadyPlaying](AlreadyPlaying)
* [ScenarioInvalid](ScenarioInvalid)
* [ScenarioStackUnderflow](ScenarioStackUnderflow)
* [DeviceFailed](DeviceFailed)


#Methods

###<a name="PlaySound">PlaySound</a> ( sii )


**Description:** Play a sound resource. 

***Parameters:****

<i>s: name</i>
The identification of the sound resource. Will be treated as filename, if no schema is given.  Format-specific options may be supplied by appending multiple ";foo=bar" statements to the  filename. Player engines that do not support these options should ignore them. 

<i>i: loop</i>
Loop. Set this to 1, if you want the sound resource to be restarted, once it ends. 0, otherwise. 

<i>i: length</i>
Length in seconds. Set this to anything other than 0 if you want to override the length of the sound resource.  Note that some audio resources have no concept of length or do know when the sound resource ends.  In these cases, you have to provide a reasonable length value or the sound will play endlessly. 



###<a name="StopSound">StopSound</a> ( s )


**Description:** Stop playing a sound resource. 

***Parameters:****

<i>s: name</i>
The identification of the sound resource. Will be treated as filename, if no schema is given. 



###<a name="StopAllSounds">StopAllSounds</a> ( )

**Description:** Stop all currently played sound resources. 


###<a name="GetAvailableScenarios">GetAvailableScenarios</a> ( ) &rarr; as


**Description:** Returns a list of supported audio scenarios. 

***Returns:***

<i>as: scenarios</i>
The supported audio scenarios. 



###<a name="GetScenario">GetScenario</a> ( ) &rarr; s


**Description:** Get the current audio scenario. 

***Returns:***

<i>s: scenario</i>
The name of the scenario. 



###<a name="SetScenario">SetScenario</a> ( s )


**Description:** Set a new audio scenario. 

***Parameters:****

<i>s: scenario</i>
The name of the scenario. 



###<a name="PushScenario">PushScenario</a> ( s )


**Description:** Push a new audio scenario onto the stack and active it. 

***Parameters:****

<i>s: scenario</i>
The new active scenario. 



###<a name="PullScenario">PullScenario</a> ( ) &rarr; s


**Description:** Pull an audio scenario from the stack and activate the next one. 

***Returns:***

<i>s: scenario</i>
The new active scenario. 



###<a name="SaveScenario">SaveScenario</a> ( s )


**Description:** Save the current scenario as a file. 

***Parameters:****

<i>s: scenario</i>
The name of the scenario. 



###<a name="GetVolume">GetVolume</a> ( ) &rarr; y


**Description:** Get the current main audio volume. 

***Implementation Note***

The main volume can depend on the current scenario. A change of scenario may change the main volume as well. 



***Returns:***

<i>y: volume</i>
The volume in percent (0-100). 



###<a name="SetVolume">SetVolume</a> ( y )


**Description:** Set the new main audio volume. 

***Implementation Note***

The main volume can depend on the current scenario. A change of scenario may change the main volume as well. 



***Parameters:****

<i>y: volume</i>
The volume in percent (0-100). 



#Signals

###
###<a name="SoundStatus">SoundStatus</a> ( ssa{sv} )

**Description:** Sent whenever a sound has been started or stopped. 

***Parameters:***

<i>s: id</i>
The identification of sound resource that changed its status. 

<i>s: status</i>
The new status for the sound resource. 

<i>a{sv}: properties</i>
An array of property values. Note that properties are optional. Expected tuples are:  <ul>  <li>...to be defined...</li>  </ul> 




###
###<a name="Scenario">Scenario</a> ( ss )

**Description:** Sent whenever there is a change of the global sound scenario. 

***Parameters:***

<i>s: scenario</i>
The scenario that is now active. 

<i>s: reason</i>
The reason for this change. Expected reasons are:  <ul>  <li>...to be defined...</li>  </ul> 




#Errors

###<a name="UnknownFormat">UnknownFormat</a>

**Description:** Raised, if the audio format is not supported. 


###<a name="PlayerError">PlayerError</a>

**Description:** Raised, if the player emits an (internal) error. 


###<a name="NotPlaying">NotPlaying</a>

**Description:** Raised, if the audio file is not playing. 


###<a name="AlreadyPlaying">AlreadyPlaying</a>

**Description:** Raised, if the audio file is already playing. 


###<a name="ScenarioInvalid">ScenarioInvalid</a>

**Description:** Raised, if the audio scenario can not be activated. 


###<a name="ScenarioStackUnderflow">ScenarioStackUnderflow</a>

**Description:** Raised, if there is no more scenario to pull from the stack. 


###<a name="DeviceFailed">DeviceFailed</a>

**Description:** Raised, if the audio device reported a problem. 



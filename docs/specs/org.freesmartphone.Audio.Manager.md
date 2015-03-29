
# freesmartphone.org: freesmartphone.org Audio Manager Interface
            

#org.freesmartphone.Audio.Manager

##Description


The Manager interface is used to manage various audio related aspects. It is  suited to manage the audio routing or can priorize differnt types of audio  streams. For managing different audio device the volume of differnt device  control types can be adjusted.


##Namespace


```org.freesmartphone.Audio.Manager```


##Methods

* [SetMode](SetMode)
* [GetMode](GetMode)
* [SetDevice](SetDevice)
* [GetDevice](GetDevice)
* [PushDevice](PushDevice)
* [PullDevice](PullDevice)
* [GetAvailableDevices](GetAvailableDevices)
* [GetVolume](GetVolume)
* [SetVolume](SetVolume)
* [SetMute](SetMute)
* [GetMute](GetMute)
* [RegisterSession](RegisterSession)
* [ReleaseSession](ReleaseSession)


##Signals

* [ModeChanged](ModeChanged)
* [DeviceChanged](DeviceChanged)
* [VolumeChanged](VolumeChanged)
* [MuteChanged](MuteChanged)


##Properties
*None*

##Errors

* [NotSupportedDevice](NotSupportedDevice)
* [DeviceStackUnderflow](DeviceStackUnderflow)


#Methods

###<a name="SetMode">SetMode</a> ( s )


**Description:** Set the current audio mode. Currently there is only a difference between  normal and call. Normal means all audio use when not in a phone call and call  means all audio within a phone call. 

####Parameters
<i>s: mode</i>
The new audio mode to set. Expected values are:  <ul>  <li>"normal" = Normal audio mode</li>  <li>"call" = Audio mode when a call is active</li>  </ul> 



###<a name="GetMode">GetMode</a> ( ) &rarr; s


**Description:** Get the current audio mode which is used. 

####Returns
<i>s: mode</i>
See <a href="specs/org.freesmartphone.Audio.Manager/#SetMode">SetMode</a> for a list of expected values. 



###<a name="SetDevice">SetDevice</a> ( s )


**Description:** Set the current audio output device which is used only within the current mode. If  you switch mode then the manager will switch even the output to the last used  one in the new mode. 

####Parameters
<i>s: name</i>
Set the current audio device to use to play audio. Expected values are:  <ul>  <li>"backspeaker" = The speaker on the back side of your device</li>  <li>"frontspeaker" = The speaker on the front side of your device</li>  <li>"headset" = The headset if plugged into the headset jack.</li>  <li>"bluetooth-sco" = Bluetooth SCO audio device</li>  <li>"bluetooth-a2dp" = Bluetooth A2DP audio device</li>  </ul> 



###<a name="GetDevice">GetDevice</a> ( ) &rarr; s


**Description:** Get the current audio device. 

####Returns
<i>s: device</i>
The current device used to play audio. For Expected values see  <a href="specs/org.freesmartphone.Audio.Manager/#SetDevice">SetDevice</a> 



###<a name="PushDevice">PushDevice</a> ( s )


**Description:** Push a new audio device onto the stack and active it. 

####Parameters
<i>s: device</i>
The new active audio device. For a list of expected values see  <a href="specs/org.freesmartphone.Audio.Manager/#SetDevice">SetDevice</a> 



###<a name="PullDevice">PullDevice</a> ( ) &rarr; s


**Description:** Pull an audio device from the stack and activate the next one. 

####Returns
<i>s: device</i>
The new active audio device. For a list of expected values see  <a href="specs/org.freesmartphone.Audio.Manager/#SetDevice">SetDevice</a> 



###<a name="GetAvailableDevices">GetAvailableDevices</a> ( s ) &rarr; as


**Description:** Get all available audio outputs for the specified audio mode. 

####Parameters
<i>s: mode</i>
Mode to retrieve the possible devices for. See  <a href="specs/org.freesmartphone.Audio.Manager/#SetMode">SetMode</a> for a list of expected values. 


####Returns
<i>as: outputs</i>
List of available output devices. For a list of expected values see  <a href="specs/org.freesmartphone.Audio.Manager/#SetDevice">SetDevice</a> 



###<a name="GetVolume">GetVolume</a> ( s ) &rarr; i


####Parameters
<i>s: control</i>
The control you want to get the volume for. 


####Returns
<i>i: volume</i>
The volume in percent (0-100). 



###<a name="SetVolume">SetVolume</a> ( si )


####Parameters
<i>s: control</i>
The control you want to set the volume for. Expected values are:  <ul>  <li>"speaker" = The currently active speaker</li>  <li>"micrphone" = The currently active microphone</li>  </ul> 

<i>i: volume</i>
The volume in percent (0-100). 



###<a name="SetMute">SetMute</a> ( sb )


**Description:** Mute current output device. 

####Parameters
<i>s: control</i>
The control you want to set the mute state for. See  <a href="specs/org.freesmartphone.Audio/#Manager">Manager</a> for detailed description of the available  controls. 

<i>b: mute</i>
The mute state of the control. The possible two values are:  <ul>  <li>true: mute the control</li>  <li>false: unmute the control</li>  </ul>  Please note:  <ul>  <li>Muting/unmuting a already muted/unmuted control does not has any effect.</li>  <li>Setting a volume of 0/100 for a control has the same effect as muting/unmuting it.</li>  </ul> 



###<a name="GetMute">GetMute</a> ( s ) &rarr; b


**Description:** Mute current output device. 

####Parameters
<i>s: control</i>
The control you want to set the mute state for. See  <a href="specs/org.freesmartphone.Audio/#Control">Control</a> for detailed description of the available  controls. 


####Returns
<i>b: mute</i>
The mute state of the control. The possible two values are:  <ul>  <li>true: mute the control</li>  <li>false: unmute the control</li>  </ul> 



###<a name="RegisterSession">RegisterSession</a> ( s ) &rarr; s


**Description:** Registering a audio session with the manager. Everytime a application  wants to play audio it has to register a audio session for this so the  audio daemon can control the played audio and maybe mutes the stream if  another audio source is more important than the current one. 

####Parameters
<i>s: stream</i>
The type of the stream the audio is playing on. Expected values are:  <ul>  <li>"media" = Default media playback is happen on this stream.</li>  <li>"alert" = High priority system alerts.</li>  <li>"ringtone" = Responsible for playing ringtones.</li>  <li>"alarm" = Alarm alerts with lower priority than alert.</li>  <li>"navigation" = Audio for navigation purpose.</li>  </ul> 


####Returns
<i>s: token</i>
A four byte long byte sequence to identify the audio session. The  token is needed to release the session after it is over. 



###<a name="ReleaseSession">ReleaseSession</a> ( s )


**Description:** Release a audio session from the manager after audio playback is over. 

####Parameters
<i>s: token</i>
A four byte long byte sequence to identify the audio session. The  token is generated and assigned when calling RegisterSession(). 



#Signals

###
###<a name="ModeChanged">ModeChanged</a> ( s )

####Parameters
<i>s: mode</i>
The new audio mode. See <a href="specs/org.freesmartphone.Audio/#Mode">Mode</a> for possible values. 




###
###<a name="DeviceChanged">DeviceChanged</a> ( s )

####Parameters
<i>s: device</i>
The new audio output device. See <a href="specs/org.freesmartphone.Audio.Manager/#SetDevice">SetDevice</a>  for a list of expected values. 




###
###<a name="VolumeChanged">VolumeChanged</a> ( si )

####Parameters
<i>s: control</i>
The control the volume was changed for. See  <a href="specs/org.freesmartphone.Audio.Manager/#SetVolume">SetVolume</a> for a list of expected values. 

<i>i: volume</i>
The new volume for the control in percent [0-100]. 




###
###<a name="MuteChanged">MuteChanged</a> ( sb )

####Parameters
<i>s: control</i>
The control the mute state was changed for. See  <a href="specs/org.freesmartphone.Audio.Manager/#SetVolume">SetVolume</a> for a list of expected values. 

<i>b: mute</i>
The new mute state for the control. Possible valus are:  <ul>  <li>true: control was muted</li>  <li>false: control was unmuted</li>  </ul> 




#Errors

###<a name="NotSupportedDevice">NotSupportedDevice</a>

**Description:** Raised, if the device to process is unsupported by the used router. 


###<a name="DeviceStackUnderflow">DeviceStackUnderflow</a>

**Description:** Raised, if there is no more device to pull from the stack. 

the footer here

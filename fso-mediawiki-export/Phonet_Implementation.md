---
title: Phonet Implementation
permalink: /Phonet_Implementation/
---

WARNING
=======

**<span style="background:red">Note that this page is not complete!!!</span>**

Lastest developments
--------------------

-   fsogsmd is now capable of registering to the network
-   phonecalls works with sound(needs to be finished because with the better code, the sound comming from the microphone is not good enough)
-   3g works

Setup
-----

This summup was made with the following setup:

-   [The 2.6.37-n900-next kernel](http://gitorious.org/nokia-n900-kernel/nokia-n900-kernel/commits/2.6.37-n900-next)
-   Running the following command:

`/etc/init.d/xserver-nodm stop`
`/etc/init.d/dbus-1 stop`
`/etc/init.d/dbus-1 start`

On a new console:

`fsogsmd`

On a new console:

`mdbus2 -s -i`
`MDBUS2> org.freesmartphone.ousaged /org/freesmartphone/Usage org.freesmartphone.Usage.RequestResource GSM`

On a new console:

`tail -f /var/log/fsogsmd.log`

And typing the other mdbus2 command on a new console(in the case it segfault it doesn't close the GSM resource)

All the commands were executed on the phone

Summup
------

| Type     | path                                                                                                                          | Working             | Comments                                                                        |
|----------|-------------------------------------------------------------------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------|
||
| [METHOD] | org.freedesktop.DBus.Introspectable.Introspect() -\> ( s:xml_data )                                                          |
| [METHOD] | org.freedesktop.DBus.Peer.GetMachineId() -\> ( s:machine_uuid )                                                              |
| [METHOD] | org.freedesktop.DBus.Peer.Ping() -\> ()                                                                                       |
| [METHOD] | org.freedesktop.DBus.Properties.GetAll( s:interface_name ) -\> ( a{sv}:properties )                                          |
| [METHOD] | org.freedesktop.DBus.Properties.Get( s:interface_name, s:property_name ) -\> ( v:value )                                    |
| [SIGNAL] | org.freedesktop.DBus.Properties.PropertiesChanged( s:interface_name, a{sv}:changed_properties, as:invalidated_properties ) |
| [METHOD] | org.freedesktop.DBus.Properties.Set( s:interface_name, s:property_name, v:value ) -\> ()                                    |
| [SIGNAL] | org.freesmartphone.Device.PowerSupply.Capacity( i:energy )                                                                    |
| [METHOD] | org.freesmartphone.Device.PowerSupply.GetCapacity() -\> ( i:result )                                                          |
| [METHOD] | org.freesmartphone.Device.PowerSupply.GetPowerStatus() -\> ( s:result )                                                       |
| [SIGNAL] | org.freesmartphone.Device.PowerSupply.PowerStatus( s:status )                                                                 |
| [SIGNAL] | org.freesmartphone.Device.RealtimeClock.Alarm( i:time )                                                                       |
| [METHOD] | org.freesmartphone.Device.RealtimeClock.GetCurrentTime() -\> ( i:result )                                                     |
| [METHOD] | org.freesmartphone.Device.RealtimeClock.GetWakeupTime() -\> ( i:result )                                                      |
| [METHOD] | org.freesmartphone.Device.RealtimeClock.SetCurrentTime( i:time ) -\> ()                                                       |
| [METHOD] | org.freesmartphone.Device.RealtimeClock.SetWakeupTime( i:time ) -\> ()                                                        |
| [SIGNAL] | org.freesmartphone.Device.RealtimeClock.WakeupTimeChanged( i:time )                                                           |
| [METHOD] | org.freesmartphone.GSM.Call.ActivateConference( i:id ) -\> ()                                                                 |
| [METHOD] | org.freesmartphone.GSM.Call.Activate( i:id ) -\> ()                                                                           |
| [SIGNAL] | org.freesmartphone.GSM.Call.CallStatus( i:id, s:status, a{sv}:properties )                                                    |
| [METHOD] | org.freesmartphone.GSM.Call.Emergency( s:number ) -\> ()                                                                      |
| [METHOD] | org.freesmartphone.GSM.Call.HoldActive() -\> ()                                                                               |
| [METHOD] | org.freesmartphone.GSM.Call.Initiate( s:number, s:type ) -\> ( i:result )                                                     |
| [METHOD] | org.freesmartphone.GSM.Call.Join() -\> ()                                                                                     |
| [METHOD] | org.freesmartphone.GSM.Call.ListCalls() -\> ( a(isa{sv}):result )                                                             |
| [METHOD] | org.freesmartphone.GSM.Call.ReleaseAll() -\> ()                                                                               |
| [METHOD] | org.freesmartphone.GSM.Call.ReleaseHeld() -\> ()                                                                              |
| [METHOD] | org.freesmartphone.GSM.Call.Release( i:id ) -\> ()                                                                            |
| [METHOD] | org.freesmartphone.GSM.Call.SendDtmf( s:tones ) -\> ()                                                                        |
| [METHOD] | org.freesmartphone.GSM.Call.Transfer( s:number ) -\> ()                                                                       |
| [METHOD] | org.freesmartphone.GSM.CB.GetCellBroadcastSubscriptions() -\> ( s:result )                                                    |
| [SIGNAL] | org.freesmartphone.GSM.CB.IncomingCellBroadcast( s:text, s:language, a{sv}:properties )                                       |
| [METHOD] | org.freesmartphone.GSM.CB.SetCellBroadcastSubscriptions( s:channels ) -\> ()                                                  |
| [METHOD] | org.freesmartphone.GSM.Debug.DebugCommand( s:command, s:channel ) -\> ( s:result )                                            |
| [METHOD] | org.freesmartphone.GSM.Debug.DebugInjectResponse( s:response, s:channel ) -\> ()                                              |
| [METHOD] | org.freesmartphone.GSM.Debug.DebugPing() -\> ()                                                                               |
| [SIGNAL] | org.freesmartphone.GSM.Debug.DebugStatus( a{ss}:channels )                                                                    |
| [SIGNAL] | org.freesmartphone.GSM.Device.DeviceStatus( s:status )                                                                        |                     | returns ("alive-sim-ready")                                                     |
| [METHOD] | org.freesmartphone.GSM.Device.GetDeviceStatus() -\> ( s:result )                                                              |
| [METHOD] | org.freesmartphone.GSM.Device.GetFeatures() -\> ( a{sv}:result )                                                              | Not yet implemented |
| [METHOD] | org.freesmartphone.GSM.Device.GetFunctionality() -\> ( s:level, b:autoregister, s:pin )                                       | Not implemented yet |
| [METHOD] | org.freesmartphone.GSM.Device.GetMicrophoneMuted() -\> ( b:result )                                                           |
| [METHOD] | org.freesmartphone.GSM.Device.GetSpeakerVolume() -\> ( i:result )                                                             |
| [SIGNAL] | org.freesmartphone.GSM.Device.KeypadEvent( s:name, b:pressed )                                                                |
| [METHOD] | org.freesmartphone.GSM.Device.SetFunctionality( s:level, b:autoregister, s:pin ) -\> ()                                       |
| [METHOD] | org.freesmartphone.GSM.Device.SetMicrophoneMuted( b:muted ) -\> ()                                                            |
| [METHOD] | org.freesmartphone.GSM.Device.SetSpeakerVolume( i:volume ) -\> ()                                                             |
| [METHOD] | org.freesmartphone.GSM.HZ.GetHomeZoneStatus() -\> ( s:result )                                                                |
| [METHOD] | org.freesmartphone.GSM.HZ.GetKnownHomeZones() -\> ( as:result )                                                               |
| [SIGNAL] | org.freesmartphone.GSM.HZ.HomeZoneStatus( s:name )                                                                            |
| [METHOD] | org.freesmartphone.GSM.Monitor.GetNeighbourCellInformation() -\> ( aa{sv}:result )                                            |
| [METHOD] | org.freesmartphone.GSM.Monitor.GetServingCellInformation() -\> ( a{sv}:result )                                               |
| [SIGNAL] | org.freesmartphone.GSM.Network.CipherStatus( s:telephony, s:pdp )                                                             |
| [METHOD] | org.freesmartphone.GSM.Network.DisableCallForwarding( s:reason, s:class_ ) -\> ()                                            |
| [METHOD] | org.freesmartphone.GSM.Network.EnableCallForwarding( s:reason, s:class_, s:number, i:timeout ) -\> ()                        |
| [METHOD] | org.freesmartphone.GSM.Network.GetCallForwarding( s:reason ) -\> ( a{sv}:result )                                             |
| [METHOD] | org.freesmartphone.GSM.Network.GetCallingIdentification() -\> ( s:result )                                                    |
| [METHOD] | org.freesmartphone.GSM.Network.GetSignalStrength() -\> ( i:result )                                                           | ???                 | reports (0) even after beeing "registered"                                      |
| [METHOD] | org.freesmartphone.GSM.Network.GetStatus() -\> ( a{sv}:result )                                                               |                     |                                                                                 |
| [METHOD] | org.freesmartphone.GSM.Network.GetTimeReport() -\> ( i:time, i:timestamp, i:zone, i:zonestamp )                               | ???                 | reports (0,0,10000,0) ,maybe I should have wait more after registering          |
| [SIGNAL] | org.freesmartphone.GSM.Network.IncomingUssd( s:mode, s:message_ )                                                            |
| [METHOD] | org.freesmartphone.GSM.Network.ListProviders() -\> ( a(sssss):result )                                                        | must re-test        |                                                                                 |
| [METHOD] | org.freesmartphone.GSM.Network.Register() -\> ()                                                                              | ???                 | Not needed, since it registers automatically(after requesting the GSM resource) |
| [METHOD] | org.freesmartphone.GSM.Network.RegisterWithProvider( s:operator_code ) -\> ()                                                |
| [METHOD] | org.freesmartphone.GSM.Network.SendUssdRequest( s:request ) -\> ()                                                            | Not Implemented yet |
| [METHOD] | org.freesmartphone.GSM.Network.SetCallingIdentification( s:status ) -\> ()                                                    |
| [SIGNAL] | org.freesmartphone.GSM.Network.SignalStrength( i:signal_strength )                                                           |
| [SIGNAL] | org.freesmartphone.GSM.Network.Status( a{sv}:status )                                                                         |
| [SIGNAL] | org.freesmartphone.GSM.Network.TimeReport( i:time, i:zone )                                                                   |
| [METHOD] | org.freesmartphone.GSM.Network.Unregister() -\> ()                                                                            |
| [METHOD] | org.freesmartphone.GSM.PDP.ActivateContext() -\> ()                                                                           |
| [SIGNAL] | org.freesmartphone.GSM.PDP.ContextStatus( s:status, a{sv}:properties )                                                        |
| [METHOD] | org.freesmartphone.GSM.PDP.DeactivateContext() -\> ()                                                                         |
| [METHOD] | org.freesmartphone.GSM.PDP.GetContextStatus() -\> ( s:status, a{sv}:properties )                                              |
| [METHOD] | org.freesmartphone.GSM.PDP.GetCredentials() -\> ( s:apn, s:username, s:password )                                             |
| [METHOD] | org.freesmartphone.GSM.PDP.InternalStatusUpdate( s:status, a{sv}:properties ) -\> ()                                          |
| [METHOD] | org.freesmartphone.GSM.PDP.SetCredentials( s:apn, s:username, s:password ) -\> ()                                             |
| [SIGNAL] | org.freesmartphone.GSM.SIM.AuthStatus( s:status )                                                                             |
| [METHOD] | org.freesmartphone.GSM.SIM.ChangeAuthCode( s:old_pin, s:new_pin ) -\> ()                                                    |
| [METHOD] | org.freesmartphone.GSM.SIM.DeleteEntry( s:category, i:index ) -\> ()                                                          |
| [METHOD] | org.freesmartphone.GSM.SIM.DeleteMessage( i:index ) -\> ()                                                                    |
| [METHOD] | org.freesmartphone.GSM.SIM.GetAuthCodeRequired() -\> ( b:result )                                                             |
| [METHOD] | org.freesmartphone.GSM.SIM.GetAuthStatus() -\> ( s:result )                                                                   |
| [METHOD] | org.freesmartphone.GSM.SIM.GetHomeZoneParameters() -\> ( a(siii):result )                                                     |
| [METHOD] | org.freesmartphone.GSM.SIM.GetPhonebookInfo( s:category ) -\> ( i:slots, i:numberlength, i:namelength )                       |
| [METHOD] | org.freesmartphone.GSM.SIM.GetServiceCenterNumber() -\> ( s:result )                                                          |
| [METHOD] | org.freesmartphone.GSM.SIM.GetSimInfo() -\> ( a{sv}:result )                                                                  | ,but must re-test   | ({"hplmn": "yyyyy","imsi": "xxxxxxxxxxxxxxx","issuer": "<unknown>"})

                                                                                                                                                                  -   the y and x are numbers(I don't know what they means so I masked them)
                                                                                                                                                                  -   maybe unknow means not implemented?                                          |
| [METHOD] | org.freesmartphone.GSM.SIM.GetUnlockCounters() -\> ( a{sv}:result )                                                           |
| [SIGNAL] | org.freesmartphone.GSM.SIM.IncomingMessage( i:index )                                                                         |
| [METHOD] | org.freesmartphone.GSM.SIM.RetrieveMessage( i:index ) -\> ( s:status, s:sender_number, s:contents, a{sv}:properties )        |
| [METHOD] | org.freesmartphone.GSM.SIM.RetrievePhonebook( s:category, i:mindex, i:maxdex ) -\> ( a(iss):result )                          |
| [METHOD] | org.freesmartphone.GSM.SIM.SendAuthCode( s:pin ) -\> ()                                                                       |
| [METHOD] | org.freesmartphone.GSM.SIM.SendGenericSimCommand( s:command ) -\> ( s:result )                                                |
| [METHOD] | org.freesmartphone.GSM.SIM.SendRestrictedSimCommand( i:command, i:fileid, i:p1, i:p2, i:p3, s:data ) -\> ( s:result )         |
| [METHOD] | org.freesmartphone.GSM.SIM.SendStoredMessage( i:index ) -\> ( i:transaction_index, s:timestamp )                             |
| [METHOD] | org.freesmartphone.GSM.SIM.SetAuthCodeRequired( b:check, s:pin ) -\> ()                                                       |
| [METHOD] | org.freesmartphone.GSM.SIM.SetServiceCenterNumber( s:number ) -\> ()                                                          |
| [METHOD] | org.freesmartphone.GSM.SIM.StoreEntry( s:category, i:index, s:name, s:number ) -\> ()                                         |
| [METHOD] | org.freesmartphone.GSM.SIM.StoreMessage( s:recipient_number, s:contents, a{sv}:properties ) -\> ( i:result )                 |
| [METHOD] | org.freesmartphone.GSM.SIM.Unlock( s:puk, s:new_pin ) -\> ()                                                                 |
| [METHOD] | org.freesmartphone.GSM.SMS.GetSizeForTextMessage( s:contents ) -\> ( u:result )                                               |
| [SIGNAL] | org.freesmartphone.GSM.SMS.IncomingMessageReport( i:reference, s:status, s:sender_number, s:contents )                       |
| [SIGNAL] | org.freesmartphone.GSM.SMS.IncomingTextMessage( s:number, s:timestamp, s:contents )                                           |
| [METHOD] | org.freesmartphone.GSM.SMS.RetrieveTextMessages() -\> ( a(issssa{sv}):result )                                                | Not yet implemented |
| [METHOD] | org.freesmartphone.GSM.SMS.SendTextMessage( s:recipient_number, s:contents, b:report ) -\> ( i:reference, s:timestamp )      |
| [METHOD] | org.freesmartphone.GSM.VoiceMail.GetStoredVoiceMails() -\> ( as:result )                                                      |
| [METHOD] | org.freesmartphone.GSM.VoiceMail.GetVoiceMailboxNumber() -\> ( s:result )                                                     |
| [SIGNAL] | org.freesmartphone.GSM.VoiceMail.IncomingVoiceMail( i:index )                                                                 |
| [METHOD] | org.freesmartphone.GSM.VoiceMail.SetVoiceMailboxNumber( s:number ) -\> ()                                                     |
| [METHOD] | org.freesmartphone.Info.GetInfo() -\> ( a{sv}:result )                                                                        |
||


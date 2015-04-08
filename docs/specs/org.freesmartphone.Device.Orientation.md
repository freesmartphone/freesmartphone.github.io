
# freesmartphone.org Orientation Interface
            
##Description


This interface provides access to the device's physical orientation.


##Namespace


```org.freesmartphone.Device.Orientation```


##Methods

* [GetOrientation](#GetOrientation)


##Signals

* [OrientationChanged](#OrientationChanged)


##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetOrientation">GetOrientation</a> ( ) &rarr; s


**Description:** Returns the orientation of the device. 

***Returns:***

<i>s: orientation</i>
The orientation. Expected substrings are:  <ul>  <li>"flat" (Laying flat on a level surface, e.g. a table),</li>  <li>"held" (Being held slightly tilt towards your face),</li>  <li>"portrait" (Display held with the long side vertically),</li>  <li>"landscape" (Display held with the long side horizontally,</li>  <li>"faceup" (Display being oriented towards the sky),</li>  <li>"facedown" (Display being oriented towards the floor),</li>  <li>"normal", (Not rotated)</li>  <li>"reverse", (180 degrees rotated)</li>  </ul> 



#Signals

###
###<a name="OrientationChanged">OrientationChanged</a> ( s )

**Description:** Sent whenever there is a change of the device orientation. 

***Parameters:***

<i>s: orientation</i>
The new orientation. See [GetOrientation](specs/org.freesmartphone.Device.Orientation.GetOrientation)</a> for supported values. 





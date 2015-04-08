
# freesmartphone.org Events Interface
            
##Description


The Events interface provides access to the rules.  All the rules are specified into the rule file : /etc/freesmartphone/oevents/rules.yaml.  See the file itself for more information about the syntax of the rules.


##Namespace


```org.freesmartphone.Events```


##Methods

* [AddRule](#AddRule)
* [RemoveRule](#RemoveRule)
* [TriggerTest](#TriggerTest)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="AddRule">AddRule</a> ( s )


**Description:** Parse a rule string and add it into the rule list. 

***Parameters:****

<i>s: rule</i>
The rule in the same format used by the rules file. 



###<a name="RemoveRule">RemoveRule</a> ( s )


**Description:** Remove a rule by name. 

***Parameters:****

<i>s: name</i>
The name of the rule, as specified by the 'name' attribute of the rule. 



###<a name="TriggerTest">TriggerTest</a> ( sb )


**Description:** Trigger or untrigger all the 'Test' triggers with matching names. 

***Parameters:****

<i>s: name</i>
the name of the Test triggers to trigger/untrigger. 

<i>b: value</i>
True to trigger, False to untrigger. 





# freesmartphone.org GSM Network Monitoring Interface
            
##Description


The Monitor interface is used to gather auxiallary information  about the GSM network, serving cells, network cells, and more,  beyond what is defined in 3GPP 07.07. Implementing this interface  is optional.


##Namespace


```org.freesmartphone.GSM.Monitor```


##Methods

* [GetServingCellInformation](#GetServingCellInformation)
* [GetNeighbourCellInformation](#GetNeighbourCellInformation)


##Signals
*None*

##Properties
*None*

##Errors
*None*

#Methods

###<a name="GetServingCellInformation">GetServingCellInformation</a> ( ) &rarr; a{sv}


**Description:** Retrieves serving cell information. 

***Returns:***

<i>a{sv}: serving_cell</i>
Information about the serving cell. Valid are the following tuples:  <ul>  <li>( "arfcn", int ):         Current Channel Number</li>  <li>( "c1", int ):            Path Loss Criterion C1 (in percentage, comparable with signal strength)</li>  <li>( "c2", int ):            Cell-Reselection Criterion C2 (in percentage, comparable with signal strength)</li>  <li>( "rxlev", int ):         Received Field Strength (in percentage, comparable with signal strength)</li>  <li>( "bsic", int ):          Base Station ID Code</li>  <li>( "cid", string ):        Cell Identifier</li>  <li>( "dsc", int ):           Downlink Signaling Counter    actual value</li>  <li>( "txlev, int ):          Transmit Power Level</li>  <li>( "tn, int ):             Timeslot Number</li>  <li>( "rlt, int ):            Radio Link Timeout Counter</li>  <li>( "tav, int ):            Timing Advance</li>  <li>( "rxlev_f, int ):        Received Field Strength full (in percentage, comparable with signal strength)</li>  <li>( "rxlev_s, int ):        Received Field Strength sub (in percentage, comparable with signal strength)</li>  <li>( "rxqual_f, int ):       Received Quality full</li>  <li>( "rxqual_s, int ):       Received Quality sub</li>  <li>( "lac", string ):        Location Area Code</li>  <li>( "cba", int ):           Cell Bar Access</li>  <li>( "cbq", int ):           Cell Bar Qualifier</li>  <li>( "ctype", int ):         Cell Type Indicator           NA/GSM/GPRS</li>  <li>( "vocoder" ):            Vocoder                       Sig/speech/efr/amr/14.4/9.6/4.8/2.4</li>  </ul>  See http://www.tele-servizi.com/janus/engfield1.html for more details. 



###<a name="GetNeighbourCellInformation">GetNeighbourCellInformation</a> ( ) &rarr; aa{sv}


**Description:** Retrieves neighbour cell information. 

***Returns:***

<i>aa{sv}: neighbour_cells</i>
Information about the neighbour cells. This is an array of maps, one for every neighbour cell. Valid are the following tuples:  <ul>  <li>( "arfcn", int ):         Current Channel Number</li>  <li>( "c1", int ):            Path Loss Criterion C1 (in percentage, comparable with signal strength)</li>  <li>( "c2", int ):            Cell-Reselection Criterion C2</li>  <li>( "rxlev", int ):         Received Field Strength (in percentage, comparable with signal strength)  <li>( "bsic", int ):          Base Station ID Code</li>  <li>( "cid", string ):        Cell Identifier</li>  <li>( "lac", string ):        Location Area Code</li>  <li>( "dsc", int ):           Downlink Signaling Counter    actual value</li>  <li>( "foffset, int ):        Frame Offset</li>  <li>( "timea, int ):          Time Alignment</li>  <li>( "cba", int ):           Cell Bar Access</li>  <li>( "cbq", int ):           Cell Bar Qualifier</li>  <li>( "ctype", int ):         Cell Type Indicator           NA/GSM/GPRS</li>  <li>( "rac", string ):        Routing Area Code</li>  <li>( "roffset, int ):        Cell Reselection Offset</li>  <li>( "toffset, int ):        Temporary Offset</li>  <li>( "rxlevam, int ):        Rxlev access min (in percentage, comparable with signal strength)</li>  </ul>  See http://www.tele-servizi.com/janus/engfield1.html for more details. 




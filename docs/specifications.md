# Specifications

The purpose of the D-Bus interface specifications is to provide interoperatibility between implementations.

## Active

For details, please see our automatically generated docs at [TODO: UNDER CONSTRUCTION]()
 
## Brainstorming

For brainstorming, please use our mailing list ```fso@openphoenux.org```.

## Style guide

* Bus names are all lowercase with ```.``` separation, e.g. ```org.freesmartphone.odeviced```.
* Object names all lowercase with ```/``` separation, e.g. ```/org/freesmartphone/device/idlenotifier/0```.
* Method and Signal names are CamelCased, e.g. ```ListFoo```, ```GetBar```.
* Use Get/Set prefixes for accessors, such as  ```GetServiceCenter```, ```SetServiceCenter```.
* Use verbs for operations, such as ```ListProviders```, ```Unlock```, ```SendAuthCode```.
* Use similar terms for similar operations, e.g. ```ListProviders```, ```ListCells```.
* Keep the vocabulary as simple as possible, but as large as necessary.
* The use of D-Bus *properties* is controversial, for now we don't use them in any of the freesmartphone.org specifications.
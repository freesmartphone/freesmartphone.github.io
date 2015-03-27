

# PIM Usage

All the Domains are mostly the same. They have the same basic structure, though some domains have a couple of minor extensions, for instance, "Missed Calls" handling in the Calls domain. Therefore, this document will use the Contacts domain for examples, though everything applies to all the others as well.

TBD. Explain about querying, query objects, entry objects and etc. Also explain about fields and types.

# Entries

Entries are the basic data objects of the domain, every time [Add](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contacts.html#Add) is called, a new entry is created in the domain. Each entry has a unique (in the domain) persistent id. The entries are accesible using the methods in the [Contact](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contact.html) path using their unique ID. For instance, in order to Delete the contact with ID 24 you will run [Delete](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contact.html#Delete) with */org/freesmartphone/PIM/Contact/24* as the dbus path.

Every entry consists of different fields of various types. Fields can have eitehr one or more values. In the case of one value, the value is stored in the field, otherwise the values are stored in a list which is stored in the field. Each entry must include one read-only field called *EntryId* which signifies the unique entry ID described before.

# Fields and Types

As explained in the [Entries](#Entries) section, each entry consists of fields. Each field has type. Fields are defined per domain, so adding a field is done on the domain (for exmalpe [Contacts](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contacts.html)). Fields should generally be declared before usage so opimd will know how to treat them. For instance, if I want to define a field for phonenumbers I will call the [AddField](http://docs.freesmartphone.org/org.freesmartphone.PIM.Fields.html#AddField) method with the wanted field name as the first paramter, and "phonenumber" as the second. The list of types is available using the [List](http://docs.freesmartphone.org/org.freesmartphone.PIM.Types.html#List) method. If a field is not added before usage, it's treated like a field with type "generic".

## Adding and Removing Fields

***There are a couple of restrictions when modifying fields***

When adding:

-   Field names are unique, you can't create two fields with the same name.
-   The *EntryId* field name is system-reserved and can not be modifyed.
-   Field names can not start with either *\_*, *@*, *\<*, *\>* or *$* as they are reserved for [Querying](#Querying).

When removing:

-   The *EntryId* field name is system-reserved and can not be deleted.
-   For each domain, there are a couple of required fields that can not be removed.

# Querying

Querying is opimd's way of finding entries matching a set of rules. This section describes the querys to be used with [GetSingleEntrySingleField](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contacts.html#GetSingleEntrySingleField) and [Query](http://docs.freesmartphone.org/org.freesmartphone.PIM.Contacts.html#Query)).

## Query Logic

All the parameters passed to a query are logically connected with 'AND' that is, all of the parameters must match an entry in order for it to match. For instance, querying for {'Name':'Tom', 'Surname':'Hacohen'} will only return the entry of "Tom Hacohen", it will not return the entry of "Tom Sawyer".

## Query Parameters

Queries are hash tables where each key is one of the following types:

-   A *Field* name to compare to.
-   A *Type* name to compare to (prefixed by '*$*').
-   A *Domain* name to connect to (prefixed by '*@*').
-   A special querying indentifier (prefixed by '*\_*').

For each key type the meaning is as follows:

### Field

When the key is a field name, the value of the key in the hash table is the value to be compared to the value of the Field of the entry. When the entry has a list of values associated with a specific field, one match is enough. For example, matching 'Name':'Tom' will match every contact where 'Tom' matches the name field. Matching is different with different field types as explained in the *Comparison Types* section.

### Type

When the key is a type name, the behavior is exactly the same as in the Field section, but instead of trying to match against one field, all the fields of a specific type are matched (Again, at least one match is enough).

### Domain

***TBD: This is not yet fully implemented and the API is not yet final.***

### Special Identifiers

There are a couple of special identifiers that change the querying behavior. For instance, *\_at\_least\_one* means at least one part of the query needs to match (that is, logically connected with OR).
 TBD: explain about the other special indetifiers.

## Comparison Types

Each type has a different comparison function, those are the comparison functions used in the time of writing this document:

-   The following types are compared according to their numerical value: *entryid*, *number*, *integer* and *date*.
-   The following types are compared according to their boolean value: *boolean*.
-   The following types are compared using regex (perl style): *name*, *longtext*, *photo*, *objectpath*, *uri*, *timezone* (should change to int), *address*, *text*, *email* and *generic* (should change to a binary comparison).
-   Phone numbers (*phonenumber*) are compared using [libphone-utils](http://git.shr-project.org/git/?p=libphone-utils.git;a=summary)'s phone number comparison functions.

Normally, the values are tested for equality, but when a field name is prefixed with either '\<' or '\>' the values are tested for lesser than, and greater than respectively. For example, '\<Age': 19 matches all the entries with an age smaller than 19. This does not work with fields that match with regex (as defined above).

# Updating

***TBD***

# Deleting

***TBD***

# Query Objects

***TBD***

# Signals

***TBD***


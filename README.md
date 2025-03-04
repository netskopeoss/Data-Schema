# Data-Schema

Netskope Data team has created a schema that will explain to customers and partners what fields our logging RESTful API endpoints can contain. It will provide information about the fields, what kind of datatype they contain, examples, and labels for filtering. 

This repository contains metadata about the parameters returned by REST API v2 dataexport Iterator Endpoints and Transaction events.

More details can be found under:

REST API v2 dataexport Endpoints:
https://docs.netskope.com/en/netskope-help/admin-console/rest-api/rest-api-v2-overview-312207/using-the-rest-api-v2-dataexport-iterator-endpoints/

Transaction events:
https://docs.netskope.com/en/netskope-help/data-security/transaction-events/


Metadata of each field will be composite of the below details :-

```
parameter_name: Field name. Rest api calls returns pre-defined set of fields per event type. 

type: Field value data type. String, Integer64, Integer32, Float, Dictionery, Boolean, LongInt and List etc.

description: Fields description for better understanding of the API response to the end users.

example: Provides sample values per field names. 

event_types: Respective field names are available in the listed event types.

applicable_for: Information about which Netskope's solution this Field will be part of. We are supporting Data Export and Log Streaming as of now.    

Ex:
"applicable_for": [
      "data_export",
      "log_streaming"
]   
   
default_value: If values are not present, default values are returned which are defined per data types. 
               Transaction Event follows w3c log format. If a field is empty, the value is string -

String:  ""
Integer64:  0
Integer32:  0
LongInt: 0
Float:   0.0
Dictionery/Map:  {}
Boolean:  False
List/Array:  []

position: For transaction events, data is in w3c log format. Position column represents the order the particular field appears in the Response.

version: Applicable for just the transaction events. Provides information about what are all the transaction events formats this Field will be part of, we are supporting up to v3 currently.
```

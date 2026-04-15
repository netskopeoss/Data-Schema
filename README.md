# Data-Schema

The Netskope Data team has created a schema to help customers and partners understand the fields available in our logging RESTful API endpoints. This schema provides information about field names, data types, examples, and labels for filtering.

This repository contains metadata about the parameters returned by REST API v2 Data Export Iterator Endpoints and Transaction Events.

## Documentation

For more details, please refer to:

**REST API v2 Data Export Endpoints:**  
https://docs.netskope.com/en/netskope-help/admin-console/rest-api/rest-api-v2-overview-312207/using-the-rest-api-v2-dataexport-iterator-endpoints/

**Transaction Events:**  
https://docs.netskope.com/en/netskope-help/data-security/transaction-events/

## Field Metadata

The metadata for each field consists of the following attributes:

**parameter_name:** The field name. REST API calls return a pre-defined set of fields per event type.

**type:** The field value data type. Supported types include: String, Integer64, Integer32, Float, Dictionary, Boolean, LongInt, and List.

**description:** A description of the field to help users better understand the API response.

**example:** Sample values for the field.

**event_types:** Lists the event types in which this field is available.

**applicable_for:** Indicates which Netskope solution(s) include this field. Currently supports Data Export and Log Streaming.

Example:
```json
"applicable_for": [
  "data_export",
  "log_streaming"
]
```

**default_value:** Default values returned when field values are not present. For transaction streams, if a field is empty, the value is the string "-".

Default values by data type:
- String: `""`
- Integer64: `0`
- Integer32: `0`
- LongInt: `0`
- Float: `0.0`
- Dictionary/Map: `{}`
- Boolean: `False`
- List/Array: `[]`

**position:** For transaction events, this represents the order in which the field appears in the response. The position is configurable and can be modified through the Log Streaming UI.

**version:** Applicable only to transaction events. Indicates which transaction event format versions include this field. Currently supports up to v3.

# Netskope Data Catalog

## Overview

The Netskope Data Catalog is a comprehensive data discovery and governance platform that provides rich metadata, lineage tracking, quality metrics, and collaboration features for all Netskope data assets.

**What started as a simple schema repository has evolved into a full-featured data catalog** that helps customers and partners discover, understand, trust, and collaborate on data.

This repository contains:
- **Schema Metadata**: Detailed field definitions for REST API v2 dataexport Iterator Endpoints and Transaction events
- **Data Lineage**: Visual maps showing how data transforms from source to consumption
- **Quality Metrics**: Trust scores and data quality assessments
- **Compliance Tracking**: PII identification and GDPR/CCPA compliance information
- **Collaboration Features**: User ratings, comments, and feedback on datasets

## Key Features

### 🔍 Discovery & Search
- **Google-like Search**: Powerful search interface to find fields, datasets, and events quickly
- **Advanced Filters**: Filter by data type, event type, PII classification, quality score, and more
- **Faceted Navigation**: Drill down through categories to discover relevant data
- **Related Fields**: Discover related fields based on usage patterns and lineage

### 📊 Data Lineage
- **Visual Lineage Maps**: See exactly where data comes from and where it goes
- **Transformation Tracking**: Understand how data is transformed along the pipeline
- **Impact Analysis**: Assess the impact of potential changes to fields or datasets
- **Field-Level Lineage**: Trace individual fields from source to consumption

### ✅ Data Quality & Trust
- **Quality Scores**: Multi-dimensional quality metrics (completeness, accuracy, consistency, etc.)
- **Trust Levels**: Verified, Trusted, or Unverified designations
- **Validation Rules**: See what validation rules are applied to data
- **Data Freshness**: Know when data was last updated and expected latency
- **Known Issues**: Track and monitor data quality issues

### 🔒 Compliance & Privacy
- **PII Identification**: Automatically identifies Personally Identifiable Information
- **Compliance Frameworks**: GDPR, CCPA, HIPAA, PCI-DSS, SOX, and more
- **Data Subject Rights**: Track right to access, erasure, portability, etc.
- **Anonymization Support**: See available anonymization methods for sensitive fields
- **Risk Assessment**: Understand privacy/security risk levels

### 👥 Collaboration
- **Ratings & Reviews**: Rate datasets and fields based on usefulness
- **Comments & Discussions**: Ask questions, share insights, and discuss data
- **Expert Contacts**: Find data owners and subject matter experts
- **Usage Feedback**: Share how you're using data to help others
- **Bookmarks**: Save frequently accessed fields and datasets

## Repository Structure

```
Data-Schema/
├── schema/
│   ├── event_schema.json          # 748 event schema fields
│   └── event_transaction.json     # 197 transaction event fields
├── catalog/
│   ├── lineage/                   # Data lineage configurations
│   │   ├── lineage_schema.json
│   │   ├── data_lineage.json
│   │   └── VISUALIZATION_GUIDE.md
│   ├── search/                    # Search & discovery configs
│   │   ├── search_config_schema.json
│   │   └── search_config.json
│   ├── compliance/                # PII & compliance tracking
│   │   ├── compliance_schema.json
│   │   └── pii_classification.json
│   ├── quality/                   # Data quality metrics
│   │   ├── quality_schema.json
│   │   └── quality_metrics.json
│   ├── collaboration/             # User collaboration features
│   │   ├── collaboration_schema.json
│   │   └── user_feedback.json
│   └── API_DOCUMENTATION.md       # Complete API documentation
└── README.md
```

## Quick Start

### 1. Browse Schemas

View the raw schema files:
- [Event Schema (748 fields)](./schema/event_schema.json) - All event types from REST API v2
- [Transaction Events (197 fields)](./schema/event_transaction.json) - Transaction event fields in W3C format

### 2. Explore Catalog Features

- **[Data Lineage](./catalog/lineage/)**: Understand data flow and transformations
- **[Search Configuration](./catalog/search/)**: See how search and discovery works
- **[Compliance Info](./catalog/compliance/)**: Check PII classification and compliance requirements
- **[Quality Metrics](./catalog/quality/)**: Review data quality scores and trust levels
- **[Collaboration](./catalog/collaboration/)**: See user ratings, comments, and feedback

### 3. Use the API

See [API Documentation](./catalog/API_DOCUMENTATION.md) for detailed API endpoints and examples.

## Schema Metadata Fields

Metadata of each field will be composite of the below details:

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

## Data Catalog Features

### Search & Discovery

The catalog provides powerful search capabilities to help you find the data you need:

- **Full-Text Search**: Search across field names, descriptions, and examples
- **Smart Filters**: Filter by data type, event type, PII classification, quality score
- **Relevance Ranking**: Results ranked by relevance, popularity, and quality
- **Faceted Navigation**: Refine searches using multiple filter dimensions

Example search queries:
- Find all PII fields: `classification:PII`
- Find user-related fields: `user OR username OR user_id`
- Find high-quality network fields: `event_type:network quality_score:>90`

### Data Lineage

Understand the complete journey of your data:

1. **Upstream Sources**: Where does the data originate?
   - Netskope Client Logs
   - Cloud App Connectors (API)
   - Network Traffic Monitors
   - Web Proxy Logs

2. **Transformations**: How is data processed?
   - Enrichment (adding user directory info)
   - Normalization (timestamp formatting)
   - Filtering (removing test events)
   - Aggregation (combining metrics)
   - Format conversion (W3C log format)

3. **Downstream Consumers**: Who uses the data?
   - Security Dashboards
   - Compliance Reports
   - REST API v2 Data Export
   - ML/Analytics Models
   - Log Streaming Services

See [Lineage Visualization Guide](./catalog/lineage/VISUALIZATION_GUIDE.md) for detailed examples.

### Data Quality & Trust

Every dataset has quality metrics to help you trust the data:

- **Overall Quality Score**: 0-100 composite score
- **Quality Dimensions**:
  - Completeness: 95% (few missing values)
  - Accuracy: 93% (validated against rules)
  - Consistency: 90% (consistent across systems)
  - Timeliness: 88% (how current the data is)
  - Validity: 94% (conforms to defined formats)
  - Uniqueness: 96% (no duplicates)

- **Trust Levels**:
  - ✅ **VERIFIED**: Gold-standard, audited data sources
  - ✓ **TRUSTED**: Reliable, regularly monitored sources
  - ? **UNVERIFIED**: Use with caution, not yet validated
  - ⚠️ **DEPRECATED**: Being phased out, migration recommended

### Compliance & Privacy

Built-in compliance tracking for regulatory requirements:

**PII Identified**: The catalog identifies 85+ fields containing PII including:
- Names and user identifiers
- Email addresses
- IP addresses
- Device identifiers
- Geographic location data

**Supported Compliance Frameworks**:
- **GDPR** (General Data Protection Regulation)
  - Right to access, rectification, erasure
  - Data portability
  - Privacy by design
- **CCPA** (California Consumer Privacy Act)
  - Right to know and delete
  - Opt-out of sale
- **HIPAA** (Health Insurance Portability)
- **PCI-DSS** (Payment Card Industry)
- **SOC2** (Security & availability controls)

**Risk Levels**: Each field is assessed for privacy/security risk:
- 🔴 **CRITICAL**: Highly sensitive credentials
- 🟠 **HIGH**: Direct PII (names, emails, locations)
- 🟡 **MEDIUM**: Indirect identifiers (IP addresses, device IDs)
- 🟢 **LOW**: Minimal privacy concern
- ⚪ **NONE**: Non-sensitive metadata

### Collaboration Features

Make data discovery a team effort:

1. **Rate Datasets**: 5-star rating system helps others know quality
   - Event Schema: ⭐⭐⭐⭐⭐ 4.7/5.0 (145 ratings)
   - Transaction Events: ⭐⭐⭐⭐☆ 4.5/5.0 (98 ratings)

2. **Comment & Discuss**: Ask questions, share insights, get answers
   - 500+ comments and discussions
   - Tagged by type (question, issue, suggestion, documentation)
   - Upvote helpful comments
   - Reply threads for detailed discussions

3. **Bookmark**: Save frequently accessed datasets and fields
   - 342 users bookmarked Event Schema
   - 215 users bookmarked Transaction Events

4. **Share Use Cases**: Help others by sharing how you use the data
   - "Building security analytics dashboard"
   - "Compliance reporting for GDPR/CCPA"
   - "Bandwidth monitoring and analysis"

5. **Find Experts**: Connect with data owners and SMEs
   - Data owners: data-team@netskope.com
   - Field-specific experts listed per dataset

## API Access

### REST API v2 Endpoints

Full API documentation: [API_DOCUMENTATION.md](./catalog/API_DOCUMENTATION.md)

**Base URL**: `https://api.netskope.com/catalog/v1`

**Common Endpoints**:
```bash
# Search fields
GET /fields/search?q=user&type=String

# Get lineage
GET /lineage/event_schema

# Get quality metrics
GET /quality/event_schema

# Check compliance
GET /compliance/field/user

# Get ratings and comments
GET /collaboration/dataset/event_schema/ratings
GET /collaboration/dataset/event_schema/comments
```

**Authentication**: Include API token in header:
```bash
curl -H "Netskope-API-Token: YOUR_TOKEN" \
  "https://api.netskope.com/catalog/v1/fields/search?q=user"
```

## Use Cases

### 1. "Where is the customer email field?"
**Before**: Ask around, search documentation, check code
**Now**: Search catalog → Find `from_user` and `to_user` fields → See they contain PII → Check compliance requirements → View usage in 12 reports

### 2. "Can I delete this field without breaking anything?"
**Before**: Hope for the best, or ask everyone
**Now**: View lineage → See 5 dashboards and 2 ML models depend on it → Coordinate with owners before making changes

### 3. "Which fields contain PII for GDPR compliance?"
**Before**: Manual audit, guesswork
**Now**: Filter by `classification:PII` → Get 85 fields → Export compliance report → See retention requirements and anonymization options

### 4. "Is this data trustworthy for my analysis?"
**Before**: Unknown data quality
**Now**: Check quality score (92/100) → See it's VERIFIED → View 95% completeness → Read validation rules → Trust level: ✅ Gold

### 5. "How is the user field populated?"
**Before**: Dig through code and ETL jobs
**Now**: View lineage → See it comes from Netskope Client Logs → Enriched with user directory → Used by 25+ downstream systems

## Contributing

We welcome contributions to improve the data catalog:

1. **Report Issues**: Found incorrect metadata? [Open an issue](../../issues)
2. **Suggest Enhancements**: Ideas for new features or improvements
3. **Add Comments**: Share your experience using specific fields
4. **Rate Datasets**: Help others by rating data quality
5. **Share Use Cases**: Add your use case to help others learn

## Support & Resources

- **Documentation**: https://docs.netskope.com/catalog
- **API Support**: api-support@netskope.com
- **Community Forum**: https://community.netskope.com/catalog
- **REST API v2 Docs**: https://docs.netskope.com/en/netskope-help/admin-console/rest-api/rest-api-v2-overview-312207/using-the-rest-api-v2-dataexport-iterator-endpoints/
- **Transaction Events**: https://docs.netskope.com/en/netskope-help/data-security/transaction-events/

## License

See [LICENSE](./LICENSE) file for details.

---

**Built with ❤️ by the Netskope Data Team**

*From schema repository to enterprise data catalog - helping teams discover, understand, and trust their data.*

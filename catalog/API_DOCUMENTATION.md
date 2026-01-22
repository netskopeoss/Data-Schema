# Data Catalog API Documentation

## Overview

This document describes the Data Catalog API endpoints for accessing metadata, lineage, quality metrics, compliance information, and collaboration features for the Netskope Data Schema.

## Base Information

- **Version**: 1.0
- **Base URL**: `https://api.netskope.com/catalog/v1`
- **Authentication**: API Token required in header: `Netskope-API-Token: <your-token>`

## Core Endpoints

### 1. Schema & Metadata

#### Get All Schemas
```http
GET /schemas
```

Returns list of all available schemas with basic metadata.

**Response**:
```json
{
  "schemas": [
    {
      "schema_id": "event_schema",
      "name": "Event Schema",
      "version": "1.0",
      "field_count": 748,
      "last_updated": "2026-01-22T00:00:00Z"
    }
  ]
}
```

#### Get Schema Details
```http
GET /schemas/{schema_id}
```

Returns detailed information about a specific schema.

**Query Parameters**:
- `include_fields` (boolean): Include full field list (default: false)
- `include_lineage` (boolean): Include lineage information (default: false)
- `include_quality` (boolean): Include quality metrics (default: false)

#### Search Fields
```http
GET /fields/search?q={query}
```

Search for fields across all schemas using Google-like search.

**Query Parameters**:
- `q` (string, required): Search query
- `type` (string): Filter by data type (String, Integer64, etc.)
- `event_type` (string): Filter by event type
- `classification` (string): Filter by PII classification
- `page` (integer): Page number (default: 1)
- `limit` (integer): Results per page (default: 20, max: 100)
- `sort` (string): Sort by relevance|popularity|name (default: relevance)

**Response**:
```json
{
  "total": 45,
  "page": 1,
  "limit": 20,
  "results": [
    {
      "parameter_name": "user",
      "type": "String",
      "description": "Username or email",
      "event_types": ["alert", "application"],
      "quality_score": 95,
      "has_lineage": true,
      "is_pii": true
    }
  ],
  "facets": {
    "types": {"String": 30, "Integer64": 10, "Boolean": 5},
    "event_types": {"alert": 20, "application": 15}
  }
}
```

### 2. Data Lineage

#### Get Lineage for Dataset
```http
GET /lineage/{dataset_name}
```

Returns lineage information showing upstream sources and downstream consumers.

**Response**:
```json
{
  "lineage_id": "event_schema_lineage_001",
  "dataset_name": "Event Schema",
  "upstream_sources": [...],
  "downstream_consumers": [...],
  "transformations": [...]
}
```

#### Get Lineage Graph
```http
GET /lineage/{dataset_name}/graph
```

Returns lineage as a graph structure suitable for visualization.

**Query Parameters**:
- `depth` (integer): How many levels up/down to traverse (default: 2)
- `direction` (string): upstream|downstream|both (default: both)

**Response**:
```json
{
  "nodes": [
    {
      "id": "event_schema",
      "name": "Event Schema",
      "type": "dataset",
      "metadata": {...}
    }
  ],
  "edges": [
    {
      "source": "netskope_client_logs",
      "target": "event_schema",
      "type": "direct",
      "fields": ["_id", "user"]
    }
  ]
}
```

#### Get Field Lineage
```http
GET /lineage/field/{field_name}
```

Trace lineage for a specific field across datasets.

### 3. Data Quality & Trust

#### Get Quality Metrics
```http
GET /quality/{dataset_name}
```

Returns quality scores and metrics for a dataset.

**Response**:
```json
{
  "dataset_name": "Event Schema",
  "quality_score": {
    "overall": 92,
    "dimensions": {
      "completeness": 95,
      "accuracy": 93,
      "consistency": 90
    }
  },
  "trust_level": "VERIFIED",
  "issues": [...]
}
```

#### Get Quality Trends
```http
GET /quality/{dataset_name}/trends
```

Returns historical quality metrics over time.

**Query Parameters**:
- `start_date` (string): ISO 8601 date
- `end_date` (string): ISO 8601 date
- `granularity` (string): day|week|month (default: week)

### 4. Compliance & Privacy

#### Get Compliance Info
```http
GET /compliance/field/{field_name}
```

Returns compliance and PII classification for a field.

**Response**:
```json
{
  "field_name": "user",
  "classification": "PII",
  "pii_type": ["NAME", "USER_ID"],
  "compliance_frameworks": [
    {
      "framework": "GDPR",
      "requirements": [...],
      "deletion_required": true
    }
  ],
  "risk_level": "HIGH"
}
```

#### Search PII Fields
```http
GET /compliance/pii
```

Returns all fields containing PII.

**Query Parameters**:
- `pii_type` (string): Filter by PII type (EMAIL, IP_ADDRESS, etc.)
- `risk_level` (string): Filter by risk level
- `framework` (string): Filter by compliance framework

#### Get Data Subject Rights
```http
GET /compliance/rights/{field_name}
```

Returns applicable data subject rights (GDPR Article 15-22).

### 5. Collaboration

#### Get Ratings
```http
GET /collaboration/{entity_type}/{entity_id}/ratings
```

Returns rating information for a dataset or field.

#### Submit Rating
```http
POST /collaboration/{entity_type}/{entity_id}/ratings
```

**Request Body**:
```json
{
  "user_id": "u123",
  "rating": 5,
  "comment": "Optional comment"
}
```

#### Get Comments
```http
GET /collaboration/{entity_type}/{entity_id}/comments
```

Returns comments and discussions.

**Query Parameters**:
- `type` (string): Filter by comment type
- `status` (string): Filter by status (open|answered|resolved)
- `sort` (string): Sort by recent|popular (default: recent)

#### Add Comment
```http
POST /collaboration/{entity_type}/{entity_id}/comments
```

**Request Body**:
```json
{
  "user_id": "u123",
  "comment": "Your comment here",
  "comment_type": "question"
}
```

#### Add Reply
```http
POST /collaboration/comments/{comment_id}/replies
```

#### Bookmark/Favorite
```http
POST /collaboration/{entity_type}/{entity_id}/bookmark
DELETE /collaboration/{entity_type}/{entity_id}/bookmark
```

#### Get Usage Feedback
```http
GET /collaboration/{entity_type}/{entity_id}/feedback
```

Returns structured feedback about how users are using the data.

### 6. Discovery & Navigation

#### Browse by Category
```http
GET /browse/{category}
```

Browse schemas by category (alert, network, application, etc.)

#### Get Popular Datasets
```http
GET /popular
```

Returns most popular/frequently accessed datasets.

**Query Parameters**:
- `period` (string): day|week|month|all (default: month)
- `limit` (integer): Number of results (default: 10)

#### Get Recently Updated
```http
GET /recent
```

Returns recently updated schemas and fields.

#### Get Related Fields
```http
GET /fields/{field_name}/related
```

Returns related fields based on usage patterns and lineage.

## Advanced Features

### Batch Operations

#### Batch Field Lookup
```http
POST /fields/batch
```

**Request Body**:
```json
{
  "fields": ["user", "timestamp", "src_ip"],
  "include": ["lineage", "compliance", "quality"]
}
```

### Export

#### Export Schema Documentation
```http
GET /schemas/{schema_id}/export
```

**Query Parameters**:
- `format` (string): json|csv|markdown|pdf (default: json)
- `include` (string[]): What to include (metadata, lineage, quality, compliance)

## Filtering & Faceting

Most list endpoints support advanced filtering using the following syntax:

```http
GET /fields/search?q=user&filters={"type":["String"],"is_pii":[true],"quality_score":{"min":80}}
```

### Available Filters
- **type**: Data type (String, Integer64, etc.)
- **event_types**: Event type
- **classification**: PII classification
- **quality_score**: Range filter (min/max)
- **trust_level**: VERIFIED, TRUSTED, etc.
- **has_lineage**: Boolean
- **is_pii**: Boolean

## Rate Limiting

- **Rate Limit**: 1000 requests per hour per API token
- **Burst Limit**: 50 requests per minute
- **Headers**: `X-RateLimit-Remaining`, `X-RateLimit-Reset`

## Error Responses

```json
{
  "error": {
    "code": "FIELD_NOT_FOUND",
    "message": "The specified field does not exist",
    "details": {...}
  }
}
```

### Common Error Codes
- `FIELD_NOT_FOUND` (404)
- `SCHEMA_NOT_FOUND` (404)
- `INVALID_PARAMETER` (400)
- `UNAUTHORIZED` (401)
- `RATE_LIMIT_EXCEEDED` (429)
- `INTERNAL_ERROR` (500)

## Webhooks (Future)

Subscribe to events for real-time updates:
- Schema changes
- Quality score changes
- New comments/ratings
- Compliance updates

## SDKs & Client Libraries

- Python: `pip install netskope-catalog-sdk`
- JavaScript: `npm install @netskope/catalog-sdk`
- Go: `go get github.com/netskope/catalog-sdk-go`

## Support

- Documentation: https://docs.netskope.com/catalog
- API Issues: api-support@netskope.com
- Community Forum: https://community.netskope.com/catalog

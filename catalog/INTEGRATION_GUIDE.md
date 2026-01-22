# Integration Guide

This guide helps you integrate the Netskope Data Catalog into your applications and workflows.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Authentication](#authentication)
3. [Common Integration Patterns](#common-integration-patterns)
4. [SDK Examples](#sdk-examples)
5. [Embedding Catalog Features](#embedding-catalog-features)
6. [Best Practices](#best-practices)

## Quick Start

### 1. Get API Access

Request an API token from your Netskope administrator or via the admin console.

### 2. Test Connectivity

```bash
curl -H "Netskope-API-Token: YOUR_TOKEN" \
  https://api.netskope.com/catalog/v1/schemas
```

### 3. Start Integrating

Choose your integration method:
- **REST API**: Direct API calls from any language
- **SDK**: Use official SDKs (Python, JavaScript, Go)
- **Webhook**: Subscribe to real-time updates
- **Export**: Batch export for offline processing

## Authentication

### API Token

Include your API token in all requests:

**Header-based** (Recommended):
```bash
curl -H "Netskope-API-Token: YOUR_TOKEN" \
  https://api.netskope.com/catalog/v1/fields/search?q=user
```

**Query parameter** (Not recommended for production):
```bash
curl "https://api.netskope.com/catalog/v1/fields/search?q=user&token=YOUR_TOKEN"
```

### Token Scopes

Request appropriate scopes for your use case:
- `catalog:read` - Read access to catalog data
- `catalog:write` - Add ratings, comments, bookmarks
- `catalog:admin` - Manage schemas and metadata

## Common Integration Patterns

### Pattern 1: Search Integration

Embed catalog search in your application:

```javascript
// JavaScript/React Example
async function searchFields(query) {
  const response = await fetch(
    `https://api.netskope.com/catalog/v1/fields/search?q=${query}`,
    {
      headers: {
        'Netskope-API-Token': process.env.CATALOG_API_TOKEN
      }
    }
  );
  return await response.json();
}

// Usage in component
function FieldSearch() {
  const [results, setResults] = useState([]);
  
  const handleSearch = async (query) => {
    const data = await searchFields(query);
    setResults(data.results);
  };
  
  return (
    <SearchBox onSearch={handleSearch} results={results} />
  );
}
```

### Pattern 2: Lineage Visualization

Display lineage in your data pipeline tools:

```python
# Python Example
import requests
import matplotlib.pyplot as plt
import networkx as nx

def get_lineage_graph(dataset_name):
    response = requests.get(
        f'https://api.netskope.com/catalog/v1/lineage/{dataset_name}/graph',
        headers={'Netskope-API-Token': 'YOUR_TOKEN'}
    )
    return response.json()

def visualize_lineage(dataset_name):
    data = get_lineage_graph(dataset_name)
    
    # Create directed graph
    G = nx.DiGraph()
    
    # Add nodes
    for node in data['nodes']:
        G.add_node(node['id'], label=node['name'], type=node['type'])
    
    # Add edges
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'], type=edge['type'])
    
    # Draw graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=3000, font_size=10, arrows=True)
    plt.show()

# Usage
visualize_lineage('event_schema')
```

### Pattern 3: Compliance Checker

Validate PII usage in your data pipelines:

```python
# Python Example
def check_pii_compliance(field_names):
    """Check if fields contain PII and return compliance info"""
    pii_fields = []
    
    for field in field_names:
        response = requests.get(
            f'https://api.netskope.com/catalog/v1/compliance/field/{field}',
            headers={'Netskope-API-Token': 'YOUR_TOKEN'}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data['classification'] in ['PII', 'PHI', 'FINANCIAL']:
                pii_fields.append({
                    'field': field,
                    'classification': data['classification'],
                    'risk_level': data['risk_level'],
                    'frameworks': [f['framework'] for f in data['compliance_frameworks']]
                })
    
    return pii_fields

# Usage in data pipeline
fields_to_check = ['user', 'src_ip', 'email', 'app']
pii_results = check_pii_compliance(fields_to_check)

if pii_results:
    print("⚠️ PII fields detected:")
    for field in pii_results:
        print(f"  - {field['field']}: {field['classification']} ({field['risk_level']})")
        print(f"    Compliance: {', '.join(field['frameworks'])}")
```

### Pattern 4: Quality Monitoring

Monitor data quality in your dashboards:

```javascript
// JavaScript Example
async function getQualityMetrics(datasetName) {
  const response = await fetch(
    `https://api.netskope.com/catalog/v1/quality/${datasetName}`,
    {
      headers: { 'Netskope-API-Token': process.env.CATALOG_API_TOKEN }
    }
  );
  return await response.json();
}

// Display quality widget
function QualityWidget({ dataset }) {
  const [quality, setQuality] = useState(null);
  
  useEffect(() => {
    getQualityMetrics(dataset).then(setQuality);
  }, [dataset]);
  
  if (!quality) return <Loading />;
  
  return (
    <div className="quality-widget">
      <h3>Data Quality: {quality.quality_score.overall}/100</h3>
      <div className="trust-badge">{quality.trust_level}</div>
      
      <div className="dimensions">
        <div>Completeness: {quality.quality_score.dimensions.completeness}%</div>
        <div>Accuracy: {quality.quality_score.dimensions.accuracy}%</div>
        <div>Timeliness: {quality.quality_score.dimensions.timeliness}%</div>
      </div>
      
      {quality.issues.length > 0 && (
        <div className="issues">
          <h4>Known Issues</h4>
          {quality.issues.map(issue => (
            <div key={issue.issue_id} className={`issue ${issue.severity}`}>
              {issue.description}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

### Pattern 5: Collaborative Features

Add ratings and comments to your data portal:

```python
# Python Example
def submit_rating(entity_type, entity_id, user_id, rating, comment=None):
    """Submit a rating for a dataset or field"""
    response = requests.post(
        f'https://api.netskope.com/catalog/v1/collaboration/{entity_type}/{entity_id}/ratings',
        headers={'Netskope-API-Token': 'YOUR_TOKEN'},
        json={
            'user_id': user_id,
            'rating': rating,
            'comment': comment
        }
    )
    return response.json()

def add_comment(entity_type, entity_id, user_id, comment, comment_type='question'):
    """Add a comment or question"""
    response = requests.post(
        f'https://api.netskope.com/catalog/v1/collaboration/{entity_type}/{entity_id}/comments',
        headers={'Netskope-API-Token': 'YOUR_TOKEN'},
        json={
            'user_id': user_id,
            'comment': comment,
            'comment_type': comment_type
        }
    )
    return response.json()

# Usage
submit_rating('dataset', 'event_schema', 'user123', 5, 'Excellent documentation!')
add_comment('field', 'user', 'user456', 'What format is the user field in?', 'question')
```

## SDK Examples

### Python SDK

```bash
pip install netskope-catalog-sdk
```

```python
from netskope_catalog import CatalogClient

# Initialize client
client = CatalogClient(api_token='YOUR_TOKEN')

# Search fields
results = client.search_fields(
    query='user',
    filters={'type': ['String'], 'is_pii': True}
)

# Get lineage
lineage = client.get_lineage('event_schema')

# Check compliance
compliance = client.get_compliance('user')

# Get quality metrics
quality = client.get_quality_metrics('event_schema')

# Add rating
client.rate_dataset('event_schema', rating=5, comment='Great!')
```

### JavaScript/TypeScript SDK

```bash
npm install @netskope/catalog-sdk
```

```typescript
import { CatalogClient } from '@netskope/catalog-sdk';

// Initialize client
const client = new CatalogClient({
  apiToken: process.env.CATALOG_API_TOKEN
});

// Search fields
const results = await client.searchFields({
  query: 'user',
  filters: { type: ['String'], isPii: true }
});

// Get lineage
const lineage = await client.getLineage('event_schema');

// Check compliance
const compliance = await client.getCompliance('user');

// Get quality metrics
const quality = await client.getQualityMetrics('event_schema');

// Add rating
await client.rateDataset('event_schema', { rating: 5, comment: 'Great!' });
```

### Go SDK

```bash
go get github.com/netskope/catalog-sdk-go
```

```go
package main

import (
    "github.com/netskope/catalog-sdk-go/catalog"
)

func main() {
    // Initialize client
    client := catalog.NewClient("YOUR_TOKEN")
    
    // Search fields
    results, err := client.SearchFields(catalog.SearchOptions{
        Query: "user",
        Filters: map[string][]string{
            "type": {"String"},
            "is_pii": {"true"},
        },
    })
    
    // Get lineage
    lineage, err := client.GetLineage("event_schema")
    
    // Check compliance
    compliance, err := client.GetCompliance("user")
    
    // Get quality metrics
    quality, err := client.GetQualityMetrics("event_schema")
}
```

## Embedding Catalog Features

### Embed Search Widget

```html
<!-- Add to your HTML page -->
<div id="catalog-search"></div>

<script src="https://catalog.netskope.com/widget/search.js"></script>
<script>
  NetskopeSearch.init({
    container: '#catalog-search',
    apiToken: 'YOUR_TOKEN',
    placeholder: 'Search fields...',
    onSelect: (field) => {
      console.log('Selected:', field);
    }
  });
</script>
```

### Embed Lineage Viewer

```html
<div id="lineage-viewer" data-dataset="event_schema"></div>

<script src="https://catalog.netskope.com/widget/lineage.js"></script>
<script>
  NetskopeLineage.init({
    container: '#lineage-viewer',
    apiToken: 'YOUR_TOKEN',
    dataset: 'event_schema',
    depth: 2,
    interactive: true
  });
</script>
```

### Embed Quality Badge

```html
<div id="quality-badge" data-dataset="event_schema"></div>

<script src="https://catalog.netskope.com/widget/quality.js"></script>
<script>
  NetskopeQuality.init({
    container: '#quality-badge',
    apiToken: 'YOUR_TOKEN',
    dataset: 'event_schema',
    displayMode: 'compact' // 'compact' or 'detailed'
  });
</script>
```

## Best Practices

### 1. Caching

Cache catalog data to reduce API calls:

```python
from functools import lru_cache
from datetime import datetime, timedelta

class CatalogCache:
    def __init__(self, ttl_seconds=3600):
        self.ttl = timedelta(seconds=ttl_seconds)
        self.cache = {}
    
    def get(self, key):
        if key in self.cache:
            data, timestamp = self.cache[key]
            if datetime.now() - timestamp < self.ttl:
                return data
        return None
    
    def set(self, key, value):
        self.cache[key] = (value, datetime.now())

# Usage
cache = CatalogCache(ttl_seconds=3600)

def get_field_info(field_name):
    cached = cache.get(field_name)
    if cached:
        return cached
    
    # Fetch from API
    response = requests.get(f'https://api.netskope.com/catalog/v1/fields/{field_name}')
    data = response.json()
    
    cache.set(field_name, data)
    return data
```

### 2. Error Handling

Always handle API errors gracefully:

```python
def safe_api_call(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("API request timed out")
        return None
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Resource not found: {url}")
        elif e.response.status_code == 429:
            print("Rate limit exceeded, retry later")
        else:
            print(f"HTTP error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

### 3. Batch Operations

Use batch endpoints for efficiency:

```python
# Instead of multiple individual calls
for field in fields:
    get_field_info(field)  # Bad: N API calls

# Use batch endpoint
def get_fields_batch(field_names):
    response = requests.post(
        'https://api.netskope.com/catalog/v1/fields/batch',
        headers={'Netskope-API-Token': 'YOUR_TOKEN'},
        json={'fields': field_names}
    )
    return response.json()

# Good: 1 API call
fields_info = get_fields_batch(['user', 'timestamp', 'src_ip'])
```

### 4. Rate Limiting

Respect rate limits:

```python
import time
from functools import wraps

def rate_limit(max_per_minute=60):
    min_interval = 60.0 / max_per_minute
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            wait_time = min_interval - elapsed
            if wait_time > 0:
                time.sleep(wait_time)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit(max_per_minute=50)
def api_call(url):
    return requests.get(url)
```

### 5. Pagination

Handle paginated results properly:

```python
def get_all_results(endpoint, params=None):
    """Fetch all paginated results"""
    all_results = []
    page = 1
    
    while True:
        params = params or {}
        params['page'] = page
        
        response = requests.get(
            endpoint,
            headers={'Netskope-API-Token': 'YOUR_TOKEN'},
            params=params
        )
        data = response.json()
        
        all_results.extend(data['results'])
        
        if page >= data['total_pages']:
            break
        
        page += 1
    
    return all_results
```

## Troubleshooting

### Common Issues

1. **401 Unauthorized**: Check your API token
2. **404 Not Found**: Verify the resource exists
3. **429 Rate Limited**: Reduce request rate or upgrade plan
4. **500 Server Error**: Check API status page or contact support

### Debug Mode

Enable debug logging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('netskope.catalog')

def api_call_with_logging(url):
    logger.debug(f"Calling API: {url}")
    response = requests.get(url)
    logger.debug(f"Response status: {response.status_code}")
    logger.debug(f"Response body: {response.text}")
    return response
```

## Support

- **Documentation**: https://docs.netskope.com/catalog/integration
- **API Status**: https://status.netskope.com
- **Support**: api-support@netskope.com
- **Community**: https://community.netskope.com/catalog
- **GitHub Issues**: https://github.com/netskopeoss/Data-Schema/issues

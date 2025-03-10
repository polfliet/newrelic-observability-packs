# Quickstart Dashboard Configuration

**Title:** Quickstart Dashboard Configuration

| Type                      | `combining`                                             |
| ------------------------- | ------------------------------------------------------- |
| **Additional properties** | [[Not allowed]](# "Additional Properties not allowed.") |
|                           |                                                         |

**Description:** The Dashboard config schema for quickstarts

| Property                       | Pattern | Type   | Deprecated | Definition | Title/Description      |
| ------------------------------ | ------- | ------ | ---------- | ---------- | ---------------------- |
| + [name](#name )               | No      | string | No         | -          | The name schema        |
| + [description](#description ) | No      | string | No         | -          | The description schema |
| + [pages](#pages )             | No      | array  | No         | -          | The pages schema       |
|                                |         |        |            |            |                        |

## <a name="autogenerated_heading_2"></a>1. Must **not** be

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

### <a name="autogenerated_heading_3"></a>1.1. The following properties are required
* permissions

## <a name="name"></a>2. [Required] Property `Quickstart Dashboard Configuration > name`

**Title:** The name schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
"Elasticsearch Monitoring"
```

## <a name="description"></a>3. [Required] Property `Quickstart Dashboard Configuration > description`

**Title:** The description schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
""
```

## <a name="pages"></a>4. [Required] Property `Quickstart Dashboard Configuration > pages`

**Title:** The pages schema

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `[]`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [items](#pages_items)           | -           |
|                                 |             |

### <a name="autogenerated_heading_4"></a>4.1. Quickstart Dashboard Configuration > pages > items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Any of(Option)                                  |
| ----------------------------------------------- |
| [The first anyOf schema](#pages_items_anyOf_i0) |
|                                                 |

#### <a name="pages_items_anyOf_i0"></a>4.1.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema`

**Title:** The first anyOf schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

| Property                                                              | Pattern | Type   | Deprecated | Definition | Title/Description      |
| --------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ---------------------- |
| + [name](#pages_items_anyOf_i0_name )                                 | No      | string | No         | -          | The name schema        |
| + [description](#pages_items_anyOf_i0_description )                   | No      | string | No         | -          | The description schema |
| + [widgets](#pages_items_anyOf_i0_widgets )                           | No      | array  | No         | -          | The widgets schema     |
| - [additionalProperties](#pages_items_anyOf_i0_additionalProperties ) | No      | object | No         | -          | -                      |
|                                                                       |         |        |            |            |                        |

**Example:** 

```json
{
    "name": "Cluster Overview",
    "description": "",
    "widgets": [
        {
            "visualization": {
                "id": "viz.markdown"
            },
            "layout": {
                "column": 1,
                "row": 1,
                "height": 3,
                "width": 3
            },
            "title": "",
            "rawConfiguration": {
                "text": "![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
            }
        }
    ]
}
```

##### <a name="pages_items_anyOf_i0_name"></a>4.1.1.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > name`

**Title:** The name schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
"Cluster Overview"
```

##### <a name="pages_items_anyOf_i0_description"></a>4.1.1.2. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > description`

**Title:** The description schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
""
```

##### <a name="pages_items_anyOf_i0_widgets"></a>4.1.1.3. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets`

**Title:** The widgets schema

| Type                      | `array`                                                                   |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `[]`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |
|                      |                    |

| Each item of this array must be              | Description |
| -------------------------------------------- | ----------- |
| [items](#pages_items_anyOf_i0_widgets_items) | -           |
|                                              |             |

##### <a name="autogenerated_heading_5"></a>4.1.1.3.1. Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items

| Type                      | `combining`                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
|                           |                                                                           |

| Any of(Option)                                         |
| ------------------------------------------------------ |
| [item 0](#pages_items_anyOf_i0_widgets_items_anyOf_i0) |
|                                                        |

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0"></a>4.1.1.3.1.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0`

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

| Property                                                                                     | Pattern | Type   | Deprecated | Definition | Title/Description           |
| -------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | --------------------------- |
| - [visualization](#pages_items_anyOf_i0_widgets_items_anyOf_i0_visualization )               | No      | object | No         | -          | The visualization schema    |
| - [layout](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout )                             | No      | object | No         | -          | The layout schema           |
| - [title](#pages_items_anyOf_i0_widgets_items_anyOf_i0_title )                               | No      | string | No         | -          | The title schema            |
| - [rawConfiguration](#pages_items_anyOf_i0_widgets_items_anyOf_i0_rawConfiguration )         | No      | object | No         | -          | The rawConfiguration schema |
| - [additionalProperties](#pages_items_anyOf_i0_widgets_items_anyOf_i0_additionalProperties ) | No      | object | No         | -          | -                           |
|                                                                                              |         |        |            |            |                             |

**Example:** 

```json
{
    "visualization": {
        "id": "viz.markdown"
    },
    "layout": {
        "column": 1,
        "row": 1,
        "height": 3,
        "width": 3
    },
    "title": "",
    "rawConfiguration": {
        "text": "![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
    }
}
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_visualization"></a>4.1.1.3.1.1.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > visualization`

**Title:** The visualization schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

| Property                                                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [id](#pages_items_anyOf_i0_widgets_items_anyOf_i0_visualization_id )                                     | No      | string | No         | -          | The id schema     |
| - [additionalProperties](#pages_items_anyOf_i0_widgets_items_anyOf_i0_visualization_additionalProperties ) | No      | object | No         | -          | -                 |
|                                                                                                            |         |        |            |            |                   |

**Example:** 

```json
{
    "id": "viz.markdown"
}
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_visualization_id"></a>4.1.1.3.1.1.1.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > visualization > id`

**Title:** The id schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
"viz.markdown"
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_layout"></a>4.1.1.3.1.1.2. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > layout`

**Title:** The layout schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

| Property                                                                                            | Pattern | Type    | Deprecated | Definition | Title/Description |
| --------------------------------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [column](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_column )                             | No      | integer | No         | -          | The column schema |
| - [row](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_row )                                   | No      | integer | No         | -          | The row schema    |
| - [height](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_height )                             | No      | integer | No         | -          | The height schema |
| - [width](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_width )                               | No      | integer | No         | -          | The width schema  |
| - [additionalProperties](#pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_additionalProperties ) | No      | object  | No         | -          | -                 |
|                                                                                                     |         |         |            |            |                   |

**Example:** 

```json
{
    "column": 1,
    "row": 1,
    "height": 3,
    "width": 3
}
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_column"></a>4.1.1.3.1.1.2.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > layout > column`

**Title:** The column schema

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `0`                                                                       |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
1
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_row"></a>4.1.1.3.1.1.2.2. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > layout > row`

**Title:** The row schema

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `0`                                                                       |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
1
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_height"></a>4.1.1.3.1.1.2.3. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > layout > height`

**Title:** The height schema

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `0`                                                                       |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
3
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_layout_width"></a>4.1.1.3.1.1.2.4. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > layout > width`

**Title:** The width schema

| Type                      | `integer`                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `0`                                                                       |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
3
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_title"></a>4.1.1.3.1.1.3. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > title`

**Title:** The title schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
""
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_rawConfiguration"></a>4.1.1.3.1.1.4. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > rawConfiguration`

**Title:** The rawConfiguration schema

| Type                      | `object`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `{}`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

| Property                                                                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [text](#pages_items_anyOf_i0_widgets_items_anyOf_i0_rawConfiguration_text )                                 | No      | string | No         | -          | The text schema   |
| - [additionalProperties](#pages_items_anyOf_i0_widgets_items_anyOf_i0_rawConfiguration_additionalProperties ) | No      | object | No         | -          | -                 |
|                                                                                                               |         |        |            |            |                   |

**Example:** 

```json
{
    "text": "![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
}
```

##### <a name="pages_items_anyOf_i0_widgets_items_anyOf_i0_rawConfiguration_text"></a>4.1.1.3.1.1.4.1. Property `Quickstart Dashboard Configuration > pages > items > anyOf > The first anyOf schema > widgets > items > anyOf > item 0 > rawConfiguration > text`

**Title:** The text schema

| Type                      | `string`                                                                  |
| ------------------------- | ------------------------------------------------------------------------- |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |
| **Default**               | `""`                                                                      |
|                           |                                                                           |

**Description:** An explanation about the purpose of this instance.

**Example:** 

```json
"![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
```

**Example:** 

```json
[
    {
        "visualization": {
            "id": "viz.markdown"
        },
        "layout": {
            "column": 1,
            "row": 1,
            "height": 3,
            "width": 3
        },
        "title": "",
        "rawConfiguration": {
            "text": "![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
        }
    }
]
```

**Example:** 

```json
[
    {
        "name": "Cluster Overview",
        "description": "",
        "widgets": [
            {
                "visualization": {
                    "id": "viz.markdown"
                },
                "layout": {
                    "column": 1,
                    "row": 1,
                    "height": 3,
                    "width": 3
                },
                "title": "",
                "rawConfiguration": {
                    "text": "![Elasticsearch](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/1024px-Elasticsearch_logo.svg.png)\n\n*Use the clickable entity names on the widgets marked `Filterable` to isolate your target data*\n\nData is from the [New Relic Elasticsearch monitoring integration](https://docs.newrelic.com/docs/integrations/host-integrations/host-integrations-list/elasticsearch-monitoring-integration/) and by tailing the JSON log files found in `/var/log/elasticsearch/*.json` using the [embedded log forwarder](https://docs.newrelic.com/docs/logs/enable-log-management-new-relic/enable-log-monitoring-new-relic/forward-your-logs-using-infrastructure-agent/) on the New Relic Infrastructure agent. "
                }
            }
        ]
    }
]
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-09-23 at 19:00:28 +0000
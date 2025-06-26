---
title: MongoDB Schemas
sidebar_position: 1
---

# Taxonomy Store

## Schema Files

📥 **Download Schema Files:**

- [Taxonomy Store JSON](/schemas/taxonomy-store.json)

```javascript
{
  "taxonomy_store": {
    "version": "1.0",
    "last_updated": "2025-06-23",
    "description": "Complete taxonomy and metadata schema for Stratoview content classification",

    "version_management": {
      "schema_version": "1.0",
      "backward_compatibility": true,
      "migration_required": false,
      "change_log": [
        {
          "version": "1.0",
          "date": "2025-06-23",
          "changes": [
            "Initial complete taxonomy store creation",
            "All 4 content types defined with validation",
            "Extensible Intelligence Areas and Topic Areas",
            "Geographic coverage for Lombardia region",
            "Database-agnostic schema design"
          ],
          "breaking_changes": false
        }
      ],
      "versioning_strategy": {
        "major_version": "Breaking changes to core taxonomy structure",
        "minor_version": "New taxonomy categories or non-breaking field additions",
        "patch_version": "Validation updates, bug fixes, documentation improvements"
      },
      "deprecation_policy": {
        "notice_period": "90 days minimum for major changes",
        "support_period": "6 months for deprecated fields",
        "migration_assistance": "Automated migration scripts provided where possible"
      }
    },

    "content_types": {
      "description": "4 fixed content types supported by the platform",
      "types": [
        {
          "id": "index",
          "name": "Index",
          "description": "Core analytical/predictive data with multiple visualization modes",
          "customer_can_create": false,
          "always_public": true,
          "visualization_modes": ["mapview", "indexview", "datavizview"]
        },
        {
          "id": "scenario",
          "name": "Scenario",
          "description": "Text-based strategic scenarios with probability assessments",
          "customer_can_create": true,
          "always_public": false,
          "required_fields": ["probabilita", "scenario_text"]
        },
        {
          "id": "trend_radar",
          "name": "Trend Radar",
          "description": "Visual radar representations of emerging trends",
          "customer_can_create": true,
          "always_public": false,
          "required_fields": ["time_reference", "radar_image"]
        },
        {
          "id": "participatory_data",
          "name": "Participatory Data",
          "description": "Data visualizations from surveys and research activities",
          "customer_can_create": true,
          "always_public": false,
          "required_fields": ["collection_date", "data_visualization"]
        }
      ]
    },

    "intelligence_areas": {
      "description": "Research domain classifications - extensible list",
      "extensible": true,
      "required": true,
      "max_selections": 1,
      "areas": [
        {
          "id": "tourism-resilience",
          "name": "Tourism Resilience Intelligence",
          "description": "Tourism sector resilience analysis against climate and economic shocks",
          "color_code": "#4A90E2",
          "is_active": true
        },
        {
          "id": "territorial-innovation",
          "name": "Territorial Innovation Intelligence",
          "description": "Regional innovation and development strategies",
          "color_code": "#5CB85C",
          "is_active": true
        },
        {
          "id": "city-housing",
          "name": "City Housing Intelligence",
          "description": "Urban housing market and real estate analysis",
          "color_code": "#FF8C42",
          "is_active": true
        },
        {
          "id": "social-resilience",
          "name": "Social Resilience Intelligence",
          "description": "Community and social system resilience assessment",
          "color_code": "#B366D9",
          "is_active": true
        },
        {
          "id": "climate-risks",
          "name": "Climate Risks Intelligence",
          "description": "Climate change impact and risk analysis",
          "color_code": "#E74C3C",
          "is_active": true
        }
      ]
    },

    "topic_areas": {
      "description": "Subject area classifications - extensible list",
      "extensible": true,
      "required": false,
      "max_selections": 10,
      "areas": [
        {
          "id": "population-demographic",
          "name": "Population and Demographic Change",
          "parent_themes": ["society", "demographics"]
        },
        {
          "id": "health",
          "name": "Health",
          "parent_themes": ["society", "wellbeing"]
        },
        {
          "id": "energy-environment",
          "name": "Energy and Environment",
          "parent_themes": ["environment", "sustainability"]
        },
        {
          "id": "food-agriculture",
          "name": "Food and Agriculture",
          "parent_themes": ["economy", "sustainability"]
        },
        {
          "id": "poverty-economic",
          "name": "Poverty and Economic Development",
          "parent_themes": ["economy", "society"]
        },
        {
          "id": "education-knowledge",
          "name": "Education and Knowledge",
          "parent_themes": ["society", "innovation"]
        },
        {
          "id": "innovation-tech",
          "name": "Innovation and Technological Change",
          "parent_themes": ["innovation", "technology"]
        },
        {
          "id": "living-conditions",
          "name": "Living Conditions, Community and Wellbeing",
          "parent_themes": ["society", "wellbeing"]
        },
        {
          "id": "human-rights",
          "name": "Human Rights and Democracy",
          "parent_themes": ["society", "governance"]
        },
        {
          "id": "violence-war",
          "name": "Violence and War",
          "parent_themes": ["society", "security"]
        }
      ]
    },

    "themes_tags": {
      "description": "Flexible tag system for cross-domain content grouping",
      "extensible": true,
      "required": false,
      "max_selections": 5,
      "autocomplete_enabled": true,
      "predefined_tags": [
        "tourism",
        "vulnerability",
        "economic-impact",
        "covid-recovery",
        "infrastructure",
        "interdependency",
        "resilience",
        "climate-tech",
        "adaptation",
        "innovation",
        "survey",
        "perception",
        "awareness",
        "transformation",
        "sustainability",
        "technology",
        "policy",
        "community",
        "environment",
        "urban-planning",
        "transport"
      ]
    },

    "geographic_coverage": {
      "description": "Spatial scope metadata for Lombardia region",
      "extensible": false,
      "required": true,
      "max_selections": 6,
      "areas": [
        {
          "id": "milano",
          "name": "Milano",
          "type": "province",
          "population": 3279944,
          "area_km2": 1575
        },
        {
          "id": "bergamo",
          "name": "Bergamo",
          "type": "province",
          "population": 1114590,
          "area_km2": 2754
        },
        {
          "id": "brescia",
          "name": "Brescia",
          "type": "province",
          "population": 1265954,
          "area_km2": 4785
        },
        {
          "id": "como",
          "name": "Como",
          "type": "province",
          "population": 599204,
          "area_km2": 1288
        },
        {
          "id": "varese",
          "name": "Varese",
          "type": "province",
          "population": 890768,
          "area_km2": 1198
        },
        {
          "id": "all-lombardia",
          "name": "All Lombardia",
          "type": "region",
          "population": 10027602,
          "area_km2": 23863
        }
      ]
    },

    "content_visibility": {
      "description": "Access control classification",
      "options": [
        {
          "id": "public",
          "name": "Public Content",
          "description": "Company-generated content accessible to all users",
          "created_by": ["admin"]
        },
        {
          "id": "private",
          "name": "Private Content",
          "description": "User-generated content accessible only to creator",
          "created_by": ["customer"]
        }
      ]
    },

    "content_metadata_schema": {
      "description": "Complete metadata structure for all content types",
      "core_fields": {
        "content_id": {
          "type": "string",
          "required": true,
          "primary_key": true,
          "format": "uuid"
        },
        "creator_id": {
          "type": "string",
          "required": true,
          "foreign_key": "users.user_id"
        },
        "content_type": {
          "type": "enum",
          "required": true,
          "options": ["index", "scenario", "trend_radar", "participatory_data"]
        },
        "titolo": {
          "type": "string",
          "required": true,
          "max_length": 100,
          "validation": "trim, no_html"
        },
        "descrizione_breve": {
          "type": "string",
          "required": true,
          "max_length": 200,
          "validation": "trim, no_html"
        },
        "descrizione_estesa": {
          "type": "text",
          "required": false,
          "max_length": 10000,
          "validation": "trim, basic_html"
        },
        "data_creazione": {
          "type": "datetime",
          "required": true,
          "auto_generated": true
        },
        "ultima_modifica": {
          "type": "datetime",
          "required": true,
          "auto_updated": true
        },
        "is_company_generated": {
          "type": "boolean",
          "required": true,
          "default": false
        },
        "visibility": {
          "type": "enum",
          "required": true,
          "options": ["public", "private"],
          "business_rule": "customer_content_always_private"
        },
        "content_source": {
          "type": "enum",
          "required": true,
          "options": ["company", "user_created"]
        }
      },
      "taxonomy_fields": {
        "intelligence_area": {
          "type": "string",
          "required": true,
          "foreign_key": "intelligence_areas.id",
          "max_selections": 1
        },
        "topic_area": {
          "type": "string",
          "required": false,
          "foreign_key": "topic_areas.id",
          "max_selections": 1
        },
        "themes": {
          "type": "array",
          "required": false,
          "item_type": "string",
          "max_selections": 5,
          "autocomplete": true
        },
        "geographic_coverage": {
          "type": "array",
          "required": true,
          "item_type": "string",
          "foreign_key": "geographic_areas.id",
          "min_selections": 1,
          "max_selections": 6
        }
      }
    },

    "content_type_specific_schemas": {
      "index": {
        "index_type": {
          "type": "enum",
          "required": true,
          "options": ["analytical", "predictive"]
        },
        "data_level": {
          "type": "enum",
          "required": true,
          "options": ["middleware", "higher_level"]
        },
        "calculation_formula": {
          "type": "text",
          "required": false
        },
        "geographic_resolution": {
          "type": "enum",
          "required": true,
          "options": ["province", "5km", "1km", "municipality"],
          "comment": "Geographic resolution determines the spatial granularity for Index data visualization. Options should be extended based on H3 grid levels and Mapbox zoom capabilities. See technical documentation for implementation details."
        },
        "has_mapview": {
          "type": "boolean",
          "required": true,
          "default": true
        },
        "has_indexview": {
          "type": "boolean",
          "required": true,
          "default": true
        },
        "has_datavizview": {
          "type": "boolean",
          "required": true,
          "default": true
        },
        "default_view_mode": {
          "type": "enum",
          "required": true,
          "options": ["mapview", "indexview", "datavizview"],
          "default": "mapview"
        }
      },
      "scenario": {
        "probabilita": {
          "type": "enum",
          "required": true,
          "options": ["very-low", "low", "medium", "high", "very-high"],
          "labels": {
            "very-low": "Very Low (0-20%)",
            "low": "Low (20-40%)",
            "medium": "Medium (40-60%)",
            "high": "High (60-80%)",
            "very-high": "Very High (80-100%)"
          }
        },
        "scenario_text": {
          "type": "rich_text",
          "required": true,
          "min_length": 50,
          "max_length": 10000,
          "validation": "rich_text_html"
        },
        "scenario_format": {
          "type": "string",
          "required": false,
          "default": "html"
        },
        "scenario_images": {
          "type": "array",
          "required": false,
          "item_type": "file_upload",
          "max_files": 5,
          "file_specs": {
            "formats": ["png", "jpg", "jpeg"],
            "max_size_mb": 10,
            "min_resolution": "800x600"
          }
        }
      },
      "trend_radar": {
        "time_reference": {
          "type": "object",
          "required": true,
          "properties": {
            "month": {
              "type": "integer",
              "required": true,
              "min": 1,
              "max": 12
            },
            "year": {
              "type": "integer",
              "required": true,
              "min": 2020,
              "max": 2030
            }
          }
        },
        "radar_image_url": {
          "type": "file_upload",
          "required": true,
          "file_specs": {
            "formats": ["png", "jpg", "jpeg", "svg"],
            "max_size_mb": 10,
            "min_resolution": "800x600",
            "recommended_resolution": "1200x1200",
            "aspect_ratio": "square_preferred"
          }
        },
        "radar_format": {
          "type": "string",
          "required": false,
          "default": "image"
        },
        "radar_data": {
          "type": "json",
          "required": false,
          "description": "Structured data representation of radar elements"
        }
      },
      "participatory_data": {
        "collection_date": {
          "type": "date",
          "required": true,
          "validation": "past_or_present_only",
          "max_age_years": 10
        },
        "data_format": {
          "type": "string",
          "required": false,
          "default": "visualization"
        },
        "participatory_content": {
          "type": "file_upload",
          "required": true,
          "file_specs": {
            "formats": ["png", "jpg", "jpeg", "svg"],
            "max_size_mb": 10,
            "min_resolution": "800x600",
            "aspect_ratio": "flexible"
          }
        },
        "methodology": {
          "type": "text",
          "required": false,
          "max_length": 2000,
          "description": "Description of data collection methodology"
        }
      }
    },

    "validation_rules": {
      "global": {
        "character_limits": {
          "title": 100,
          "brief_description": 200,
          "extended_description": 10000
        },
        "file_upload": {
          "max_size_mb": 10,
          "supported_formats": ["png", "jpg", "jpeg", "svg"],
          "min_resolution": "800x600"
        }
      },
      "business_rules": {
        "content_creation": [
          "customers_cannot_create_index_content",
          "customer_content_always_private",
          "admin_content_can_be_public_or_private",
          "max_5_tags_per_content",
          "at_least_1_geographic_area_required"
        ],
        "content_visibility": [
          "only_admins_can_change_visibility",
          "private_to_public_requires_admin_approval",
          "customers_cannot_access_others_private_content"
        ]
      }
    },

    "implementation_notes": {
      "geographic_resolution": {
        "note": "Geographic resolution levels are closely tied to the H3 grid system implementation and Mapbox zoom capabilities. Detailed specifications including H3 levels, coordinate systems, and performance considerations should be documented in the technical implementation guide.",
        "related_documentation": [
          "H3 Grid System Integration Guide",
          "Mapbox Performance Optimization",
          "Geospatial Data Processing Pipeline"
        ]
      },
      "extensibility": {
        "note": "Intelligence Areas and Topic Areas are designed to be extensible. New categories should follow the established naming conventions and include proper color coding for UI consistency.",
        "admin_permissions": "Only Super Admin users can add new Intelligence Areas. Content Admin users can suggest additions through the taxonomy management interface."
      },
      "validation_implementation": {
        "note": "All validation rules should be implemented both client-side (for immediate user feedback) and server-side (for data integrity). File upload validations require both size and format checking with proper error messaging."
      }
    }
  }
}

```

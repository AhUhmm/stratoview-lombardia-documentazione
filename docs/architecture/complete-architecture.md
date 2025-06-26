# Stratoview Whitelabel Lombardia - Complete Architecture Documentation

**CONVERSATION LABEL:** Stratoview Whitelabel Lombardia Architecture Analysis  
**DOCUMENT VERSION:** 0.6  
**LAST UPDATED:** June 23, 2025

## Project Overview

**Stratoview Whitelabel Lombardia** is a SaaS platform designed as a repository of content oriented to foresight and strategic design making practices. The platform serves as a comprehensive intelligence system that combines data analysis, visualization, and collaborative strategic planning tools.

### Core Product Concept

Stratoview Whitelabel Lombardia functions as a content management and visualization platform where users can:

- Access and analyze **4 distinct content types**: Indexes, Scenarios, Trend Radar, and Participatory Data
- Create **Projects** that display up to 4 pieces of content simultaneously in customizable layouts
- Browse and discover content through **dual content discovery system** (project-focused + personal content management)
- Generate private user content alongside accessing company-produced intelligence
- Manage individual **ContentBlock controls** with enhanced interaction capabilities

### Key Product Features

**Content Types:**

- **Indexes**: Core analytical/predictive data with multiple visualization modes (Map, Index, DataViz views) accessible via tabs
- **Scenarios**: Text-based strategic scenarios with probability assessments
- **Trend Radar**: Visual radar representations of emerging trends
- **Participatory Data**: Data visualizations of polls and other research activities to gather quantitative feedback from communities around specific topics

**Enhanced Project Management:**

- Up to 4 ContentBlocks per project displaying any mix of content types
- 2 layout modes: Grid View (2x2), Columns View (side-by-side)
- **Individual ContentBlock single view**: Any ContentBlock can expand to full workspace
- **Add Content functionality**: Direct access to Content Browser from project toolbar
- **Project state management**: Empty state vs Active state based on ContentBlock presence
- Persistent state saving for layout preferences, ContentBlock view modes, and individual configurations

**Dual Content Discovery System:**

- **Content Browser (Screen 5)**: Public + Private content for project building with "Add to Project" + "Details" CTAs (accessible from Project Workspace)
- **Personal Content Browser (Screen 7)**: Private content library management with "Edit Content" + "Details" CTAs (accessible from Home Dashboard)
- **Content Detail Modal**: Unified detailed information display with comprehensive metadata
- **Context-aware CTAs**: Different actions based on content ownership and user intent

**Enhanced ContentBlock Management:**

- **Individual ContentBlock Controls**: Info modal, single view toggle, removal from project
- **Index View Tabs**: Map | Index | DataViz tabs for Index ContentBlocks (replaces switch button)
- **ContentBlock State Persistence**: Individual view modes and configurations persist across sessions
- **Info Modal System**: Comprehensive content metadata with Intelligence Area, Topic Area, tags, coverage, and Details CTA

**Visualization Capabilities:**

- **MapView**: Mapbox integration with H3 grid system for geospatial data
- **IndexView**: Structured data presentations
- **DataVizView**: Interactive charts and visualizations
- Geographic search and filtering capabilities

## Master Architecture - Level 1 (Corrected)

```mermaid
graph TB
    %% Presentation Layer
    subgraph "🎨 Presentation Layer"
        LOGIN[Login]
        DASHBOARD[Home Dashboard]
        PROJECT_VIEW[Project Workspace]
        CONTENT_BROWSER[Content Browser]
        PERSONAL_BROWSER[Personal Content Library]
        CONTENT_MODAL[Content Detail Modal]
    end

    %% Business Logic Layer
    subgraph "⚙️ Business Logic"
        PROJECT_MGT[Project Management]
        CONTENTBLOCK_MGT[ContentBlock Individual Controls]
        LAYOUT_ENGINE[Layout Engine]
        CONTENT_MGT[Content Management]
        SEARCH_ENGINE[Search & Filters]
        STATE_MGT[State Management]
    end

    %% Content Layer
    subgraph "📄 Content Types"
        INDEX_CONTENT[Index Content]
        SCENARIO_CONTENT[Scenario Content]
        TREND_CONTENT[Trend Radar Content]
        PARTICIPATORY_CONTENT[Participatory Data Content]
    end

    %% Data Layer
    subgraph "💾 Data Infrastructure"
        CONTENT_REPO[Content Repository]
        GEOSPATIAL_DB[Geospatial Database]
        STATE_STORAGE[State Persistence]
        EXTERNAL_APIs[External Services]
    end

    %% Primary Flow (corrected)
    LOGIN ==> DASHBOARD
    DASHBOARD ==> PROJECT_VIEW
    DASHBOARD ==> PERSONAL_BROWSER
    PROJECT_VIEW ==> CONTENT_BROWSER

    %% Business Logic Connections
    PROJECT_VIEW --> PROJECT_MGT
    PROJECT_VIEW --> LAYOUT_ENGINE
    PROJECT_VIEW --> CONTENTBLOCK_MGT
    CONTENT_BROWSER --> CONTENT_MGT
    CONTENT_BROWSER --> SEARCH_ENGINE
    PERSONAL_BROWSER --> CONTENT_MGT
    PERSONAL_BROWSER --> SEARCH_ENGINE

    %% Content Detail Modal Integration
    CONTENT_BROWSER --> CONTENT_MODAL
    PERSONAL_BROWSER --> CONTENT_MODAL
    CONTENTBLOCK_MGT --> CONTENT_MODAL

    %% Data Flow
    PROJECT_MGT --> STATE_STORAGE
    CONTENTBLOCK_MGT --> STATE_STORAGE
    CONTENT_MGT --> CONTENT_REPO
    LAYOUT_ENGINE --> STATE_STORAGE
    SEARCH_ENGINE --> CONTENT_REPO
    SEARCH_ENGINE --> GEOSPATIAL_DB
    STATE_MGT --> STATE_STORAGE

    %% Content Integration
    CONTENT_REPO --> INDEX_CONTENT
    CONTENT_REPO --> SCENARIO_CONTENT
    CONTENT_REPO --> TREND_CONTENT
    CONTENT_REPO --> PARTICIPATORY_CONTENT

    %% External Integration
    GEOSPATIAL_DB --> EXTERNAL_APIs

    %% Enhanced Styling - 60% Saturation + High Contrast Text
    classDef presentation fill:#4A90E2,stroke:#2E5A87,stroke-width:3px,color:#FFFFFF
    classDef business fill:#FF8C42,stroke:#B8631F,stroke-width:3px,color:#FFFFFF
    classDef content fill:#5CB85C,stroke:#3D7C3D,stroke-width:3px,color:#FFFFFF
    classDef data fill:#E74C3C,stroke:#A93226,stroke-width:3px,color:#FFFFFF

    class LOGIN,DASHBOARD,PROJECT_VIEW,CONTENT_BROWSER,PERSONAL_BROWSER,CONTENT_MODAL presentation
    class PROJECT_MGT,CONTENTBLOCK_MGT,LAYOUT_ENGINE,CONTENT_MGT,SEARCH_ENGINE,STATE_MGT business
    class INDEX_CONTENT,SCENARIO_CONTENT,TREND_CONTENT,PARTICIPATORY_CONTENT content
    class CONTENT_REPO,GEOSPATIAL_DB,STATE_STORAGE,EXTERNAL_APIs data
```

## Entity Relationship Diagram

```mermaid
erDiagram
    User {
        string user_id PK
        string username
        string email
        datetime created_at
        datetime last_login
    }

    Project {
        string project_id PK
        string user_id FK
        string nome
        string descrizione
        datetime data_creazione
        datetime ultima_modifica
        string saved_layout_mode "grid|columns"
        string project_state "empty|active"
        integer contentblock_count
    }

    ContentBlock {
        string contentblock_id PK
        string project_id FK
        string content_id FK
        integer position "1-4"
        boolean is_active
        string current_view_mode "mapview|indexview|datavizview|default"
        boolean single_view_active
        datetime last_interaction
        json contentblock_state
    }

    Content {
        string content_id PK
        string creator_id FK
        string content_type "index|scenario|trend_radar|participatory_data"
        string titolo
        string descrizione_breve
        string descrizione_estesa
        datetime data_creazione
        datetime ultima_modifica
        boolean is_company_generated
        string visibility "public|private"
        string intelligence_area
        string topic_area
        json themes "array_of_theme_tags"
        string geographic_coverage
        string content_source "company|user_created"
    }

    Index {
        string content_id PK,FK
        string index_type "analytical|predictive"
        string data_level "middleware|higher_level"
        string calculation_formula
        string geographic_resolution "province|5km|1km|municipality|etc"
        boolean has_mapview
        boolean has_indexview
        boolean has_datavizview
        string default_view_mode "mapview|indexview|datavizview"
    }

    Scenario {
        string content_id PK,FK
        string probabilita
        text scenario_text
        string scenario_format
        json scenario_images
    }

    TrendRadar {
        string content_id PK,FK
        string radar_image_url
        string radar_format
        json radar_data
        string time_reference
    }

    ParticipatoryData {
        string content_id PK,FK
        string data_format
        json participatory_content
        string methodology
        date collection_date
    }

    IndexVisualization {
        string visualization_id PK
        string content_id FK
        string view_type "mapview|indexview|datavizview"
        json visualization_config
        string data_source_url
        datetime last_updated
    }

    Taxonomy {
        string taxonomy_id PK
        string taxonomy_type "intelligence_area|topic_area|theme"
        string name
        string description
        string parent_id FK "for hierarchical themes"
        boolean is_active
        datetime created_at
        datetime updated_at
    }

    MapData {
        string mapdata_id PK
        string visualization_id FK
        string h3_grid_level
        json geospatial_data
        json mapbox_config
        string nosql_source
    }

    ContentDetailModal {
        string modal_id PK
        string content_id FK
        json modal_metadata
        string access_context "content_browser|personal_browser|contentblock_info"
        datetime last_accessed
    }

    %% Relationships
    User ||--o{ Project : "creates"
    User ||--o{ Content : "creates"

    Project ||--o{ ContentBlock : "contains"
    Content ||--o{ ContentBlock : "displayed_in"

    Content ||--o| Index : "extends"
    Content ||--o| Scenario : "extends"
    Content ||--o| TrendRadar : "extends"
    Content ||--o| ParticipatoryData : "extends"

    Index ||--o{ IndexVisualization : "has"
    IndexVisualization ||--o| MapData : "uses"

    Taxonomy ||--o{ Content : "categorizes"
    Content ||--o{ ContentDetailModal : "generates"
```

## User Permissions & Access Control Architecture

```mermaid
classDiagram

%% === USER TYPES ===
class User {
    +id: UUID
    +username: String
    +email: String
    +userType: "ADMIN" | "CUSTOMER"
    +createdAt: DateTime
    +lastLogin: DateTime
    +isActive: Boolean
}

class AdminUser {
    +accessLevel: "SUPER_ADMIN" | "CONTENT_ADMIN"
    +managedAreas: IntelligenceArea[]
    +canManageTaxonomy: Boolean
    +canManageUsers: Boolean
    +backendAccess: Boolean
}

class CustomerUser {
    +subscriptionTier: "BASIC" | "PROFESSIONAL" | "ENTERPRISE"
    +organizationId: UUID
    +maxPrivateContent: Number
    +maxProjects: Number
    +allowsAdminSupport: Boolean
    +frontendAccess: Boolean
}

%% === INTERFACE SEPARATION ===
class BackendInterface {
    +contentManagement: Boolean
    +userManagement: Boolean
    +taxonomyManagement: Boolean
    +systemAnalytics: Boolean
    +advancedFiltering: Boolean
    +bulkOperations: Boolean
}

class FrontendInterface {
    +contentBrowser: Boolean
    +projectWorkspace: Boolean
    +contentEditor: Boolean
    +basicFiltering: Boolean
    +personalContent: Boolean
}

%% === PERMISSION INTERFACES ===
class ContentPermissions {
    <<interface>>
    +canCreateContent(contentType, visibility): Boolean
    +canReadContent(content): Boolean
    +canUpdateContent(content): Boolean
    +canDeleteContent(content): Boolean
    +canChangeVisibility(content): Boolean
    +canAccessPrivateContent(content, reason): Boolean
}

class ProjectPermissions {
    <<interface>>
    +canCreateProject(): Boolean
    +canReadProject(project): Boolean
    +canUpdateProject(project): Boolean
    +canDeleteProject(project): Boolean
    +canShareProject(project): Boolean
}

class SystemPermissions {
    <<interface>>
    +canAccessBackend(): Boolean
    +canAccessFrontend(): Boolean
    +canManageTaxonomy(): Boolean
    +canManageUsers(): Boolean
    +canViewAnalytics(): Boolean
    +canPerformBulkOperations(): Boolean
}

%% === CONDITIONAL ACCESS PATTERNS ===
class ConditionalAccess {
    +accessType: "SUPPORT" | "MODERATION" | "COMPLIANCE"
    +requestedBy: AdminUser
    +targetContent: Content
    +targetUser: CustomerUser
    +reason: String
    +approvalStatus: "PENDING" | "APPROVED" | "DENIED"
    +approvedBy: AdminUser
    +accessGrantedAt: DateTime
    +accessExpiresAt: DateTime
    +auditTrail: AccessLog[]
}

class AccessLog {
    +timestamp: DateTime
    +adminUser: AdminUser
    +action: String
    +contentAccessed: Content
    +reason: String
    +ipAddress: String
}

%% === ADMIN PERMISSIONS (BACKEND) ===
class AdminContentPermissions {
    +canCreateContent(contentType, visibility): true
    +canReadContent(content): true if public OR ownedContent OR conditionalAccess
    +canUpdateContent(content): true if public OR ownedContent
    +canDeleteContent(content): true if public OR ownedContent
    +canChangeVisibility(content): true if public OR ownedContent
    +canAccessPrivateContent(content, reason): true if approved OR support
    ---
    • Full CRUD on public content
    • Conditional access to customer private content
    • Can create Index content (always public)
    • Audit trail for private content access
}

class AdminProjectPermissions {
    +canCreateProject(): true
    +canReadProject(project): true if ownedProject
    +canUpdateProject(project): true if ownedProject
    +canDeleteProject(project): true if ownedProject
    +canShareProject(project): true if ownedProject
    ---
    • Standard project management
    • No access to customer projects
    • Backend project analytics only
}

class AdminSystemPermissions {
    +canAccessBackend(): true
    +canAccessFrontend(): false
    +canManageTaxonomy(): true
    +canManageUsers(): true
    +canViewAnalytics(): true
    +canPerformBulkOperations(): true
    ---
    • Backend interface only
    • Full administrative capabilities
    • Advanced content management tools
}

%% === CUSTOMER PERMISSIONS (FRONTEND) ===
class CustomerContentPermissions {
    +canCreateContent(contentType, visibility): true if private AND contentType != INDEX
    +canReadContent(content): true if public OR ownedPrivateContent
    +canUpdateContent(content): true if ownedPrivateContent
    +canDeleteContent(content): true if ownedPrivateContent
    +canChangeVisibility(content): false
    +canAccessPrivateContent(content, reason): false
    ---
    • Read-only access to public content
    • Full CRUD on own private content
    • Cannot create Index content
    • Cannot access others' private content
}

class CustomerProjectPermissions {
    +canCreateProject(): true if withinLimit
    +canReadProject(project): true if ownedProject
    +canUpdateProject(project): true if ownedProject
    +canDeleteProject(project): true if ownedProject
    +canShareProject(project): false
    ---
    • Project limit based on subscription
    • No project sharing capabilities
    • Standard project management
}

class CustomerSystemPermissions {
    +canAccessBackend(): false
    +canAccessFrontend(): true
    +canManageTaxonomy(): false
    +canManageUsers(): false
    +canViewAnalytics(): false
    +canPerformBulkOperations(): false
    ---
    • Frontend interface only
    • No administrative functions
    • Basic content browser functionality
}

%% === INTERFACE-SPECIFIC UI RULES ===
class BackendUIRules {
    +showAdvancedFiltering(): true
    +showBulkOperations(): true
    +showUserManagement(): true
    +showTaxonomyManager(): true
    +showContentModeration(): true
    +showSystemAnalytics(): true
    +showPrivateContentAccess(): true with_approval
    +showAuditLogs(): true
    ---
    • Administrative dashboard
    • Advanced content management
    • User and system management
    • Compliance and moderation tools
}

class FrontendUIRules {
    +showBasicFiltering(): true
    +showContentBrowser(): true
    +showProjectWorkspace(): true
    +showContentEditor(): true
    +showPersonalContent(): true
    +showCreateIndexButton(): false
    +showVisibilityToggle(): false
    +showAdvancedOptions(): false
    ---
    • Clean content consumption interface
    • Personal content management
    • Project creation and management
    • No administrative features
}

%% === ACCESS APPROVAL WORKFLOW ===
class AccessApprovalWorkflow {
    <<enumeration>>
    SUPPORT_REQUEST: CustomerUser → Admin (Auto-approved with audit)
    MODERATION_REVIEW: SystemTrigger → Admin (Manual approval required)
    COMPLIANCE_AUDIT: Legal/Regulatory → SuperAdmin (Manual approval + legal review)
    EMERGENCY_ACCESS: SecurityIncident → SuperAdmin (Auto-approved + immediate audit)
    ---
    Note: All access logged and time-limited
    Note: Customer notification for non-support access
}

%% === RELATIONSHIPS ===
User <|-- AdminUser
User <|-- CustomerUser

AdminUser --> BackendInterface : accesses
CustomerUser --> FrontendInterface : accesses

AdminUser --> AdminContentPermissions : implements
AdminUser --> AdminProjectPermissions : implements
AdminUser --> AdminSystemPermissions : implements
AdminUser --> BackendUIRules : implements

CustomerUser --> CustomerContentPermissions : implements
CustomerUser --> CustomerProjectPermissions : implements
CustomerUser --> CustomerSystemPermissions : implements
CustomerUser --> FrontendUIRules : implements

AdminContentPermissions ..|> ContentPermissions
AdminProjectPermissions ..|> ProjectPermissions
AdminSystemPermissions ..|> SystemPermissions

CustomerContentPermissions ..|> ContentPermissions
CustomerProjectPermissions ..|> ProjectPermissions
CustomerSystemPermissions ..|> SystemPermissions

ConditionalAccess --> AdminUser : requestedBy
ConditionalAccess --> CustomerUser : targetUser
ConditionalAccess --> AccessLog : generates
AccessApprovalWorkflow --> ConditionalAccess : governs

%% === BACKEND vs FRONTEND DISTINCTION ===
note for BackendInterface "Admin Backend Features:
• Advanced content management dashboard
• User and organization management
• Taxonomy and metadata management
• System analytics and reporting
• Bulk content operations
• Moderation and compliance tools
• Audit logs and access controls"

note for FrontendInterface "Customer Frontend Features:
• Content discovery and browsing
• Project creation and management
• Personal content editor
• Basic search and filtering
• Clean, consumption-focused UI
• No administrative complexity"

%% === CONDITIONAL ACCESS RULES ===
note for ConditionalAccess "Conditional Access Patterns:
• Support: Auto-approved when customer enables support
• Moderation: Manual approval for content violations
• Compliance: Legal/regulatory requirements with audit
• Emergency: Security incidents with immediate audit trail
• All access is time-limited and fully logged"

%% === PRIVACY PROTECTION ===
note for AccessApprovalWorkflow "Privacy Protection:
• Default: Admins cannot access customer private content
• Exception: Only with explicit approval workflow
• Transparency: Customers notified of access (except support)
• Audit: Complete trail of who accessed what and why
• Time limits: Access expires automatically"
```

### Permission System Overview

[Spiegazione concisa del sistema]

_For detailed permission specifications and conditional access workflows, see [user-roles-documentation.md](./user-roles)_

## System Architecture Diagram

```mermaid
graph TB
    %% User Interface Layer
    subgraph "User Interface Layer"
        LOGIN[Login]
        HOME[Home Dashboard]
        PROJ_LIST[Projects List]
        CONTENT_EDITOR[Content Editor]
        CONTENT_BROWSER[Content Browser]
        PERSONAL_BROWSER[Personal Content Browser]
        PROJECT[Project Container]
        CONTENT_MODAL[Content Detail Modal]
    end

    %% Project Management Layer
    subgraph "Project Workspace"
        LAYOUT[Layout Controller]
        PROJECT_STATE[Project State Manager]
        CB1[ContentBlock 1]
        CB2[ContentBlock 2]
        CB3[ContentBlock 3]
        CB4[ContentBlock 4]
        EMPTY_STATE[Empty State]
        ADD_CONTENT[Add Content CTA]
    end

    %% ContentBlock Enhanced Controls
    subgraph "ContentBlock Individual Controls"
        CB_INFO[Info Modal]
        CB_SINGLE[Individual Single View]
        CB_REMOVE[Remove from Project]
        INDEX_TABS[Index View Tabs]
        CB_STATE[State Persistence]
    end

    %% Layout States
    subgraph "Layout Modes"
        LAYOUT_GRID[Grid View]
        LAYOUT_COLUMNS[Columns View]
        INDIVIDUAL_SINGLE[Individual Single View]
    end

    %% Content Types Layer
    subgraph "Content Types"
        INDEX[Index Content]
        SCENARIO[Scenario Content]
        TREND[Trend Radar Content]
        PARTICIPATORY[Participatory Data Content]
    end

    %% Index Visualizations
    subgraph "Index Visualizations"
        MAPVIEW[Map View]
        INDEXVIEW[Index View]
        DATAVIZVIEW[Data Viz View]
        VIEW_TABS[View Tabs Controller]
    end

    %% Dual Content Management
    subgraph "Dual Content Discovery"
        PUBLIC_CONTENT[Public Content Access]
        PRIVATE_CONTENT[Private Content Access]
        PERSONAL_LIBRARY[Personal Content Library]
        CONTENT_OWNERSHIP[Content Ownership Recognition]
    end

    %% Content Management
    subgraph "Content Management"
        CONTENT_BASE[Content Repository]
        TAXONOMY[Taxonomy System]
        CONTENT_DETAIL[Content Detail System]
    end

    %% Search & Discovery
    subgraph "Search & Discovery"
        SEARCH_ENGINE[Search Engine]
        FILTER_SYSTEM[Filter System]
        GEO_SEARCH[Geographic Search]
        CONTEXT_AWARE[Context-Aware CTAs]
    end

    %% Data Infrastructure
    subgraph "Data Infrastructure"
        MAPBOX[Mapbox Service]
        H3_GRID[H3 Grid System]
        GEOSPATIAL_DB[Geospatial Database]
        METADATA[Content Metadata]
        STATE_STORAGE[State Persistence Storage]
    end

    %% Main Navigation Flow - CORRECTED
    LOGIN --> HOME
    HOME --> PROJ_LIST
    HOME --> CONTENT_EDITOR
    HOME --> PERSONAL_BROWSER

    %% Project Flow - CORRECTED
    PROJ_LIST --> PROJECT
    PROJECT --> CONTENT_BROWSER
    PROJECT --> ADD_CONTENT
    CONTENT_EDITOR --> PERSONAL_BROWSER

    %% Enhanced Project Structure
    PROJECT --> PROJECT_STATE
    PROJECT_STATE --> EMPTY_STATE
    PROJECT_STATE --> LAYOUT

    LAYOUT --> LAYOUT_GRID
    LAYOUT --> LAYOUT_COLUMNS
    LAYOUT --> INDIVIDUAL_SINGLE

    LAYOUT --> CB1
    LAYOUT --> CB2
    LAYOUT --> CB3
    LAYOUT --> CB4

    %% ContentBlock Enhanced Controls
    CB1 --> CB_INFO
    CB1 --> CB_SINGLE
    CB1 --> CB_REMOVE
    CB1 --> CB_STATE

    %% ContentBlock to Content
    CB1 --> INDEX
    CB1 --> SCENARIO
    CB1 --> TREND
    CB1 --> PARTICIPATORY

    %% Index Enhanced Features
    INDEX --> VIEW_TABS
    VIEW_TABS --> MAPVIEW
    VIEW_TABS --> INDEXVIEW
    VIEW_TABS --> DATAVIZVIEW

    %% Dual Content Discovery - CORRECTED
    CONTENT_BROWSER --> PUBLIC_CONTENT
    CONTENT_BROWSER --> PRIVATE_CONTENT
    PERSONAL_BROWSER --> PERSONAL_LIBRARY
    PERSONAL_BROWSER --> CONTENT_OWNERSHIP

    %% Content Detail Modal Integration
    CB_INFO --> CONTENT_MODAL
    CONTENT_BROWSER --> CONTENT_MODAL
    PERSONAL_BROWSER --> CONTENT_MODAL

    %% Content Management Integration
    SEARCH_ENGINE --> CONTENT_BASE
    FILTER_SYSTEM --> TAXONOMY
    GEO_SEARCH --> METADATA
    CONTEXT_AWARE --> CONTENT_OWNERSHIP

    CONTENT_BASE --> INDEX
    CONTENT_BASE --> SCENARIO
    CONTENT_BASE --> TREND
    CONTENT_BASE --> PARTICIPATORY

    CONTENT_BASE --> METADATA
    TAXONOMY --> METADATA
    CONTENT_DETAIL --> CONTENT_MODAL

    %% Data Infrastructure Enhanced
    MAPVIEW --> MAPBOX
    MAPVIEW --> H3_GRID
    MAPVIEW --> GEOSPATIAL_DB

    INDEXVIEW --> GEOSPATIAL_DB
    DATAVIZVIEW --> GEOSPATIAL_DB

    CB_STATE --> STATE_STORAGE
    PROJECT_STATE --> STATE_STORAGE

    %% Color Legend
    subgraph "Legend"
        UI_COLOR[UI Screens<br/>User interface screens/pages + modal]
        PROJECT_COLOR[Project Management<br/>Enhanced project + ContentBlock management]
        CONTENT_COLOR[Content Types<br/>Content types and dual discovery system]
        CONTROL_COLOR[System Controls<br/>Interactive controls and individual management]
        VISUAL_COLOR[Visualizations<br/>Enhanced Index views with tabs]
        DATA_COLOR[Data/Infrastructure<br/>External services + state persistence]
    end

    %% Enhanced Styling - 60% Saturation + High Contrast Text
    classDef uiLayer fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF
    classDef projectLayer fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef contentLayer fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef controlLayer fill:#F0C419,stroke:#A67C00,stroke-width:2px,color:#333333
    classDef visualLayer fill:#B366D9,stroke:#7A4593,stroke-width:2px,color:#FFFFFF
    classDef dataLayer fill:#E74C3C,stroke:#A93226,stroke-width:2px,color:#FFFFFF

    class LOGIN,HOME,PROJ_LIST,CONTENT_EDITOR,CONTENT_BROWSER,PERSONAL_BROWSER,PROJECT,CONTENT_MODAL,UI_COLOR uiLayer
    class LAYOUT,CB1,CB2,CB3,CB4,LAYOUT_GRID,LAYOUT_COLUMNS,INDIVIDUAL_SINGLE,PROJECT_STATE,ADD_CONTENT,EMPTY_STATE,PROJECT_COLOR projectLayer
    class INDEX,SCENARIO,TREND,PARTICIPATORY,CONTENT_BASE,PUBLIC_CONTENT,PRIVATE_CONTENT,PERSONAL_LIBRARY,CONTENT_COLOR contentLayer
    class CB_INFO,CB_SINGLE,CB_REMOVE,SEARCH_ENGINE,FILTER_SYSTEM,GEO_SEARCH,TAXONOMY,CONTEXT_AWARE,CONTENT_OWNERSHIP,CONTROL_COLOR controlLayer
    class MAPVIEW,INDEXVIEW,DATAVIZVIEW,VIEW_TABS,INDEX_TABS,VISUAL_COLOR visualLayer
    class MAPBOX,H3_GRID,GEOSPATIAL_DB,METADATA,STATE_STORAGE,DATA_COLOR dataLayer
```

## Technical Architecture Details

### Data Model Key Relationships

**Enhanced Projects & ContentBlocks:**

- Each Project can contain 0-4 ContentBlocks with **project state management** (Empty/Active)
- ContentBlocks act as UI containers with **individual control capabilities**
- **Individual single view**: Any ContentBlock can expand to full workspace while hiding others
- Same content can appear in multiple projects/ContentBlocks (many-to-many relationship)
- Projects maintain layout state (`saved_layout_mode`) and **individual ContentBlock states**
- **Add Content functionality**: Projects have direct access to Content Browser for content addition

**Enhanced Content Types & Specialization:**

- Base `Content` entity with common metadata and **content ownership tracking**
- 4 specialized content types extend the base: Index, Scenario, TrendRadar, ParticipatoryData
- **Index content supports tabbed view switching** (Map | Index | DataViz tabs)
- Content visibility controls access with **dual discovery system** (public company content vs private user content)
- **Content source attribution**: Company-generated vs user-created content tracking

**Enhanced Metadata & Taxonomy:**

- **Intelligence Area**: Single research domain classification per content
- **Topic Area**: Single subject area classification per content
- **Themes**: Multiple tag-based categorization for cross-domain grouping
- **Geographic Coverage**: Spatial scope metadata for geographic filtering
- **Geographic Resolution**: Spatial granularity for Index content (provinces, 5km, etc.)
- **Content Detail Modal**: Unified metadata display system across all contexts

### User Experience Flow

## Overview

The Stratoview user experience is built around **dual content discovery patterns**, **enhanced project management**, and **individual ContentBlock control systems**. User flows adapt dynamically based on **content ownership**, **project state**, and **user intent context**.

**Main Navigation Paths Enhanced:**

1. **Login** → **Home** → **Personal Content Browser** → **Edit Content** → **Content Editor**
2. **Login** → **Home** → **Projects List** → **Project Container** → **Content Browser** → **Add to Project**
3. **Login** → **Home** → **Projects List** → **Existing Project** → **Project Container** (Active/Empty State)
4. **Login** → **Home** → **Personal Content Browser** → **Content Details** → **Content Detail Modal**
5. **Login** → **Home** → **Content Editor** → **New Content** → **Content Creation**

**Enhanced Project Interaction:**

- Users access projects from Projects List with **dual project states**
- **Empty Projects**: Show empty state with "Browse Content" CTA leading to Content Browser
- **Active Projects**: Display ContentBlocks in configurable layouts (Grid/Columns only)
- **Add Content**: Project toolbar CTA leads to Content Browser for project content addition
- **Individual ContentBlock Management**: Info modal, single view toggle, removal from project
- **ContentBlock state persistence**: Individual view modes and configurations maintained across sessions

**Dual Content Discovery System:**

- **Content Browser (Screen 5)**: Accessible from Project Container → Public company + Private user content → "Add to Project" + "Details" CTAs
- **Personal Content Browser (Screen 7)**: Accessible from Home Dashboard → Private user content exclusively → "Edit Content" + "Details" CTAs
- **Content Detail Modal**: Comprehensive metadata display with Intelligence Area, Topic Area, tags, geographic coverage
- **Context-aware CTAs**: Different actions based on content ownership and user access context
- Advanced search and filtering with **context-appropriate filtering options**

## Primary User Journeys Overview

_This overview diagram shows all main user pathways through the application, organized by functional areas (Project Management, Personal Content, Content Discovery, Workspace Interactions) to provide stakeholders with a clear understanding of user flow architecture._

```mermaid
graph TB
    %% Entry Points
    START[👤 User Access]
    LOGIN[🔐 Login Screen]

    %% Main Hub
    HOME[🏠 Home Dashboard]

    %% Primary Navigation Paths
    subgraph "📁 Project Management Journey"
        PROJ_LIST[Projects List]
        NEW_PROJECT[Create New Project]
        EXISTING_PROJECT[Open Existing Project]

        subgraph "🏗️ Project States"
            EMPTY_PROJECT[Empty Project State]
            ACTIVE_PROJECT[Active Project State]
        end

        subgraph "📦 Content Addition Flow"
            ADD_CONTENT_CTA[Add Content CTA]
            CONTENT_BROWSER[Content Browser]
            ADD_TO_PROJECT[Add to Project Action]
            PROJECT_UPDATED[Project State Updated]
        end
    end

    %% Personal Content Journey
    subgraph "👤 Personal Content Journey"
        PERSONAL_BROWSER[Personal Content Browser]
        CONTENT_EDITOR[Content Editor]

        subgraph "✏️ Content Creation Flow"
            NEW_CONTENT[Create New Content]
            EDIT_CONTENT[Edit Existing Content]
            SAVE_CONTENT[Save Content]
            CONTENT_LIBRARY[Personal Library Updated]
        end
    end

    %% Content Detail Journey
    subgraph "🔍 Content Discovery Journey"
        CONTENT_DETAIL[Content Detail Modal]

        subgraph "🎯 Context-Aware Actions"
            PUBLIC_ACTIONS[Public Content Actions]
            PRIVATE_ACTIONS[Private Content Actions]
            PROJECT_ACTIONS[Project Context Actions]
        end
    end

    %% Enhanced Project Interactions
    subgraph "🎛️ Project Workspace Interactions"
        LAYOUT_SWITCH[Layout Mode Switch]
        CONTENTBLOCK_INFO[ContentBlock Info]
        SINGLE_VIEW[Individual Single View]
        REMOVE_CONTENT[Remove from Project]
    end

    %% Primary Flow
    START --> LOGIN
    LOGIN --> HOME

    %% Project Management Flow
    HOME --> PROJ_LIST
    PROJ_LIST --> NEW_PROJECT
    PROJ_LIST --> EXISTING_PROJECT

    NEW_PROJECT --> EMPTY_PROJECT
    EXISTING_PROJECT --> ACTIVE_PROJECT
    EXISTING_PROJECT --> EMPTY_PROJECT

    EMPTY_PROJECT --> ADD_CONTENT_CTA
    ACTIVE_PROJECT --> ADD_CONTENT_CTA

    ADD_CONTENT_CTA --> CONTENT_BROWSER
    CONTENT_BROWSER --> ADD_TO_PROJECT
    ADD_TO_PROJECT --> PROJECT_UPDATED
    PROJECT_UPDATED --> ACTIVE_PROJECT

    %% Personal Content Flow
    HOME --> PERSONAL_BROWSER
    HOME --> CONTENT_EDITOR

    PERSONAL_BROWSER --> EDIT_CONTENT
    CONTENT_EDITOR --> NEW_CONTENT

    NEW_CONTENT --> SAVE_CONTENT
    EDIT_CONTENT --> SAVE_CONTENT
    SAVE_CONTENT --> CONTENT_LIBRARY
    CONTENT_LIBRARY --> PERSONAL_BROWSER

    %% Content Detail Flow
    CONTENT_BROWSER --> CONTENT_DETAIL
    PERSONAL_BROWSER --> CONTENT_DETAIL
    CONTENTBLOCK_INFO --> CONTENT_DETAIL

    CONTENT_DETAIL --> PUBLIC_ACTIONS
    CONTENT_DETAIL --> PRIVATE_ACTIONS
    CONTENT_DETAIL --> PROJECT_ACTIONS

    %% Project Workspace Interactions
    ACTIVE_PROJECT --> LAYOUT_SWITCH
    ACTIVE_PROJECT --> CONTENTBLOCK_INFO
    ACTIVE_PROJECT --> SINGLE_VIEW
    ACTIVE_PROJECT --> REMOVE_CONTENT

    REMOVE_CONTENT --> ACTIVE_PROJECT
    REMOVE_CONTENT --> EMPTY_PROJECT

    %% Styling
    classDef entry fill:#E8F5E8,stroke:#2E7D32,stroke-width:3px,color:#000
    classDef primary fill:#E3F2FD,stroke:#1565C0,stroke-width:3px,color:#000
    classDef content fill:#FFF3E0,stroke:#EF6C00,stroke-width:3px,color:#000
    classDef action fill:#FCE4EC,stroke:#AD1457,stroke-width:2px,color:#000
    classDef detail fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#000

    class START,LOGIN entry
    class HOME,PROJ_LIST,NEW_PROJECT,EXISTING_PROJECT,EMPTY_PROJECT,ACTIVE_PROJECT primary
    class PERSONAL_BROWSER,CONTENT_EDITOR,CONTENT_BROWSER,NEW_CONTENT,EDIT_CONTENT content
    class ADD_CONTENT_CTA,ADD_TO_PROJECT,SAVE_CONTENT,LAYOUT_SWITCH,SINGLE_VIEW,REMOVE_CONTENT action
    class CONTENT_DETAIL,PUBLIC_ACTIONS,PRIVATE_ACTIONS,PROJECT_ACTIONS,CONTENTBLOCK_INFO detail
```

## Detailed User Pathways

### 1. Project Building Journey

**Path 1A: Empty Project → Active Project**

_This state diagram illustrates the transition from an empty project to an active project through content addition, showing the UI states and user interactions involved._

```mermaid
stateDiagram-v2
    [*] --> EmptyProject: Create New Project
    EmptyProject --> ContentBrowser: "Browse Content" CTA
    ContentBrowser --> FilteringContent: Apply Filters
    FilteringContent --> ContentFound: Discover Content
    ContentFound --> AddToProject: "Add to Project" CTA
    AddToProject --> ActiveProject: ContentBlock Created
    ActiveProject --> [*]: Project Ready

    note right of EmptyProject
        • Empty state display
        • Project toolbar with disabled layout controls
        • Single "Browse Content" CTA
        • Project info: "Empty workspace ready for content"
    end note

    note right of ActiveProject
        • Layout controls enabled (Grid/Columns)
        • "Add Content" CTA in toolbar
        • Individual ContentBlock controls visible
        • Project state: "Active"
    end note
```

**Path 1B: Active Project → Enhanced Management**

_This state diagram demonstrates the enhanced project management capabilities, including individual ContentBlock controls, layout switching, and content detail access within active projects._

```mermaid
stateDiagram-v2
    [*] --> ActiveProject: Open Existing Project
    ActiveProject --> ContentBlockAction: User Interaction

    ContentBlockAction --> InfoModal: Info Button
    ContentBlockAction --> SingleView: Single View Toggle
    ContentBlockAction --> RemoveBlock: Remove Button
    ContentBlockAction --> LayoutChange: Grid to Columns
    ContentBlockAction --> AddMore: "Add Content" CTA

    InfoModal --> DetailModal: "View Details"
    SingleView --> IndexTabs: Switch Views (Index Content)
    IndexTabs --> SingleView: Tab Selection
    RemoveBlock --> ActiveProject: ContentBlock Removed
    RemoveBlock --> EmptyProject: Last ContentBlock Removed
    LayoutChange --> ActiveProject: Layout Updated
    AddMore --> ContentBrowser: Browse for More Content
    ContentBrowser --> ActiveProject: Content Added

    DetailModal --> EditContent: "Edit Content" (if Owned)
    DetailModal --> ActiveProject: "Close"

    note right of SingleView
        • Selected ContentBlock expands to full workspace
        • Other ContentBlocks hidden but states preserved
        • Exit single view returns to current layout
        • Index Content: Map/Index/DataViz tabs available
    end note
```

### 2. Dual Content Discovery Journey

**Path 2A: Content Browser (Project-Focused)**

_This flowchart shows the Content Browser accessed from projects, where users can browse both public company content and private user content together in a unified interface for adding to projects._

```mermaid
flowchart TD
    PROJECT[Active/Empty Project] --> |Browse or Add Content| CB_ENTRY[Content Browser Entry]
    CB_ENTRY --> CB_CONTEXT[Project Context Established]

    CB_CONTEXT --> DUAL_CONTENT[Dual Content Access]
    DUAL_CONTENT --> PUBLIC_CONTENT[Public Company Content]
    DUAL_CONTENT --> PRIVATE_CONTENT[Private User Content]

    PUBLIC_CONTENT --> CB_FILTERING[Apply Filters]
    PRIVATE_CONTENT --> CB_FILTERING

    CB_FILTERING --> CB_RESULTS[Filtered Results]
    CB_RESULTS --> CONTENT_ACTIONS{Content Action}

    CONTENT_ACTIONS --> |Add to Project| ADD_ACTION[Add ContentBlock to Project]
    CONTENT_ACTIONS --> |Details| DETAIL_ACTION[Open Content Detail Modal]

    ADD_ACTION --> PROJECT_RETURN[Return to Project - Active State]
    DETAIL_ACTION --> DETAIL_CONTEXT[Detail Modal with Project Context]

    DETAIL_CONTEXT --> DETAIL_CTA{CTA Choice}
    DETAIL_CTA --> |Edit Content if owned| EDITOR_FLOW[Content Editor]
    DETAIL_CTA --> |Add to Project| ADD_ACTION
    DETAIL_CTA --> |Close| CB_RETURN[Return to Content Browser]

    CB_RETURN --> CB_RESULTS
    PROJECT_RETURN --> PROJECT

    %% Styling
    classDef projectContext fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef contentAccess fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef userAction fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF
    classDef modal fill:#B366D9,stroke:#7A4593,stroke-width:2px,color:#FFFFFF

    class PROJECT,CB_CONTEXT,PROJECT_RETURN projectContext
    class DUAL_CONTENT,PUBLIC_CONTENT,PRIVATE_CONTENT,CB_RESULTS contentAccess
    class CB_ENTRY,CB_FILTERING,ADD_ACTION,EDITOR_FLOW userAction
    class DETAIL_ACTION,DETAIL_CONTEXT,DETAIL_CTA modal
```

**Path 2B: Personal Content Browser (Management-Focused)**

_This flowchart illustrates the Personal Content Browser workflow, focused on managing private user content with editing capabilities and multiple save options._

```mermaid
flowchart TD
    HOME[Home Dashboard] --> |Browse Personal Content| PB_ENTRY[Personal Browser Entry]
    PB_ENTRY --> PB_CONTEXT[Personal Management Context]

    PB_CONTEXT --> PERSONAL_ONLY[Private Content Exclusively]
    PERSONAL_ONLY --> PB_FILTERING[Personal Content Filters]

    PB_FILTERING --> PB_RESULTS[Personal Content Library]
    PB_RESULTS --> PERSONAL_ACTIONS{Content Action}

    PERSONAL_ACTIONS --> |Edit Content| EDIT_ACTION[Direct to Content Editor]
    PERSONAL_ACTIONS --> |Details| PERSONAL_DETAIL[Content Detail Modal]

    EDIT_ACTION --> EDITOR_CONTEXT[Editor with Personal Context]
    PERSONAL_DETAIL --> PERSONAL_DETAIL_CTA{Modal CTA}

    PERSONAL_DETAIL_CTA --> |Edit Content| EDIT_ACTION
    PERSONAL_DETAIL_CTA --> |Close| PB_RETURN[Return to Personal Browser]

    EDITOR_CONTEXT --> SAVE_OPTIONS{Save Choice}
    SAVE_OPTIONS --> |Save Draft| PB_RETURN
    SAVE_OPTIONS --> |Save| PB_RETURN
    SAVE_OPTIONS --> |Save and Add to Project| PROJECT_SELECTION[Select Target Project]

    PROJECT_SELECTION --> PROJECT_ADD[Add to Selected Project]
    PROJECT_ADD --> PROJECT_CONTEXT[Switch to Project Context]

    PB_RETURN --> PB_RESULTS

    %% Styling
    classDef personalContext fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef editAction fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef modal fill:#B366D9,stroke:#7A4593,stroke-width:2px,color:#FFFFFF
    classDef projectFlow fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF

    class HOME,PB_CONTEXT,PERSONAL_ONLY,PB_RESULTS,PB_RETURN personalContext
    class EDIT_ACTION,EDITOR_CONTEXT,SAVE_OPTIONS editAction
    class PERSONAL_DETAIL,PERSONAL_DETAIL_CTA modal
    class PROJECT_SELECTION,PROJECT_ADD,PROJECT_CONTEXT projectFlow
```

## State Transition Documentation

### Project State Management

**Project State Definitions:**

_This state diagram defines the two main project states (Empty/Active) and their associated UI elements and user capabilities._

```mermaid
stateDiagram-v2
    [*] --> EmptyProject: New Project Created
    EmptyProject --> ActiveProject: First ContentBlock Added
    ActiveProject --> EmptyProject: Last ContentBlock Removed
    ActiveProject --> ActiveProject: ContentBlock Added/Removed (1-4 remain)

    state EmptyProject {
        [*] --> NoContentBlocks: 0 ContentBlocks
        NoContentBlocks --> EmptyStateDisplay: UI State
        EmptyStateDisplay --> BrowseContentCTA: User Action Available
    }

    state ActiveProject {
        [*] --> HasContentBlocks: 1-4 ContentBlocks Present
        HasContentBlocks --> LayoutEnabled: Grid/Columns Available
        LayoutEnabled --> IndividualControls: ContentBlock Management
        IndividualControls --> StateePersistence: User Interactions Saved
    }

    note right of EmptyProject
        UI Elements:
        • Empty state illustration
        • "Browse Content" CTA
        • Project info display
        • Layout controls hidden
        • Toolbar minimal
    end note

    note right of ActiveProject
        UI Elements:
        • ContentBlock grid/columns
        • Layout toggle controls
        • "Add Content" CTA
        • Individual ContentBlock controls
        • State persistence active
    end note
```

### ContentBlock Individual States

**ContentBlock State Transitions:**

_This state diagram shows how individual ContentBlocks transition between different view modes (Default, Single View, Info Modal) and the available features in each state._

```mermaid
stateDiagram-v2
    [*] --> DefaultView: ContentBlock Added to Project
    DefaultView --> SingleView: Single View Toggle
    SingleView --> DefaultView: Exit Single View

    DefaultView --> InfoModal: Info Button Clicked
    SingleView --> InfoModal: Info Button Clicked
    InfoModal --> DefaultView: Modal Closed
    InfoModal --> SingleView: Modal Closed (if was in SingleView)

    state SingleView {
        [*] --> ExpandedView: ContentBlock Fills Workspace
        ExpandedView --> IndexTabs: Index Content Only
        IndexTabs --> MapView: Map Tab Selected
        IndexTabs --> IndexView: Index Tab Selected
        IndexTabs --> DataVizView: DataViz Tab Selected
        MapView --> IndexTabs: Tab Switch
        IndexView --> IndexTabs: Tab Switch
        DataVizView --> IndexTabs: Tab Switch
    }

    DefaultView --> Removed: Remove Button
    SingleView --> Removed: Remove Button
    Removed --> [*]: ContentBlock Deleted

    note right of SingleView
        Features Available:
        • Full workspace occupation
        • Other ContentBlocks hidden
        • Index view tabs (if Index content)
        • Info modal access maintained
        • Remove capability maintained
    end note
```

### Content Detail Modal States

**Modal Context Management:**

_This state diagram shows how the unified Content Detail Modal adapts its CTAs and content based on the context from which it was accessed (Content Browser, Personal Browser, or ContentBlock Info)._

```mermaid
stateDiagram-v2
    [*] --> ModalClosed: Default State

    ModalClosed --> ContentBrowserModal: From Content Browser
    ModalClosed --> PersonalBrowserModal: From Personal Browser
    ModalClosed --> ContentBlockModal: From ContentBlock Info

    state ContentBrowserModal {
        [*] --> ProjectContext: Project Context Active
        ProjectContext --> PublicOrPrivateContent: Public + Private Content Available
        PublicOrPrivateContent --> AddCTA: "Add to Project"
        PublicOrPrivateContent --> EditCTA: "Edit Content" (if owned)
        PublicOrPrivateContent --> DetailsCTA: "View Details"
    }

    state PersonalBrowserModal {
        [*] --> PersonalContext: Personal Context Active
        PersonalContext --> OwnedContent: User's Private Content Only
        OwnedContent --> EditCTA: "Edit Content"
        OwnedContent --> DetailsCTA: "View Details"
    }

    state ContentBlockModal {
        [*] --> ProjectContentContext: Project Content Context
        ProjectContentContext --> CurrentContent: ContentBlock Content
        CurrentContent --> ViewDetailsCTA: "View Details"
        CurrentContent --> EditCTA: "Edit Content" (if owned)
    }

    ContentBrowserModal --> ModalClosed: Close Action
    PersonalBrowserModal --> ModalClosed: Close Action
    ContentBlockModal --> ModalClosed: Close Action

    note right of ContentBrowserModal
        Context Features:
        • Project-focused CTAs
        • Add to current project capability
        • Unified access to public + private content
        • Context-aware edit permissions
    end note

    note right of PersonalBrowserModal
        Context Features:
        • Personal management focus
        • Edit-centric CTAs
        • Private content exclusively
        • Content library organization
    end note
```

## Navigation Decision Points

### Context-Aware Action Matrix

**User Action Decision Tree:**

_This decision flowchart illustrates how the system determines which CTAs to show based on content ownership (user-owned vs company content) and current user context (Personal Browser, Content Browser, or ContentBlock Info)._

```mermaid
flowchart TD
    USER_ACTION[User Initiates Action] --> CONTENT_CHECK{Content Ownership?}

    CONTENT_CHECK --> |User Owned| OWNED_ACTIONS[Owned Content Actions]
    CONTENT_CHECK --> |Company Content| PUBLIC_ACTIONS[Public Content Actions]

    OWNED_ACTIONS --> CONTEXT_CHECK_OWNED{Current Context?}
    PUBLIC_ACTIONS --> CONTEXT_CHECK_PUBLIC{Current Context?}

    %% Owned Content Paths
    CONTEXT_CHECK_OWNED --> |Personal Browser| PERSONAL_OWNED[Personal Context + Owned]
    CONTEXT_CHECK_OWNED --> |Content Browser| PROJECT_OWNED[Project Context + Owned]
    CONTEXT_CHECK_OWNED --> |ContentBlock Info| BLOCK_OWNED[Block Context + Owned]

    PERSONAL_OWNED --> PERSONAL_CTA[Edit Content and Details]
    PROJECT_OWNED --> PROJECT_OWNED_CTA[Add to Project and Edit and Details]
    BLOCK_OWNED --> BLOCK_OWNED_CTA[View Details and Edit Content]

    %% Public Content Paths
    CONTEXT_CHECK_PUBLIC --> |Personal Browser| NOT_AVAILABLE[Not Available in Personal Browser]
    CONTEXT_CHECK_PUBLIC --> |Content Browser| PROJECT_PUBLIC[Project Context + Public]
    CONTEXT_CHECK_PUBLIC --> |ContentBlock Info| BLOCK_PUBLIC[Block Context + Public]

    PROJECT_PUBLIC --> PROJECT_PUBLIC_CTA[Add to Project and Details]
    BLOCK_PUBLIC --> BLOCK_PUBLIC_CTA[View Details Only]

    %% Styling
    classDef decision fill:#F0C419,stroke:#A67C00,stroke-width:2px,color:#333333
    classDef owned fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef public fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF
    classDef cta fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef unavailable fill:#E74C3C,stroke:#A93226,stroke-width:2px,color:#FFFFFF

    class USER_ACTION,CONTENT_CHECK,CONTEXT_CHECK_OWNED,CONTEXT_CHECK_PUBLIC decision
    class OWNED_ACTIONS,PERSONAL_OWNED,PROJECT_OWNED,BLOCK_OWNED owned
    class PUBLIC_ACTIONS,PROJECT_PUBLIC,BLOCK_PUBLIC public
    class PERSONAL_CTA,PROJECT_OWNED_CTA,BLOCK_OWNED_CTA,PROJECT_PUBLIC_CTA,BLOCK_PUBLIC_CTA cta
    class NOT_AVAILABLE unavailable
```

### Enhanced ContentBlock Management Decision Flow

**ContentBlock Interaction Decision Matrix:**

_This comprehensive flowchart maps all possible ContentBlock interactions (Info, Single View, Remove, Index Tabs) and their resulting system behaviors and state changes._

```mermaid
flowchart TD
    CB_INTERACTION[ContentBlock User Interaction] --> CB_ACTION_TYPE{Action Type?}

    CB_ACTION_TYPE --> |Info Button| INFO_FLOW[Info Modal Flow]
    CB_ACTION_TYPE --> |Single View Toggle| SINGLE_FLOW[Single View Flow]
    CB_ACTION_TYPE --> |Remove Button| REMOVE_FLOW[Remove Flow]
    CB_ACTION_TYPE --> |Index Tab| INDEX_FLOW[Index View Flow]

    %% Info Modal Flow
    INFO_FLOW --> INFO_MODAL[Display ContentBlock Info Modal]
    INFO_MODAL --> INFO_ACTIONS{Modal Action?}
    INFO_ACTIONS --> |View Details| DETAIL_MODAL[Full Content Detail Modal]
    INFO_ACTIONS --> |Edit Content| EDIT_CHECK{User Owns Content?}
    INFO_ACTIONS --> |Close| CB_RETURN[Return to ContentBlock]

    EDIT_CHECK --> |Yes| CONTENT_EDITOR[Open Content Editor]
    EDIT_CHECK --> |No| INFO_MODAL

    %% Single View Flow
    SINGLE_FLOW --> SINGLE_STATE_CHECK{Currently in Single View?}
    SINGLE_STATE_CHECK --> |No| ENTER_SINGLE[Enter Single View]
    SINGLE_STATE_CHECK --> |Yes| EXIT_SINGLE[Exit Single View]

    ENTER_SINGLE --> SINGLE_VIEW_STATE[ContentBlock Fills Workspace]
    SINGLE_VIEW_STATE --> SINGLE_FEATURES[Single View Features Available]

    SINGLE_FEATURES --> INDEX_CHECK{Index Content?}
    INDEX_CHECK --> |Yes| INDEX_TABS[Map/Index/DataViz Tabs]
    INDEX_CHECK --> |No| SINGLE_CONTENT[Content Display Only]

    INDEX_TABS --> TAB_INTERACTION[User Selects Tab]
    TAB_INTERACTION --> VIEW_SWITCH[Switch Index View]
    VIEW_SWITCH --> SINGLE_VIEW_STATE

    EXIT_SINGLE --> LAYOUT_RETURN[Return to Current Layout]

    %% Remove Flow
    REMOVE_FLOW --> REMOVE_CONFIRM{Confirm Removal?}
    REMOVE_CONFIRM --> |Yes| EXECUTE_REMOVE[Remove ContentBlock]
    REMOVE_CONFIRM --> |No| CB_RETURN

    EXECUTE_REMOVE --> COUNT_CHECK{Remaining ContentBlocks?}
    COUNT_CHECK --> |1-4 Remaining| ACTIVE_PROJECT[Active Project State]
    COUNT_CHECK --> |0 Remaining| EMPTY_PROJECT[Empty Project State]

    %% Index View Flow (when not in Single View)
    INDEX_FLOW --> CURRENT_VIEW_CHECK{Current View Context?}
    CURRENT_VIEW_CHECK --> |Single View| INDEX_TABS
    CURRENT_VIEW_CHECK --> |Normal View| NORMAL_INDEX_SWITCH[Switch Index View in Layout]

    NORMAL_INDEX_SWITCH --> CB_RETURN

    %% Return Points
    DETAIL_MODAL --> CB_RETURN
    CONTENT_EDITOR --> CB_RETURN
    LAYOUT_RETURN --> CB_RETURN
    ACTIVE_PROJECT --> CB_RETURN
    EMPTY_PROJECT --> EMPTY_STATE[Empty State Display]
    SINGLE_CONTENT --> SINGLE_VIEW_STATE

    %% Styling
    classDef interaction fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF
    classDef flow fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef decision fill:#F0C419,stroke:#A67C00,stroke-width:2px,color:#333333
    classDef state fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef modal fill:#B366D9,stroke:#7A4593,stroke-width:2px,color:#FFFFFF

    class CB_INTERACTION,TAB_INTERACTION interaction
    class INFO_FLOW,SINGLE_FLOW,REMOVE_FLOW,INDEX_FLOW flow
    class CB_ACTION_TYPE,INFO_ACTIONS,SINGLE_STATE_CHECK,INDEX_CHECK,REMOVE_CONFIRM,COUNT_CHECK,CURRENT_VIEW_CHECK,EDIT_CHECK decision
    class SINGLE_VIEW_STATE,ACTIVE_PROJECT,EMPTY_PROJECT,LAYOUT_RETURN,CB_RETURN state
    class INFO_MODAL,DETAIL_MODAL modal
```

## Mobile User Experience Adaptations

### Mobile Navigation Flow

_This flowchart shows how the desktop user flows adapt to mobile interfaces, with vertical ContentBlock stacking, touch interactions, and mobile-specific UI patterns._

```mermaid
flowchart TD
    MOBILE_ENTRY[Mobile App Entry] --> MOBILE_HOME[Mobile Home Dashboard]

    MOBILE_HOME --> MOBILE_NAV{Navigation Choice}
    MOBILE_NAV --> |Projects| MOBILE_PROJECTS[Projects List - Mobile]
    MOBILE_NAV --> |Personal Content| MOBILE_PERSONAL[Personal Content - Mobile]
    MOBILE_NAV --> |Create| MOBILE_EDITOR[Content Editor - Mobile]

    %% Mobile Project Flow
    MOBILE_PROJECTS --> MOBILE_PROJECT[Project View - Mobile]
    MOBILE_PROJECT --> MOBILE_PROJECT_STATE{Project State}

    MOBILE_PROJECT_STATE --> |Empty| MOBILE_EMPTY[Empty State - Stacked]
    MOBILE_PROJECT_STATE --> |Active| MOBILE_ACTIVE[ContentBlocks Vertical Stack]

    MOBILE_ACTIVE --> MOBILE_CB_ACTIONS{ContentBlock Action}
    MOBILE_CB_ACTIONS --> |Tap ContentBlock| MOBILE_SINGLE[Mobile Single View]
    MOBILE_CB_ACTIONS --> |Info Icon| MOBILE_INFO[Mobile Info Sheet]
    MOBILE_CB_ACTIONS --> |Remove| MOBILE_REMOVE[Mobile Remove Confirmation]

    MOBILE_SINGLE --> MOBILE_SINGLE_FEATURES[Mobile Single View Features]
    MOBILE_SINGLE_FEATURES --> MOBILE_INDEX_TABS[Index Tabs - Mobile]
    MOBILE_SINGLE_FEATURES --> MOBILE_BACK[Back to Stack]

    MOBILE_BACK --> MOBILE_ACTIVE

    %% Mobile Content Discovery
    MOBILE_EMPTY --> |Browse Content| MOBILE_CONTENT_BROWSER[Mobile Content Browser]
    MOBILE_CONTENT_BROWSER --> MOBILE_FILTERS[Mobile Filter Drawer]
    MOBILE_CONTENT_BROWSER --> MOBILE_CONTENT_LIST[Mobile Content Cards]

    MOBILE_CONTENT_LIST --> MOBILE_CONTENT_ACTIONS{Content Action}
    MOBILE_CONTENT_ACTIONS --> |Add| MOBILE_ADD[Add to Project - Mobile]
    MOBILE_CONTENT_ACTIONS --> |Details| MOBILE_DETAIL[Mobile Detail Sheet]

    MOBILE_ADD --> MOBILE_ACTIVE

    %% Styling
    classDef mobileEntry fill:#4A90E2,stroke:#2E5A87,stroke-width:2px,color:#FFFFFF
    classDef mobileNav fill:#FF8C42,stroke:#B8631F,stroke-width:2px,color:#FFFFFF
    classDef mobileContent fill:#5CB85C,stroke:#3D7C3D,stroke-width:2px,color:#FFFFFF
    classDef mobileAction fill:#B366D9,stroke:#7A4593,stroke-width:2px,color:#FFFFFF

    class MOBILE_ENTRY,MOBILE_HOME mobileEntry
    class MOBILE_NAV,MOBILE_PROJECT_STATE,MOBILE_CB_ACTIONS,MOBILE_CONTENT_ACTIONS mobileNav
    class MOBILE_PROJECTS,MOBILE_PROJECT,MOBILE_ACTIVE,MOBILE_CONTENT_BROWSER mobileContent
    class MOBILE_SINGLE,MOBILE_INFO,MOBILE_DETAIL,MOBILE_ADD mobileAction
```

## Performance and State Management

### State Persistence Strategy

```
ContentBlock State Storage:
├── Individual ContentBlock States
│   ├── View mode preference (MapView/IndexView/DataVizView)
│   ├── Single view activation status
│   ├── Position in project layout
│   └── Last interaction timestamp
├── Project-Level States
│   ├── Active layout mode (Grid/Columns)
│   ├── ContentBlock arrangement
│   ├── Project state classification (Empty/Active)
│   └── Last modified timestamp
└── User Session States
    ├── Last visited project
    ├── Content browser filter preferences
    └── Personal browser organization preferences
```

### Technical Implementation Notes

**Modal Interaction Tracking**: _For advanced implementations, consider tracking which modals users access most frequently and from which contexts to optimize UI patterns and predict user needs._

**Navigation State Management**: _Advanced features like deep linking to specific ContentBlocks, browser back/forward support for modal states, and connection loss recovery can enhance user experience but add complexity to state management architecture._

## Technical Implementation Notes

### Enhanced Frontend Architecture

- **UI Layer**: React-based interfaces for all user-facing screens + Content Detail Modal
- **Dual Content Discovery**: Context-specific content browsers for project building vs content management
- **Enhanced Project Management**: Dynamic layout system with individual ContentBlock controls
- **ContentBlock Individual Control System**: Reusable components with persistent state management and individual interaction capabilities
- **Content Detail Modal**: Unified detailed content information display with context-aware CTAs

### Enhanced Backend Architecture

- **Content Repository**: Centralized content management with access control and **content ownership tracking**
- **Taxonomy System**: Hierarchical categorization system for content organization
- **Enhanced Visualization Engine**: Multiple rendering modes for Index content with **tabbed view switching**
- **Geographic Services**: Integration with Mapbox and H3 grid system
- **State Persistence System**: Individual ContentBlock states and project configuration storage

### Data Infrastructure Enhanced

- **Geospatial Database**: NoSQL storage for geographic and visualization data
- **Content Metadata**: Structured storage for taxonomy, content relationships, and **content ownership**
- **State Storage**: ContentBlock individual states, project configurations, and user preferences
- **External Services**: Mapbox for mapping, H3 for spatial indexing
- **Content Detail System**: Unified content information storage for modal display

## Version History

### v0.6 (2025-06-23)

- Integrated User Permissions & Access Control Architecture
- Added detailed permission matrices and conditional access patterns

### v0.5 (2025-06-23)

- Complete User Experience Flow integration
- Dual content discovery system
- Individual ContentBlock management

### v0.4 (2025-06-18)

- Initial complete architecture with ERD
- System architecture diagrams
- Technical implementation notes

## Migration Information for New Conversations

### Key Decisions Made

1. **ContentBlock Individual Controls**: Enhanced granular control over ContentBlocks with info modal, single view, and removal capabilities
2. **Dual Content Discovery Strategy**: Separate browsers for project building vs personal content management
3. **Project state management**: Empty vs Active states based on ContentBlock presence with appropriate CTAs
4. **Index View Tabs**: Replaced switch button with tabbed interface (Map | Index | DataViz)
5. **Content ownership recognition**: Tracking and context-aware CTAs based on content source
6. **Individual Single View**: Any ContentBlock can expand independently of layout mode
7. **Navigation flow correction**: Content Browser accessible from Project, Personal Browser from Home
8. **Geographic search logic**: Filters by content metadata, not visualization data
9. **Enhanced mobile responsive**: ContentBlock vertical stacking with adapted controls

### Outstanding Design Questions

1. **Cross-ContentBlock interactions**: Should ContentBlocks be able to interact with each other in advanced scenarios?
2. **Personal content sharing**: Future capability for sharing personal content between users in same organization?
3. **Advanced ContentBlock features**: Additional controls beyond current set (e.g., minimize, duplicate, advanced filtering)?
4. **Content Detail Modal extensions**: Integration with external data sources for enhanced content information?

### Progressive Enhancement Pipeline

**Phase 1: Master Architecture (COMPLETED)**

- ✅ Simplified master architecture with corrected navigation flows
- ✅ Dual content discovery system properly represented
- ✅ ContentBlock individual controls integration
- ✅ Foundation for detailed phases

**Phase 2: User Journey Flow Implementation (COMPLETED)**

- ✅ **Purpose**: Detailed user pathways with state transitions
- ✅ **Content**: Project workspace interactions, dual content discovery flows, context-aware actions
- ✅ **Deliverable**: Complete User Experience Flow section with Primary User Journeys Overview, Detailed Pathways (4), State Transition Documentation (3), Navigation Decision Points (2), Mobile Adaptations
- ✅ **Target**: UX implementation teams and developers

**Phase 3: Component Architecture Development (NEXT)**

- **Purpose**: Technical component hierarchy for development teams
- **Content**: Component relationships, ContentBlock individual controls, TypeScript interfaces
- **Target**: Development teams and sprint planning

**Phase 4: Index Visualizations Technical Detail**

- **Purpose**: Data layer implementation specifics
- **Content**: 3-layer map architecture, performance optimization, H3 integration
- **Target**: Technical implementation and performance optimization

### Related Documentation Available

- Original Stratoview Whitelabel Lombardia diagrams (object mapping and user flow PDFs)
- Stratoview project analysis (`stratoview_knowledgebase.md`) for related geospatial intelligence concepts
- Enhanced user roles and permissions documentation for implementation guidance
- Progressive disclosure strategy documentation for architectural approach

---

**For Developers:** Use the Master Architecture for high-level understanding, ERD for database schema design, and System Architecture for detailed component relationships including individual ContentBlock management and corrected navigation flows.

**For AI Screen Generation:** The Master and System Architecture provide enhanced component hierarchy and data relationships for generating contextually appropriate interfaces with dual content discovery and individual ContentBlock controls.

**Next Steps:** Proceed with Progressive Enhancement Phases 2-4 to complete detailed implementation documentation for development teams and AI code generation.

**Document Status:** READY FOR PHASE 3 - Component Architecture Development

# Stratoview Whitelabel Lombardia - User Roles & Permissions Documentation

**CONVERSATION LABEL:** Stratoview Whitelabel Lombardia Architecture Analysis  
**DOCUMENT VERSION:** 1.0  
**LAST UPDATED:** June 18, 2025

## Overview

This document defines the comprehensive user roles, permissions, and access control system for Stratoview Whitelabel Lombardia. The platform implements a dual-interface architecture with distinct backend and frontend experiences, ensuring appropriate feature separation between administrative and customer functions.

## Architecture Principles

### 1. Interface Separation
- **Backend Interface**: Administrative dashboard for content management, user administration, and system configuration
- **Frontend Interface**: Customer-focused interface for content consumption, project management, and personal content creation
- **Clear Boundaries**: Admins use backend exclusively, customers use frontend exclusively

### 2. Privacy-First Design
- **Default Privacy**: Admins cannot access customer private content by default
- **Conditional Access**: Structured approval workflow for exceptional access needs
- **Complete Audit Trail**: All access logged with timestamps, reasons, and responsible parties
- **Transparency**: Customer notifications for non-support administrative access

### 3. Role-Based Access Control
- **Permission Interfaces**: Standardized permission contracts for consistent implementation
- **Concrete Implementations**: Specific permission classes for each user type
- **UI Visibility Rules**: Interface-specific rules determining feature availability

## User Types & Characteristics

### Admin Users
**Primary Role**: Platform administration and public content management

**Characteristics:**
- Access Level: `SUPER_ADMIN` or `CONTENT_ADMIN`
- Managed Areas: Specific Intelligence Areas responsibility
- Backend Access: Exclusive administrative interface
- Taxonomy Management: Can modify content categorization
- User Management: Can manage customer accounts (based on access level)

**Subscription/Access Model:**
- Internal platform employees or contracted administrators
- No subscription tiers (role-based access instead)

### Customer Users  
**Primary Role**: Content consumption and private content creation

**Characteristics:**
- Subscription Tier: `BASIC`, `PROFESSIONAL`, or `ENTERPRISE`
- Organization ID: Multi-user organization support
- Content Limits: Maximum private content based on subscription
- Project Limits: Maximum projects based on subscription
- Frontend Access: Customer-focused interface only
- Support Access Control: Can enable/disable admin support access

**Subscription Features:**
- **Basic**: Limited private content, basic project count
- **Professional**: Increased limits, advanced filtering
- **Enterprise**: High limits, organizational features

## Permission System Architecture

### Content Permissions

**Interface Definition:**
```typescript
interface ContentPermissions {
    canCreateContent(contentType: string, visibility: string): boolean
    canReadContent(content: Content): boolean
    canUpdateContent(content: Content): boolean
    canDeleteContent(content: Content): boolean
    canChangeVisibility(content: Content): boolean
    canAccessPrivateContent(content: Content, reason: string): boolean
}
```

**Admin Implementation:**
- **Create**: All content types, any visibility
- **Read**: All public content + own private content + conditionally approved private content
- **Update**: All public content + own private content
- **Delete**: All public content + own private content
- **Visibility**: Can change visibility of public content and own content
- **Private Access**: Through conditional access workflow only

**Customer Implementation:**
- **Create**: Scenario, Trend Radar, Participatory Data (private only)
- **Read**: All public content + own private content only
- **Update**: Own private content only
- **Delete**: Own private content only
- **Visibility**: Cannot change content visibility
- **Private Access**: Not permitted

### Project Permissions

**Admin Project Management:**
- Standard project creation and management
- No access to customer projects
- Project analytics in backend interface
- Can share projects with other admins

**Customer Project Management:**
- Project creation within subscription limits
- Full CRUD on own projects only
- No project sharing capabilities
- Projects limited by subscription tier

### System Permissions

**Backend Access (Admin Only):**
- Content management dashboard
- User and organization management
- Taxonomy and metadata administration
- System analytics and reporting
- Bulk operations on content
- Audit logs and compliance tools

**Frontend Access (Customer Only):**
- Content browser and discovery
- Project workspace management
- Personal content editor
- Basic search and filtering
- No administrative functions

## Content Creation Matrix

| Content Type | Admin (Public) | Admin (Private) | Customer (Public) | Customer (Private) |
|--------------|----------------|-----------------|-------------------|-------------------|
| **Index** | ✅ Always | ❌ N/A | ❌ Never | ❌ Never |
| **Scenario** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Trend Radar** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |
| **Participatory Data** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes |

**Key Rules:**
- **Index Content**: Always public, only admins can create
- **Customer Content**: Always private, cannot be made public
- **Admin Content**: Can be public or private, admin's choice
- **Visibility Changes**: Only admins can promote private→public content

## Conditional Access System

### Access Types & Approval Workflow

**1. Support Access**
- **Trigger**: Customer enables support access in settings
- **Approval**: Auto-approved when customer opts in
- **Scope**: Customer's private content for troubleshooting
- **Duration**: Until customer disables support access
- **Notification**: Customer aware through opt-in settings

**2. Moderation Access**
- **Trigger**: Content violation reports or automated detection
- **Approval**: Manual approval by Super Admin required
- **Scope**: Specific flagged content only
- **Duration**: Limited to investigation period (max 30 days)
- **Notification**: Customer notified of moderation review

**3. Compliance Access**
- **Trigger**: Legal, regulatory, or court-ordered requirements
- **Approval**: Super Admin + legal team approval required
- **Scope**: Specified content or user account
- **Duration**: As required by legal obligation
- **Notification**: Customer notified per legal requirements

**4. Emergency Access**
- **Trigger**: Security incidents, data breaches, system threats
- **Approval**: Auto-approved for Super Admin with immediate audit
- **Scope**: Minimum necessary for incident response
- **Duration**: Limited to incident resolution (max 7 days)
- **Notification**: Customer notified post-incident

### Audit Trail Requirements

**Access Logging:**
- Timestamp of access
- Admin user identity
- Specific content accessed
- Reason for access
- Access type (support/moderation/compliance/emergency)
- IP address and session information
- Duration of access session

**Audit Retention:**
- Support access: 1 year retention
- Moderation access: 3 years retention
- Compliance access: Per legal requirements
- Emergency access: 7 years retention

## Interface-Specific Features

### Backend Interface (Admin)

**Content Management:**
- Advanced content dashboard with bulk operations
- Detailed content analytics and performance metrics
- Content moderation queue and review tools
- Public content editing and visibility management
- Taxonomy and metadata management interface

**User Management:**
- Customer account administration
- Organization and subscription management
- Support access monitoring and control
- User activity analytics and reporting

**System Administration:**
- Platform configuration and settings
- Intelligence Area and Topic Area management
- Theme taxonomy creation and organization
- System health monitoring and analytics
- Compliance and audit reporting tools

### Frontend Interface (Customer)

**Content Discovery:**
- Clean content browser with basic filtering
- Search by Intelligence Area, Topic Area, Themes
- Geographic coverage filtering
- Content type and date sorting
- Default grouping by Intelligence Area

**Project Management:**
- Project creation within subscription limits
- Up to 4 ContentBlock workspace
- Layout management (single/grid/columns)
- Content addition through browser integration

**Personal Content:**
- Private content creation (3 of 4 content types)
- Personal content library management
- Basic editing and organization tools
- No visibility or sharing controls

## Implementation Guidelines

### Database Schema Considerations

**User Tables:**
```sql
Users (id, username, email, user_type, created_at, last_login, is_active)
AdminUsers (user_id, access_level, managed_areas, can_manage_taxonomy, can_manage_users)
CustomerUsers (user_id, subscription_tier, organization_id, max_private_content, max_projects, allows_admin_support)
```

**Access Control Tables:**
```sql
ConditionalAccess (id, access_type, requested_by, target_content, target_user, reason, approval_status, approved_by, granted_at, expires_at)
AccessLogs (id, timestamp, admin_user, action, content_accessed, reason, ip_address)
```

### API Endpoint Security

**Authentication Requirements:**
- JWT tokens with role-based claims
- Backend endpoints require admin authentication
- Frontend endpoints require customer authentication
- Cross-interface access strictly prohibited

**Authorization Middleware:**
- Permission checking before content access
- Conditional access validation for private content
- Audit logging for all administrative actions
- Rate limiting based on user type and subscription

### Frontend Route Protection

**Backend Routes (Admin Only):**
- `/admin/*` - Administrative dashboard
- `/manage/*` - Content and user management
- `/analytics/*` - System analytics and reporting
- `/audit/*` - Compliance and audit interfaces

**Frontend Routes (Customer Only):**
- `/app/*` - Main application interface
- `/projects/*` - Project management
- `/content/*` - Content browser and editor
- `/profile/*` - Personal settings and preferences

## Security Considerations

### Data Protection
- Customer private content encrypted at rest
- Access logs protected from unauthorized access
- Conditional access requires multi-factor authentication
- Regular security audits of permission implementations

### Privacy Compliance
- GDPR compliance for EU customers
- Right to deletion for customer private content
- Data portability for customer-generated content
- Transparent privacy policies for conditional access

### Audit Requirements
- Immutable audit logs for compliance access
- Regular access pattern analysis for anomaly detection
- Automated alerts for unauthorized access attempts
- Quarterly access review and cleanup procedures

## Migration and Rollout Strategy

### Phase 1: Core Permission System
- Implement user types and basic permissions
- Deploy frontend/backend interface separation
- Basic content access controls

### Phase 2: Conditional Access
- Deploy conditional access workflow
- Implement audit logging system
- Customer notification system

### Phase 3: Advanced Features
- Advanced filtering and bulk operations (backend)
- Enhanced content management tools
- Comprehensive analytics and reporting

## Outstanding Technical Decisions

1. **Session Management**: How to handle cross-interface session sharing for support scenarios
2. **Content Migration**: Process for moving customer private content during subscription changes
3. **Organization Features**: Multi-user organization content sharing within customer accounts
4. **API Rate Limiting**: Different limits for admin bulk operations vs customer browsing
5. **Backup Access**: Emergency access procedures when primary authentication fails

---

**Next Steps:** 
- Implement permission interfaces in chosen backend framework
- Design UI mockups for backend and frontend interfaces based on visibility rules
- Develop conditional access approval workflow
- Create comprehensive testing strategy for access controls

**Related Documentation:**
- Main Stratoview Whitelabel Lombardia Architecture Documentation
- Content Creation & Management Workflow (pending)
- UI State Management & Transitions (pending)
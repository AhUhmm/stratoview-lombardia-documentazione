# Implementation Guide

## Database Implementation Status

### Current State: **Database Agnostic**

The taxonomy store and schemas are designed to work with multiple database technologies. **Final stack selection pending.**

### Available Implementations

#### 🍃 MongoDB + Mongoose

- **File**: `taxonomy/mongodb-schema.js`
- **Status**: ✅ Complete with validation, discriminators, middleware
- **Best for**: Rapid prototyping, flexible schema evolution, JSON-heavy workloads
- **Team fit**: JavaScript/Node.js focused teams

#### 🐍 Django + PostgreSQL

- **File**: `taxonomy/django-models.py`
- **Status**: ✅ Complete with admin integration, custom validators, business rules
- **Best for**: Robust validation, admin interfaces, structured data
- **Team fit**: Python focused teams, strong admin requirements

### Implementation Decision Matrix

| Criteria               | MongoDB/Mongoose                | Django/PostgreSQL                |
| ---------------------- | ------------------------------- | -------------------------------- |
| **Development Speed**  | ⭐⭐⭐⭐⭐ Fast prototyping     | ⭐⭐⭐ Structured approach       |
| **Schema Flexibility** | ⭐⭐⭐⭐⭐ Dynamic schema       | ⭐⭐ Migration-based             |
| **Validation**         | ⭐⭐⭐ Application level        | ⭐⭐⭐⭐⭐ Database + App        |
| **Admin Interface**    | ⭐⭐ Custom required            | ⭐⭐⭐⭐⭐ Built-in Django Admin |
| **Geographic Data**    | ⭐⭐⭐⭐ Native GeoJSON         | ⭐⭐⭐⭐⭐ PostGIS integration   |
| **Learning Curve**     | ⭐⭐⭐⭐ JavaScript familiarity | ⭐⭐⭐ Python + Django concepts  |

## Taxonomy Implementation Notes

### Business Rules Implementation

Both implementations include critical business rules:

```javascript
// MongoDB Example
ContentSchema.pre("save", function (next) {
  if (this.content_source === "user_created" && this.visibility === "public") {
    return next(new Error("Customer content must be private"));
  }
  next();
});
```

```python
# Django Example
def clean(self):
    if self.content_source == 'user_created' and self.visibility == 'public':
        raise ValidationError('Customer content must be private')
```

### Geographic Resolution Technical Notes

**Implementation Pending**: Geographic resolution levels (`province`, `5km`, `1km`, `municipality`) require integration with:

- **H3 Grid System**: For spatial indexing and performant queries
- **Mapbox GL JS**: For visualization rendering at different zoom levels
- **PostGIS/MongoDB Geospatial**: For efficient geographic queries

**Related Documentation Needed**:

- H3 Grid System Integration Guide
- Mapbox Performance Optimization
- Geospatial Data Processing Pipeline

**Performance Considerations**:

- Resolution level directly impacts query performance
- Different resolutions require different caching strategies
- Mobile optimization needed for higher resolution data

### File Upload Strategy

**Current Status**: Schema includes file upload fields, **storage strategy TBD**

**Options for Production**:

```yaml
Local Development:
  - File system storage
  - Simple validation

Production Options:
  MongoDB: GridFS or AWS S3 with metadata in MongoDB
  Django: django-storages with S3/GCS + database metadata

Validation Requirements:
  - File size: 10MB max
  - Formats: PNG, JPG, JPEG, SVG
  - Image resolution: 800x600 minimum
  - Virus scanning: Recommended for production
```

### Extensibility Implementation

**Intelligence Areas & Topic Areas** are designed for runtime extension:

```javascript
// MongoDB - Adding new Intelligence Area
const newArea = new IntelligenceArea({
  _id: "new-intelligence-area",
  name: "New Intelligence Area",
  description: "Description...",
  color_code: "#FF5722",
  is_active: true,
});
```

```python
# Django - Adding new Intelligence Area
new_area = IntelligenceArea.objects.create(
    id='new-intelligence-area',
    name='New Intelligence Area',
    description='Description...',
    color_code='#FF5722',
    is_active=True
)
```

**Admin Permissions**: Only Super Admin users should create new Intelligence Areas through dedicated admin interfaces.

## API Strategy (Future)

### Recommended API Patterns

**REST Endpoints Structure**:

```
Authentication:
POST /api/auth/login/
POST /api/auth/logout/

Taxonomy:
GET  /api/taxonomy/intelligence-areas/
GET  /api/taxonomy/topic-areas/
GET  /api/taxonomy/geographic-areas/
GET  /api/taxonomy/themes/

Content Management:
GET    /api/content/                    # List with filters
POST   /api/content/                    # Create new
GET    /api/content/{id}/               # Get specific
PUT    /api/content/{id}/               # Update
DELETE /api/content/{id}/               # Delete

Project Management:
GET    /api/projects/                   # User projects
POST   /api/projects/                   # Create project
GET    /api/projects/{id}/              # Get project
PUT    /api/projects/{id}/              # Update project
DELETE /api/projects/{id}/              # Delete project

ContentBlock Management:
GET    /api/projects/{id}/contentblocks/           # List ContentBlocks
POST   /api/projects/{id}/contentblocks/           # Add ContentBlock
PUT    /api/projects/{id}/contentblocks/{block_id}/ # Update ContentBlock
DELETE /api/projects/{id}/contentblocks/{block_id}/ # Remove ContentBlock
```

### Authentication Strategy

- **JWT tokens** for stateless authentication
- **Role-based permissions** (Admin vs Customer)
- **Content ownership validation** on all operations

## Development Workflow

### 1. Choose Stack

```bash
# Option A: MongoDB + Node.js
npm init
npm install mongoose express multer jsonwebtoken

# Option B: Django + PostgreSQL
pip install django psycopg2-binary pillow django-cors-headers
```

### 2. Initialize Database

```bash
# MongoDB
node -e "require('./taxonomy/mongodb-schema.js')"

# Django
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata taxonomy/initial-data.json
```

### 3. Load Initial Taxonomy

Both implementations include scripts for loading initial taxonomy data from `taxonomy-store.json`.

## Testing Strategy

### Required Test Coverage

- **Business rule validation**: Customer content privacy, admin-only Index creation
- **File upload validation**: Size, format, resolution checks
- **Taxonomy relationships**: Foreign key constraints, cascade deletes
- **ContentBlock management**: Project state updates, position constraints
- **Geographic coverage**: Min/max selection validation

### Test Data

Use `taxonomy-store.json` as source for test fixtures to ensure consistency.

## Deployment Considerations

### Environment Variables

```bash
# Common
SECRET_KEY=your-secret-key
ENVIRONMENT=production
ALLOWED_HOSTS=yourdomain.com

# MongoDB
MONGODB_URI=mongodb://localhost:27017/stratoview

# Django
DATABASE_URL=postgresql://user:pass@localhost/stratoview
```

### File Storage Production

- **AWS S3**: For scalable file storage
- **CDN**: CloudFront or CloudFlare for image delivery
- **Image Processing**: On-upload resizing and optimization

---

## Decision Checklist

Before proceeding with implementation:

- [ ] **Team Stack Preference**: MongoDB vs Django preference survey
- [ ] **Geographic Requirements**: H3 integration complexity assessment
- [ ] **Admin Interface Needs**: Django Admin vs custom admin build
- [ ] **File Upload Volume**: Expected usage for storage planning
- [ ] **Performance Requirements**: Expected concurrent users and data size
- [ ] **Mobile Strategy**: Native app vs responsive web priority

## Next Steps

1. **Stack Decision**: Team meeting to choose MongoDB vs Django
2. **Initial Setup**: Follow chosen implementation guide
3. **API Development**: Implement core CRUD operations
4. **Frontend Integration**: Connect with chosen backend
5. **Testing & Deployment**: Set up CI/CD pipeline

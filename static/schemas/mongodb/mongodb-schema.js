// Stratoview Lombardia - MongoDB Schema Implementation
// Compatible with Mongoose ODM
// Based on Taxonomy Store v1.0

const mongoose = require("mongoose");
const { Schema } = mongoose;

// ================================
// TAXONOMY COLLECTIONS
// ================================

// Intelligence Areas Schema
const IntelligenceAreaSchema = new Schema(
  {
    _id: {
      type: String, // Using semantic ID instead of ObjectId
      required: true,
    },
    name: {
      type: String,
      required: true,
      trim: true,
      maxlength: 100,
    },
    description: {
      type: String,
      required: true,
      trim: true,
      maxlength: 500,
    },
    color_code: {
      type: String,
      required: true,
      match: /^#[0-9A-F]{6}$/i, // Hex color validation
    },
    is_active: {
      type: Boolean,
      required: true,
      default: true,
    },
    created_at: {
      type: Date,
      default: Date.now,
    },
    updated_at: {
      type: Date,
      default: Date.now,
    },
  },
  {
    _id: false, // Disable auto _id since we're using custom string IDs
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
  }
);

// Topic Areas Schema
const TopicAreaSchema = new Schema(
  {
    _id: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
      trim: true,
      maxlength: 100,
    },
    parent_themes: [
      {
        type: String,
        trim: true,
      },
    ],
    is_active: {
      type: Boolean,
      required: true,
      default: true,
    },
  },
  {
    _id: false,
    timestamps: true,
  }
);

// Geographic Areas Schema
const GeographicAreaSchema = new Schema(
  {
    _id: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
      trim: true,
    },
    type: {
      type: String,
      required: true,
      enum: ["province", "region", "municipality"],
    },
    population: {
      type: Number,
      min: 0,
    },
    area_km2: {
      type: Number,
      min: 0,
    },
  },
  {
    _id: false,
    timestamps: true,
  }
);

// ================================
// USER MANAGEMENT
// ================================

const UserSchema = new Schema(
  {
    username: {
      type: String,
      required: true,
      unique: true,
      trim: true,
      minlength: 3,
      maxlength: 50,
    },
    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      match: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    },
    user_type: {
      type: String,
      required: true,
      enum: ["ADMIN", "CUSTOMER"],
    },
    last_login: {
      type: Date,
    },
  },
  {
    timestamps: { createdAt: "created_at", updatedAt: "updated_at" },
  }
);

// ================================
// CONTENT MANAGEMENT
// ================================

// Base Content Schema (used by all content types)
const ContentSchema = new Schema(
  {
    creator_id: {
      type: Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    content_type: {
      type: String,
      required: true,
      enum: ["index", "scenario", "trend_radar", "participatory_data"],
    },
    titolo: {
      type: String,
      required: true,
      trim: true,
      minlength: 1,
      maxlength: 100,
    },
    descrizione_breve: {
      type: String,
      required: true,
      trim: true,
      minlength: 1,
      maxlength: 200,
    },
    descrizione_estesa: {
      type: String,
      trim: true,
      maxlength: 10000,
    },
    is_company_generated: {
      type: Boolean,
      required: true,
      default: false,
    },
    visibility: {
      type: String,
      required: true,
      enum: ["public", "private"],
    },
    content_source: {
      type: String,
      required: true,
      enum: ["company", "user_created"],
    },

    // Taxonomy Fields
    intelligence_area: {
      type: String,
      ref: "IntelligenceArea",
      required: true,
    },
    topic_area: {
      type: String,
      ref: "TopicArea",
    },
    themes: [
      {
        type: String,
        trim: true,
        validate: {
          validator: function (themes) {
            return themes.length <= 5; // Max 5 tags
          },
          message: "Maximum 5 themes allowed",
        },
      },
    ],
    geographic_coverage: [
      {
        type: String,
        ref: "GeographicArea",
        validate: {
          validator: function (coverage) {
            return coverage.length >= 1 && coverage.length <= 6;
          },
          message: "At least 1 and maximum 6 geographic areas required",
        },
      },
    ],
  },
  {
    timestamps: { createdAt: "data_creazione", updatedAt: "ultima_modifica" },
    discriminatorKey: "content_type",
    collection: "contents",
  }
);

// Content Type Specific Schemas

// Index Content Schema
const IndexSchema = new Schema({
  index_type: {
    type: String,
    required: true,
    enum: ["analytical", "predictive"],
  },
  data_level: {
    type: String,
    required: true,
    enum: ["middleware", "higher_level"],
  },
  calculation_formula: {
    type: String,
    maxlength: 2000,
  },
  geographic_resolution: {
    type: String,
    required: true,
    enum: ["province", "5km", "1km", "municipality"],
  },
  has_mapview: {
    type: Boolean,
    required: true,
    default: true,
  },
  has_indexview: {
    type: Boolean,
    required: true,
    default: true,
  },
  has_datavizview: {
    type: Boolean,
    required: true,
    default: true,
  },
  default_view_mode: {
    type: String,
    required: true,
    enum: ["mapview", "indexview", "datavizview"],
    default: "mapview",
  },
});

// Scenario Content Schema
const ScenarioSchema = new Schema({
  probabilita: {
    type: String,
    required: true,
    enum: ["very-low", "low", "medium", "high", "very-high"],
  },
  scenario_text: {
    type: String,
    required: true,
    minlength: 50,
    maxlength: 10000,
  },
  scenario_format: {
    type: String,
    default: "html",
  },
  scenario_images: [
    {
      filename: String,
      original_name: String,
      mimetype: String,
      size: Number,
      upload_date: {
        type: Date,
        default: Date.now,
      },
    },
  ],
});

// Trend Radar Content Schema
const TrendRadarSchema = new Schema({
  time_reference: {
    month: {
      type: Number,
      required: true,
      min: 1,
      max: 12,
    },
    year: {
      type: Number,
      required: true,
      min: 2020,
      max: 2030,
    },
  },
  radar_image_url: {
    filename: {
      type: String,
      required: true,
    },
    original_name: String,
    mimetype: String,
    size: Number,
    upload_date: {
      type: Date,
      default: Date.now,
    },
  },
  radar_format: {
    type: String,
    default: "image",
  },
  radar_data: {
    type: Schema.Types.Mixed, // Flexible JSON structure
  },
});

// Participatory Data Content Schema
const ParticipatoryDataSchema = new Schema({
  collection_date: {
    type: Date,
    required: true,
    validate: {
      validator: function (date) {
        const now = new Date();
        const tenYearsAgo = new Date(
          now.getFullYear() - 10,
          now.getMonth(),
          now.getDate()
        );
        return date <= now && date >= tenYearsAgo;
      },
      message:
        "Collection date must be in the past and not older than 10 years",
    },
  },
  data_format: {
    type: String,
    default: "visualization",
  },
  participatory_content: {
    filename: {
      type: String,
      required: true,
    },
    original_name: String,
    mimetype: String,
    size: Number,
    upload_date: {
      type: Date,
      default: Date.now,
    },
  },
  methodology: {
    type: String,
    maxlength: 2000,
  },
});

// ================================
// PROJECT MANAGEMENT
// ================================

const ProjectSchema = new Schema(
  {
    user_id: {
      type: Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    nome: {
      type: String,
      required: true,
      trim: true,
      maxlength: 100,
    },
    descrizione: {
      type: String,
      trim: true,
      maxlength: 500,
    },
    saved_layout_mode: {
      type: String,
      enum: ["grid", "columns"],
      default: "grid",
    },
    project_state: {
      type: String,
      enum: ["empty", "active"],
      default: "empty",
    },
    contentblock_count: {
      type: Number,
      min: 0,
      max: 4,
      default: 0,
    },
  },
  {
    timestamps: { createdAt: "data_creazione", updatedAt: "ultima_modifica" },
  }
);

const ContentBlockSchema = new Schema(
  {
    project_id: {
      type: Schema.Types.ObjectId,
      ref: "Project",
      required: true,
    },
    content_id: {
      type: Schema.Types.ObjectId,
      ref: "Content",
      required: true,
    },
    position: {
      type: Number,
      required: true,
      min: 1,
      max: 4,
    },
    is_active: {
      type: Boolean,
      required: true,
      default: true,
    },
    current_view_mode: {
      type: String,
      enum: ["mapview", "indexview", "datavizview", "default"],
      default: "default",
    },
    single_view_active: {
      type: Boolean,
      default: false,
    },
    last_interaction: {
      type: Date,
      default: Date.now,
    },
    contentblock_state: {
      type: Schema.Types.Mixed, // Flexible state storage
    },
  },
  {
    timestamps: true,
  }
);

// ================================
// MIDDLEWARE & VALIDATION
// ================================

// Pre-save middleware for business rules
ContentSchema.pre("save", function (next) {
  // Customer content must be private
  if (this.content_source === "user_created" && this.visibility === "public") {
    return next(new Error("Customer content must be private"));
  }

  // Only admins can create Index content
  if (this.content_type === "index" && this.content_source === "user_created") {
    return next(new Error("Only admins can create Index content"));
  }

  next();
});

// Update project state when ContentBlocks change
ContentBlockSchema.post("save", async function () {
  const project = await this.model("Project").findById(this.project_id);
  if (project) {
    const blockCount = await this.model("ContentBlock").countDocuments({
      project_id: this.project_id,
      is_active: true,
    });

    project.contentblock_count = blockCount;
    project.project_state = blockCount > 0 ? "active" : "empty";
    await project.save();
  }
});

// ================================
// MODEL EXPORTS
// ================================

// Create discriminated models for content types
const Content = mongoose.model("Content", ContentSchema);
const Index = Content.discriminator("index", IndexSchema);
const Scenario = Content.discriminator("scenario", ScenarioSchema);
const TrendRadar = Content.discriminator("trend_radar", TrendRadarSchema);
const ParticipatoryData = Content.discriminator(
  "participatory_data",
  ParticipatoryDataSchema
);

// Export all models
module.exports = {
  // Taxonomy Models
  IntelligenceArea: mongoose.model("IntelligenceArea", IntelligenceAreaSchema),
  TopicArea: mongoose.model("TopicArea", TopicAreaSchema),
  GeographicArea: mongoose.model("GeographicArea", GeographicAreaSchema),

  // User Models
  User: mongoose.model("User", UserSchema),

  // Content Models (discriminated)
  Content,
  Index,
  Scenario,
  TrendRadar,
  ParticipatoryData,

  // Project Models
  Project: mongoose.model("Project", ProjectSchema),
  ContentBlock: mongoose.model("ContentBlock", ContentBlockSchema),
};

// ================================
// USAGE EXAMPLES & SETUP
// ================================

/*
// Database Connection Example
const mongoose = require('mongoose');

async function connectDB() {
  try {
    await mongoose.connect('mongodb://localhost:27017/stratoview', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('Database connection error:', error);
    process.exit(1);
  }
}

// Initialize Taxonomy Data
async function initializeTaxonomy() {
  const { IntelligenceArea, TopicArea, GeographicArea } = require('./models');
  
  // Create Intelligence Areas
  const intelligenceAreas = [
    {
      _id: 'tourism-resilience',
      name: 'Tourism Resilience Intelligence',
      description: 'Tourism sector resilience analysis against climate and economic shocks',
      color_code: '#4A90E2'
    }
    // ... add other areas
  ];
  
  await IntelligenceArea.insertMany(intelligenceAreas);
}

// Content Creation Example
async function createScenario(userId, scenarioData) {
  const { Scenario } = require('./models');
  
  const scenario = new Scenario({
    creator_id: userId,
    content_type: 'scenario',
    titolo: scenarioData.title,
    descrizione_breve: scenarioData.brief_description,
    intelligence_area: 'climate-risks',
    geographic_coverage: ['milano'],
    visibility: 'private',
    content_source: 'user_created',
    probabilita: 'medium',
    scenario_text: scenarioData.text
  });
  
  return await scenario.save();
}
*/

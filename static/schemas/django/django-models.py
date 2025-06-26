# Stratoview Lombardia - Django Models Implementation
# Based on Taxonomy Store v1.0
# Compatible with Django 4.x+

import uuid
from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MinLengthValidator, MaxLengthValidator, RegexValidator,
    MinValueValidator, MaxValueValidator, FileExtensionValidator
)
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import json

# ================================
# CUSTOM VALIDATORS
# ================================

def validate_hex_color(value):
    """Validate hex color format #RRGGBB"""
    import re
    if not re.match(r'^#[0-9A-F]{6}$', value, re.IGNORECASE):
        raise ValidationError('Color must be in hex format #RRGGBB')

def validate_past_date(value):
    """Validate date is not in the future"""
    if value > date.today():
        raise ValidationError('Date cannot be in the future')

def validate_not_too_old(value):
    """Validate date is not older than 10 years"""
    ten_years_ago = date.today() - timedelta(days=365*10)
    if value < ten_years_ago:
        raise ValidationError('Date cannot be older than 10 years')

def validate_max_tags(value):
    """Validate maximum 5 tags"""
    if len(value) > 5:
        raise ValidationError('Maximum 5 tags allowed')

def validate_geographic_coverage(value):
    """Validate geographic coverage requirements"""
    if len(value) < 1:
        raise ValidationError('At least 1 geographic area required')
    if len(value) > 6:
        raise ValidationError('Maximum 6 geographic areas allowed')

def validate_file_size(value):
    """Validate file size is under 10MB"""
    limit = 10 * 1024 * 1024  # 10MB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 10 MB.')

# ================================
# TAXONOMY MODELS
# ================================

class IntelligenceArea(models.Model):
    """Intelligence Areas - Research domain classifications"""
    
    id = models.CharField(
        max_length=50, 
        primary_key=True,
        help_text="Semantic ID like 'tourism-resilience'"
    )
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1)]
    )
    description = models.TextField(
        max_length=500,
        help_text="Brief description of the intelligence area"
    )
    color_code = models.CharField(
        max_length=7,
        validators=[validate_hex_color],
        help_text="Hex color code for UI display"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Intelligence Area"
        verbose_name_plural = "Intelligence Areas"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class TopicArea(models.Model):
    """Topic Areas - Subject area classifications"""
    
    id = models.CharField(
        max_length=50,
        primary_key=True,
        help_text="Semantic ID like 'population-demographic'"
    )
    name = models.CharField(max_length=100)
    parent_themes = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        help_text="Related parent theme categories"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Topic Area"
        verbose_name_plural = "Topic Areas"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class GeographicArea(models.Model):
    """Geographic Areas - Lombardia region coverage"""
    
    AREA_TYPES = [
        ('province', 'Province'),
        ('region', 'Region'),
        ('municipality', 'Municipality'),
    ]
    
    id = models.CharField(
        max_length=50,
        primary_key=True,
        help_text="Semantic ID like 'milano' or 'all-lombardia'"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=AREA_TYPES)
    population = models.PositiveIntegerField(null=True, blank=True)
    area_km2 = models.FloatField(
        null=True, blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="Area (km²)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Geographic Area"
        verbose_name_plural = "Geographic Areas"
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

# ================================
# USER MANAGEMENT
# ================================

class User(AbstractUser):
    """Extended User model with Stratoview-specific fields"""
    
    USER_TYPES = [
        ('ADMIN', 'Administrator'),
        ('CUSTOMER', 'Customer'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

# ================================
# CONTENT MANAGEMENT
# ================================

class Content(models.Model):
    """Base Content model for all content types"""
    
    CONTENT_TYPES = [
        ('index', 'Index'),
        ('scenario', 'Scenario'),
        ('trend_radar', 'Trend Radar'),
        ('participatory_data', 'Participatory Data'),
    ]
    
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    
    SOURCE_CHOICES = [
        ('company', 'Company'),
        ('user_created', 'User Created'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_content')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    
    # Core Content Fields
    titolo = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1)],
        verbose_name="Title"
    )
    descrizione_breve = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1)],
        verbose_name="Brief Description"
    )
    descrizione_estesa = models.TextField(
        max_length=10000,
        blank=True,
        verbose_name="Extended Description"
    )
    
    # Metadata
    is_company_generated = models.BooleanField(default=False)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    content_source = models.CharField(max_length=15, choices=SOURCE_CHOICES)
    
    # Taxonomy Fields
    intelligence_area = models.ForeignKey(
        IntelligenceArea,
        on_delete=models.PROTECT,
        help_text="Required: Select one intelligence area"
    )
    topic_area = models.ForeignKey(
        TopicArea,
        on_delete=models.PROTECT,
        null=True, blank=True,
        help_text="Optional: Select one topic area"
    )
    themes = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        validators=[validate_max_tags],
        help_text="Maximum 5 tags allowed"
    )
    geographic_coverage = ArrayField(
        models.CharField(max_length=50),
        validators=[validate_geographic_coverage],
        help_text="Select 1-6 geographic areas"
    )
    
    # Timestamps
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"
        ordering = ['-ultima_modifica']
        indexes = [
            models.Index(fields=['content_type', 'visibility']),
            models.Index(fields=['intelligence_area', 'topic_area']),
            models.Index(fields=['creator', 'content_type']),
        ]
    
    def clean(self):
        """Business rule validation"""
        # Customer content must be private
        if self.content_source == 'user_created' and self.visibility == 'public':
            raise ValidationError('Customer content must be private')
        
        # Only admins can create Index content
        if self.content_type == 'index' and self.content_source == 'user_created':
            raise ValidationError('Only admins can create Index content')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.titolo} ({self.get_content_type_display()})"

# ================================
# CONTENT TYPE SPECIFIC MODELS
# ================================

class Index(models.Model):
    """Index Content - Analytics and predictive data with visualizations"""
    
    INDEX_TYPES = [
        ('analytical', 'Analytical'),
        ('predictive', 'Predictive'),
    ]
    
    DATA_LEVELS = [
        ('middleware', 'Middleware'),
        ('higher_level', 'Higher Level'),
    ]
    
    RESOLUTION_CHOICES = [
        ('province', 'Province'),
        ('5km', '5km Grid'),
        ('1km', '1km Grid'),
        ('municipality', 'Municipality'),
    ]
    
    VIEW_MODES = [
        ('mapview', 'Map View'),
        ('indexview', 'Index View'),
        ('datavizview', 'Data Visualization View'),
    ]
    
    content = models.OneToOneField(
        Content, 
        on_delete=models.CASCADE, 
        primary_key=True,
        limit_choices_to={'content_type': 'index'}
    )
    
    index_type = models.CharField(max_length=20, choices=INDEX_TYPES)
    data_level = models.CharField(max_length=20, choices=DATA_LEVELS)
    calculation_formula = models.TextField(
        max_length=2000,
        blank=True,
        help_text="Formula used for index calculation"
    )
    geographic_resolution = models.CharField(
        max_length=20,
        choices=RESOLUTION_CHOICES,
        help_text="Spatial granularity for data visualization"
    )
    
    # Visualization capabilities
    has_mapview = models.BooleanField(default=True)
    has_indexview = models.BooleanField(default=True)
    has_datavizview = models.BooleanField(default=True)
    default_view_mode = models.CharField(
        max_length=15,
        choices=VIEW_MODES,
        default='mapview'
    )
    
    class Meta:
        verbose_name = "Index Content"
        verbose_name_plural = "Index Contents"
    
    def __str__(self):
        return f"Index: {self.content.titolo}"

class Scenario(models.Model):
    """Scenario Content - Strategic scenarios with probability assessments"""
    
    PROBABILITY_CHOICES = [
        ('very-low', 'Very Low (0-20%)'),
        ('low', 'Low (20-40%)'),
        ('medium', 'Medium (40-60%)'),
        ('high', 'High (60-80%)'),
        ('very-high', 'Very High (80-100%)'),
    ]
    
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'content_type': 'scenario'}
    )
    
    probabilita = models.CharField(
        max_length=10,
        choices=PROBABILITY_CHOICES,
        verbose_name="Probability Assessment"
    )
    scenario_text = models.TextField(
        validators=[MinLengthValidator(50), MaxLengthValidator(10000)],
        help_text="Minimum 50 characters, maximum 10,000 characters"
    )
    scenario_format = models.CharField(max_length=20, default='html')
    
    class Meta:
        verbose_name = "Scenario Content"
        verbose_name_plural = "Scenario Contents"
    
    def __str__(self):
        return f"Scenario: {self.content.titolo}"

def scenario_image_upload_path(instance, filename):
    """Generate upload path for scenario images"""
    return f'scenarios/{instance.scenario.content.id}/images/{filename}'

class ScenarioImage(models.Model):
    """Images associated with Scenario content"""
    
    scenario = models.ForeignKey(
        Scenario,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        upload_to=scenario_image_upload_path,
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])
        ]
    )
    original_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Scenario Image"
        verbose_name_plural = "Scenario Images"

class TrendRadar(models.Model):
    """Trend Radar Content - Visual radar representations"""
    
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'content_type': 'trend_radar'}
    )
    
    # Time Reference
    time_month = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        help_text="Month (1-12)"
    )
    time_year = models.PositiveIntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(2030)],
        help_text="Year (2020-2030)"
    )
    
    # Radar Image
    radar_image = models.ImageField(
        upload_to='trend_radars/',
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])
        ],
        help_text="PNG, JPG, or SVG format, max 10MB"
    )
    original_filename = models.CharField(max_length=255)
    radar_format = models.CharField(max_length=20, default='image')
    radar_data = models.JSONField(
        default=dict,
        blank=True,
        help_text="Structured data representation of radar elements"
    )
    
    class Meta:
        verbose_name = "Trend Radar Content"
        verbose_name_plural = "Trend Radar Contents"
    
    def clean(self):
        """Validate time reference constraints"""
        from datetime import date
        current_year = date.today().year
        
        # Time reference validation
        if self.time_year > current_year + 2:
            raise ValidationError('Time reference cannot be more than 2 years in the future')
        
        if self.time_year < current_year - 5:
            raise ValidationError('Time reference cannot be more than 5 years in the past')
    
    def __str__(self):
        return f"Trend Radar: {self.content.titolo} ({self.time_month}/{self.time_year})"

class ParticipatoryData(models.Model):
    """Participatory Data Content - Survey and research visualizations"""
    
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={'content_type': 'participatory_data'}
    )
    
    collection_date = models.DateField(
        validators=[validate_past_date, validate_not_too_old],
        help_text="Date when the data was collected (max 10 years ago)"
    )
    data_format = models.CharField(max_length=50, default='visualization')
    
    # Data Visualization
    data_visualization = models.ImageField(
        upload_to='participatory_data/',
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])
        ],
        help_text="Data visualization image, max 10MB"
    )
    original_filename = models.CharField(max_length=255)
    
    methodology = models.TextField(
        max_length=2000,
        blank=True,
        help_text="Description of data collection methodology"
    )
    
    class Meta:
        verbose_name = "Participatory Data Content"
        verbose_name_plural = "Participatory Data Contents"
    
    def __str__(self):
        return f"Participatory Data: {self.content.titolo}"

# ================================
# PROJECT MANAGEMENT
# ================================

class Project(models.Model):
    """User Projects - Container for ContentBlocks"""
    
    LAYOUT_MODES = [
        ('grid', 'Grid View'),
        ('columns', 'Columns View'),
    ]
    
    PROJECT_STATES = [
        ('empty', 'Empty'),
        ('active', 'Active'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    nome = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1)],
        verbose_name="Project Name"
    )
    descrizione = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Description"
    )
    saved_layout_mode = models.CharField(
        max_length=10,
        choices=LAYOUT_MODES,
        default='grid'
    )
    project_state = models.CharField(
        max_length=10,
        choices=PROJECT_STATES,
        default='empty'
    )
    contentblock_count = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(4)]
    )
    
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-ultima_modifica']
        indexes = [
            models.Index(fields=['user', 'project_state']),
        ]
    
    def update_state(self):
        """Update project state based on ContentBlock count"""
        count = self.contentblocks.filter(is_active=True).count()
        self.contentblock_count = count
        self.project_state = 'active' if count > 0 else 'empty'
        self.save(update_fields=['contentblock_count', 'project_state', 'ultima_modifica'])
    
    def __str__(self):
        return f"{self.nome} ({self.user.username})"

class ContentBlock(models.Model):
    """ContentBlocks - Individual content containers within projects"""
    
    VIEW_MODES = [
        ('mapview', 'Map View'),
        ('indexview', 'Index View'),
        ('datavizview', 'Data Visualization View'),
        ('default', 'Default'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='contentblocks'
    )
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name='contentblocks'
    )
    position = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        help_text="Position within project (1-4)"
    )
    is_active = models.BooleanField(default=True)
    current_view_mode = models.CharField(
        max_length=15,
        choices=VIEW_MODES,
        default='default'
    )
    single_view_active = models.BooleanField(default=False)
    last_interaction = models.DateTimeField(auto_now=True)
    contentblock_state = models.JSONField(
        default=dict,
        blank=True,
        help_text="Flexible state storage for ContentBlock configuration"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "ContentBlock"
        verbose_name_plural = "ContentBlocks"
        unique_together = [('project', 'position')]
        ordering = ['position']
        indexes = [
            models.Index(fields=['project', 'is_active']),
        ]
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update project state after ContentBlock changes
        self.project.update_state()
    
    def delete(self, *args, **kwargs):
        project = self.project
        super().delete(*args, **kwargs)
        # Update project state after ContentBlock deletion
        project.update_state()
    
    def __str__(self):
        return f"Block {self.position}: {self.content.titolo} in {self.project.nome}"

# ================================
# DJANGO ADMIN CONFIGURATION
# ================================

from django.contrib import admin

@admin.register(IntelligenceArea)
class IntelligenceAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'description']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['titolo', 'content_type', 'creator', 'visibility', 'intelligence_area', 'ultima_modifica']
    list_filter = ['content_type', 'visibility', 'intelligence_area', 'content_source']
    search_fields = ['titolo', 'descrizione_breve']
    readonly_fields = ['data_creazione', 'ultima_modifica']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['nome', 'user', 'project_state', 'contentblock_count', 'ultima_modifica']
    list_filter = ['project_state', 'saved_layout_mode']
    search_fields = ['nome', 'user__username']
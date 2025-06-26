# Stratoview Content Editor - Validation Requirements

**DOCUMENT ID:** VR_001  
**VERSION:** 1.0  
**DATE:** June 19, 2025  
**SCOPE:** Form validation specifications for customer content creation

## Overview

This document defines the complete validation requirements for the Stratoview Content Editor, covering all form fields across the 3 customer content types: Scenario, Trend Radar, and Participatory Data.

## Universal Validation Rules

### **Required Fields (All Content Types)**
- **Title**: Mandatory, 1-100 characters
- **Brief Description**: Mandatory, 1-200 characters  
- **Intelligence Area**: Mandatory, single selection from dropdown
- **Geographic Coverage**: Mandatory, at least 1 area selected

### **Character Limits**
- **Title**: Max 100 characters with real-time counter
- **Brief Description**: Max 200 characters with real-time counter
- **Extended Description**: No limit (optional field)

### **Taxonomy Validation**
- **Intelligence Area**: Must select exactly 1 from predefined list
- **Topic Area**: Max 10 selections, autocomplete from predefined list
- **Tags**: Max 5 selections, autocomplete from predefined list
- **Geographic Coverage**: Min 1, max 6 (all Lombardia provinces + "All Lombardia")

## Content Type Specific Validation

### **Scenario Content**
```
Required Fields:
- Probability Assessment: Must select from 5-tier dropdown
- Scenario Content: Min 50 characters, rich text format

Field Specifications:
- Probability: [Very Low (0-20%), Low (20-40%), Medium (40-60%), High (60-80%), Very High (80-100%)]
- Scenario Body: Min 50 chars, max 10,000 chars
- Image Uploads: Optional, max 5 images, 10MB each, PNG/JPG only

Validation Logic:
- If probability "Very High" or "Very Low" → suggest review
- Scenario content must contain minimum 3 sentences
- Rich text formatting preserved on save
```

### **Trend Radar Content**
```
Required Fields:
- Time Reference: Month + Year both required
- Radar Image: Single image upload mandatory

Field Specifications:
- Month: Dropdown 1-12 (January-December)
- Year: Input field, range 2020-2030
- Image: Single file, max 10MB, PNG/JPG/SVG
- Image Resolution: Min 800x600px, recommended 1200x1200px

Validation Logic:
- Time reference cannot be more than 2 years in future
- Time reference cannot be more than 5 years in past
- Image aspect ratio should be square (warning, not error)
- File size validation with progress indicator
```

### **Participatory Data Content**
```
Required Fields:
- Data Collection Date: Past or present date only
- Data Visualization: Single image upload mandatory

Field Specifications:
- Collection Date: Date picker, max date = today
- Image: Single file, max 10MB, PNG/JPG/SVG
- Image Resolution: Min 800x600px, any aspect ratio

Validation Logic:
- Collection date cannot be in future
- Collection date cannot be older than 10 years
- Multiple chart images can be combined into single visualization
- File metadata preserved for audit trail
```

## File Upload Validation

### **Supported Formats**
- **Images**: PNG, JPG, JPEG, SVG
- **Maximum Size**: 10MB per file
- **Minimum Resolution**: 800x600 pixels
- **Recommended Resolution**: 1200x1200 (square) or 1200x800 (rectangular)

### **Upload Process Validation**
```
Pre-Upload Checks:
1. File format validation
2. File size validation  
3. Virus scanning (placeholder for production)
4. Resolution check with warnings

During Upload:
1. Progress indicator
2. Error handling for network issues
3. Cancellation capability
4. Multiple retry attempts

Post-Upload Validation:
1. Image integrity check
2. Metadata extraction
3. Thumbnail generation
4. Storage confirmation
```

## Form State Management

### **Save as Draft Requirements**
```
Minimum Fields for Draft:
- Title (min 1 character)
- Content Type selection

Optional Fields:
- All other fields can be empty
- Partial completion allowed
- Auto-save every 2 minutes
- Manual save confirmation message

Draft Limitations:
- Cannot be added to projects until validation complete
- Cannot be published until all required fields filled
- Draft retention: 30 days of inactivity
```

### **Save & Add to Project Requirements**
```
Full Validation Required:
- All required fields completed
- All format validations passed
- File uploads completed successfully
- Geographic coverage selected

Project Integration:
- Content immediately available in Content Browser
- Content automatically flagged as "Private"
- Creator attribution maintained
- Creation timestamp recorded
```

## Real-Time Validation Feedback

### **Character Counters**
- **Display**: "0/100" format with real-time updates
- **Color Coding**: 
  - Green: 0-80% of limit
  - Orange: 80-95% of limit  
  - Red: 95-100% of limit
- **Over Limit**: Red background, save disabled

### **Field Validation Indicators**
```
Valid Field:
- Green checkmark icon
- Normal border color
- No error message

Invalid Field:
- Red X icon  
- Red border color
- Error message below field
- Specific error description

Warning Field:
- Orange triangle icon
- Orange border color
- Warning message below field
- Save still allowed
```

### **Autocomplete Validation**
```
Topic Area & Tags:
- Prevent duplicate selections
- Max limit enforcement with user feedback
- Invalid entries automatically removed
- Suggestion dropdown with partial match
- Case-insensitive search

Chip Management:
- Visual feedback for selection
- Click to remove functionality
- Hover states for better UX
- Keyboard navigation support
```

## Error Handling

### **Validation Error Messages**
```
Title Errors:
- "Title is required"
- "Title must be between 1-100 characters"
- "Title contains invalid characters"

Description Errors:
- "Brief description is required"  
- "Brief description must be between 1-200 characters"
- "Description contains unsupported formatting"

Content Type Specific:
Scenario:
- "Probability assessment is required"
- "Scenario content must be at least 50 characters"
- "Rich text formatting error detected"

Trend Radar:
- "Time reference month is required"
- "Time reference year must be between 2020-2030"
- "Radar image is required"
- "Image resolution too low (min 800x600)"

Participatory Data:
- "Collection date is required"
- "Collection date cannot be in the future"
- "Data visualization image is required"
```

### **File Upload Error Messages**
```
Format Errors:
- "File format not supported. Please use PNG, JPG, or SVG"
- "File size exceeds 10MB limit"
- "Image resolution below minimum 800x600"

Upload Errors:
- "Upload failed. Please check your connection and try again"
- "Upload cancelled by user"
- "File corrupted during upload. Please try again"
- "Storage limit exceeded. Please contact support"
```

## Accessibility Requirements

### **Screen Reader Support**
- All form fields have proper labels
- Error messages associated with fields via aria-describedby
- Required fields marked with aria-required="true"
- Validation status communicated via aria-live regions

### **Keyboard Navigation**
- Tab order follows logical flow
- All interactive elements keyboard accessible
- Enter key submits forms appropriately
- Escape key cancels operations

### **Visual Accessibility**
- Color contrast minimum 4.5:1 for text
- Error states don't rely solely on color
- Focus indicators clearly visible
- Text size minimum 14px for form fields

## Performance Requirements

### **Form Response Times**
- Field validation: < 100ms
- Character counting: Real-time (< 50ms)
- Autocomplete suggestions: < 200ms
- Form submission: < 2 seconds
- File upload progress: Real-time updates

### **Browser Compatibility**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Security Considerations

### **Input Sanitization**
- XSS prevention for all text inputs
- SQL injection prevention (server-side)
- File upload virus scanning
- Content Security Policy enforcement

### **Data Privacy**
- No sensitive data in browser storage
- Encrypted transmission for all form data
- Audit trail for content modifications
- GDPR compliance for EU users

---

**Implementation Priority:**
1. Required field validation with clear error messages
2. Character counters with visual feedback  
3. File upload validation with progress indicators
4. Real-time autocomplete validation
5. Accessibility features
6. Advanced security measures

**Testing Requirements:**
- Unit tests for all validation rules
- Integration tests for form submission flows
- Cross-browser compatibility testing
- Accessibility compliance testing
- Performance testing under load
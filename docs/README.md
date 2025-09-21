# Price Assignment System Documentation

This directory contains the essential documentation for the ML Project Delivery assignment.

## Files Overview

### 1. ANNOTATION_INSTRUCTIONS_PRESENTATION.html
- **Purpose**: Interactive HTML presentation for annotation team
- **Content**: Comprehensive guidelines for drawing bounding boxes for tooth paste products
- **Key Topics**:
  - Product identification guidelines
  - Handling different orientations (angled, turned, occluded)
  - Single vs multi-pack handling
  - Image quality issues (blurry, dark, angled)
  - Non-tooth paste product handling
  - Bounding box drawing guidelines
  - Quality control checklist

### 2. MODEL_ANALYSIS_REPORT.md
- **Purpose**: Detailed analysis of model training and evaluation questions
- **Content**: Answers to specific ML questions including:
  - Annotation strategy for non-tooth paste products
  - Loss plot analysis and interpretation
  - Model selection justification
  - Adam optimizer beta parameters analysis
  - Dataset characteristics and implications

## Usage

### For Annotation Team
1. Open `ANNOTATION_INSTRUCTIONS_PRESENTATION.html` in a web browser
2. Review all slides for comprehensive understanding
3. Use as reference during annotation process
4. Follow quality control checklist before submitting

### For Model Analysis
1. Review `MODEL_ANALYSIS_REPORT.md` for detailed ML insights
2. Understand the reasoning behind annotation strategies
3. Learn about model selection criteria
4. Understand optimizer parameter implications

## Key Guidelines

### Annotation Strategy
- **Tag only tooth paste products** as "Tooth Paste Product"
- **Do NOT tag non-tooth paste products**
- **Focus on maximum recall** (finding all tooth paste products)
- **Include all variants, sizes, and brands**

### Model Training
- Use binary classification approach
- Focus on positive class identification
- Implement appropriate confidence thresholding
- Consider dataset characteristics in optimization

## Quality Standards

### Annotation Quality
- All visible tooth paste products must be tagged
- Bounding boxes should encompass full products
- Multi-packs treated as single units
- Include products with 50%+ visibility

### Model Quality
- Validation loss should be stable and decreasing
- Balance between performance and training time
- Consider dataset characteristics in parameter selection
- Implement robust optimization strategies

## Contact

For questions about annotation guidelines or model analysis, refer to the respective documentation files in this directory.

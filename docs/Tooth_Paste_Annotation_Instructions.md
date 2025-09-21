# Tooth Paste Annotation Instructions

## Overview
This document provides detailed instructions for annotating tooth paste products in retail images for the ML Project Delivery assignment.

## Objective
Report as many tooth paste products as possible, even if variant/size is not visible. Tag them as "Tooth Paste Product".

## Visual Examples

### Example 1: Standard Tooth Paste Products
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │    │
│  │         │  │ Health  │  │& Protect│  │Whitening│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │Toothbrush│  │Mouthwash│  │Dental   │  │  Other  │    │
│  │         │  │         │  │ Floss   │  │ Products │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✗ SKIP     ✗ SKIP       ✗ SKIP       ✗ SKIP        │
└─────────────────────────────────────────────────────────┘
```

### Example 2: Multi-Pack Handling
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐              │
│  │   Colgate 3-Pack│  │   Crest 2-Pack  │              │
│  │  ┌─┐ ┌─┐ ┌─┐   │  │   ┌─┐ ┌─┐      │              │
│  │  │1│ │2│ │3│   │  │   │1│ │2│      │              │
│  │  └─┘ └─┘ └─┘   │  │   └─┘ └─┘      │              │
│  └─────────────────┘  └─────────────────┘              │
│        ✓ TAG              ✓ TAG                        │
│    (One box for         (One box for                   │
│     entire pack)         entire pack)                  │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │ Single  │  │ Single  │  │ Single  │  │ Single  │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG         │
│  (Individual  (Individual  (Individual  (Individual    │
│   products)    products)    products)    products)     │
└─────────────────────────────────────────────────────────┘
```

### Example 3: Angled and Turned Products
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │    │
│  │         │  │ Health  │  │& Protect│  │Whitening│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │    │
│  │  (tilted)│  │ Health  │  │& Protect│  │Whitening│    │
│  │         │  │ (angled)│  │(turned) │  │         │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG         │
│  (Include in  (Include in  (Include in  (Include in    │
│   bounding    bounding    bounding    bounding         │
│   box)        box)        box)        box)             │
└─────────────────────────────────────────────────────────┘
```

### Example 4: Partially Occluded Products
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │    │
│  │         │  │ Health  │  │& Protect│  │Whitening│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│    │
│  │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │    │
│  │(50% vis)│  │ Health  │  │& Protect│  │Whitening│    │
│  │         │  │(75% vis)│  │(90% vis)│  │(25% vis)│    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✓ TAG      ✓ TAG        ✓ TAG        ✗ SKIP        │
│  (Include -   (Include -   (Include -   (Too little    │
│   50%+ vis)    50%+ vis)    50%+ vis)    visible)      │
└─────────────────────────────────────────────────────────┘
```

### Example 5: Bounding Box Examples
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ ││
│  │ │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│ ││
│  │ │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │ ││
│  │ │         │  │ Health  │  │& Protect│  │Whitening│ ││
│  │ └─────────┘  └─────────┘  └─────────┘  └─────────┘ ││
│  │    ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG      ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ ││
│  │ │ Colgate │  │  Crest  │  │Sensodyne│  │Aquafresh│ ││
│  │ │  Total  │  │ Pro-    │  │ Repair  │  │Advanced │ ││
│  │ │         │  │ Health  │  │& Protect│  │Whitening│ ││
│  │ └─────────┘  └─────────┘  └─────────┘  └─────────┘ ││
│  │    ✓ TAG      ✓ TAG        ✓ TAG        ✓ TAG      ││
│  └─────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘

Legend:
┌─────────┐ = Bounding box around individual product
└─────────┘ = Complete product included in box
✓ TAG = Tag as "Tooth Paste Product"
✗ SKIP = Do not tag
```

### Example 6: What NOT to Tag
```
┌─────────────────────────────────────────────────────────┐
│                    RETAIL SHELF                         │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │Toothbrush│  │Mouthwash│  │Dental   │  │Tooth    │    │
│  │         │  │         │  │ Floss   │  │Whitening│    │
│  │         │  │         │  │         │  │ Strips  │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✗ SKIP     ✗ SKIP       ✗ SKIP       ✗ SKIP        │
│                                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │
│  │  Other  │  │  Other  │  │  Other  │  │  Other  │    │
│  │ Dental  │  │ Dental  │  │ Dental  │  │ Dental  │    │
│  │Products │  │Products │  │Products │  │Products │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘    │
│     ✗ SKIP     ✗ SKIP       ✗ SKIP       ✗ SKIP        │
└─────────────────────────────────────────────────────────┘
```

## Product Identification

### What to Tag as "Tooth Paste Product":
- All tooth paste brands (Colgate, Crest, Sensodyne, Aquafresh, etc.)
- All variants (Whitening, Sensitive, Fresh Mint, etc.)
- All sizes (Travel size, regular, family size)
- All packaging (Tubes, pumps, dispensers)
- Multi-packs (2-pack, 3-pack, value packs)

### What NOT to Tag:
- Tooth brushes
- Mouthwash
- Dental floss
- Tooth whitening strips
- Any other dental products

## Handling Different Orientations

### Angled Products
- Draw bounding box around the entire visible product
- Don't worry about perfect rectangular alignment
- Focus on capturing the complete product

### Turned Products
- If you can identify it as tooth paste, tag it
- Use context clues (shelf placement, nearby products)
- When in doubt, include it

### Occluded Products
- Only tag if at least 50% of the product is visible
- If partially hidden by other products, still tag if recognizable
- If mostly hidden, skip it

## Single vs Multi-Pack Handling

### Single Products
- Draw one bounding box per individual product
- Each tube/pump gets its own annotation
- Tag as "Tooth Paste Product"

### Multi-Packs
- Draw bounding box around the entire multi-pack
- Tag as "Tooth Paste Product"
- Don't annotate individual items within the pack

## Image Quality Issues

### Blurry Images
- If you can identify it as tooth paste, tag it
- Use shape, size, and context clues
- When in doubt, include it

### Dark Images
- Adjust your screen brightness if needed
- Look for recognizable shapes and sizes
- Use context from surrounding products

### Angled Images
- Draw bounding boxes that capture the full product
- Don't worry about perfect alignment
- Focus on completeness over precision

## Bounding Box Guidelines

### Drawing Bounding Boxes:
1. Click and drag to create rectangle around product
2. Include the entire product within the box
3. Don't worry about perfect alignment
4. Ensure no part of the product is cut off

### Quality Standards:
- Box should encompass the full product
- Minimal background included
- Consistent approach across all images
- When in doubt, make the box slightly larger

## Quality Control Checklist

Before submitting each image:
- ✓ All visible tooth paste products are tagged
- ✓ No non-tooth paste products are tagged
- ✓ Bounding boxes encompass full products
- ✓ Multi-packs are treated as single units
- ✓ Partially visible products (50%+) are included
- ✓ All variants and sizes are captured

## Key Principles

1. **Maximum Recall**: It's better to include a questionable product than to miss a clear tooth paste item
2. **Consistency**: Use the same approach across all images
3. **Completeness**: Include all visible tooth paste products
4. **Quality**: Focus on capturing the full product in bounding boxes

## Success Metric

High recall (finding all tooth paste products) is more important than perfect precision. The goal is to identify as many tooth paste products as possible while maintaining reasonable accuracy.

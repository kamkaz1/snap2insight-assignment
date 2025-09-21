# Price Assignment System

A simple system for matching products with their corresponding prices based on spatial proximity and basic overlap analysis.

## Features

- **Simple Matching**: Basic overlap and distance-based matching
- **JSON Export**: Export results in JSON format
- **Visualization**: Basic visual output with bounding boxes
- **Easy to Use**: Simple command line interface
- **Beginner Friendly**: Clean, straightforward code structure

## Quick Start

### Simple Mode (Default)
```bash
# Process all images
python main.py --mode simple

# Process single image
python main.py --mode simple --single_image image_name

# Custom distance threshold
python main.py --mode simple --max_distance 300
```

### Advanced Mode
```bash
# Process with advanced features
python main.py --mode advanced --single_image image_name --export_json --export_csv --export_report
```

## Input Format

The system expects three files for each image:
- `image_name.txt` - Product data (x, y, width, height, upc)
- `image_name_price.txt` - Price data (x, y, width, height, price)
- `image_name.jpg` - Original image for visualization

## Output

- **JSON Export**: `image_name_export.json` - Results in JSON format
- **Visualization**: `image_name_visualization.jpg` - Image with bounding boxes and connections

## Requirements

- Python 3.6+
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the system: `python main.py --mode simple`

## How It Works

1. **Load Data**: Reads product and price data from text files
2. **Match Prices**: Uses overlap and distance to match products with prices
3. **Export Results**: Saves results in JSON format
4. **Create Visualization**: Generates image with bounding boxes and connections

## Simple Algorithm

The system uses a straightforward approach:
1. First, try to match products with prices based on bounding box overlap
2. If no overlap, use distance between centers
3. Assign the best match and mark the price as used
4. Continue until all products are processed

This is a beginner-friendly implementation that focuses on simplicity and clarity.

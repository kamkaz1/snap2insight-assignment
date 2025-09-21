#!/usr/bin/env python3

"""
Simple example showing how to use the price assignment system.
This is a beginner-friendly example that demonstrates basic usage.
"""

import os
import sys

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(__file__))

from scripts.price_assignment import load_products, load_prices, assign_prices, save_results, create_visualization

def main():
    print("Simple Price Assignment Example")
    print("=" * 40)
    
    # Set up file paths
    input_dir = "data/input"
    output_dir = "data/output"
    image_name = "18cfbcc2-8b71-4c19-b6cb-6ded35aafb9c"
    
    product_file = os.path.join(input_dir, f"{image_name}.txt")
    price_file = os.path.join(input_dir, f"{image_name}_price.txt")
    image_file = os.path.join(input_dir, f"{image_name}.jpg")
    
    print(f"Loading data for {image_name}...")
    
    # Load the data
    products = load_products(product_file)
    prices = load_prices(price_file)
    
    print(f"Found {len(products)} products")
    print(f"Found {len(prices)} prices")
    
    # Assign prices
    print("Assigning prices...")
    assigned_count = assign_prices(products, prices, max_distance=200)
    
    print(f"Assigned prices to {assigned_count} products")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save results
    output_file = os.path.join(output_dir, f"{image_name}_export.json")
    save_results(products, output_file)
    print(f"Results saved to {output_file}")
    
    # Create visualization
    if os.path.exists(image_file):
        viz_file = os.path.join(output_dir, f"{image_name}_visualization.jpg")
        if create_visualization(image_file, products, prices, viz_file):
            print(f"Visualization saved to {viz_file}")
    
    print("\nExample completed successfully!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import json
import math
import argparse
import cv2
import numpy as np

class Product:
    def __init__(self, x, y, width, height, upc):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.upc = upc
        self.center_x = x + width // 2
        self.center_y = y + height // 2
        self.price = None

class Price:
    def __init__(self, x, y, width, height, price_str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.price_str = price_str
        self.center_x = x + width // 2
        self.center_y = y + height // 2
        self.used = False

def load_products(filename):
    products = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 5:
                    x = int(parts[0])
                    y = int(parts[1])
                    width = int(parts[2])
                    height = int(parts[3])
                    upc = parts[4]
                    products.append(Product(x, y, width, height, upc))
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
    return products

def load_prices(filename):
    prices = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 5:
                    x = int(parts[0])
                    y = int(parts[1])
                    width = int(parts[2])
                    height = int(parts[3])
                    price_str = parts[4]
                    prices.append(Price(x, y, width, height, price_str))
    except FileNotFoundError:
        print(f"Error: Could not find file {filename}")
    return prices

def calculate_distance(product, price):
    dx = product.center_x - price.center_x
    dy = product.center_y - price.center_y
    return math.sqrt(dx * dx + dy * dy)

def calculate_overlap(product, price):
    # Simple overlap calculation
    left = max(product.x, price.x)
    top = max(product.y, price.y)
    right = min(product.x + product.width, price.x + price.width)
    bottom = min(product.y + product.height, price.y + price.height)
    
    if left < right and top < bottom:
        overlap_area = (right - left) * (bottom - top)
        product_area = product.width * product.height
        price_area = price.width * price.height
        smaller_area = min(product_area, price_area)
        return overlap_area / smaller_area if smaller_area > 0 else 0
    return 0

def assign_prices(products, prices, max_distance=200):
    assigned_count = 0
    
    for product in products:
        best_price = None
        best_score = 0
        
        for price in prices:
            if price.used:
                continue
                
            # Try overlap first
            overlap = calculate_overlap(product, price)
            if overlap > 0.1:  # 10% overlap threshold
                if overlap > best_score:
                    best_score = overlap
                    best_price = price
            
            # If no overlap, try distance
            elif best_price is None:
                distance = calculate_distance(product, price)
                if distance <= max_distance:
                    score = 1.0 - (distance / max_distance)
                    if score > best_score:
                        best_score = score
                        best_price = price
        
        if best_price:
            product.price = best_price.price_str
            best_price.used = True
            assigned_count += 1
    
    return assigned_count

def save_results(products, output_file):
    results = {"products": []}
    
    for product in products:
        product_data = {
            "left_top_x": product.x,
            "left_top_y": product.y,
            "width": product.width,
            "height": product.height,
            "upc": product.upc,
            "price": product.price if product.price else None
        }
        results["products"].append(product_data)
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

def create_visualization(image_file, products, prices, output_file):
    try:
        image = cv2.imread(image_file)
        if image is None:
            print(f"Could not load image: {image_file}")
            return False
        
        # Draw products in blue
        for product in products:
            cv2.rectangle(image, (product.x, product.y), 
                         (product.x + product.width, product.y + product.height), 
                         (255, 0, 0), 2)
            cv2.putText(image, product.upc, (product.x, product.y - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        
        # Draw prices in green
        for price in prices:
            cv2.rectangle(image, (price.x, price.y), 
                         (price.x + price.width, price.y + price.height), 
                         (0, 255, 0), 2)
            cv2.putText(image, price.price_str, (price.x, price.y - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        # Draw connections for assigned prices
        for product in products:
            if product.price:
                for price in prices:
                    if price.price_str == product.price and price.used:
                        cv2.line(image, (product.center_x, product.center_y), 
                                (price.center_x, price.center_y), (0, 0, 255), 2)
                        break
        
        cv2.imwrite(output_file, image)
        return True
    except Exception as e:
        print(f"Error creating visualization: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Simple Price Assignment Tool')
    parser.add_argument('--input_dir', default='data/input', help='Input directory')
    parser.add_argument('--output_dir', default='data/output', help='Output directory')
    parser.add_argument('--single_image', help='Process single image (base name)')
    parser.add_argument('--max_distance', type=float, default=200, help='Max distance for matching')
    parser.add_argument('--no_visualization', action='store_true', help='Skip visualization')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_dir):
        print(f"Error: Input directory {args.input_dir} does not exist")
        return
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    if args.single_image:
        # Process single image
        base_name = args.single_image
        product_file = os.path.join(args.input_dir, f"{base_name}.txt")
        price_file = os.path.join(args.input_dir, f"{base_name}_price.txt")
        image_file = os.path.join(args.input_dir, f"{base_name}.jpg")
        
        print(f"Processing {base_name}...")
        
        products = load_products(product_file)
        prices = load_prices(price_file)
        
        print(f"Found {len(products)} products and {len(prices)} prices")
        
        assigned = assign_prices(products, prices, args.max_distance)
        
        print(f"Assigned prices to {assigned} products")
        
        # Save results
        output_file = os.path.join(args.output_dir, f"{base_name}_export.json")
        save_results(products, output_file)
        print(f"Results saved to {output_file}")
        
        # Create visualization
        if not args.no_visualization and os.path.exists(image_file):
            viz_file = os.path.join(args.output_dir, f"{base_name}_visualization.jpg")
            if create_visualization(image_file, products, prices, viz_file):
                print(f"Visualization saved to {viz_file}")
    
    else:
        # Process all images
        print("Processing all images...")
        total_products = 0
        total_prices = 0
        total_assigned = 0
        
        for filename in os.listdir(args.input_dir):
            if filename.endswith('.txt') and not filename.endswith('_price.txt'):
                base_name = filename[:-4]  # Remove .txt extension
                
                product_file = os.path.join(args.input_dir, f"{base_name}.txt")
                price_file = os.path.join(args.input_dir, f"{base_name}_price.txt")
                image_file = os.path.join(args.input_dir, f"{base_name}.jpg")
                
                if os.path.exists(price_file):
                    print(f"Processing {base_name}...")
                    
                    products = load_products(product_file)
                    prices = load_prices(price_file)
                    
                    total_products += len(products)
                    total_prices += len(prices)
                    
                    assigned = assign_prices(products, prices, args.max_distance)
                    total_assigned += assigned
                    
                    # Save results
                    output_file = os.path.join(args.output_dir, f"{base_name}_export.json")
                    save_results(products, output_file)
                    
                    # Create visualization
                    if not args.no_visualization and os.path.exists(image_file):
                        viz_file = os.path.join(args.output_dir, f"{base_name}_visualization.jpg")
                        create_visualization(image_file, products, prices, viz_file)
        
        print(f"\nSummary:")
        print(f"Total products: {total_products}")
        print(f"Total prices: {total_prices}")
        print(f"Assigned: {total_assigned}")
        if total_products > 0:
            print(f"Assignment rate: {(total_assigned/total_products)*100:.1f}%")

if __name__ == "__main__":
    main()

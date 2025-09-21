#!/usr/bin/env python3
"""
Main entry point for the Price Assignment System.

This script provides a unified interface to the price assignment system
with both simple and advanced modes.

Usage:
    python main.py --help
    python main.py --mode simple
    python main.py --mode advanced --max_distance 300
"""

import argparse
import sys
import os


def run_simple_mode(args):
    """Run the simple price assignment mode."""
    print("=" * 60)
    print("Price Assignment System - Simple Mode")
    print("=" * 60)
    
    # Import and run the simple script
    from scripts.price_assignment import main as script_main
    
    # Set up arguments for simple script
    sys.argv = ['price_assignment.py']
    if args.input_dir:
        sys.argv.extend(['--input_dir', args.input_dir])
    if args.output_dir:
        sys.argv.extend(['--output_dir', args.output_dir])
    if args.max_distance:
        sys.argv.extend(['--max_distance', str(args.max_distance)])
    if args.single_image:
        sys.argv.extend(['--single_image', args.single_image])
    if args.no_visualization:
        sys.argv.append('--no_visualization')
    
    script_main()

def run_advanced_mode(args):
    """Run the advanced price assignment mode."""
    print("=" * 60)
    print("Price Assignment System - Advanced Mode")
    print("=" * 60)
    print("Advanced mode is not available in this simplified version.")
    print("Please use simple mode instead.")
    print("=" * 60)

def main():
    """Main entry point with mode selection."""
    parser = argparse.ArgumentParser(
        description='Price Assignment System - Unified Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all images
  python main.py --mode simple
  
  # Process single image
  python main.py --mode simple --single_image image_name
  
  # Custom distance threshold
  python main.py --mode simple --max_distance 300
        """
    )
    
    # Mode selection
    parser.add_argument('--mode', choices=['simple', 'advanced'], default='simple',
                       help='Choose between simple or advanced mode (default: simple)')
    
    # Common options
    parser.add_argument('--input_dir', '-i', 
                       help='Input directory containing data files')
    parser.add_argument('--output_dir', '-o',
                       help='Output directory for results')
    parser.add_argument('--single_image', '-s', type=str,
                       help='Process only a single image (provide base name without extension)')
    parser.add_argument('--max_distance', '-d', type=float,
                       help='Maximum distance for price-product matching')
    parser.add_argument('--no_visualization', action='store_true',
                       help='Skip creating visualization images')
    
    
    args = parser.parse_args()
    
    # Ensure data directories exist
    if not args.input_dir:
        args.input_dir = 'data/input'
    if not args.output_dir:
        args.output_dir = 'data/output'
    
    os.makedirs(args.input_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Run the selected mode
    if args.mode == 'simple':
        run_simple_mode(args)
    else:
        run_advanced_mode(args)

if __name__ == "__main__":
    main()

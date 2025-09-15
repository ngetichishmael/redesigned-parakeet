import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import random
import math
from typing import List, Tuple, Optional, Dict
import argparse

class EnhancedOrganicFractal:
    """
    Enhanced organic fractal generator with extensive customization options.
    Creates complex fractal patterns with white circles and dark grey spiky elements.
    """
    
    def __init__(self, width=1200, height=1200, dpi=300, **kwargs):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.center_x = width / 2
        self.center_y = height / 2
        
        # Fractal parameters with defaults
        self.max_depth = kwargs.get('max_depth', 8)
        self.branch_angle_variance = kwargs.get('branch_angle_variance', 0.3)
        self.branch_length_decay = kwargs.get('branch_length_decay', 0.7)
        self.circle_size_decay = kwargs.get('circle_size_decay', 0.8)
        self.central_void_radius = kwargs.get('central_void_radius', 80)
        self.num_main_branches = kwargs.get('num_main_branches', 8)
        self.circle_density = kwargs.get('circle_density', 0.7)
        self.spike_density = kwargs.get('spike_density', 0.3)
        self.spike_min_depth = kwargs.get('spike_min_depth', 2)
        self.max_sub_branches = kwargs.get('max_sub_branches', 3)
        self.sub_branch_probability = kwargs.get('sub_branch_probability', 0.8)
        
        # Color customization
        self.background_color = kwargs.get('background_color', 'black')
        self.circle_color = kwargs.get('circle_color', 'white')
        self.spike_color = kwargs.get('spike_color', '#404040')
        self.void_color = kwargs.get('void_color', 'black')
        
        # Storage for fractal elements
        self.circles = []
        self.spikes = []
        
    def generate_fractal(self, seed: Optional[int] = None):
        """Generate the complete fractal pattern"""
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
            
        print("Generating enhanced organic fractal...")
        print(f"Parameters: depth={self.max_depth}, branches={self.num_main_branches}, "
              f"void_radius={self.central_void_radius}")
        
        # Clear previous elements
        self.circles = []
        self.spikes = []
        
        # Generate main branches from center
        for i in range(self.num_main_branches):
            angle = (2 * math.pi * i / self.num_main_branches) + random.uniform(-0.2, 0.2)
            start_radius = self.central_void_radius + random.uniform(20, 40)
            start_x = self.center_x + start_radius * math.cos(angle)
            start_y = self.center_y + start_radius * math.sin(angle)
            
            self._generate_branch(
                start_x, start_y, angle, 
                initial_length=random.uniform(150, 250),
                initial_circle_size=random.uniform(8, 15),
                depth=0
            )
        
        print(f"Generated {len(self.circles)} circles and {len(self.spikes)} spikes")
        
    def _generate_branch(self, x: float, y: float, angle: float, 
                        initial_length: float, initial_circle_size: float, depth: int):
        """Recursively generate a branch with circles and sub-branches"""
        
        if depth >= self.max_depth:
            return
            
        # Calculate branch length and circle size for this depth
        length = initial_length * (self.branch_length_decay ** depth)
        circle_size = initial_circle_size * (self.circle_size_decay ** depth)
        
        # Don't create branches that are too small
        if length < 5 or circle_size < 0.5:
            return
            
        # Generate points along this branch
        num_points = max(3, int(length / 15))
        for i in range(num_points):
            progress = i / (num_points - 1) if num_points > 1 else 0
            
            # Add some randomness to the path
            current_angle = angle + random.uniform(-self.branch_angle_variance, self.branch_angle_variance)
            current_length = length * progress
            
            point_x = x + current_length * math.cos(current_angle)
            point_y = y + current_length * math.sin(current_angle)
            
            # Add circles along the branch
            if random.random() < self.circle_density:
                size_variation = random.uniform(0.5, 1.5)
                current_circle_size = circle_size * size_variation
                
                self.circles.append({
                    'x': point_x,
                    'y': point_y,
                    'radius': current_circle_size,
                    'depth': depth
                })
            
            # Add spikes at certain points
            if (random.random() < self.spike_density and 
                depth >= self.spike_min_depth):
                self._add_spikes_around_point(point_x, point_y, circle_size, current_angle)
        
        # Create sub-branches
        if depth < self.max_depth - 1 and random.random() < self.sub_branch_probability:
            num_sub_branches = random.randint(1, self.max_sub_branches) if depth < 3 else random.randint(0, 2)
            
            for _ in range(num_sub_branches):
                # Choose a point along the branch for sub-branch origin
                sub_progress = random.uniform(0.3, 0.8)
                sub_x = x + length * sub_progress * math.cos(angle)
                sub_y = y + length * sub_progress * math.sin(angle)
                
                # Calculate sub-branch angle
                sub_angle = angle + random.uniform(-math.pi/3, math.pi/3)
                
                # Recursively generate sub-branch
                self._generate_branch(
                    sub_x, sub_y, sub_angle,
                    length * 0.6, circle_size * 0.7, depth + 1
                )
    
    def _add_spikes_around_point(self, x: float, y: float, base_size: float, angle: float):
        """Add spiky elements around a point"""
        num_spikes = random.randint(3, 8)
        spike_length = base_size * random.uniform(0.3, 0.8)
        
        for i in range(num_spikes):
            spike_angle = angle + random.uniform(-math.pi/2, math.pi/2)
            spike_x = x + spike_length * math.cos(spike_angle)
            spike_y = y + spike_length * math.sin(spike_angle)
            
            self.spikes.append({
                'x1': x,
                'y1': y,
                'x2': spike_x,
                'y2': spike_y,
                'thickness': random.uniform(0.5, 2.0)
            })
    
    def create_visualization(self, save_path: str = 'enhanced_fractal.png', show_plot: bool = True):
        """Create and save the fractal visualization"""
        print("Creating visualization...")
        
        # Create figure with customizable background
        fig, ax = plt.subplots(figsize=(self.width/self.dpi, self.height/self.dpi), dpi=self.dpi)
        ax.set_facecolor(self.background_color)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Create central void
        void = patches.Circle((self.center_x, self.center_y), self.central_void_radius, 
                            facecolor=self.void_color, edgecolor='none')
        ax.add_patch(void)
        
        # Draw circles
        circle_patches = []
        for circle in self.circles:
            # Skip circles that are too close to center (inside void)
            distance_from_center = math.sqrt(
                (circle['x'] - self.center_x)**2 + (circle['y'] - self.center_y)**2
            )
            if distance_from_center < self.central_void_radius + 10:
                continue
                
            circle_patch = patches.Circle(
                (circle['x'], circle['y']), 
                circle['radius'], 
                facecolor=self.circle_color, 
                edgecolor='none'
            )
            circle_patches.append(circle_patch)
        
        if circle_patches:
            circle_collection = PatchCollection(circle_patches, match_original=True)
            ax.add_collection(circle_collection)
        
        # Draw spikes
        for spike in self.spikes:
            ax.plot([spike['x1'], spike['x2']], [spike['y1'], spike['y2']], 
                   color=self.spike_color, linewidth=spike['thickness'], alpha=0.8)
        
        # Save the image
        plt.tight_layout()
        plt.savefig(save_path, dpi=self.dpi, bbox_inches='tight', 
                   facecolor=self.background_color, edgecolor='none')
        
        if show_plot:
            plt.show()
        else:
            plt.close()
        
        print(f"Fractal saved to {save_path}")
        return fig, ax

def create_preset_fractals():
    """Create several preset fractal configurations"""
    presets = {
        'delicate': {
            'max_depth': 6,
            'num_main_branches': 6,
            'circle_density': 0.5,
            'spike_density': 0.2,
            'central_void_radius': 60,
            'branch_length_decay': 0.8
        },
        'dense': {
            'max_depth': 10,
            'num_main_branches': 12,
            'circle_density': 0.9,
            'spike_density': 0.5,
            'central_void_radius': 100,
            'branch_length_decay': 0.6
        },
        'sparse': {
            'max_depth': 5,
            'num_main_branches': 4,
            'circle_density': 0.3,
            'spike_density': 0.1,
            'central_void_radius': 50,
            'branch_length_decay': 0.9
        },
        'spiky': {
            'max_depth': 8,
            'num_main_branches': 8,
            'circle_density': 0.6,
            'spike_density': 0.7,
            'spike_min_depth': 1,
            'central_void_radius': 80
        }
    }
    return presets

def main():
    """Main function with command line interface"""
    parser = argparse.ArgumentParser(description='Generate organic fractal patterns')
    parser.add_argument('--preset', choices=['delicate', 'dense', 'sparse', 'spiky'], 
                       help='Use a preset configuration')
    parser.add_argument('--seed', type=int, help='Random seed for reproducibility')
    parser.add_argument('--output', default='enhanced_fractal.png', help='Output filename')
    parser.add_argument('--width', type=int, default=1200, help='Image width')
    parser.add_argument('--height', type=int, default=1200, help='Image height')
    parser.add_argument('--dpi', type=int, default=300, help='Image DPI')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display the plot')
    
    args = parser.parse_args()
    
    print("Enhanced Organic Fractal Generator")
    print("=" * 40)
    
    # Get preset configuration if specified
    config = {}
    if args.preset:
        presets = create_preset_fractals()
        config = presets[args.preset]
        print(f"Using preset: {args.preset}")
    
    # Create fractal generator
    fractal = EnhancedOrganicFractal(
        width=args.width, 
        height=args.height, 
        dpi=args.dpi,
        **config
    )
    
    # Generate the fractal
    fractal.generate_fractal(seed=args.seed)
    
    # Create visualization
    fractal.create_visualization(args.output, show_plot=not args.no_show)
    
    print("Fractal generation complete!")

if __name__ == "__main__":
    main()

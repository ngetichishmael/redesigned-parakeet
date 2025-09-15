import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import random
import math
from typing import List, Tuple, Optional

class OrganicFractal:
    """
    Generate an organic fractal pattern with white circles and dark grey spiky elements
    against a black background, featuring a central void and radial branching structure.
    """
    
    def __init__(self, width=1200, height=1200, dpi=300):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.center_x = width / 2
        self.center_y = height / 2
        
        # Fractal parameters
        self.max_depth = 8
        self.branch_angle_variance = 0.3
        self.branch_length_decay = 0.7
        self.circle_size_decay = 0.8
        self.central_void_radius = 80
        
        # Storage for fractal elements
        self.circles = []
        self.spikes = []
        
    def generate_fractal(self):
        """Generate the complete fractal pattern"""
        print("Generating organic fractal...")
        
        # Clear previous elements
        self.circles = []
        self.spikes = []
        
        # Generate main branches from center
        num_main_branches = random.randint(6, 10)
        for i in range(num_main_branches):
            angle = (2 * math.pi * i / num_main_branches) + random.uniform(-0.2, 0.2)
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
            if random.random() < 0.7:  # 70% chance to place a circle
                size_variation = random.uniform(0.5, 1.5)
                current_circle_size = circle_size * size_variation
                
                self.circles.append({
                    'x': point_x,
                    'y': point_y,
                    'radius': current_circle_size,
                    'depth': depth
                })
            
            # Add spikes at certain points
            if random.random() < 0.3 and depth > 2:  # 30% chance for spikes, not on main branches
                self._add_spikes_around_point(point_x, point_y, circle_size, current_angle)
        
        # Create sub-branches
        if depth < self.max_depth - 1:
            num_sub_branches = random.randint(1, 3) if depth < 3 else random.randint(0, 2)
            
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
    
    def create_visualization(self, save_path: str = 'organic_fractal.png'):
        """Create and save the fractal visualization"""
        print("Creating visualization...")
        
        # Create figure with black background
        fig, ax = plt.subplots(figsize=(self.width/self.dpi, self.height/self.dpi), dpi=self.dpi)
        ax.set_facecolor('black')
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Create central void
        void = patches.Circle((self.center_x, self.center_y), self.central_void_radius, 
                            facecolor='black', edgecolor='none')
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
                facecolor='white', 
                edgecolor='none'
            )
            circle_patches.append(circle_patch)
        
        if circle_patches:
            circle_collection = PatchCollection(circle_patches, match_original=True)
            ax.add_collection(circle_collection)
        
        # Draw spikes
        for spike in self.spikes:
            ax.plot([spike['x1'], spike['x2']], [spike['y1'], spike['y2']], 
                   color='#404040', linewidth=spike['thickness'], alpha=0.8)
        
        # Save the image
        plt.tight_layout()
        plt.savefig(save_path, dpi=self.dpi, bbox_inches='tight', 
                   facecolor='black', edgecolor='none')
        plt.show()
        
        print(f"Fractal saved to {save_path}")
        return fig, ax

def main():
    """Main function to generate and display the organic fractal"""
    print("Organic Fractal Generator")
    print("=" * 40)
    
    # Set random seed for reproducibility (optional)
    random.seed(42)
    np.random.seed(42)
    
    # Create fractal generator
    fractal = OrganicFractal(width=1200, height=1200, dpi=300)
    
    # Generate the fractal
    fractal.generate_fractal()
    
    # Create visualization
    fractal.create_visualization('organic_fractal.png')
    
    print("Fractal generation complete!")

if __name__ == "__main__":
    main()

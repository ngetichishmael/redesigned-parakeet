import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Slider, Button
import random
import math
from typing import List, Tuple, Optional, Dict
from enhanced_fractal import EnhancedOrganicFractal

class InteractiveFractal:
    """
    Interactive fractal generator with real-time parameter adjustment
    """
    
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 10))
        plt.subplots_adjust(bottom=0.25, left=0.1, right=0.95)
        
        # Initialize fractal with default parameters
        self.fractal = EnhancedOrganicFractal(width=800, height=800, dpi=100)
        self.fractal.generate_fractal(seed=42)
        
        # Create initial plot
        self.setup_plot()
        self.setup_sliders()
        self.setup_buttons()
        
        # Draw initial fractal
        self.update_fractal()
        
    def setup_plot(self):
        """Setup the main plot area"""
        self.ax.set_facecolor('black')
        self.ax.set_xlim(0, 800)
        self.ax.set_ylim(0, 800)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.ax.set_title('Interactive Organic Fractal Generator', 
                         color='white', fontsize=16, fontweight='bold')
        
    def setup_sliders(self):
        """Setup parameter sliders"""
        # Define slider positions and parameters
        slider_params = [
            ('max_depth', 1, 12, 8, 'Max Depth'),
            ('num_main_branches', 3, 15, 8, 'Main Branches'),
            ('central_void_radius', 20, 150, 80, 'Void Radius'),
            ('circle_density', 0.1, 1.0, 0.7, 'Circle Density'),
            ('spike_density', 0.0, 1.0, 0.3, 'Spike Density'),
            ('branch_length_decay', 0.3, 0.9, 0.7, 'Length Decay'),
            ('circle_size_decay', 0.3, 0.9, 0.8, 'Size Decay'),
            ('branch_angle_variance', 0.1, 0.8, 0.3, 'Angle Variance')
        ]
        
        self.sliders = {}
        slider_height = 0.02
        slider_spacing = 0.025
        
        for i, (param, min_val, max_val, init_val, label) in enumerate(slider_params):
            # Create slider
            ax_slider = plt.axes([0.1, 0.05 + i * slider_spacing, 0.3, slider_height])
            slider = Slider(ax_slider, label, min_val, max_val, valinit=init_val, 
                          valfmt='%.2f', facecolor='#404040', edgecolor='white')
            
            # Style the slider
            slider.label.set_color('white')
            slider.valtext.set_color('white')
            slider.poly.set_facecolor('#666666')
            
            # Store slider and parameter info
            self.sliders[param] = {
                'slider': slider,
                'min': min_val,
                'max': max_val,
                'init': init_val
            }
            
            # Connect slider to update function
            slider.on_changed(self.on_slider_change)
    
    def setup_buttons(self):
        """Setup control buttons"""
        # Regenerate button
        ax_regenerate = plt.axes([0.5, 0.15, 0.15, 0.04])
        self.btn_regenerate = Button(ax_regenerate, 'Regenerate', 
                                   color='#404040', hovercolor='#666666')
        self.btn_regenerate.label.set_color('white')
        self.btn_regenerate.on_clicked(self.regenerate_fractal)
        
        # Random seed button
        ax_random = plt.axes([0.5, 0.10, 0.15, 0.04])
        self.btn_random = Button(ax_random, 'Random Seed', 
                               color='#404040', hovercolor='#666666')
        self.btn_random.label.set_color('white')
        self.btn_random.on_clicked(self.random_seed)
        
        # Preset buttons
        presets = ['delicate', 'dense', 'sparse', 'spiky']
        for i, preset in enumerate(presets):
            ax_preset = plt.axes([0.7 + (i % 2) * 0.1, 0.15 - (i // 2) * 0.05, 0.08, 0.04])
            btn_preset = Button(ax_preset, preset.title(), 
                              color='#404040', hovercolor='#666666')
            btn_preset.label.set_color('white')
            btn_preset.on_clicked(lambda event, p=preset: self.apply_preset(p))
    
    def on_slider_change(self, val):
        """Handle slider value changes"""
        # Update fractal parameters
        for param, slider_info in self.sliders.items():
            setattr(self.fractal, param, slider_info['slider'].val)
        
        # Regenerate fractal
        self.update_fractal()
    
    def regenerate_fractal(self, event):
        """Regenerate fractal with current parameters"""
        self.update_fractal()
    
    def random_seed(self, event):
        """Generate fractal with random seed"""
        seed = random.randint(1, 10000)
        self.fractal.generate_fractal(seed=seed)
        self.update_fractal()
        print(f"Generated with random seed: {seed}")
    
    def apply_preset(self, preset_name):
        """Apply a preset configuration"""
        from enhanced_fractal import create_preset_fractals
        presets = create_preset_fractals()
        
        if preset_name in presets:
            config = presets[preset_name]
            
            # Update fractal parameters
            for param, value in config.items():
                if hasattr(self.fractal, param):
                    setattr(self.fractal, param, value)
                    # Update slider if it exists
                    if param in self.sliders:
                        self.sliders[param]['slider'].set_val(value)
            
            # Regenerate fractal
            self.update_fractal()
            print(f"Applied preset: {preset_name}")
    
    def update_fractal(self):
        """Update the fractal display"""
        # Clear the plot
        self.ax.clear()
        self.setup_plot()
        
        # Generate new fractal
        self.fractal.generate_fractal()
        
        # Create central void
        void = patches.Circle((self.fractal.center_x, self.fractal.center_y), 
                            self.fractal.central_void_radius, 
                            facecolor='black', edgecolor='none')
        self.ax.add_patch(void)
        
        # Draw circles
        circle_patches = []
        for circle in self.fractal.circles:
            # Skip circles that are too close to center
            distance_from_center = math.sqrt(
                (circle['x'] - self.fractal.center_x)**2 + 
                (circle['y'] - self.fractal.center_y)**2
            )
            if distance_from_center < self.fractal.central_void_radius + 10:
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
            self.ax.add_collection(circle_collection)
        
        # Draw spikes
        for spike in self.fractal.spikes:
            self.ax.plot([spike['x1'], spike['x2']], [spike['y1'], spike['y2']], 
                       color='#404040', linewidth=spike['thickness'], alpha=0.8)
        
        # Update display
        self.fig.canvas.draw_idle()
        
        # Print statistics
        print(f"Fractal updated: {len(self.fractal.circles)} circles, {len(self.fractal.spikes)} spikes")
    
    def show(self):
        """Show the interactive fractal generator"""
        plt.show()

def main():
    """Main function to run the interactive fractal generator"""
    print("Interactive Organic Fractal Generator")
    print("=" * 40)
    print("Use the sliders to adjust parameters in real-time!")
    print("Click 'Regenerate' to create a new fractal with current settings.")
    print("Click 'Random Seed' to generate with a random seed.")
    print("Use preset buttons to apply predefined configurations.")
    
    # Create and show interactive fractal
    interactive_fractal = InteractiveFractal()
    interactive_fractal.show()

if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.patches as patches

class InteractiveSpirograph:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 12))
        self.setup_plot()
        self.setup_sliders()
        self.update_plot()
        
    def setup_plot(self):
        """Setup the plot with black background"""
        self.ax.set_facecolor('black')
        self.fig.patch.set_facecolor('black')
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Initialize the plot line
        self.line, = self.ax.plot([], [], color='white', linewidth=1.5, alpha=0.9)
        
        # Add formula text
        self.formula_text = self.ax.text(0.5, 0.95, '', transform=self.ax.transAxes, 
                                        fontsize=16, color='white', ha='center', va='top',
                                        bbox=dict(boxstyle="round,pad=0.3", facecolor='black', alpha=0.7))
        
    def setup_sliders(self):
        """Setup interactive sliders for parameters"""
        # Create space for sliders
        plt.subplots_adjust(bottom=0.3)
        
        # Slider positions
        ax_a = plt.axes([0.2, 0.25, 0.6, 0.03])
        ax_b = plt.axes([0.2, 0.20, 0.6, 0.03])
        ax_c = plt.axes([0.2, 0.15, 0.6, 0.03])
        ax_freq1 = plt.axes([0.2, 0.10, 0.6, 0.03])
        ax_freq2 = plt.axes([0.2, 0.05, 0.6, 0.03])
        ax_freq3 = plt.axes([0.2, 0.00, 0.6, 0.03])
        
        # Create sliders
        self.s_a = Slider(ax_a, 'A', 0.1, 10.0, valinit=2.0, color='white')
        self.s_b = Slider(ax_b, 'B', 0.1, 10.0, valinit=5.0, color='white')
        self.s_c = Slider(ax_c, 'C', 0.1, 10.0, valinit=0.5, color='white')
        self.s_freq1 = Slider(ax_freq1, 'Freq1', 1, 50, valinit=13, valstep=1, color='white')
        self.s_freq2 = Slider(ax_freq2, 'Freq2', 1, 50, valinit=12, valstep=1, color='white')
        self.s_freq3 = Slider(ax_freq3, 'Freq3', 1, 50, valinit=45, valstep=1, color='white')
        
        # Connect sliders to update function
        self.s_a.on_changed(self.update_plot)
        self.s_b.on_changed(self.update_plot)
        self.s_c.on_changed(self.update_plot)
        self.s_freq1.on_changed(self.update_plot)
        self.s_freq2.on_changed(self.update_plot)
        self.s_freq3.on_changed(self.update_plot)
        
        # Style sliders
        for slider in [self.s_a, self.s_b, self.s_c, self.s_freq1, self.s_freq2, self.s_freq3]:
            slider.label.set_color('white')
            slider.valtext.set_color('white')
    
    def generate_pattern(self, a, b, c, freq1, freq2, freq3):
        """Generate spirograph pattern with given parameters"""
        t = np.linspace(0, 2*np.pi, 2000)  # Reduced from 5000 to 2000 for speed
        
        # Pre-calculate common values for speed
        freq1_t = freq1 * t
        freq2_t = freq2 * t
        it = 1j * t
        
        # Calculate the complex function
        z = (a * np.exp(1j * freq1_t) + 
             b * np.sin(freq2_t) * np.exp(it) + 
             c * np.exp(1j * freq3 * t))
        
        return np.real(z), np.imag(z)
    
    def update_plot(self, val=None):
        """Update the plot with current parameter values"""
        # Get current parameter values
        a = self.s_a.val
        b = self.s_b.val
        c = self.s_c.val
        freq1 = self.s_freq1.val
        freq2 = self.s_freq2.val
        freq3 = self.s_freq3.val
        
        # Generate new pattern
        x, y = self.generate_pattern(a, b, c, freq1, freq2, freq3)
        
        # Update the line data
        self.line.set_data(x, y)
        
        # Update formula text
        formula = f'$z(t) = {a:.1f}e^{{i{freq1:.0f}t}} + {b:.1f}\\sin({freq2:.0f}t) e^{{it}} + {c:.1f} e^{{i{freq3:.0f}t}}$'
        self.formula_text.set_text(formula)
        
        # Update plot limits
        margin = 0.1
        x_range = x.max() - x.min()
        y_range = y.max() - y.min()
        self.ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
        self.ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
        
        self.fig.canvas.draw_idle()

def create_preset_patterns():
    """Create some preset patterns to demonstrate different effects"""
    presets = {
        'Original': {'a': 2.0, 'b': 5.0, 'c': 0.5, 'freq1': 13, 'freq2': 12, 'freq3': 45},
        'Flower': {'a': 3.0, 'b': 4.0, 'c': 1.0, 'freq1': 8, 'freq2': 6, 'freq3': 24},
        'Star': {'a': 1.5, 'b': 6.0, 'c': 0.3, 'freq1': 5, 'freq2': 10, 'freq3': 15},
        'Spiral': {'a': 2.0, 'b': 3.0, 'c': 2.0, 'freq1': 3, 'freq2': 7, 'freq3': 11},
        'Complex': {'a': 4.0, 'b': 2.0, 'c': 1.5, 'freq1': 17, 'freq2': 13, 'freq3': 29}
    }
    return presets

if __name__ == "__main__":
    print("Creating interactive spirograph pattern generator...")
    print("Use the sliders to adjust parameters and see the pattern change in real-time!")
    
    # Create interactive spirograph
    spiro = InteractiveSpirograph()
    
    # Show preset patterns
    presets = create_preset_patterns()
    print("\nPreset patterns available:")
    for name in presets.keys():
        print(f"- {name}")
    
    plt.show()

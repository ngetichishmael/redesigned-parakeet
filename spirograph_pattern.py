import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

def generate_spirograph_pattern():
    """
    Generate the spirograph pattern from the formula:
    z(t) = 2e^(i13t) + 5 sin(12t) e^(it) + 0.5 e^(i45t)
    where t ∈ [0, 2π]
    """
    # Create parameter t from 0 to 2π (reduced for speed)
    t = np.linspace(0, 2*np.pi, 3000)
    
    # Pre-calculate common values for speed
    freq1_t = 13 * t
    freq2_t = 12 * t
    it = 1j * t
    
    # Calculate the complex function
    z = (2 * np.exp(1j * freq1_t) + 
         5 * np.sin(freq2_t) * np.exp(it) + 
         0.5 * np.exp(1j * 45 * t))
    
    # Extract real and imaginary parts
    x = np.real(z)
    y = np.imag(z)
    
    return x, y, t

def create_visualization():
    """Create the complete visualization with the pattern and styling"""
    # Generate the pattern
    x, y, t = generate_spirograph_pattern()
    
    # Create figure with black background
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Plot the main pattern in white
    ax.plot(x, y, color='white', linewidth=1.5, alpha=0.9)
    
    # Add dynamic elements (the green lines and white circles)
    # Find interesting points on the curve for the dynamic elements
    idx1 = int(len(t) * 0.3)  # 30% along the curve
    idx2 = int(len(t) * 0.4)  # 40% along the curve
    idx3 = int(len(t) * 0.5)  # 50% along the curve
    
    # Plot white circles at these points
    ax.plot(x[idx1], y[idx1], 'o', color='white', markersize=8, markeredgecolor='white', markeredgewidth=2)
    ax.plot(x[idx2], y[idx2], 'o', color='white', markersize=8, markeredgecolor='white', markeredgewidth=2)
    ax.plot(x[idx3], y[idx3], 'o', color='white', markersize=8, markeredgecolor='white', markeredgewidth=2)
    
    # Draw green lines connecting the circles
    ax.plot([x[idx1], x[idx2]], [y[idx1], y[idx2]], color='lime', linewidth=3, alpha=0.8)
    ax.plot([x[idx2], x[idx3]], [y[idx2], y[idx3]], color='lime', linewidth=3, alpha=0.8)
    
    # Add the mathematical formula as text
    formula_text = r'$z(t) = 2e^{i13t} + 5 \sin(12t) e^{it} + 0.5 e^{i45t}$' + '\n' + r'$t \in [0, 2\pi]$'
    ax.text(0.5, 0.95, formula_text, transform=ax.transAxes, 
            fontsize=16, color='white', ha='center', va='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='black', alpha=0.7))
    
    # Set equal aspect ratio and remove axes
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set plot limits to show the full pattern
    margin = 0.1
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
    ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
    
    plt.tight_layout()
    return fig, ax

def create_animated_version():
    """Create an animated version showing the curve being drawn"""
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Generate the pattern
    x, y, t = generate_spirograph_pattern()
    
    # Initialize empty line
    line, = ax.plot([], [], color='white', linewidth=1.5)
    
    # Set up the plot
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set plot limits
    margin = 0.1
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
    ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
    
    # Add formula text
    formula_text = r'$z(t) = 2e^{i13t} + 5 \sin(12t) e^{it} + 0.5 e^{i45t}$' + '\n' + r'$t \in [0, 2\pi]$'
    ax.text(0.5, 0.95, formula_text, transform=ax.transAxes, 
            fontsize=16, color='white', ha='center', va='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='black', alpha=0.7))
    
    def animate(frame):
        # Draw the curve up to the current frame
        end_idx = min(frame * step, len(x))
        line.set_data(x[:end_idx], y[:end_idx])
        return line,
    
    # Create animation (faster with fewer frames)
    step = max(1, len(x) // 300)  # Only 300 frames max for speed
    anim = FuncAnimation(fig, animate, frames=300, interval=10, blit=True, repeat=True)
    
    return fig, anim

if __name__ == "__main__":
    # Create static visualization
    print("Creating static spirograph pattern...")
    fig, ax = create_visualization()
    plt.savefig('spirograph_pattern.png', dpi=300, bbox_inches='tight', facecolor='black')
    plt.show()
    
    # Create animated version
    print("Creating animated spirograph pattern...")
    fig_anim, anim = create_animated_version()
    plt.show()

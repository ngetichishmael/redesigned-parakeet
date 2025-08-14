import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('MacOSX')  # Use MacOSX backend for better performance on macOS

def generate_spirograph_pattern_fast(a=2.0, b=5.0, c=0.5, freq1=13, freq2=12, freq3=45, num_points=2000):
    """
    Fast spirograph pattern generation with reduced points and optimized calculations
    """
    # Use fewer points for speed
    t = np.linspace(0, 2*np.pi, num_points)
    
    # Pre-calculate common values
    freq1_t = freq1 * t
    freq2_t = freq2 * t
    freq3_t = freq3 * t
    it = 1j * t
    
    # Optimized complex function calculation
    z = (a * np.exp(1j * freq1_t) + 
         b * np.sin(freq2_t) * np.exp(it) + 
         c * np.exp(1j * freq3_t))
    
    return np.real(z), np.imag(z)

def create_fast_visualization(num_points=2000):
    """Create fast visualization with minimal styling"""
    x, y = generate_spirograph_pattern_fast(num_points=num_points)
    
    # Create figure with minimal setup
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Plot with minimal styling
    ax.plot(x, y, color='white', linewidth=1, alpha=0.9)
    
    # Add dynamic elements (simplified)
    idx1, idx2, idx3 = int(len(x) * 0.3), int(len(x) * 0.4), int(len(x) * 0.5)
    
    # White circles
    ax.plot(x[idx1], y[idx1], 'o', color='white', markersize=6)
    ax.plot(x[idx2], y[idx2], 'o', color='white', markersize=6)
    ax.plot(x[idx3], y[idx3], 'o', color='white', markersize=6)
    
    # Green lines
    ax.plot([x[idx1], x[idx2]], [y[idx1], y[idx2]], color='lime', linewidth=2)
    ax.plot([x[idx2], x[idx3]], [y[idx2], y[idx3]], color='lime', linewidth=2)
    
    # Simplified formula text
    ax.text(0.5, 0.95, r'$z(t) = 2e^{i13t} + 5 \sin(12t) e^{it} + 0.5 e^{i45t}$', 
            transform=ax.transAxes, fontsize=14, color='white', ha='center', va='top')
    
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Auto-scale
    margin = 0.1
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
    ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
    
    return fig, ax

def create_ultra_fast_animation(num_points=1000, interval=10):
    """Create ultra-fast animation with minimal frames and fast rendering"""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Generate pattern
    x, y = generate_spirograph_pattern_fast(num_points=num_points)
    
    # Initialize line
    line, = ax.plot([], [], color='white', linewidth=1)
    
    # Setup plot
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Set limits once
    margin = 0.1
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
    ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
    
    # Use fewer frames for speed
    step = max(1, len(x) // 200)  # Only 200 frames max
    
    def animate(frame):
        end_idx = min(frame * step, len(x))
        line.set_data(x[:end_idx], y[:end_idx])
        return line,
    
    # Fast animation with minimal interval
    anim = FuncAnimation(fig, animate, frames=200, interval=interval, blit=True, repeat=True)
    
    return fig, anim

def create_batch_patterns(num_patterns=10, num_points=1000):
    """Generate multiple patterns quickly for comparison"""
    patterns = []
    
    # Pre-define parameter sets
    param_sets = [
        {'a': 2.0, 'b': 5.0, 'c': 0.5, 'freq1': 13, 'freq2': 12, 'freq3': 45},
        {'a': 3.0, 'b': 4.0, 'c': 1.0, 'freq1': 8, 'freq2': 6, 'freq3': 24},
        {'a': 1.5, 'b': 6.0, 'c': 0.3, 'freq1': 5, 'freq2': 10, 'freq3': 15},
        {'a': 2.0, 'b': 3.0, 'c': 2.0, 'freq1': 3, 'freq2': 7, 'freq3': 11},
        {'a': 4.0, 'b': 2.0, 'c': 1.5, 'freq1': 17, 'freq2': 13, 'freq3': 29},
    ]
    
    for i, params in enumerate(param_sets[:num_patterns]):
        x, y = generate_spirograph_pattern_fast(num_points=num_points, **params)
        patterns.append((x, y, params))
    
    return patterns

def show_fast_comparison():
    """Show multiple patterns quickly for comparison"""
    patterns = create_batch_patterns(num_patterns=5, num_points=1000)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.patch.set_facecolor('black')
    
    for i, (x, y, params) in enumerate(patterns):
        row, col = i // 3, i % 3
        ax = axes[row, col]
        
        ax.set_facecolor('black')
        ax.plot(x, y, color='white', linewidth=1, alpha=0.8)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Auto-scale
        margin = 0.1
        x_range = x.max() - x.min()
        y_range = y.max() - y.min()
        ax.set_xlim(x.min() - margin * x_range, x.max() + margin * x_range)
        ax.set_ylim(y.min() - margin * y_range, y.max() + margin * y_range)
        
        ax.set_title(f'Pattern {i+1}', color='white', fontsize=10)
    
    # Hide unused subplot
    axes[1, 2].set_visible(False)
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    import time
    
    print("=== Fast Spirograph Pattern Generator ===")
    print("1. Single fast pattern")
    print("2. Ultra-fast animation")
    print("3. Multiple patterns comparison")
    
    choice = input("Choose option (1-3): ").strip()
    
    if choice == "1":
        print("Generating fast single pattern...")
        start_time = time.time()
        fig, ax = create_fast_visualization(num_points=2000)
        end_time = time.time()
        print(f"Generated in {end_time - start_time:.3f} seconds")
        plt.show()
        
    elif choice == "2":
        print("Generating ultra-fast animation...")
        start_time = time.time()
        fig, anim = create_ultra_fast_animation(num_points=1000, interval=5)
        end_time = time.time()
        print(f"Generated in {end_time - start_time:.3f} seconds")
        plt.show()
        
    elif choice == "3":
        print("Generating multiple patterns...")
        start_time = time.time()
        fig = show_fast_comparison()
        end_time = time.time()
        print(f"Generated in {end_time - start_time:.3f} seconds")
        plt.show()
        
    else:
        print("Invalid choice. Running fast single pattern...")
        fig, ax = create_fast_visualization()
        plt.show()

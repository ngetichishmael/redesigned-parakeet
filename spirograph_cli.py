import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend

def generate_spirograph_pattern(a=2.0, b=5.0, c=0.5, freq1=13, freq2=12, freq3=45):
    """
    Generate the spirograph pattern from the formula:
    z(t) = a*e^(i*freq1*t) + b*sin(freq2*t)*e^(it) + c*e^(i*freq3*t)
    where t ∈ [0, 2π]
    """
    # Create parameter t from 0 to 2π
    t = np.linspace(0, 2*np.pi, 10000)
    
    # Calculate the complex function
    z = (a * np.exp(1j * freq1 * t) + 
         b * np.sin(freq2 * t) * np.exp(1j * t) + 
         c * np.exp(1j * freq3 * t))
    
    # Extract real and imaginary parts
    x = np.real(z)
    y = np.imag(z)
    
    return x, y, t

def create_spirograph_image(filename='spirograph_pattern.png', 
                           a=2.0, b=5.0, c=0.5, freq1=13, freq2=12, freq3=45,
                           width=1200, height=1200, dpi=300):
    """Create and save a spirograph pattern image"""
    # Generate the pattern
    x, y, t = generate_spirograph_pattern(a, b, c, freq1, freq2, freq3)
    
    # Create figure with black background
    fig, ax = plt.subplots(figsize=(width/100, height/100))
    ax.set_facecolor('black')
    fig.patch.set_facecolor('black')
    
    # Plot the main pattern in white
    ax.plot(x, y, color='white', linewidth=2, alpha=0.9)
    
    # Add dynamic elements (the green lines and white circles)
    # Find interesting points on the curve for the dynamic elements
    idx1 = int(len(t) * 0.3)  # 30% along the curve
    idx2 = int(len(t) * 0.4)  # 40% along the curve
    idx3 = int(len(t) * 0.5)  # 50% along the curve
    
    # Plot white circles at these points
    ax.plot(x[idx1], y[idx1], 'o', color='white', markersize=10, markeredgecolor='white', markeredgewidth=2)
    ax.plot(x[idx2], y[idx2], 'o', color='white', markersize=10, markeredgecolor='white', markeredgewidth=2)
    ax.plot(x[idx3], y[idx3], 'o', color='white', markersize=10, markeredgecolor='white', markeredgewidth=2)
    
    # Draw green lines connecting the circles
    ax.plot([x[idx1], x[idx2]], [y[idx1], y[idx2]], color='lime', linewidth=4, alpha=0.8)
    ax.plot([x[idx2], x[idx3]], [y[idx2], y[idx3]], color='lime', linewidth=4, alpha=0.8)
    
    # Add the mathematical formula as text
    formula_text = f'$z(t) = {a:.1f}e^{{i{freq1:.0f}t}} + {b:.1f}\\sin({freq2:.0f}t) e^{{it}} + {c:.1f} e^{{i{freq3:.0f}t}}$' + '\n' + r'$t \in [0, 2\pi]$'
    ax.text(0.5, 0.95, formula_text, transform=ax.transAxes, 
            fontsize=18, color='white', ha='center', va='top',
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
    
    # Save the image
    plt.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='black')
    plt.close()
    
    print(f"Spirograph pattern saved as '{filename}'")
    print(f"Parameters: a={a}, b={b}, c={c}, freq1={freq1}, freq2={freq2}, freq3={freq3}")

def create_preset_patterns():
    """Generate several preset patterns"""
    presets = {
        'original': {'a': 2.0, 'b': 5.0, 'c': 0.5, 'freq1': 13, 'freq2': 12, 'freq3': 45},
        'flower': {'a': 3.0, 'b': 4.0, 'c': 1.0, 'freq1': 8, 'freq2': 6, 'freq3': 24},
        'star': {'a': 1.5, 'b': 6.0, 'c': 0.3, 'freq1': 5, 'freq2': 10, 'freq3': 15},
        'spiral': {'a': 2.0, 'b': 3.0, 'c': 2.0, 'freq1': 3, 'freq2': 7, 'freq3': 11},
        'complex': {'a': 4.0, 'b': 2.0, 'c': 1.5, 'freq1': 17, 'freq2': 13, 'freq3': 29}
    }
    
    for name, params in presets.items():
        filename = f'spirograph_{name}.png'
        create_spirograph_image(filename=filename, **params)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate spirograph patterns')
    parser.add_argument('--output', '-o', default='spirograph_pattern.png', 
                       help='Output filename (default: spirograph_pattern.png)')
    parser.add_argument('--a', type=float, default=2.0, help='Parameter a (default: 2.0)')
    parser.add_argument('--b', type=float, default=5.0, help='Parameter b (default: 5.0)')
    parser.add_argument('--c', type=float, default=0.5, help='Parameter c (default: 0.5)')
    parser.add_argument('--freq1', type=int, default=13, help='Frequency 1 (default: 13)')
    parser.add_argument('--freq2', type=int, default=12, help='Frequency 2 (default: 12)')
    parser.add_argument('--freq3', type=int, default=45, help='Frequency 3 (default: 45)')
    parser.add_argument('--width', type=int, default=1200, help='Image width (default: 1200)')
    parser.add_argument('--height', type=int, default=1200, help='Image height (default: 1200)')
    parser.add_argument('--dpi', type=int, default=300, help='Image DPI (default: 300)')
    parser.add_argument('--presets', action='store_true', help='Generate all preset patterns')
    
    args = parser.parse_args()
    
    if args.presets:
        print("Generating all preset patterns...")
        create_preset_patterns()
    else:
        print("Generating custom spirograph pattern...")
        create_spirograph_image(
            filename=args.output,
            a=args.a, b=args.b, c=args.c,
            freq1=args.freq1, freq2=args.freq2, freq3=args.freq3,
            width=args.width, height=args.height, dpi=args.dpi
        )

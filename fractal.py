import numpy as np
import matplotlib.pyplot as plt
import math

def julia_set_variation(h, w, max_iter=256, zoom=1, move_x=0, move_y=0):
    """
    Generate a Julia set variation with organic branching patterns
    """
    # Create coordinate arrays
    x_min, x_max = -2.0 / zoom + move_x, 2.0 / zoom + move_x
    y_min, y_max = -2.0 / zoom + move_y, 2.0 / zoom + move_y
    
    # Create meshgrid for vectorized computation
    x = np.linspace(x_min, x_max, w)
    y = np.linspace(y_min, y_max, h)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    # Initialize arrays
    fractal = np.zeros((h, w))
    
    # Complex parameter for Julia set (creates branching patterns)
    c = complex(-0.7269, 0.1889)
    
    # Iterate for each point
    for i in range(max_iter):
        # Find points that haven't diverged
        mask = np.abs(Z) <= 2.0
        
        if not np.any(mask):
            break
            
        # Update only non-diverged points
        Z[mask] = Z[mask] * Z[mask] + c
        
        # Add organic distortion after some iterations
        if i > 10:
            angle = np.angle(Z)
            radius = np.abs(Z)
            # Create branching effect
            distortion = 0.1 * np.sin(8 * angle) * np.exp(-radius * 0.5)
            Z[mask] = Z[mask] + distortion[mask] * np.exp(1j * angle[mask])
        
        # Update fractal for points that just diverged
        newly_diverged = (np.abs(Z) > 2.0) & (fractal == 0)
        fractal[newly_diverged] = i
    
    # Set remaining points to max_iter
    fractal[fractal == 0] = max_iter
    
    return fractal

def mandelbrot_variation(h, w, max_iter=256, zoom=1, move_x=0, move_y=0):
    """
    Generate a Mandelbrot variation with organic features
    """
    x_min, x_max = -2.5 / zoom + move_x, 1.0 / zoom + move_x
    y_min, y_max = -1.25 / zoom + move_y, 1.25 / zoom + move_y
    
    # Create coordinate meshgrid
    x = np.linspace(x_min, x_max, w)
    y = np.linspace(y_min, y_max, h)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    
    fractal = np.zeros((h, w))
    
    for i in range(max_iter):
        # Find points that haven't diverged
        mask = np.abs(Z) <= 2.0
        
        if not np.any(mask):
            break
        
        # Standard Mandelbrot iteration
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        
        # Add organic branching after some iterations
        if i > 5:
            angle = np.angle(Z)
            radius = np.abs(Z)
            branch_factor = 0.05 * np.sin(12 * angle) * np.cos(6 * angle)
            organic_mult = 1 + branch_factor * np.exp(-radius * 0.3)
            Z[mask] = Z[mask] * organic_mult[mask]
        
        # Update fractal for newly diverged points
        newly_diverged = (np.abs(Z) > 2.0) & (fractal == 0)
        fractal[newly_diverged] = i
    
    # Set remaining points to max_iter
    fractal[fractal == 0] = max_iter
    
    return fractal

def diffusion_limited_aggregation(width, height, num_particles=5000, stickiness=0.3):
    """
    Generate organic patterns using Diffusion Limited Aggregation
    This creates coral-like branching structures
    """
    # Initialize grid
    grid = np.zeros((height, width), dtype=bool)
    
    # Set seed point at center
    center_y, center_x = height // 2, width // 2
    grid[center_y, center_x] = True
    
    # Random walk particles
    for _ in range(num_particles):
        # Start particle at random edge position
        if np.random.random() < 0.5:
            # Start from left or right edge
            start_x = 0 if np.random.random() < 0.5 else width - 1
            start_y = np.random.randint(0, height)
        else:
            # Start from top or bottom edge
            start_x = np.random.randint(0, width)
            start_y = 0 if np.random.random() < 0.5 else height - 1
        
        x, y = start_x, start_y
        
        # Random walk until particle sticks or leaves bounds
        max_steps = width + height  # Prevent infinite loops
        for _ in range(max_steps):
            # Check if adjacent to existing structure
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    neighbors.append((nx, ny))
            
            # Check if any neighbor is part of the structure
            if any(grid[ny, nx] for nx, ny in neighbors):
                if np.random.random() < stickiness:
                    grid[y, x] = True
                    break
            
            # Random step
            dx, dy = np.random.choice([-1, 0, 1], 2)
            x, y = x + dx, y + dy
            
            # Check bounds
            if x < 0 or x >= width or y < 0 or y >= height:
                break
    
    return grid.astype(float) * 255

def create_organic_fractal(width=800, height=800, fractal_type="julia", zoom=1.0, 
                          move_x=0, move_y=0, max_iter=256):
    """
    Create an organic-looking fractal similar to the provided image
    """
    if fractal_type == "julia":
        fractal_data = julia_set_variation(height, width, max_iter, zoom, move_x, move_y)
    elif fractal_type == "mandelbrot":
        fractal_data = mandelbrot_variation(height, width, max_iter, zoom, move_x, move_y)
    elif fractal_type == "dla":
        fractal_data = diffusion_limited_aggregation(width, height)
    else:
        fractal_data = julia_set_variation(height, width, max_iter, zoom, move_x, move_y)
    
    return fractal_data

def apply_organic_coloring(fractal_data, threshold=50):
    """
    Apply coloring to create the organic white-on-black appearance
    """
    # Create binary mask for the organic structures
    mask = fractal_data < threshold
    
    # Create the final image
    colored_fractal = np.zeros_like(fractal_data)
    colored_fractal[mask] = 255  # White branches
    colored_fractal[~mask] = 0   # Black background
    
    return colored_fractal

def add_noise_texture(fractal, noise_strength=0.1):
    """Add subtle noise for more organic texture"""
    noise = np.random.random(fractal.shape) * noise_strength * 255
    textured = np.clip(fractal + noise - noise_strength * 255 / 2, 0, 255)
    return textured

def generate_layered_fractal(width=800, height=800):
    """
    Generate a complex fractal by layering multiple iterations
    """
    print("Generating layer 1...")
    layer1 = create_organic_fractal(width, height, "julia", zoom=0.8, max_iter=100)
    
    print("Generating layer 2...")
    layer2 = create_organic_fractal(width, height, "julia", zoom=1.2, 
                                   move_x=0.1, move_y=0.1, max_iter=150)
    
    print("Generating layer 3...")
    layer3 = create_organic_fractal(width, height, "mandelbrot", zoom=0.6, 
                                   move_x=-0.5, move_y=0.2, max_iter=80)
    
    # Combine layers for complexity
    print("Combining layers...")
    combined = np.minimum(layer1, np.minimum(layer2, layer3))
    
    return combined

def create_radial_pattern(width, height):
    """Create a radial organic pattern similar to the image"""
    # Create coordinate system centered at image center
    y, x = np.ogrid[:height, :width]
    center_x, center_y = width // 2, height // 2
    
    # Convert to polar coordinates
    dx = x - center_x
    dy = y - center_y
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    
    # Create organic radial pattern
    # Multiple frequency components for complexity
    pattern = np.zeros((height, width))
    
    # Base radial waves
    for freq in [8, 12, 16, 20]:
        wave = np.sin(freq * theta + r * 0.02)
        pattern += wave * np.exp(-r * 0.003)
    
    # Add some randomness
    for freq in [3, 5, 7]:
        wave = np.sin(freq * theta + r * 0.01 + np.pi/4)
        pattern += 0.5 * wave * np.exp(-r * 0.002)
    
    # Create branching effect
    branch_mask = np.abs(pattern) > 0.5
    
    # Convert to 0-255 range
    result = np.zeros_like(pattern)
    result[branch_mask] = 255
    
    return result

# Main execution
def main():
    print("Generating organic fractal patterns...")
    
    width, height = 800, 800
    
    # Option 1: Layered fractal approach
    print("\n=== Generating Layered Fractal ===")
    fractal_raw = generate_layered_fractal(width, height)
    fractal_colored = apply_organic_coloring(fractal_raw, threshold=60)
    
    # Option 2: Radial organic pattern
    print("\n=== Generating Radial Pattern ===")
    radial_pattern = create_radial_pattern(width, height)
    
    # Option 3: DLA pattern
    print("\n=== Generating DLA Pattern ===")
    dla_pattern = create_organic_fractal(width, height, "dla")
    
    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(16, 16))
    
    # Show layered fractal
    axes[0, 0].imshow(fractal_colored, cmap='gray', origin='lower')
    axes[0, 0].set_title('Layered Fractal Pattern', color='white', fontsize=14)
    axes[0, 0].axis('off')
    axes[0, 0].set_facecolor('black')
    
    # Show radial pattern
    axes[0, 1].imshow(radial_pattern, cmap='gray', origin='lower')
    axes[0, 1].set_title('Radial Organic Pattern', color='white', fontsize=14)
    axes[0, 1].axis('off')
    axes[0, 1].set_facecolor('black')
    
    # Show DLA pattern
    axes[1, 0].imshow(dla_pattern, cmap='gray', origin='lower')
    axes[1, 0].set_title('Diffusion Limited Aggregation', color='white', fontsize=14)
    axes[1, 0].axis('off')
    axes[1, 0].set_facecolor('black')
    
    # Show combined/textured version
    combined_textured = add_noise_texture(radial_pattern, 0.05)
    axes[1, 1].imshow(combined_textured, cmap='gray', origin='lower')
    axes[1, 1].set_title('Textured Organic Pattern', color='white', fontsize=14)
    axes[1, 1].axis('off')
    axes[1, 1].set_facecolor('black')
    
    plt.tight_layout()
    fig.patch.set_facecolor('black')
    plt.show()
    
    print("\nFractal generation complete!")
    print("\nTo customize:")
    print("- Try quick_fractal() for single patterns")
    print("- Adjust parameters like zoom, threshold")
    print("- Use create_radial_pattern() for patterns similar to your image")

def quick_fractal(pattern_type="radial", size=600):
    """Quick generation of organic patterns"""
    if pattern_type == "radial":
        fractal = create_radial_pattern(size, size)
    elif pattern_type == "julia":
        fractal_raw = create_organic_fractal(size, size, "julia", zoom=0.8)
        fractal = apply_organic_coloring(fractal_raw, threshold=50)
    elif pattern_type == "dla":
        fractal = create_organic_fractal(size, size, "dla")
    else:
        fractal = create_radial_pattern(size, size)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(fractal, cmap='gray', origin='lower')
    plt.axis('off')
    plt.gca().set_facecolor('black')
    plt.title(f'{pattern_type.title()} Organic Pattern', color='white', pad=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Install only numpy and matplotlib:
    # uv add numpy matplotlib
    
    main()
    
    # Uncomment for quick single patterns:
    quick_fractal("radial")
    quick_fractal("julia")
    quick_fractal("dla")
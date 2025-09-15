# Organic Fractal Generator

A collection of Python tools for generating complex organic fractal patterns with white circles and dark grey spiky elements against a black background, featuring central voids and radial branching structures.

## Features

- **Organic Branching**: Recursive fractal generation with natural, coral-like growth patterns
- **Circle-based Structure**: White circles of varying sizes form the main fractal body
- **Spiky Textures**: Dark grey spiky elements add organic texture and detail
- **Central Void**: Irregular central void creates the characteristic fractal shape
- **Multiple Presets**: Predefined configurations for different fractal styles
- **Interactive Controls**: Real-time parameter adjustment with sliders
- **High-Quality Output**: Configurable resolution and DPI for print-quality images

## Files

### Core Generators

1. **`organic_fractal.py`** - Basic fractal generator
   - Simple, straightforward implementation
   - Good for understanding the core algorithm
   - Generates single fractal with default parameters

2. **`enhanced_fractal.py`** - Advanced fractal generator
   - Extensive customization options
   - Command-line interface
   - Multiple preset configurations
   - Batch generation capabilities

3. **`interactive_fractal.py`** - Interactive fractal generator
   - Real-time parameter adjustment
   - Live preview with sliders
   - Preset buttons for quick configuration
   - Perfect for experimentation

## Usage

### Basic Usage

```bash
# Generate a basic fractal
uv run python organic_fractal.py

# Generate with specific preset
uv run python enhanced_fractal.py --preset dense

# Generate with custom parameters
uv run python enhanced_fractal.py --width 1600 --height 1600 --dpi 300 --seed 123
```

### Interactive Mode

```bash
# Launch interactive fractal generator
uv run python interactive_fractal.py
```

### Available Presets

- **`delicate`**: Light, airy fractal with fewer elements
- **`dense`**: Complex, heavily detailed fractal
- **`sparse`**: Minimal fractal with clean lines
- **`spiky`**: Fractal with prominent spiky textures

## Parameters

### Core Parameters

- **`max_depth`**: Maximum recursion depth (1-12)
- **`num_main_branches`**: Number of main branches from center (3-15)
- **`central_void_radius`**: Size of central void (20-150)
- **`circle_density`**: Probability of placing circles (0.1-1.0)
- **`spike_density`**: Probability of placing spikes (0.0-1.0)

### Branching Parameters

- **`branch_length_decay`**: How much branches shrink each level (0.3-0.9)
- **`circle_size_decay`**: How much circles shrink each level (0.3-0.9)
- **`branch_angle_variance`**: Randomness in branch angles (0.1-0.8)

### Rendering Parameters

- **`width`**: Image width in pixels
- **`height`**: Image height in pixels
- **`dpi`**: Dots per inch for output
- **`seed`**: Random seed for reproducible results

## Algorithm

The fractal generation uses a recursive branching algorithm:

1. **Initialization**: Create main branches radiating from center
2. **Branch Generation**: For each branch:
   - Place circles along the branch path
   - Add spiky elements for texture
   - Create sub-branches at random points
3. **Recursion**: Repeat for each sub-branch with reduced parameters
4. **Rendering**: Draw circles and spikes on black background with central void

## Examples

### Generated Images

The following fractal variations have been generated:

- `organic_fractal.png` - Basic fractal (157 circles, 81 spikes)
- `delicate_fractal.png` - Delicate preset (126 circles, 144 spikes)
- `dense_fractal.png` - Dense preset (286 circles, 179 spikes)
- `spiky_fractal.png` - Spiky preset (176 circles, 629 spikes)

### Customization Examples

```python
# Create a custom fractal
fractal = EnhancedOrganicFractal(
    width=1600, height=1600, dpi=300,
    max_depth=10,
    num_main_branches=12,
    circle_density=0.8,
    spike_density=0.4,
    central_void_radius=100
)

fractal.generate_fractal(seed=42)
fractal.create_visualization('custom_fractal.png')
```

## Dependencies

- `numpy` - Numerical computations
- `matplotlib` - Plotting and visualization
- `random` - Random number generation
- `math` - Mathematical functions

## Installation

```bash
# Install dependencies
uv sync

# Run any of the fractal generators
uv run python organic_fractal.py
```

## Performance Tips

- **Interactive Mode**: Use lower DPI (100) for real-time updates
- **High-Quality Output**: Use DPI 300+ for print-quality images
- **Large Images**: Increase width/height for detailed fractals
- **Complex Fractals**: Increase max_depth and num_main_branches

## Troubleshooting

### Common Issues

1. **Memory Usage**: Large fractals with high depth can use significant memory
2. **Rendering Time**: High DPI images take longer to generate
3. **Random Seeds**: Use fixed seeds for reproducible results

### Optimization

- Reduce `max_depth` for faster generation
- Lower `circle_density` and `spike_density` for simpler fractals
- Use smaller image dimensions for testing

## Future Enhancements

- Color variations and gradients
- Animation support
- 3D fractal generation
- Export to vector formats (SVG)
- Web-based interface

## License

This project is part of the random pattern generation collection.

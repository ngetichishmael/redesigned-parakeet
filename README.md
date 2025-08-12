# Conway's Game of Life Visualization

A Python implementation of Conway's Game of Life with animated visualization using matplotlib.

## Features

- **Animated Visualization**: Real-time display of the cellular automaton
- **Classic Patterns**: Includes glider, blinker, block, toad, and beacon patterns
- **Random Initialization**: Starts with a mix of predefined patterns and random cells
- **Customizable Grid**: Adjustable grid size and animation speed
- **Professional Display**: Clean grid layout with proper labeling

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the visualization:
```bash
python conway.py
```

## Controls

- The animation will start automatically
- Press `Ctrl+C` in the terminal to stop the animation
- Close the matplotlib window to exit

## Conway's Rules

1. **Underpopulation**: Any live cell with fewer than 2 live neighbors dies
2. **Survival**: Any live cell with 2 or 3 live neighbors lives
3. **Overpopulation**: Any live cell with more than 3 live neighbors dies
4. **Reproduction**: Any dead cell with exactly 3 live neighbors becomes alive

## Patterns Included

- **Glider**: A pattern that moves diagonally across the grid
- **Blinker**: A simple oscillator that alternates between horizontal and vertical
- **Block**: A still life pattern that remains unchanged
- **Toad**: An oscillator with a 2-period cycle
- **Beacon**: An oscillator that blinks on and off

## Customization

You can modify the `main()` function to:
- Change grid size by modifying `width` and `height` parameters
- Adjust animation speed by changing the `interval` parameter
- Add or remove patterns
- Change the number of random cells

## Dependencies

- `numpy`: For efficient array operations
- `matplotlib`: For visualization and animation




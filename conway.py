import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import random

class ConwayGameOfLife:
    def __init__(self, width=50, height=50):
        """Initialize the Conway's Game of Life with a random grid."""
        self.width = width
        self.height = height
        self.grid = np.random.choice([0, 1], size=(height, width), p=[0.85, 0.15])
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        
    def count_neighbors(self, row, col):
        """Count the number of live neighbors for a given cell."""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if (0 <= new_row < self.height and 
                    0 <= new_col < self.width and 
                    self.grid[new_row][new_col] == 1):
                    count += 1
        return count
    
    def update_grid(self):
        """Update the grid according to Conway's Game of Life rules."""
        new_grid = np.zeros((self.height, self.width), dtype=int)
        
        for row in range(self.height):
            for col in range(self.width):
                neighbors = self.count_neighbors(row, col)
                
                # Conway's rules:
                # 1. Any live cell with fewer than 2 live neighbors dies (underpopulation)
                # 2. Any live cell with 2 or 3 live neighbors lives
                # 3. Any live cell with more than 3 live neighbors dies (overpopulation)
                # 4. Any dead cell with exactly 3 live neighbors becomes alive (reproduction)
                
                if self.grid[row][col] == 1:  # Live cell
                    if neighbors == 2 or neighbors == 3:
                        new_grid[row][col] = 1
                else:  # Dead cell
                    if neighbors == 3:
                        new_grid[row][col] = 1
        
        self.grid = new_grid
        return self.grid
    
    def draw_grid(self):
        """Draw the current state of the grid."""
        self.ax.clear()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.set_title('Conway\'s Game of Life', fontsize=16, fontweight='bold')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        
        # Draw live cells as black squares
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 1:
                    rect = Rectangle((col, self.height - 1 - row), 1, 1, 
                                   facecolor='black', edgecolor='gray', linewidth=0.5)
                    self.ax.add_patch(rect)
        
        # Add grid lines
        self.ax.grid(True, which='both', color='lightgray', linewidth=0.5)
        self.ax.set_xticks(range(0, self.width + 1, 5))
        self.ax.set_yticks(range(0, self.height + 1, 5))
    
    def animate(self, frame):
        """Animation function for matplotlib."""
        self.update_grid()
        self.draw_grid()
        return []
    
    def run_animation(self, frames=100, interval=200):
        """Run the animated visualization."""
        self.draw_grid()
        anim = animation.FuncAnimation(self.fig, self.animate, 
                                     frames=frames, interval=interval, 
                                     repeat=True, blit=False)
        plt.tight_layout()
        plt.show()
        return anim
    
    def add_pattern(self, pattern, start_row, start_col):
        """Add a specific pattern to the grid at the given position."""
        pattern_height, pattern_width = pattern.shape
        for i in range(pattern_height):
            for j in range(pattern_width):
                if (start_row + i < self.height and 
                    start_col + j < self.width):
                    self.grid[start_row + i][start_col + j] = pattern[i][j]
    
    def clear_grid(self):
        """Clear the entire grid."""
        self.grid = np.zeros((self.height, self.width), dtype=int)

# Predefined patterns
def create_glider():
    """Create a glider pattern."""
    return np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])

def create_blinker():
    """Create a blinker pattern."""
    return np.array([
        [1, 1, 1]
    ])

def create_block():
    """Create a still life block pattern."""
    return np.array([
        [1, 1],
        [1, 1]
    ])

def create_toad():
    """Create a toad pattern."""
    return np.array([
        [0, 1, 1, 1],
        [1, 1, 1, 0]
    ])

def create_beacon():
    """Create a beacon pattern."""
    return np.array([
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ])

def main():
    """Main function to run the Conway's Game of Life visualization."""
    print("Conway's Game of Life Visualization")
    print("=" * 40)
    
    # Create the game
    game = ConwayGameOfLife(width=60, height=60)
    
    # Add some interesting patterns
    game.add_pattern(create_glider(), 10, 10)
    game.add_pattern(create_blinker(), 20, 20)
    game.add_pattern(create_block(), 30, 30)
    game.add_pattern(create_toad(), 40, 40)
    game.add_pattern(create_beacon(), 50, 50)
    
    # Add some random cells for variety
    for _ in range(100):
        row = random.randint(0, game.height - 1)
        col = random.randint(0, game.width - 1)
        game.grid[row][col] = 1
    
    print("Starting animation... Press Ctrl+C to stop")
    print("Patterns included: Glider, Blinker, Block, Toad, Beacon, and random cells")
    
    # Run the animation
    try:
        game.run_animation(frames=200, interval=150)
    except KeyboardInterrupt:
        print("\nAnimation stopped by user")

if __name__ == "__main__":
    main()


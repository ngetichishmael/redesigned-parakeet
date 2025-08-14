#!/usr/bin/env python3
"""
Asili Logo Generator
Creates a mandala-like design with concentric rings featuring geometric patterns
in traditional African-inspired colors (red, green, gold) against a black background.
"""

from PIL import Image, ImageDraw
import math
import random

class AsiliLogo:
    def __init__(self, size=800, background_color=(0, 0, 0)):
        self.size = size
        self.center = size // 2
        self.background_color = background_color
        self.colors = {
            'red': (139, 0, 0),      # Dark red
            'green': (34, 139, 34),  # Forest green
            'gold': (218, 165, 32)   # Golden rod
        }
        
    def create_image(self):
        """Create the main image with black background"""
        self.image = Image.new('RGB', (self.size, self.size), self.background_color)
        self.draw = ImageDraw.Draw(self.image)
        
    def draw_central_circle(self, radius=20):
        """Draw the central black circle"""
        x1 = self.center - radius
        y1 = self.center - radius
        x2 = self.center + radius
        y2 = self.center + radius
        self.draw.ellipse([x1, y1, x2, y2], fill=(0, 0, 0))
        
    def draw_ring_pattern_1(self, inner_radius, outer_radius, color):
        """Ring 1: Small intricate patterns (squares, dots, lines)"""
        pattern_size = 3
        spacing = 8
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            pattern_type = random.choice(['square', 'dot', 'line'])
            
            if pattern_type == 'square':
                x1, y1 = x - pattern_size, y - pattern_size
                x2, y2 = x + pattern_size, y + pattern_size
                self.draw.rectangle([x1, y1, x2, y2], fill=color)
            elif pattern_type == 'dot':
                self.draw.ellipse([x-2, y-2, x+2, y+2], fill=color)
            else:  # line
                x2 = x + pattern_size * math.cos(rad + math.pi/4)
                y2 = y + pattern_size * math.sin(rad + math.pi/4)
                self.draw.line([x, y, x2, y2], fill=color, width=1)
                
    def draw_ring_pattern_2(self, inner_radius, outer_radius, color):
        """Ring 2: Inverted U shapes/arches"""
        arch_width = 6
        arch_height = 4
        spacing = 15
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw inverted U shape
            points = [
                (x - arch_width, y),
                (x - arch_width, y - arch_height),
                (x + arch_width, y - arch_height),
                (x + arch_width, y)
            ]
            self.draw.line(points, fill=color, width=2)
            
    def draw_ring_pattern_3(self, inner_radius, outer_radius, color):
        """Ring 3: Interconnected triangles (zigzag)"""
        triangle_size = 5
        spacing = 12
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw triangle pointing outward
            points = [
                (x, y - triangle_size),
                (x - triangle_size, y + triangle_size),
                (x + triangle_size, y + triangle_size)
            ]
            self.draw.polygon(points, fill=color)
            
    def draw_ring_pattern_4(self, inner_radius, outer_radius, color):
        """Ring 4: Short parallel vertical lines"""
        line_length = 8
        line_width = 2
        spacing = 10
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw vertical line
            x1, y1 = x - line_width//2, y - line_length//2
            x2, y2 = x + line_width//2, y + line_length//2
            self.draw.rectangle([x1, y1, x2, y2], fill=color)
            
    def draw_ring_pattern_5(self, inner_radius, outer_radius, color):
        """Ring 5: Flowing wavy/squiggly line"""
        radius = (inner_radius + outer_radius) // 2
        points = []
        
        for angle in range(0, 360, 2):
            rad = math.radians(angle)
            wave_offset = 3 * math.sin(angle * 0.1)
            r = radius + wave_offset
            
            x = self.center + r * math.cos(rad)
            y = self.center + r * math.sin(rad)
            points.append((x, y))
            
        if len(points) > 1:
            self.draw.line(points, fill=color, width=2)
            
    def draw_ring_pattern_6(self, inner_radius, outer_radius, color):
        """Ring 6: Repeating elongated S shapes"""
        s_width = 8
        s_height = 6
        spacing = 20
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw S shape
            points = [
                (x - s_width//2, y - s_height//2),
                (x + s_width//2, y - s_height//2),
                (x + s_width//2, y),
                (x - s_width//2, y),
                (x - s_width//2, y + s_height//2),
                (x + s_width//2, y + s_height//2)
            ]
            self.draw.line(points, fill=color, width=2)
            
    def draw_ring_pattern_7(self, inner_radius, outer_radius, color):
        """Ring 7: Repeating elongated U shapes"""
        u_width = 10
        u_height = 8
        spacing = 25
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw U shape
            points = [
                (x - u_width//2, y - u_height//2),
                (x - u_width//2, y + u_height//2),
                (x + u_width//2, y + u_height//2),
                (x + u_width//2, y - u_height//2)
            ]
            self.draw.line(points, fill=color, width=2)
            
    def draw_ring_pattern_8(self, inner_radius, outer_radius, color):
        """Ring 8: Small irregular shapes (squares, crosses)"""
        shape_size = 4
        spacing = 12
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            shape_type = random.choice(['square', 'cross'])
            
            if shape_type == 'square':
                x1, y1 = x - shape_size, y - shape_size
                x2, y2 = x + shape_size, y + shape_size
                self.draw.rectangle([x1, y1, x2, y2], fill=color)
            else:  # cross
                self.draw.line([x-shape_size, y, x+shape_size, y], fill=color, width=2)
                self.draw.line([x, y-shape_size, x, y+shape_size], fill=color, width=2)
                
    def draw_ring_pattern_9(self, inner_radius, outer_radius, color):
        """Ring 9: Repeating triangles (larger zigzag)"""
        triangle_size = 8
        spacing = 18
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw larger triangle
            points = [
                (x, y - triangle_size),
                (x - triangle_size, y + triangle_size),
                (x + triangle_size, y + triangle_size)
            ]
            self.draw.polygon(points, fill=color)
            
    def draw_ring_pattern_10(self, inner_radius, outer_radius, color):
        """Ring 10: Short, thick parallel vertical lines"""
        line_length = 12
        line_width = 4
        spacing = 15
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw thick vertical line
            x1, y1 = x - line_width//2, y - line_length//2
            x2, y2 = x + line_width//2, y + line_length//2
            self.draw.rectangle([x1, y1, x2, y2], fill=color)
            
    def draw_ring_pattern_11(self, inner_radius, outer_radius, color):
        """Ring 11: Swirling/spiral shapes (stylized eyes)"""
        spiral_size = 6
        spacing = 20
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw spiral shape
            points = []
            for i in range(8):
                spiral_rad = rad + i * 0.5
                spiral_r = spiral_size * (1 - i/8)
                px = x + spiral_r * math.cos(spiral_rad)
                py = y + spiral_r * math.sin(spiral_rad)
                points.append((px, py))
                
            if len(points) > 1:
                self.draw.line(points, fill=color, width=2)
                
    def draw_ring_pattern_12(self, inner_radius, outer_radius, color):
        """Ring 12: Repeating square spirals/labyrinth shapes"""
        spiral_size = 8
        spacing = 25
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw square spiral
            points = []
            for i in range(4):
                offset = spiral_size * (1 - i/4)
                if i == 0:
                    points.extend([(x-offset, y-offset), (x+offset, y-offset)])
                elif i == 1:
                    points.extend([(x+offset, y-offset), (x+offset, y+offset)])
                elif i == 2:
                    points.extend([(x+offset, y+offset), (x-offset, y+offset)])
                else:
                    points.extend([(x-offset, y+offset), (x-offset, y-offset)])
                    
            if len(points) > 1:
                self.draw.line(points, fill=color, width=2)
                
    def draw_ring_pattern_13(self, inner_radius, outer_radius, color):
        """Ring 13: Another ring of short, thick parallel vertical lines"""
        self.draw_ring_pattern_10(inner_radius, outer_radius, color)
        
    def draw_ring_pattern_14(self, inner_radius, outer_radius, color):
        """Ring 14: Long, thin parallel vertical lines"""
        line_length = 20
        line_width = 1
        spacing = 12
        
        for angle in range(0, 360, spacing):
            rad = math.radians(angle)
            radius = (inner_radius + outer_radius) // 2
            
            x = self.center + radius * math.cos(rad)
            y = self.center + radius * math.sin(rad)
            
            # Draw thin vertical line
            x1, y1 = x - line_width//2, y - line_length//2
            x2, y2 = x + line_width//2, y + line_length//2
            self.draw.rectangle([x1, y1, x2, y2], fill=color)
            
    def generate_logo(self):
        """Generate the complete logo"""
        self.create_image()
        
        # Define ring configurations: (inner_radius, outer_radius, color, pattern_function)
        rings = [
            (20, 40, self.colors['red'], self.draw_ring_pattern_1),
            (40, 60, self.colors['green'], self.draw_ring_pattern_2),
            (60, 80, self.colors['gold'], self.draw_ring_pattern_3),
            (80, 100, self.colors['red'], self.draw_ring_pattern_4),
            (100, 120, self.colors['green'], self.draw_ring_pattern_5),
            (120, 140, self.colors['gold'], self.draw_ring_pattern_6),
            (140, 160, self.colors['red'], self.draw_ring_pattern_7),
            (160, 180, self.colors['green'], self.draw_ring_pattern_8),
            (180, 200, self.colors['gold'], self.draw_ring_pattern_9),
            (200, 220, self.colors['red'], self.draw_ring_pattern_10),
            (220, 240, self.colors['green'], self.draw_ring_pattern_11),
            (240, 260, self.colors['gold'], self.draw_ring_pattern_12),
            (260, 280, self.colors['red'], self.draw_ring_pattern_13),
            (280, 300, self.colors['green'], self.draw_ring_pattern_14),
        ]
        
        # Draw central circle
        self.draw_central_circle()
        
        # Draw each ring
        for inner_radius, outer_radius, color, pattern_func in rings:
            pattern_func(inner_radius, outer_radius, color)
            
        return self.image
        
    def save_logo(self, filename="asili_logo.png"):
        """Save the logo to a file"""
        self.image.save(filename)
        print(f"Logo saved as {filename}")

def main():
    """Main function to generate and save the logo"""
    print("Generating Asili Logo...")
    
    # Create logo with different sizes
    sizes = [400, 800, 1200]
    
    for size in sizes:
        logo = AsiliLogo(size=size)
        image = logo.generate_logo()
        filename = f"asili_logo_{size}.png"
        logo.save_logo(filename)
        
    print("Logo generation complete!")

if __name__ == "__main__":
    main()


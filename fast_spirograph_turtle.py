import turtle
import numpy as np
import time

def generate_spirograph_pattern_fast(a=2.0, b=5.0, c=0.5, freq1=13, freq2=12, freq3=45, num_points=1000):
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

def create_ultra_fast_turtle_animation(num_points=1000, delay=0.001, scale_factor=20):
    """
    Create ultra-fast turtle animation with minimal delay and optimized drawing
    """
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Ultra Fast Spirograph Animation - Ish")
    screen.tracer(0)  # Turn off animation for faster drawing
    
    # Create turtle
    artist = turtle.Turtle()
    artist.speed(0)  # Fastest speed
    artist.color("white")
    artist.pensize(1)
    artist.hideturtle()
    
    # Generate pattern data
    print("Generating spirograph pattern...")
    x, y = generate_spirograph_pattern_fast(num_points=num_points)
    
    # Scale the coordinates to fit the screen
    x_scaled = x * scale_factor
    y_scaled = y * scale_factor
    
    # Animation parameters
    step = max(1, len(x) // 200)  # Only 200 frames max for speed
    current_frame = 0
    max_frames = len(x) // step
    
    def animate():
        nonlocal current_frame
        
        if current_frame < max_frames:
            # Clear previous drawing
            artist.clear()
            
            # Calculate end index for current frame
            end_idx = min((current_frame + 1) * step, len(x))
            
            # Draw the spirograph up to current frame
            if end_idx > 0:
                # Move to starting point without drawing
                artist.penup()
                artist.goto(x_scaled[0], y_scaled[0])
                artist.pendown()
                
                # Draw the pattern
                for i in range(1, end_idx):
                    artist.goto(x_scaled[i], y_scaled[i])
            
            # Add some dynamic elements at current position
            if end_idx > 0:
                current_x, current_y = x_scaled[end_idx-1], y_scaled[end_idx-1]
                
                # Draw a small circle at current position
                artist.penup()
                artist.goto(current_x, current_y - 3)
                artist.pendown()
                artist.color("lime")
                artist.begin_fill()
                artist.circle(3)
                artist.end_fill()
                artist.color("white")
            
            # Update screen
            screen.update()
            current_frame += 1
            
            # Schedule next frame
            screen.ontimer(animate, int(delay * 1000))  # Convert to milliseconds
        else:
            # Animation complete - restart
            current_frame = 0
            screen.ontimer(animate, int(delay * 1000))
    
    # Add formula text
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(-350, 350)
    text_turtle.color("white")
    text_turtle.write("z(t) = 2e^(i13t) + 5sin(12t)e^(it) + 0.5e^(i45t)", 
                     font=("Arial", 12, "normal"))
    
    # Add controls text
    text_turtle.goto(-350, 320)
    text_turtle.write("Press SPACE to toggle animation, ESC to exit", 
                     font=("Arial", 10, "normal"))
    
    # Animation control variables
    animation_running = True
    
    def toggle_animation():
        nonlocal animation_running
        animation_running = not animation_running
        if animation_running:
            animate()
    
    def exit_animation():
        screen.bye()
    
    # Bind keys
    screen.onkey(toggle_animation, "space")
    screen.onkey(exit_animation, "Escape")
    screen.listen()
    
    # Start animation
    print("Starting ultra-fast turtle animation...")
    print("Controls:")
    print("- SPACE: Toggle animation")
    print("- ESC: Exit")
    
    animate()  # Start the animation loop
    
    # Keep the window open
    try:
        screen.mainloop()
    except turtle.Terminator:
        pass

def create_static_turtle_spirograph(num_points=2000, scale_factor=20):
    """
    Create a static turtle spirograph for comparison
    """
    # Setup screen
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Static Spirograph - Ish")
    screen.tracer(0)  # Turn off animation for faster drawing
    
    # Create turtle
    artist = turtle.Turtle()
    artist.speed(0)
    artist.color("white")
    artist.pensize(1)
    artist.hideturtle()
    
    # Generate and draw pattern
    print("Generating and drawing static spirograph...")
    start_time = time.time()
    
    x, y = generate_spirograph_pattern_fast(num_points=num_points)
    x_scaled = x * scale_factor
    y_scaled = y * scale_factor
    
    # Draw the complete pattern
    artist.penup()
    artist.goto(x_scaled[0], y_scaled[0])
    artist.pendown()
    
    for i in range(1, len(x_scaled)):
        artist.goto(x_scaled[i], y_scaled[i])
    
    # Add some decorative elements
    # Mark key points
    idx1, idx2, idx3 = int(len(x) * 0.3), int(len(x) * 0.4), int(len(x) * 0.5)
    
    for idx in [idx1, idx2, idx3]:
        artist.penup()
        artist.goto(x_scaled[idx], y_scaled[idx] - 3)
        artist.pendown()
        artist.color("lime")
        artist.begin_fill()
        artist.circle(3)
        artist.end_fill()
        artist.color("white")
    
    # Connect points with green lines
    artist.color("lime")
    artist.penup()
    artist.goto(x_scaled[idx1], y_scaled[idx1])
    artist.pendown()
    artist.goto(x_scaled[idx2], y_scaled[idx2])
    artist.goto(x_scaled[idx3], y_scaled[idx3])
    
    # Add text
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(-350, 350)
    text_turtle.color("white")
    text_turtle.write("z(t) = 2e^(i13t) + 5sin(12t)e^(it) + 0.5e^(i45t)", 
                     font=("Arial", 12, "normal"))
    
    end_time = time.time()
    text_turtle.goto(-350, 320)
    text_turtle.write(f"Generated in {end_time - start_time:.3f} seconds", 
                     font=("Arial", 10, "normal"))
    
    screen.update()
    
    def exit_app():
        screen.bye()
    
    screen.onkey(exit_app, "Escape")
    screen.listen()
    
    print(f"Static spirograph completed in {end_time - start_time:.3f} seconds")
    print("Press ESC to exit")
    
    try:
        screen.mainloop()
    except turtle.Terminator:
        pass

if __name__ == "__main__":
    print("=== Ultra Fast Turtle Spirograph ===")
    print("1. Ultra-fast animation")
    print("2. Static pattern (for speed comparison)")
    
    choice = input("Choose option (1-2): ").strip()
    
    if choice == "1":
        create_ultra_fast_turtle_animation(num_points=1000, delay=0.005, scale_factor=25)
    elif choice == "2":
        create_static_turtle_spirograph(num_points=2000, scale_factor=25)
    else:
        print("Invalid choice. Running ultra-fast animation...")
        create_ultra_fast_turtle_animation(num_points=1000, delay=0.005, scale_factor=25)
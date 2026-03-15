'''
#Michael Pavicic
Please describe the scene you created in a sentence or two.
A house between two trees with a cat in the bottom left corner a pond in the bottom right and a sun in the top right corner.
'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


#YOU MUST add function calls in this draw_scence function defintion
# to create your scence (No statements outside of function definiions)
def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    #start of my code
    #landscape
    jump_to(t,-500,100)
    draw_square(t , 1000, "#145028")

    #drawing trees
    #left side tree
    jump_to(t,-325,200)
    draw_rectangle(t,50,150,"#8B4513")
    jump_to(t,-300,180)
    draw_circle(t,100,"#145028")
    #right side tree
    jump_to(t,275,200)
    draw_rectangle(t,50,150,"#8B4513")
    jump_to(t,300,180)
    draw_circle(t,100,"#145028")

    #sun
    jump_to(t,500,375)
    draw_circle(t,50,"yellow")

    #drawing house
    #main square
    jump_to(t,-100,200)
    draw_square(t,200,"#F5E09A")
    #roof
    draw_triangle(t,200,"#550808")
    #door
    jump_to(t,25,80)
    draw_rectangle(t,50,80,"#552B08")
    jump_to(t,70,30)
    draw_circle(t,4,"#000000")
    #window
    jump_to(t,-75,150)
    draw_square(t,50,"#19BEE7")

    #cat
    jump_to(t,-200,-350)
    draw_triangle(t,30, "#000000")
    jump_to(t,-185,-330)
    draw_circle(t,10,"#000000")
    jump_to(t,-194,-314)
    draw_triangle(t,9,"#000000")   
    jump_to(t,-185,-314)
    draw_triangle(t,9,"#000000")   

    #pond
    jump_to(t,500,-700)
    draw_circle(t,300,"#19BEE7")
    

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()
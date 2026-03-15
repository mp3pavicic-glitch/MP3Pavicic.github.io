'''
#Michael Pavicic
Please describe the scene you created in a sentence or two.
A house between two trees with a cat in the bottom left corner a pond in the bottom right and a sun in the top right corner.
The updated scene has three houses in the middle of a more fleshed out forest, a gang of cats (as well as one in a tree), and the previously mentioned pond and sun!

My changes to the code are as follows.  
First I cleaned up the functions so that they could be called at any position and the according adjustments so that when the objects are called it asks for the coordinates they should go to.
This was difficult due to how I initially programmed these functions and I had to figure out how much to offset each object within the function wherever the function was called to still build them in the same way.
I also added the ability to change the color of the cats within the scene. (Check the text for the final cat for an easter egg :) )
After that I added more objects those being four more trees, three cats and two houses.
I did not add another pond or sun as it did not fit the scene.
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
    jump_to(t,-1000,100)
    draw_square(t , 2000, "#145028")

    #drawing functions for scene objects

    #draw a tree at (x, y)
    def draw_tree(t, x, y):
        jump_to(t, x, y)
        draw_rectangle(t, 50, 150, "#8B4513")
        jump_to(t, x + 25, y - 20)
        draw_circle(t, 100, "#145028")

    #draw a sun at (x, y)
    def draw_sun(t, x, y):
        jump_to(t, x, y)
        draw_circle(t, 50, "yellow")

    #draw a house at (x, y) (starts atbottom left corner of house)
    def draw_house(t, x, y):
        #main square
        jump_to(t, x, y)
        draw_square(t, 200, "#F5E09A")
        #roof
        draw_triangle(t, 200, "#550808")
        #door
        jump_to(t, x + 125, y - 120)
        draw_rectangle(t, 50, 80, "#552B08")
        jump_to(t, x + 170, y - 170)
        draw_circle(t, 4, "#000000")
        #window
        jump_to(t, x + 25, y - 50)
        draw_square(t, 50, "#19BEE7")

    #draw a cat at (x, y) (bottom left of cat) with customizable color
    def draw_cat(t, x, y, color="#000000"):
        jump_to(t, x, y)
        draw_triangle(t, 30, color)
        jump_to(t, x + 15, y + 20)
        draw_circle(t, 10, color)
        jump_to(t, x + 6, y + 36)
        draw_triangle(t, 9, color)
        jump_to(t, x + 15, y + 36)
        draw_triangle(t, 9, color)

    #draw a pond at (x, y) (center of pond)
    def draw_pond(t, x, y):
        jump_to(t, x, y)
        draw_circle(t, 300, "#19BEE7")

    #draw objects in the scene
    #original objects from project 2
    draw_tree(t, -325, 200)   # left tree
    draw_tree(t, 275, 200)    # right tree
    draw_sun(t, 500, 375)
    draw_house(t, -170, 300) #this house is new
    draw_house(t, 70, 250)  #this house is also new
    draw_house(t, -100, 200)
    draw_cat(t, -200, -350)
    draw_pond(t, 500, -700)

    #these are all new objects added to the scene
    draw_tree(t, -500, 150) 
    draw_tree(t, -250, 100)
    draw_tree(t, 400, 150)
    draw_cat(t, 250, 270, "#FFFFFF")
    draw_cat(t, -220, -360, "#838383")
    draw_cat(t, -180, -355, "#F89C24") #Oro aka my cat :)
    draw_tree(t, 250, 100)

# This is the main() function that starts off the execution
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()

# if this script is executed, call the main() function
# meaning when is file is run directly
if __name__ == "__main__":
    main()
from turtle import *

#change color!!!!!
#hill = input("#006400")
#could not use color inside a variable

#background color is changed to either day or night and what you see in the sky will change too
import random 
time=random.randint(1,2)
if time <= 1:
    #night
    bgcolor("#17035E")
    #star!
    teleport(350,340)
    pencolor("#FFFF00")
    fillcolor("#FFFF00")
    begin_fill()
    points = 1
    while points < 6:
        forward(38)
        penup()
        forward(24)
        pendown()
        forward(38)
        left(144)
        points = points + 1
    end_fill()
    setheading(0)
    forward(38)
    begin_fill()
    for i in range(5):
        forward(24)
        left(72)
    end_fill()
else:
    #daytime!
    bgcolor("#00FFFF")
    teleport(-450,300)
    pencolor("#FFFF00")
    fillcolor("#FFFF00")
    begin_fill()
    circle(100)
    end_fill()

setheading(0)
speed(10000)

#making hills
teleport(-510,-100)
fillcolor("#006400")
pencolor("#006400")
begin_fill()
#variables to change hills easily
shift=0.7
move=1

for i in range(4):
    def curve():
        for i in range(75):
            right(shift)
            forward(move)

    curve()
    def curve():
        for i in range(75):
            left(shift)
            forward(move)

    curve()
    def curve():
        for i in range(75):
            left(shift)
            forward(move)

    curve()

    def curve():
        for i in range(75):
            right(shift)
            forward(move)

    curve()
right(90)
forward(400)
right(90)
forward(1040)
right(90)
forward(400)
end_fill()
#end of hills

setheading(0)

#tree!
teleport(350,-200)
pencolor("#8B4513")
fillcolor("#8B4513")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()
pencolor("#006400")
fillcolor("#006400")
teleport(400,-20)
begin_fill()
circle(135)
end_fill()
#end of tree

setheading(0)

pencolor("#000000")
#house
teleport(-150,-200)
def draw(num_sides, side, fill_color):

    color(fill_color)

    begin_fill()
    for i in range(num_sides):
        forward(side)
        angle =360/num_sides
        left(angle)
    end_fill
draw(4, 300, "#696969")
#roof
teleport(-150,100)
draw(3,300, "#000000")
#window
teleport(80,-60)
draw(4, 60, "#191970")
#door
teleport(-130,-200)
pencolor("#000000")
fillcolor("#8B4513")
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(200)
    left(90)
end_fill()
#end of house



done()
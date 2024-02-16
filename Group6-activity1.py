"""
Group6-activity1.py

Name of group members: Mohammad, Faisal, Khadija

Contribution of each member:

Collectively we all contributed in the patterns function, and main function

Mohammad: Square functions, comments and docstrings

Faisal: Circle functions

Khadija: Hexagon functions, x and y coordinates, and setPos functions

Describtion:
The code creates an interactive program where users can input colors for shapes,
and it generates a pattern of hexagons, circles, and squares arranged in three rows, 
each with three repetitions of the shapes.
"""
from turtle import Turtle, Screen # This allows us to draw with a turtle on a screen.
import turtle as turta # This gives the name turta to the turtle.

def setPos( x, y):
    """
    Set the position of the turtle without leaving any trace.

    Args:
        turta (turtle.Turtle): The turtle object.
        x (int): x-coordinate for the position.
        y (int): y-coordinate for the position.
    """
    turta.penup()
    turta.home()
    turta.goto(x, y)
    turta.pendown()


def hexagon(turta, hexa_color, border_color):
    """
    Draw a hexagon filled with hexa_color and borders of border_color.
    
    turta (turtle.Turtle): The turtle object.
    
    hexa_color: Color to fill the hexagon.
    
    border_color: Color for borders.
    
    turta.pensize(3) sets the width of the drawing pen
    """
    turta.pensize(3)
    side_length=(50)
    turta.pencolor(border_color)
    turta.fillcolor(hexa_color)
    turta.begin_fill()
    side_length = 50
    turta.forward(side_length)
    turta.right(60)
    turta.forward(side_length)
    turta.right(60)
    turta.forward(side_length)
    turta.right(60)
    turta.forward(side_length)
    turta.right(60)
    turta.forward(side_length)
    turta.right(60)
    turta.forward(side_length)
    turta.end_fill()




def circle(turta, circle_color, border_color):
    """
    Draw a circle filled with circ_color and borders of border_color.
    
    turta (turtle.Turtle): The turtle object.
    
    circ_color: Color to fill the circle.
    
    border_color: Color for borders.
    
    turta.pensize(3) sets the width of the drawing pen
    """
    turta.pensize(3)
    turta.fillcolor(circle_color)
    turta.pencolor(border_color)
    turta.begin_fill()
    turta.circle(48)
    turta.end_fill()

def square(turta, square_color, border_color):
    """
    Draw a square that is filled with square_color and has a border of border_color.
    
    turta (turtle.Turtle): The turtle object.

    square_color: The color that fills the square.

    border_color: Color for border.

    turta.pensize(3) sets the width of the drawing pen

    """
    turta.pensize(3)
    side_length= 90
    turta.pencolor(border_color)
    turta.fillcolor(square_color)
    turta.begin_fill()
    turta.forward(side_length)
    turta.right(90)
    turta.forward(side_length)
    turta.right(90)
    turta.forward(side_length)
    turta.right(90)
    turta.forward(side_length)
    turta.end_fill()

def pattern(turta, hexa_color, circle_color, square_color,border_color):
    """
    Each shape is called three times which determines that each shape should be drawn three times.

    setPos function is called to set the coordinates of both the x axis and the y axis for each of the shapes.
    """
    
    # First row Hexagon
    setPos(-210,140)
    hexagon(turta, hexa_color,border_color)
    
    # First row Circle
    setPos(-40,50)
    circle(turta, circle_color,border_color)
    
    # First row Square
    setPos(60,140)
    square(turta, square_color, border_color)
    
    # Second row Hexagon
    setPos(-140,-10)
    hexagon(turta, hexa_color,border_color)
    
    # Second row Circle
    setPos(30,-100)
    circle(turta, circle_color,border_color)
    
    # Second row Square
    setPos(150,0)
    square(turta, square_color, border_color)
    
    # Third row Hexagon
    setPos(-60,-140)
    hexagon(turta, hexa_color,border_color)
    
    # Third row Circle
    setPos(110,-230)
    circle(turta, circle_color,border_color)
    
    # Third row Square
    setPos(210,-140)
    square(turta, square_color, border_color)


def main():
    """
    turta.hideturtle() is called to hide the turtle cursor before drawing the shapes.
    
    turta.speed() is used to set the speed of the turta while drawing.

    turta.bgcolor() is used to set a backgroung color.

    Four input functions are called that determine the color of each of the shapes and the border color of the shapes.

    pattern function is called which contains all the shapes and their structure.

    turta.done() finalizes the drawing.
    """

    turta.hideturtle() # Hides the turtle cursor, making it invisible during the drawing process.
    turta.speed('fast')
    turta.bgcolor('light blue')
    hexa_color= input('Enter the color for hexagon: ')
    circle_color= input('Enter the color for circle: ')
    square_color= input('Enter the color for square: ')
    border_color= input('Enter the color of shape borders: ')
    pattern(turta, hexa_color, circle_color, square_color, border_color)
    visual = Screen() # Creates a drawing screen.
    visual.exitonclick() # Closes the drawing screen when it is clicked.
    turta.done()
    
main()
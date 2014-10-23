"""
    \file turtlevisual.py
    \author Tatiana Bradley
    \brief Visualize some elliptic curves over prime fields
           using turtle graphics.
"""
from turtle import *
from primecurves import *
from randomcurve import *

PRIME = 71
LABEL_FREQUENCY = 5
LABEL_PADDING = 20
SCALE = 10
BUFFER = 200
POINT_RADIUS = 2
START_X = - ( PRIME + 2 * BUFFER)
START_Y = - ( PRIME + BUFFER)
TICK_LENGTH = 10

# Prelim commands
hideturtle()
speed(5)

# FUNCTIONS
def drawPoint(x, y, color = "black"):
    gotoPoint(x, y)
    pendown()
    dot(color)
    penup()

def toOrigin():
    penup()
    goto(START_X, START_Y)

def gotoPoint(x, y):
    xPos = START_X + x * SCALE
    yPos = START_Y + y * SCALE 
    penup()
    goto(xPos, yPos)

def drawPrimePoint(point, color = "black"):
    if not point.isInf():
        drawPoint(point.x.value, point.y.value, color)

def drawAxes(prime):
    toOrigin()
    drawXAxis(prime)
    toOrigin()
    drawYAxis(prime)
    toOrigin()

def drawVertTick(index):
    oldX = xcor()
    oldY = ycor()
    penup()
    goto(oldX, oldY + TICK_LENGTH / 2)
    pendown()
    goto(oldX, oldY - TICK_LENGTH / 2)
    markTick(270, index)
    goto(oldX, oldY)

def drawHorizTick(index):
    oldX = xcor()
    oldY = ycor()
    penup()
    goto(oldX + TICK_LENGTH / 2, oldY)
    pendown()
    goto(oldX - TICK_LENGTH / 2, oldY)
    markTick(180, index)
    penup()
    goto(oldX, oldY)

def markTick(angle, index):
    if index % LABEL_FREQUENCY == 0 or index == PRIME:
        penup()
        setheading(angle)
        forward(LABEL_PADDING)
        write(str(index))
    
def drawXAxis(end):
    for i in range(end):
        pendown()
        goto(START_X + i * SCALE, START_Y)
        drawVertTick(i)
        
def drawYAxis(end):
    for i in range(end):
        pendown()
        goto(START_X, START_Y + i * SCALE)
        drawHorizTick(i)

def drawListOfPoints(points):
    for point in points:
        drawPrimePoint(point)

def labelPoint(point, label):
    if not point.isInf():
        gotoPoint(point.x.value + .5, point.y.value)
        pd()
        write(str(label))
        pu()

def highlightPoint(point, index):
    drawPrimePoint(point, "red")
    labelPoint(point, index)

def drawRandomCurve(prime):
    Seed, E = generateRandomCurve(prime)
    E.getAllPoints()
    drawAxes(E.prime)
    drawListOfPoints(E.allPoints)

""" Draw the example from Smart's
    paper. Note that there is
    a change of variables... """
def drawSmartCurve():
    E = PrimeCurve(17, 36, 43)
    E.getAllPoints()
    P = PrimePoint(38, 16, E)
    drawAxes(E.prime)
    drawListOfPoints(E.allPoints)
    multiples = P.getMultiples(16)
    for i in range(len(multiples)):
        point = multiples[i]
        highlightPoint(point, i)
    print E.getOrder()
    

# COMMANDS
toOrigin()
#drawSmartCurve()
drawRandomCurve(PRIME)
    
# Exit on click
exitonclick()
    
    
    

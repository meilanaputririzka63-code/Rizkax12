# Python program to draw patterns using Turtle
# using Turtle Programming
import turtle #Outside_in
import turtle
import time
import random

print("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the number of sides of the shape: ")
if not num_str.isdigit():
       squares = int(num_str)

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0
y = 0
turtle.setpos(x, y)


numshapes = 8
for j in range(numshapes):
    turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    turtle.forward(x)
    turtle.left(y)
    for i in range(squares):
        turtle.begin_fill()
        turtle.down()
        turtle.forward(40)
        turtle.left(angle)
        turtle.forward(40)
        print (turtle.pos())
        turtle.up()
        turtle.end_fill()

time.sleep(11)
turtle.bye()
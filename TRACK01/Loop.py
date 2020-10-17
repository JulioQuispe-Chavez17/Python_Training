#COMMNET
import turtle

cesar_turtle = turtle.Turtle()
cesar_turtle.speed(1000)
def square():
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)

for i in range(5):
    square()
    
import turtle

cesar_turtle = turtle.Turtle()
def square():
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)
    cesar_turtle.right(90)
    cesar_turtle.forward(100)

elephant_weights = 3000
ant_weights = 0.1

if(elephant_weights < ant_weights):
    square()
else:
    cesar_turtle.forward(100)
print(3000 > 0.1)
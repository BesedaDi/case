import turtle

def triangle(x, y, a, b, color):
 turtle.up()
turtle.setposition(x, y)
turtle.down()
turtle.color(color)
turtle.begin_fill()
turtle.forward(a)
turtle.right(90)
turtle.forward(a)
turtle.right(135)
turtle.forward(b)
turtle.end_fill()

def main():
    triangle(0, 0, 90, 160, 'red')


    turtle.done()
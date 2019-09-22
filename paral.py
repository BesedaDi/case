import turtle

def parallogram(x, y, a1, b1, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a1)
    turtle.right(60)
    turtle.forward(b1)
    turtle.right(120)
    turtle.forward(a1)
    turtle.end_fill()

def main():
    parallogram(0, 0, 90, 160, 'red')

    turtle.done()


main()
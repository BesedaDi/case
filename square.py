def square(x,y, a3, color):
# TODO: (A) Paint  a square.
  turtle.up()
 turtle.setposition(x, y)
turtle.down()
turtle.color(color)
turtle.begin_fill()
turtle.forward(a3)
turtle.right(90)
turtle.forward(a3)
turtle.right(90)
turtle.forward(a3)
turtle.right(90)
turtle.forward(a3)
turtle.right(90)
turtle.end_fill()
pass
def main():
    square(0, 0, 'red')
pass
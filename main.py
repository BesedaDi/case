# Case-study #1
# Developers:   Besedina D. (%),
#               Zaitseva A. (%),
#               Kuzmin E. (%)
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

pass

def parallelogram(x, y, a1, b1, color):
     # TODO: (E) Paint a parallelogram.
pass

def square(x, y, a, color):
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.color(color)
        turtle.begin_fill()
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.end_fill()

    pass

def figure1():
     # TODO: (D) Paint a figure1.
pass

def figure2():
     # TODO: (D) Paint a figure2.
pass

def figure3():
     # TODO: (D) Paint a figure3.
pass

def figure4():
     # TODO: (E) Paint a figure4.
pass

def figure5():
     # TODO: (E) Paint a figure5.
pass

def figure6():
     # TODO: (E) Paint a figure6.
pass

def figure7():
     # TODO: (A) Paint a figure7.
pass

def figure8():
     # TODO: (A) Paint a figure8.
pass

def figure9():
     # TODO: (A) Paint a figure9.
pass

def main():
    triangle(-200, 200, 180, 260, 'red')
    turtle.done()

    pass
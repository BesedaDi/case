# Case-study #1
# Developers:   Besedina D. (%),
#               Zaitseva A. (%),
#               Kuzmin E. (%)
import turtle




 def triangle(x, y, a, b, color):
     # TODO: (D) Paint a triangle.

     '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :param b: side length of the diagonal of the triangle
    :return: None
    '''

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

def square(x,y, a3):
#TODO: (A) Paint  a square.
    pass



def main():
    triangle(-200, 200, 180, 260, 'red')
    turtle.done()

    pass
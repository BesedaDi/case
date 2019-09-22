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


def square(x, y, a, color):
    '''
        Function, drawing square.
        :param x: upper left corner coordinate x
        :param y: upper left corner coordinate y
        :param a: side length of a square
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
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
pass

def parallel(x, y, a, color):
    # Параллелограмм
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.up()
    turtle.end_fill()

pass


def main():
    turtle.hideturtle()
    parallel(-585, 330, 25, 'green')
    turtle.right(120)
    square(-560, 305, 25, 'orange')
    turtle.right(90)
    triangle(-563, 295, 60, 70, 'red')
    turtle.right(-45)
    triangle(-623, 172, 60, 70, 'yellow')
    turtle.left(45)
    triangle(-570, 220, 50, 60, 'blue')
    turtle.right(225)
    triangle(-537, 170, 30, 40, 'pink')
    turtle.right(360)
    triangle(-560, 255, 30, 40, 'gray')
    turtle.right(90)
    parallel(-450, 280, 25, 'green')
    turtle.right(30)
    triangle(-432, 235, 20, 30, 'purple')
    turtle.left(45)
    triangle(-435, 255, 20, 30, 'blue')
    turtle.left(180)
    square(-368, 257, 30, 'orange')
    turtle.left(45)
    triangle(-366, 254, 60, 70, 'red')
    turtle.right(45)
    triangle(-425, 319, 60, 70, 'pink')
    turtle.left(180)
    triangle(-360, 288, 40, 50, 'gold')
    turtle.right(90)
    parallel(-250, 270, 55, 'green')
    

    turtle.done()

if __name__ == '__main__':
    main()
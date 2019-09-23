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
    parallel(-250, 270, 55, 'white')

    turtle.right(75)
    triangle(400, -100, 40, 50, 'pink')
    turtle.left(180)
    triangle(400, -105, 55, 50, 'blue')
    turtle.left(180)
    triangle(400, -110, 75, 50, 'yellow')
    turtle.left(45)
    triangle(455, -275, 75, 50, 'red')
    turtle.left(45)
    square(400, -225, 40, 'orange' )
    turtle.left(180)
    turtle.left(180)
    triangle(370, -260, 40, 50, 'pink')
    turtle.left(60)
    parallel(492, -295, 40, 'green')

    turtle.right(225)
    triangle(175, -100, 50, 50, 'pink')
    turtle.right(120)
    parallel(250, -100, 30, 'green')
    turtle.right(225)
    triangle(250, -105, 90, 50, 'red')
    turtle.left(45)
    triangle(245, -230, 90, 50, 'yellow')
    turtle.left(135)
    triangle(140, -210, 55, 50, 'blue')
    turtle.left(45)
    triangle(175, -170, 55, 50, 'pink')
    turtle.left(45)
    square(65, -155, 30, 'orange')

    turtle.right(90)
    triangle(-80, -40, 90, 50, 'red')
    turtle.right(45)
    square(-44, -136, 43, 'orange')
    turtle.right(0)
    triangle(-79, -170, 45, 50, 'purple')
    turtle.right(315)
    triangle(-18, -173, 70, 90, 'blue')
    turtle.left(10)
    parallel(-170, -183, 70, 'green')
    turtle.left(140)
    triangle(-85, -70, 90, 50, 'yellow')
    triangle(-79, -170, 45, 50, 'purple')


    turtle.done()

if __name__ == '__main__':
    main()
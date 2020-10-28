import turtle


def jump(turtleagain, x, y):
    turtleagain.penup()
    turtleagain.setpos(x, y)
    turtleagain.pendown()


def olimpiadas(turtle):
    # jump(t, 10, 10)
    turtle.circle(30)
    jump(t, 35, -30)
    turtle.circle(30)
    jump(t, 70, 0)
    turtle.circle(30)
    jump(t, 105, -30)
    turtle.circle(30)
    jump(t, 140, 0)
    turtle.circle(30)


s = turtle.Screen()
t = turtle.Turtle()
olimpiadas(t)
input('Pressione uma tecla para terminar...')
# Implemente a função olimpiadas(t) que faz com que a tartaruga desenha o simbolo das olimpiadas (5 aneis entrelaçados).
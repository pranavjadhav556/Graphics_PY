import turtle
colors = ['orange', 'blue', 'red', 'brown', 'green', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x//100 + 10)
    t.forward(100)
    t.left(angle=100)

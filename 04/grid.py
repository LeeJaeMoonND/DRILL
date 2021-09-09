import turtle as t

countX=5
countY=5

while(countY>=0):
    t.penup()
    t.goto(0,100*countY)
    t.pendown()
    t.forward(500)
    countY=countY-1

t.right(90)

while(countX>=0):
    t.penup()
    t.goto(100*countX,500)
    t.pendown()
    t.forward(500)
    countX=countX-1

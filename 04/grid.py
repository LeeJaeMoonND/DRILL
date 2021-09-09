import turtle as t

countX=5
countY=5

while(countY>=0):
    t.penup()
    t.goto(100,100*countY)
    t.pendown()
    t.forward(500)
    countY=countY-1
    

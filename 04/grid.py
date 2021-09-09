import turtle as t

countX=5
countY=5

#가로 축 그리기

while(countY>=0):
    t.penup()
    t.goto(-250,(100*countY)-250)
    t.pendown()
    t.forward(500)
    countY=countY-1
t.right(90) 

#세로 축 그리기
while(countX>=0):
    t.penup()
    t.goto((100*countX)-250,250)
    t.pendown()
    t.forward(500)
    countX=countX-1

t.exitonclick() #클릭 전까지 안꺼짐

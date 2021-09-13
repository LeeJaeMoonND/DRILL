#2017152030 이재문
#https://youtu.be/f5lDu4yP5zA 유튜브 링크 추가

import turtle

#터틀의 왼쪽 움직임
def turtle_Left():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

#터틀의 오른쪽 움직임
def turtle_Right():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

#터틀의 상 움직임
def turtle_Up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

#터틀의 하 움직임
def turtle_Down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()


#리셋 함수
def reset_turtle():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_Left,'d')
turtle.onkey(turtle_Right,'a')
turtle.onkey(turtle_Up,'w')
turtle.onkey(turtle_Down,'s')
turtle.onkey(reset_turtle,'Escape')
turtle.listen()


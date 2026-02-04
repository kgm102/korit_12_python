import turtle

# 화면 설정
screen = turtle.Screen()
screen.setup(width=500, height=500)

# 거북이 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("red") # 선 색상

# 동그라미 그리기 (반지름이 100인 원)
t.circle(100)

# 클릭하면 종료
screen.exitonclick()
import turtle

# 定位
def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

goto(0, 0)
turtle.speed(100)
turtle.color("#F5E16F")
for i in range(20):
    # 顺时针移动18度
    turtle.right(18)
    turtle.begin_fill()
    # 向前移动的距离
    turtle.forward(220)
    # 画半径为 40 的半圆
    turtle.circle(40, 180)
    # 画完半圆之后回到（0，0）
    turtle.goto(0, 0)
    turtle.right(360)
    turtle.end_fill()
# 设置画笔粗细
turtle.pensize(20)
# 填充颜色（外部、内部）
turtle.color("#F5E16F", "#FF9933")
goto(0, -200)
# 准备开始填充
turtle.begin_fill()
turtle.circle(200)
# 填充结束
turtle.end_fill()
turtle.right(360)
turtle.color('#F5E16F')
goto(0, -180)
for i in range(12):
    turtle.begin_fill()
    turtle.circle(60, 120)
    turtle.left(180)
    turtle.circle(60, 120)
    turtle.end_fill()
turtle.right(50)
goto(-80, -50)
turtle.color("#F5E16F")
turtle.write("豆沙", font=("隶书", 60, "bold"))
turtle.hideturtle()
turtle.done()
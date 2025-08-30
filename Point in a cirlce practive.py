import turtle

x1, y1 = eval(input("Enter the center of a circle x,y: "))
radius = eval(input("Enter the radius of the circle: "))
x2, y2 = eval(input("Enter a point x, y: "))

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()

turtle.done()

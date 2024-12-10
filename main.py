import turtle
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('cornflower Blue')
t = turtle.Turtle()
t.write("Nasir Anderson", font=("Arial", 24, "bold"), align="center")

t.penup()
t.goto(0, -50)
t.pendown()

t.write("Turtle presentation Assignment", font=("Arial", 20, "bold"), align="center")

t.penup()
t.goto(0, -100)
t.pendown()
t.pensize(4)
t.circle(25)

t.penup()
turtle.addshape("legs5.gif")
t.shape("legs5.gif")
t.goto(-150,150)
a = t.stamp()

t.goto(150,-150)
turtle.addshape("flying.gif")
t.shape("flying.gif")
b = t.stamp()

enter = input("Press Enter to Start")
t.clear()
t.clearstamps()
t.hideturtle()

screen.bgcolor('Green')

t.goto(0,100)
t.write("My favorite foods", font=("Arial", 24, "bold"), align="center")

t.goto(-50, -50)

t.pendown()
t.pensize(3)
t.speed(3)


for _ in range(3):
    t.forward(100)
    t.left(120)
t.penup()

turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(-150,-150)
a = t.stamp()

t.goto(150,-150)
turtle.addshape("crab.gif")
t.shape("crab.gif")
b = t.stamp()
t.goto(0,0)

enter = input("Press Enter to go to next page")

t.clear()
t.clearstamps()
t.hideturtle()

screen.bgcolor('pink')

t.goto(0,100)
t.write("My Hobbies", font=("Arial", 24, "bold"), align="center")

t.goto(-50, -50)

t.pendown()
t.pensize(3)
t.speed(3)

for _ in range(4):
    t.forward(100)
    t.right(90)
t.penup()

turtle.addshape("bike.gif")
t.shape("bike.gif")
t.goto(-150,-150)
a = t.stamp()

t.goto(150,-150)
turtle.addshape("ps5.gif")
t.shape("ps5.gif")
b = t.stamp()
t.goto(0,0)

enter = input("Press Enter to go to next page")

t.clear()
t.clearstamps()
t.hideturtle()

screen.bgcolor('Dark red')

t.goto(0,100)
t.write("My Favorite food", font=("Arial", 24, "bold"), align="center")

t.goto(-50, -50)

t.pendown()
t.pensize(3)
t.speed(3)

for _ in range(8):
    t.forward(50)
    t.left(45)
t.penup()

turtle.addshape("rush.gif")
t.shape("rush.gif")
t.goto(-150,-150)
a = t.stamp()

t.goto(150,-150)
turtle.addshape("burger.gif")
t.shape("burger.gif")
b = t.stamp()
t.goto(0, 0)

enter = input("Press Enter to go to next page")

t.clear()
t.clearstamps()
t.hideturtle()

screen.bgcolor('coral')

t.goto(0,100)
t.write("My Favorite sports", font=("Arial", 24, "bold"), align="center")

t.goto(-50, -50)
t.pendown()

for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.left(90)

t.penup()
turtle.addshape("court.gif")
t.shape("court.gif")
t.goto(-150,-150)
a = t.stamp()

t.goto(150,-150)
turtle.addshape("track.gif")
t.shape("track.gif")
b = t.stamp()
t.goto(0, 0)















turtle.done()
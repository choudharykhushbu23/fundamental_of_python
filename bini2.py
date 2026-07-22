# import turtle
# import time

# screen = turtle.Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()

# # Moon
# t.penup()
# t.goto(250, 180)
# t.pendown()
# t.color("yellow")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# # Stars
# stars = [(-300,200),(-150,150),(0,220),(150,100),
#          (280,150),(-250,50),(100,250),(-50,120)]

# for x, y in stars:
#     t.penup()
#     t.goto(x, y)
#     t.dot(10, "white")

# # Moving star
# star = turtle.Turtle()
# star.shape("circle")
# star.color("white")
# star.shapesize(0.5)
# star.penup()
# star.speed(0)

# while True:
#     for x in range(-380, 381, 10):
#         star.goto(x, 250)
#         time.sleep(0.02)

#     star.goto(-380, 250)


# import turtle
# import time

# screen = turtle.Screen()
# screen.setup(800, 600)
# screen.bgcolor("black")
# screen.title("Night Animation")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()

# # Moon
# t.penup()
# t.goto(250, 180)
# t.pendown()
# t.color("yellow")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# # Stars
# stars = [(-300,200),(-150,150),(0,220),(150,100),
#          (280,150),(-250,50),(100,250),(-50,120)]

# for x, y in stars:
#     t.penup()
#     t.goto(x, y)
#     t.dot(10, "white")

# # Moving star
# star = turtle.Turtle()
# star.shape("circle")
# star.color("white")
# star.shapesize(0.5)
# star.penup()
# star.speed(0)

# while True:
#     for x in range(-380, 381, 10):
#         star.goto(x, 250)
#         time.sleep(0.02)

#     star.goto(-380, 250)



import turtle
import time

# Screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Night Animation")

# Good Night Text
text = turtle.Turtle()
text.hideturtle()
text.color("white")
text.penup()
text.goto(0, -250)
text.write("Good Night", align="center",
           font=("Arial", 24, "bold"))

# Moon
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
moon.penup()
moon.goto(250, 150)
moon.pendown()
moon.color("yellow")
moon.begin_fill()
moon.circle(50)
moon.end_fill()

# Stars
star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.penup()
star.color("white")

positions = [
    (-300,200), (-150,170), (0,220), (180,180),
    (300,220), (-250,80), (100,250), (-50,130)
]

for x, y in positions:
    star.goto(x, y)
    star.dot(8)

# Cloud
cloud = turtle.Turtle()
cloud.shape("circle")
cloud.color("white")
cloud.penup()
cloud.speed(0)

while True:
    for x in range(-420, 421, 5):
        cloud.goto(x, 120)
        time.sleep(0.02)
    cloud.goto(-420, 120)

turtle.done()
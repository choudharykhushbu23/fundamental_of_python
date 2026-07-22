# import turtle

# t = turtle.Turtle()

# t.speed(5)
# t.color("red")

# for i in range(5):
#     t.forward(150)
#     t.right(144)

# turtle.done()

# import turtle

# t = turtle.Turtle()

# # Movement
# t.forward(100)      # Move forward
# t.backward(50)      # Move backward
# t.left(90)          # Turn left
# t.right(90)         # Turn right
# t.goto(100, 100)    # Go to (x, y)
# t.home()            # Return to starting position

# # Pen Control
# t.penup()           # Lift pen
# t.pendown()         # Put pen down
# t.pensize(5)        # Pen thickness
# t.speed(5)          # Speed (1-10, 0 = fastest)

# # Colors
# t.color("red")      # Pen color
# t.fillcolor("blue") # Fill color

# # Shapes
# t.circle(50)        # Draw circle
# t.dot(20, "green")  # Draw dot

# # Filling
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()

# # Writing
# t.write("Hello", font=("Arial", 16, "bold"))

# # Hide/Show Turtle
# t.hideturtle()
# t.showturtle()

# # Clear Screen
# t.clear()

# # Reset Turtle
# t.reset()

# # Stamp
# t.stamp()

# # Background Color
# screen = turtle.Screen()
# screen.bgcolor("yellow")

# # Screen Title
# screen.title("Turtle Graphics")

# # Exit
# turtle.done()

# import turtle

# t = turtle.Turtle()
# screen = turtle.Screen()

# t.speed(0)          # Fastest speed
# t.width(2)

# colors = ["red", "blue", "green", "orange", "purple", "pink"]

# for i in range(72):
#     t.color(colors[i % 6])
#     t.circle(100)
#     t.left(5)

# turtle.done()

# import turtle

# t = turtle.Turtle()

# t.speed(0)

# for i in range(100):
#     t.circle(120)
#     t.left(10)

# turtle.done()

import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("pink")
t.speed(0)
t.width(4)

colors = ["red", "blue", "green", "orange", "purple", "pink", "cyan", "yellow"]

for i in range(72):
    t.pencolor(colors[i % len(colors)])
    t.circle(100)
    t.left(5)

t.hideturtle()
turtle.done()
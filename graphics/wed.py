import turtle

def draw_heart():
    turtle.begin_fill()
    turtle.color("red")
    turtle.left(140)
    turtle.forward(180)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(180)
    turtle.end_fill()

def write_message():
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.color("black")
    turtle.write("I LOVE U MY HALF...WILL U MARRY ME?", align="center", font=("Arial", 16, "bold"))

# Set up the screen
turtle.setup(600, 600)
turtle.bgcolor("white")
turtle.speed(3)

# Draw the heart and write the proposal
draw_heart()
write_message()

# Hide the turtle and finish
turtle.hideturtle()
turtle.done()

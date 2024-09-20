import turtle

# Set up the screen and turtle
screen = turtle.Screen()    # Create a screen
screen.bgcolor("lightblue")  # Set background color

t = turtle.Turtle()         # Create a turtle
t.color("red")              # Set turtle color to red
t.speed(3)                  # Set speed (1 slow, 10 fast)

# Draw heart
t.begin_fill()              # Start coloring
t.left(50)                  # Turn left
t.forward(133)              # Move forward
t.circle(50, 200)           # Draw left side of the heart
t.right(140)                # Turn right
t.circle(50, 200)           # Draw right side of the heart
t.forward(133)              # Move forward
t.end_fill()                # Finish coloring

# Write text
t.penup()                   # Lift pen (no drawing)
t.goto(-70, -150)           # Move to a new position
t.pendown()                 # Put pen down (start writing)
t.color("black")            # Set text color to black
t.write("I Love AMMA!", font=("Arial", 14, "bold"))  # Write message

# Hide the turtle and keep the window open
t.hideturtle()              # Hide turtle cursor
turtle.done()               # Keep window open

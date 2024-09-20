


#house pattern
import turtle

t = turtle.Turtle()

# Draw the base
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw the roof
t.right(45)
for _ in range(3):
    t.forward(70)
    t.right(90)

turtle.done()

#fflower pattern
import turtle

t = turtle.Turtle()
t.speed(0)  # Fastest speed

for i in range(36):
    t.circle(50)
    t.right(10)

turtle.done()

#square
import turtle

t = turtle.Turtle()

# Fixed loop with range(4) to iterate 4 times
for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()




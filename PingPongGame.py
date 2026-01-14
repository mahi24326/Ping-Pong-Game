# Ping-Pong

import turtle
import random
import pygame

myscreen = turtle.Screen()
myscreen.title("Ball Blash")
myscreen.bgcolor("black")
myscreen.setup(width=800, height=600)
myscreen.tracer(0)

# Background
def draw_stars():
    star_drawer = turtle.Turtle()
    star_drawer.hideturtle()
    star_drawer.penup()
    star_drawer.speed(0)
    star_drawer.color("white")
    for _ in range(30): 
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        star_drawer.goto(x, y)
        star_drawer.dot(random.randint(2, 6)) 

draw_stars()

#background music
pygame.mixer.init()

# Background music
# pygame.mixer.music.load("energetic-bgm-242515.mp3")  
# pygame.mixer.music.set_volume(0.5)  
# pygame.mixer.music.play(-1, 0.0)

# Scores
score_a = 0
score_b = 0

# Paddle A


# Ball
ball = turtle.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("salmon")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Ask for player names using popups
x = myscreen.textinput("Player Name", "Enter Player A's name:")
y = myscreen.textinput("Player Name", "Enter Player B's name:")

# Function to update the score display
def names_update():
    pen.clear()
    pen.write(f"{x}: {score_a}   {y}: {score_b}", align="center", font=("Courier", 24, "normal"))

# Initialize score display
names_update()

paddle_limit = 250
# Functions to move paddles


# Reduce paddle height
def shrink_paddle(paddle):
    current_size = paddle.shapesize()[0]
    if current_size > 1:  # Ensure the paddle doesn't disappear
        paddle.shapesize(stretch_wid=current_size - 0.5, stretch_len=1)

# Keyboard binding
myscreen.listen()
myscreen.onkeypress(paddle_a_up, "w")
myscreen.onkeypress(paddle_a_down, "s")
myscreen.onkeypress(paddle_b_up, "Up")
myscreen.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    myscreen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Top & bottom border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Side borders points
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        names_update()
        shrink_paddle(paddle_b)  # Player B loses a point, shrink their paddle
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        names_update()
        shrink_paddle(paddle_a)  # Player A loses a point, shrink their paddle
        
    # Paddle collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - paddle_b.shapesize()[0] * 10 < ball.ycor() < paddle_b.ycor() + paddle_b.shapesize()[0] * 10):
        ball.setx(340)
        ball.dx *= -1
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - paddle_a.shapesize()[0] * 10 < ball.ycor() < paddle_a.ycor() + paddle_a.shapesize()[0] * 10):
        ball.setx(-340)
        ball.dx *= -1


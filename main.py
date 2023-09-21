import turtle
from random import randint
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle!")
FONT = ('Arial', 30, 'normal')
score = 0
game_over = False

turtle_list = []

# Score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8

    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

setup_score_turtle()

def create_turtle(x, y):
    turtle_instance = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    turtle_instance.shapesize(1.5, 1.5)
    turtle_instance.speed(3)
    turtle_instance.shape('turtle')
    turtle_instance.color('green')
    turtle_instance.penup()
    turtle_instance.goto(x, y)
    turtle_instance.onclick(handle_click)
    turtle_list.append(turtle_instance)

def turtle_click():
    for _ in range(30):
        create_turtle(randint(-300, 300), randint(-250, 250))

def hide_turtles():
    for turtle_instance in turtle_list:
        turtle_instance.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    top_height= screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda : countdown(time -1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align= "center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    turtle_click()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()
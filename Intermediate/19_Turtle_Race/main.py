import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Dialog for user to place their prediction
user_bet = screen.textinput(title="Turtle Predictions",
                            prompt="Which colored turtle will win the race? Enter a color: ")

# Colors for the turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Starting y-position for each turtle
y_positions = [-120, -60, 0, 60, 120, 180]
# List of turtles
all_turtles = []

for turtle_index in range(0, 6):
    myTurtle = Turtle(shape="turtle")
    myTurtle.color(colors[turtle_index])
    myTurtle.penup()
    myTurtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(myTurtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet.lower():
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")

        # Randomize each turtle's distance traveled
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()

from turtle import Turtle,Screen
import random

race_ongoing = False
screen = Screen()
screen.setup(width=600,height=500)
answer = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(answer)
colors=['red','orange','yellow', 'green', 'blue', 'purple']
all_turtles=[]
if answer:
    race_ongoing=True


x = -280
y =  -70
for _ in colors:
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(_)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 30
    all_turtles.append(new_turtle)


while race_ongoing:
    for turtle in all_turtles:
        if turtle.xcor() > 260:
            race_ongoing = False
            winning_color= turtle.pencolor()
            if winning_color == answer:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        random_move = random.randint(0,10)
        turtle.forward(random_move)



screen.exitonclick()

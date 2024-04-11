from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
turtle = Turtle()

states = pd.read_csv("50_states.csv")
image = "blank_states_img.gif"

state_dict = states["state"].to_list()
total_state = len(states["state"])
score = 0
total_score = f"{score}/{total_state}"

screen.title(f"State Guessing Game | Score: {total_score}")


def state_selector(state_x, state_y, answer):
    turtle.hideturtle()
    turtle.penup()
    turtle.color("black")
    turtle.goto(state_x, state_y)
    turtle.write(answer, align='center', font=('Arial', 8, 'bold'))
    turtle.goto(0, 0)
    turtle.showturtle()


def update_score():
    screen.title(f"State Guessing Game | Score: {score}/{total_state}")


game_is_on = True

while game_is_on:
    screen.addshape(image)
    turtle.shape(image)

    answer = screen.textinput(title="Guess the State", prompt="What is the State Name?")

    if answer is None:
        break

    if answer.lower() == "exit":
        break

    for state_name in state_dict:
        if answer.lower() == state_name.lower():
            state_data = states[states["state"] == state_name]
            score += 1
            state_x = state_data["x"].values[0]
            state_y = state_data["y"].values[0]
            state_selector(state_x, state_y, answer)
            update_score()
            state_dict.remove(state_name)  # Remove the guessed state from the list
            break  # Exit the loop once a correct guess is made

    if score == total_state:
        screen.title("Congratulations! You guessed all the states!")
        break

screen.mainloop()






























































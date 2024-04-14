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

    state_data = next((states[states["state"] == state_name] for state_name in state_dict if answer.lower() == state_name.lower()), None)
    if state_data is not None:
        score += 1
        state_x, state_y = state_data.iloc[0]["x"], state_data.iloc[0]["y"]
        state_selector(state_x, state_y, answer)
        update_score()
        state_dict = [state for state in state_dict if state.lower() != answer.lower()]
    # Exit the loop once a correct guess is made

    if score == total_state:
        screen.title("Congratulations! You guessed all the states!")
        break

screen.mainloop()






























































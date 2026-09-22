import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Fetch data from states.csv file
states_df = pd.read_csv("50_states.csv")

# Fetch state names
states_df['state'] = states_df['state'].apply(lambda x: x.lower())

all_states = states_df.state.to_list()
states_guessed = []

while len(states_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").strip().lower()

    state_details = states_df[states_df.state == answer_state]

    if answer_state == "exit":
        # states_to_learn.csv
        states_to_learn = [state.title() for state in all_states if state not in states_guessed]
        # creating dataframe
        df = pd.DataFrame(states_to_learn, columns=["States_To_Learn"])
        df.to_csv("states_to_learn.csv", index=False)
        break

    if not state_details.empty and answer_state not in states_guessed:
        # Fetch coordinates based on state and answer_state match
        state_name = state_details['state'].item().title()
        x_cord = state_details['x'].item()
        y_cord = state_details['y'].item()

        states_guessed.append(answer_state)

        # new turtle to write the statename
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cord, y_cord)
        t.write(state_name, align="center", font=("Arial", 8, "normal"))




import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# load image as turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()
states_names = data.state.to_list()

def print_state(answer_state):

    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    x_cor = data.loc[data["state"] == answer_state, "x"].item()
    y_cor = data.loc[data["state"] == answer_state, "y"].item()
    state_turtle.goto(x_cor, y_cor)
    state_turtle.write(f"{answer_state}")

guessed_states = [] # save guess states to export as csv

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states) }/50 States Correct", prompt="What's another state's name?").lower()
    if answer_state == "exit":
        break
    if answer_state in data["state"].values:
        print("Correct")
        print_state(answer_state)
        guessed_states.append(answer_state)

# states to learn saved in csv file
missing_states = list(set(states_names) - set(guessed_states))
missing_states = pandas.DataFrame(missing_states)
missing_states.to_csv("states_to_learn.csv")


screen.exitonclick()

 

# If we needed to get the coordinates ourselves:
# # get coordinates of a click
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # keeps screen open


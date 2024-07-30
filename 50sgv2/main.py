# Game work is being done here
import turtle

import pandas as pd

from getcor import get_mouse_click_corr
from gamelogic import StateGuessGame

# Screen Setup
scr = turtle.Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("USBootyMap")
img = "bsg.gif"
scr.addshape(img)
turtle.shape(img)

# Loading the data into a dataframe
data = pd.read_csv('s50.csv')

# Initialize the game
game = StateGuessGame(scr, data)
game.start_game()

# --- Project Setup ---
# Getting the coordinates in the image
getMouseClick = get_mouse_click_corr  # This already done  s50.csv
# Using Main loop
# scr.exitonclick()
# turtle.mainloop()

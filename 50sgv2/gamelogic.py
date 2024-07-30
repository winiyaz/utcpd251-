# This definition is going to be for the game logic

import turtle

import pandas as pd


class StateGuessGame:
	def __init__(self, scr, data):
		self.scr = scr
		self.data = data
		self.all_states = data.state.to_list()
		self.gues = []

	def start_game(self):
		while len(self.gues) < 50:
			# Setting dialog
			ans = self.scr.textinput(title=f"{len(self.gues)}/50 StateCorrect", prompt="WhichFlavor").title()
			print(ans)

			# Logic with data from the dataframe
			if ans == "Exit":
				miss = [s for s in self.all_states if s not in self.gues]
				print(f'Missed = {len(miss)}')  # Missed States
				print(miss)
				new_data = pd.DataFrame(miss, columns=["state"])
				new_data.to_csv("bastard.csv")
				break
			if ans in self.all_states:
				self.gues.append(ans)
				t = turtle.Turtle()
				t.hideturtle()
				t.penup()
				t.color("#facc15")
				state_data = self.data[self.data.state == ans]
				t.goto(state_data.x.item(), state_data.y.item())
				t.write(state_data.state.item())

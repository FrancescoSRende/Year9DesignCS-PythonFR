import tkinter as tk
from tkinter import ttk
from tkinter import *
import random



playerClass = "Soldier"
yourHP = 500
enemyHP = 500
yourATK = []
enemyATK = [0,25,40]
yourDEF = []
enemyDEF = [0,20]
yourACC = 80
enemyACC = 75



def change(*args):
	playerClass = classVar.get()
	if playerClass == "Soldier":
		yourATK = [0,25,40]
		yourDEF = [10,20]
		yourACC = 80
	elif playerClass == "Berserker":
		yourHP = 400
		yourATK = [0,40,60]
		yourDEF = [5,15]
		yourACC = 75
	elif playerClass == "Wizard":
		yourHP = 550
		yourATK = [0,25,35]
		yourDEF = [10,20]
		yourACC = 90
	elif playerClass == "Knight":
		yourHP = 600
		yourATK = [0,20,35]
		yourDEF = [20,30]
		yourACC = 80

def fight():

	if playerClass == "Soldier":

		if random.randint(1,6) > 1:
			chanceSoldier = random.randint(0,2)

			enemyHP -= yourATK[chanceSoldier]

			if random.randint(1,5) == 4:
				chanceEnemy = random.randint(0,2)
				yourHP -= enemyATK[chanceEnemy]

			else:
				enemyStatsOutput.config(state = "normal")
				enemyStatsOutput.insert(tk.INSERT, "Enemy missed.\n")
				enemyStatsOutput.config(state = "disabled")

			yourStatsOutput.config(state = "normal")
			yourStatsOutput.delete(1.0,END)
			yourStatsOutput.insert(tk.INSERT, "Your HP is now "+str(yourHP)+".\n")
			yourStatsOutput.config(state = "disabled")

			enemyStatsOutput.config(state = "normal")
			enemyStatsOutput.delete(1.0,END)
			enemyStatsOutput.insert(tk.INSERT, "Enemy HP is now "+str(yourHP)+".\n")
			enemyStatsOutput.config(state = "disabled")

		else:
			yourStatsOutput.config(state = "normal")
			yourStatsOutput.insert(tk.INSERT, "You missed.\n")
			yourStatsOutput.config(state = "disabled")
	


	elif playerClass == "Berserker":
		print("H")

	elif playerClass == "Wizard":
		print("H")

	elif playerClass == "Knight":
		print("H")





def defend():
	print("H")




root = tk.Tk()
root.title("Calculator")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Choose Class")
tabControl.grid()

classTitle = tk.Label(tab1, text = "Choose Class")
classTitle.grid(row = 0, column = 0)

classList = ["Soldier", "Berserker", "Wizard", "Knight"]
classVar = tk.StringVar(tab1)
classVar.set(classList[0])
classVar.trace("w",change)
classDropdown = tk.OptionMenu(tab1,classVar,classList[0],classList[1],classList[2],classList[3])
classDropdown.grid(row = 0, column = 1)




tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Fight")
tabControl.grid()

battleTitle = tk.Label(tab2, text = "Fight")
battleTitle.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

fightButton = tk.Button(tab2, text="Fight", command = fight)
fightButton.grid(row = 1, column = 0)

defendButton = tk.Button(tab2, text="Defend", command = defend)
defendButton.grid(row = 1, column = 1)

battleTitle = tk.Label(tab2, text = "")
battleTitle.grid(row = 2, column = 0, columnspan = 2, sticky = "NESW")

yourStatsOutput = tk.Text(tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
yourStatsOutput.config(state="normal", bg = "black", foreground = "white", font=("Courier"))
if playerClass == "Soldier":
	yourStatsOutput.insert(tk.INSERT, "Your HP is 500.\n")
	yourStatsOutput.config(state = "disabled")
elif playerClass == "Berserker":
	yourStatsOutput.insert(tk.INSERT, "Your HP is 400.\n")
	yourStatsOutput.config(state = "disabled")
elif playerClass == "Wizard":
	yourStatsOutput.insert(tk.INSERT, "Your HP is 550.\n")
	yourStatsOutput.config(state = "disabled")
elif playerClass == "Knight":
	yourStatsOutput.insert(tk.INSERT, "Your HP is 600.\n")
	yourStatsOutput.config(state = "disabled")
yourStatsOutput.grid(row = 3, column = 0)

enemyStatsOutput = tk.Text(tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
enemyStatsOutput.config(state="normal", bg = "black", foreground = "white", font=("Courier"))
enemyStatsOutput.insert(tk.INSERT, "Enemy HP is 500.\n")
enemyStatsOutput.config(state = "disabled")
enemyStatsOutput.grid(row = 3, column = 1)




root.mainloop()
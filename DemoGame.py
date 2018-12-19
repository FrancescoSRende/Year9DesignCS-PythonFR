import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

#A class is a blueprint an instnace of the class is an object.  You can make as many objects as you want from a class. 

class World():

	#A class has a special function called a constuctor. A constructor is a special method that is ONLY CALLED ONCE!!!
	#It is only called when we INSTANTIATE/CREATE an instance of class.

	def __init__(self):
		
		#When I thnk of a class I think of two things.  
		#Fields: These are attributes that describe an object
		#Methods: These are behaviours of the class.

		self.playerClass = "Soldier"
		self.yourHP = 500
		self.enemyHP = 500
		self.yourATK = []
		self.enemyATK = [30,45]
		self.yourDEF = []
		self.enemyDEF = [0,20]
		self.yourACC = 80
		self.enemyACC = 75

		self.root = tk.Tk()
		self.root.title("Fighting Game")

		self.tabControl = ttk.Notebook(self.root)

		self.tab1 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1, text="Choose Class")
		self.tabControl.grid()

		self.classTitle = tk.Label(self.tab1, text = "Choose Class")
		self.classTitle.grid(row = 0, column = 0)

		self.classList = ["Soldier", "Berserker", "Wizard", "Knight"]
		self.classVar = tk.StringVar(self.tab1)
		self.classVar.set(self.classList[0])
		self.classVar.trace("w",self.change)
		self.classDropdown = tk.OptionMenu(self.tab1,self.classVar,self.classList[0],self.classList[1],self.classList[2],self.classList[3])
		self.classDropdown.grid(row = 0, column = 1)




		self.tab2 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2, text="Fight")
		self.tabControl.grid()

		self.battleTitle = tk.Label(self.tab2, text = "Fight")
		self.battleTitle.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

		self.fightButton = tk.Button(self.tab2, text="Fight", command = self.fight)
		self.fightButton.grid(row = 1, column = 0)

		self.defendButton = tk.Button(self.tab2, text="Defend", command = self.defend)
		self.defendButton.grid(row = 1, column = 1)

		self.battleTitle = tk.Label(self.tab2, text = "")
		self.battleTitle.grid(row = 2, column = 0, columnspan = 2, sticky = "NESW")

		self.yourStatsOutput = tk.Text(self.tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
		self.yourStatsOutput.config(state="normal", bg = "black", foreground = "white", font=("Courier"))
		if self.playerClass == "Soldier":
			self.yourStatsOutput.insert(tk.INSERT, "Your HP is 500.\n")
			self.yourStatsOutput.config(state = "disabled")
		elif self.playerClass == "Berserker":
			self.yourStatsOutput.insert(tk.INSERT, "Your HP is 400.\n")
			self.yourStatsOutput.config(state = "disabled")
		elif self.playerClass == "Wizard":
			self.yourStatsOutput.insert(tk.INSERT, "Your HP is 550.\n")
			self.yourStatsOutput.config(state = "disabled")
		elif self.playerClass == "Knight":
			self.yourStatsOutput.insert(tk.INSERT, "Your HP is 600.\n")
			self.yourStatsOutput.config(state = "disabled")
		self.yourStatsOutput.grid(row = 3, column = 0)

		self.enemyStatsOutput = tk.Text(self.tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
		self.enemyStatsOutput.config(state="normal", bg = "black", foreground = "white", font=("Courier"))
		self.enemyStatsOutput.insert(tk.INSERT, "Enemy HP is 500.\n")
		self.enemyStatsOutput.config(state = "disabled")
		self.enemyStatsOutput.grid(row = 3, column = 1)


		
		self.root.mainloop()



	def change(self, *args):
		print("CHANGE")
		self.playerClass = self.classVar.get()
		if self.playerClass == "Soldier":
			self.yourHP = 500
			self.yourATK = [25,40,60]
			self.yourDEF = [10,20]
			self.yourACC = 80
		elif self.playerClass == "Berserker":
			self.yourHP = 400
			self.yourATK = [40,60,85]
			self.yourDEF = [5,15]
			self.yourACC = 75
		elif self.playerClass == "Wizard":
			self.yourHP = 550
			self.yourATK = [25,35,50]
			self.yourDEF = [10,20]
			self.yourACC = 90
		elif self.playerClass == "Knight":
			self.yourHP = 600
			self.yourATK = [20,35,55]
			self.yourDEF = [20,30]
			self.yourACC = 80



	def fight(self):

		if random.randint(1,101) < self.yourACC:

			chanceSoldier = random.randint(0,len(self.yourATK)-1) #Since chanceSoldier is only in this function no self needed

			chanceEnemyDEF = random.randint(0,len(self.enemyDEF)-1)

			if self.yourATK[chanceSoldier] > self.enemyDEF[chanceEnemyDEF]:
				self.enemyHP = self.enemyHP - self.yourATK[chanceSoldier] + self.enemyDEF[chanceEnemyDEF]

			else:
				self.enemyStatsOutput.config(state = "normal")
				self.enemyStatsOutput.insert(tk.INSERT, "Enemy blocked attack.\n")
				self.enemyStatsOutput.config(state = "disabled")

			if random.randint(1,101) < self.enemyACC:
				chanceEnemy = random.randint(0,len(self.enemyATK)-1)
				self.yourHP -= self.enemyATK[chanceEnemy]

			else:
				self.enemyStatsOutput.config(state = "normal")
				self.enemyStatsOutput.insert(tk.INSERT, "Enemy missed.\n")
				self.enemyStatsOutput.config(state = "disabled")

			self.yourStatsOutput.config(state = "normal")
			self.yourStatsOutput.delete(1.0,END)
			self.yourStatsOutput.insert(tk.INSERT, "Your HP is now "+str(self.yourHP)+".\n")
			self.yourStatsOutput.config(state = "disabled")

			self.enemyStatsOutput.config(state = "normal")
			self.enemyStatsOutput.delete(1.0,END)
			self.enemyStatsOutput.insert(tk.INSERT, "Enemy HP is now "+str(self.enemyHP)+".\n")
			self.enemyStatsOutput.config(state = "disabled")

			if self.yourHP <= 0:
				self.yourStatsOutput.config(state = "normal")
				self.yourStatsOutput.delete(1.0,END)
				self.yourStatsOutput.insert(tk.INSERT, "You are dead.\n")
				self.yourStatsOutput.config(state = "disabled")

			if self.enemyHP <= 0:
				self.enemyStatsOutput.config(state = "normal")
				self.enemyStatsOutput.delete(1.0,END)
				self.enemyStatsOutput.insert(tk.INSERT, "Enemy is dead.\n")
				self.enemyStatsOutput.config(state = "disabled")

				self.yourStatsOutput.config(state = "normal")
				self.yourStatsOutput.delete(1.0,END)
				self.yourStatsOutput.insert(tk.INSERT, "You win.\n")
				self.yourStatsOutput.config(state = "disabled")

		else:
			self.yourStatsOutput.config(state = "normal")
			self.yourStatsOutput.insert(tk.INSERT, "You missed.\n")
			self.yourStatsOutput.config(state = "disabled")



	def defend(self):
		
		chanceSoldierDEF = random.randint(0,len(self.yourDEF)-1)

		chanceEnemy = random.randint(0,len(self.enemyATK)-1)

		if random.randint(1,101) > self.enemyACC:
			self.enemyStatsOutput.config(state = "normal")
			self.enemyStatsOutput.insert(tk.INSERT, "Enemy missed.\n")
			self.enemyStatsOutput.config(state = "disabled")

		else:
			if self.enemyATK[chanceEnemy] > self.yourDEF[chanceSoldierDEF]:
				self.yourHP = self.yourHP - self.enemyATK[chanceEnemy] + self.yourDEF[chanceSoldierDEF]

			else:
				self.yourStatsOutput.config(state = "normal")
				self.yourStatsOutput.insert(tk.INSERT, "You blocked attack.\n")
				self.yourStatsOutput.config(state = "disabled")

		self.yourStatsOutput.config(state = "normal")
		self.yourStatsOutput.delete(1.0,END)
		self.yourStatsOutput.insert(tk.INSERT, "Your HP is now "+str(self.yourHP)+".\n")
		self.yourStatsOutput.config(state = "disabled")

		if self.yourHP <= 0:
			self.yourStatsOutput.config(state = "normal")
			self.yourStatsOutput.delete(1.0,END)
			self.yourStatsOutput.insert(tk.INSERT, "You are dead.\n")
			self.yourStatsOutput.config(state = "disabled")





world = World()
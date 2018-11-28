import tkinter as tk
from tkinter import ttk



#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data
#Use lists, append function and reading/writing files to store answers from data



h_object = 0
h_image = 0
scale_ratio = 0
scale_percent = 0
meas_1 = 0
meas_2 = 0
units_1 = "cm"
units_2 = "cm"

def calc_scale():

	h_object = float(ent1var1.get())
	h_image = float(ent1var2.get())
	scale_ratio = h_image / h_object
	scale_percent = scale_ratio * 100
	output1eq1.config(state = "normal")
	output1eq1.insert(tk.INSERT, "The object has been scaled up by a factor of "+str(round(scale_ratio,1))+", which is a percentage increase of "+str(round(scale_percent,2))+"%. ")
	output1eq1.config(state = "disabled")


def change_1(*args):
	units_1 = optionVar1.get()

def change_2(*args):
	units_2 = optionVar2.get()

def convert():
	units_1 = optionVar1.get()
	units_2 = optionVar2.get()
	meas_1 = float(ent2var1.get())
	meas_2 = float(ent2var2.get())
	if units_1 == units_2:
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "Already in same units. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "cm" and units_2 == "mm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 10)+" mm and the second measurement is "+str(meas_2)+" mm. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "cm" and units_2 == "μm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 10000)+" μm and the second measurement is "+str(meas_2)+" μm. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "mm" and units_2 == "cm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" mm and the second measurement is "+str(meas_2 * 10)+" mm. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "mm" and units_2 == "μm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 1000)+" μm and the second measurement is "+str(meas_2)+" μm. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "μm" and units_2 == "cm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" μm and the second measurement is "+str(meas_2 * 10000)+" μm. ")
		output2eq1.config(state = "disabled")
	elif units_1 == "μm" and units_2 == "mm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" μm and the second measurement is "+str(meas_2 * 1000)+" μm. ")
		output2eq1.config(state = "disabled")




root = tk.Tk()
root.title("Calculator")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Scale Calculator")
tabControl.grid()

lab1_0 = tk.Label(tab1, text = "PLEASE ENSURE BOTH MEASUREMENTS ARE IN THE SAME UNITS")
lab1_0.config(font = ("Arrus BT", 20))
lab1_0.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

lab1var1 = tk.Label(tab1, text = "Input Dimension of Object")
lab1var1.grid(row = 1, column = 0, sticky = "NESW")

ent1var1 = tk.Entry(tab1)
ent1var1.config(bg = "black", foreground = "lime", font=("Courier"))
ent1var1.grid(row = 1, column = 1, sticky = "NESW")

lab1var2 = tk.Label(tab1, text = "Input Dimension of Image")
lab1var2.grid(row = 4, column = 0, sticky = "NESW")

ent1var2 = tk.Entry(tab1)
ent1var2.config(bg = "black", foreground = "lime", font=("Courier"))
ent1var2.grid(row = 4, column = 1, sticky = "NESW")

button1eq2 = tk.Button(tab1, text="Calculate magnification", bg="red", command = calc_scale)
button1eq2.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")

output1eq1 = tk.Text(tab1, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output1eq1.config(state="disabled", bg = "black", foreground="white", font=("Courier"))
output1eq1.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW")

logo = tk.PhotoImage(file = "rendevous_inc_logo.png")
logoImage = tk.Label(tab1, image = logo)
logoImage.grid(row = 7, column = 0, columnspan = 2)





tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Conversion of Units")
tabControl.grid()

lab2var1 = tk.Label(tab2, text = "Input First Number")
lab2var1.grid(row = 0, column = 0, sticky = "NESW")

ent2var1 = tk.Entry(tab2)
ent2var1.config(bg = "black", foreground = "lime", font=("Courier"))
ent2var1.grid(row = 0, column = 1, sticky = "NESW")

lab2var2 = tk.Label(tab2, text = "Input First Unit")
lab2var2.grid(row = 1, column = 0, sticky = "NESW")

optionList1 = ["cm", "mm", "μm"]
optionVar1 = tk.StringVar(tab2) #This is keeping track of what the drop down is set to.  
optionVar1.set(optionList1[0]) #This initalizes your variable 
optionVar1.trace("w",change_1) #Runs the function change when we write to optionVar, which happens when we change the drop down
dropdown1 = tk.OptionMenu(tab2,optionVar1,optionList1[0],optionList1[1],optionList1[2])
dropdown1.grid(row = 1, column = 1)

lab2var3 = tk.Label(tab2, text = "Input Second Number")
lab2var3.grid(row = 2, column = 0, sticky = "NESW")

ent2var2 = tk.Entry(tab2)
ent2var2.config(bg = "black", foreground = "lime", font=("Courier"))
ent2var2.grid(row = 2, column = 1, sticky = "NESW")

lab2var4 = tk.Label(tab2, text = "Input Second Unit")
lab2var4.grid(row = 3, column = 0, sticky = "NESW")

optionList2 = ["cm", "mm", "μm"]
optionVar2 = tk.StringVar(tab2) #This is keeping track of what the drop down is set to.  
optionVar2.set(optionList2[0]) #This initalizes your variable 
optionVar2.trace("w",change_1) #Runs the function change when we write to optionVar, which happens when we change the drop down
dropdown2 = tk.OptionMenu(tab2,optionVar2,optionList2[0],optionList2[1],optionList2[2])
dropdown2.grid(row = 3, column = 1)

button2eq2 = tk.Button(tab2, text="Convert Both Measurements to the Same Units", command = convert)
button2eq2.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW")

output2eq1 = tk.Text(tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output2eq1.config(state="disabled", bg = "black", foreground = "white", font=("Courier"))
output2eq1.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")

logo = tk.PhotoImage(file = "rendevous_inc_logo.png")
logoImage = tk.Label(tab2, image = logo)
logoImage.grid(row = 7, column = 0, columnspan = 2)

root.mainloop()
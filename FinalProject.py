import tkinter as tk
from tkinter import ttk




h_object = 0
h_image = 0
scale_ratio = 0
scale_percent = 0
meas_1 = 0
meas_2 = 0
units_1 = "cm"
units_2 = "cm"
oper = "+"
num_1 = 0
num_2 = 0
answer = 0



def calc_scale():

	h_object = float(ent_obj.get())
	h_image = float(ent_img.get())
	scale_ratio = h_image / h_object
	scale_percent = scale_ratio * 100
	output_scale.config(state = "normal")
	output_scale.insert(tk.INSERT, "The object has been scaled up by a factor of "+str(round(scale_ratio,1))+", which is a percentage increase of "+str(round(scale_percent,2))+"%.\n")
	output_scale.config(state = "disabled")

	f = open("FinalProj.txt", "a")
	f.write("Object was scaled up by: "+str(round(scale_ratio,1))+", or a percent increase of: "+str(round(scale_percent,2))+"%.\n")
	f.close()

def get_info():

	info_output.config(state = "normal")
	info_output.insert(tk.INSERT, "This formula finds the scale by which an image of an object is drawn, typically for things such as cell drawings.\n")
	info_output.config(state = "disabled")

def change_1(*args):
	units_1 = optionVar1.get()

def change_2(*args):
	units_2 = optionVar2.get()

def convert():

	units_1 = optionVar1.get()
	units_2 = optionVar2.get()
	meas_1 = float(ent_var1.get())
	meas_2 = float(ent_var2.get())

	if units_1 == units_2:
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "Already in same units.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1)+" "+units_1+" and "+str(meas_2)+" "+units_2+".\n")
		f.close()

	elif units_1 == "cm" and units_2 == "mm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 10)+" mm and the second measurement is "+str(meas_2)+" mm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1 * 10)+" mm and "+str(meas_2)+" mm.\n")
		f.close()

	elif units_1 == "cm" and units_2 == "μm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 10000)+" μm and the second measurement is "+str(meas_2)+" μm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1 * 10000)+" μm and "+str(meas_2)+" μm.\n")
		f.close()

	elif units_1 == "mm" and units_2 == "cm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" mm and the second measurement is "+str(meas_2 * 10)+" mm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1)+" mm and "+str(meas_2 * 10)+" mm.\n")
		f.close()

	elif units_1 == "mm" and units_2 == "μm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1 * 1000)+" μm and the second measurement is "+str(meas_2)+" μm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1 * 1000)+" μm and "+str(meas_2)+" μm.\n")
		f.close()

	elif units_1 == "μm" and units_2 == "cm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" μm and the second measurement is "+str(meas_2 * 10000)+" μm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1)+" μm and "+str(meas_2 * 10000)+" μm.\n")
		f.close()

	elif units_1 == "μm" and units_2 == "mm":
		output2eq1.config(state = "normal")
		output2eq1.insert(tk.INSERT, "The first measurement is "+str(meas_1)+" μm and the second measurement is "+str(meas_2 * 1000)+" μm.\n")
		output2eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write("Units are: "+str(meas_1)+" μm and "+str(meas_2 * 1000)+" μm.\n")
		f.close()


def change_3(*args):
	oper = optionVar3.get()

def calculate():
	oper = optionVar3.get()
	num_1 = float(ent_num1.get())
	num_2 = float(ent_num2.get())

	if oper == "+":
		answer = num_1 + num_2
		output3eq1.config(state = "normal")
		output3eq1.insert(tk.INSERT, str(num_1)+" "+str(oper)+" "+str(num_2)+" = "+str(answer)+".\n")
		output3eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write(str(num_1)+" + "+str(num_2)+" = "+str(answer)+".\n")
		f.close()

	elif oper == "-":
		answer = num_1 - num_2
		output3eq1.config(state = "normal")
		output3eq1.insert(tk.INSERT, str(num_1)+" "+str(oper)+" "+str(num_2)+" = "+str(answer)+".\n")
		output3eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write(str(num_1)+" - "+str(num_2)+" = "+str(answer)+".\n")
		f.close()

	elif oper == "*":
		answer = num_1 * num_2
		output3eq1.config(state = "normal")
		output3eq1.insert(tk.INSERT, str(num_1)+" "+str(oper)+" "+str(num_2)+" = "+str(answer)+".\n")
		output3eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write(str(num_1)+" * "+str(num_2)+" = "+str(answer)+".\n")
		f.close()

	elif oper == "/":
		answer = num_1 / num_2
		output3eq1.config(state = "normal")
		output3eq1.insert(tk.INSERT, str(num_1)+" "+str(oper)+" "+str(num_2)+" = "+str(answer)+".\n")
		output3eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write(str(num_1)+" / "+str(num_2)+" = "+str(answer)+".\n")
		f.close()

	elif oper == "^":
		answer = num_1 ** num_2
		output3eq1.config(state = "normal")
		output3eq1.insert(tk.INSERT, str(num_1)+" "+str(oper)+" "+str(num_2)+" = "+str(answer)+".\n")
		output3eq1.config(state = "disabled")
		f = open("FinalProj.txt", "a")
		f.write(str(num_1)+" ^ "+str(num_2)+" = "+str(answer)+".\n")
		f.close()





root = tk.Tk()
root.title("Calculator")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Scale Calculator")
tabControl.grid()

title_1 = tk.Label(tab1, text = "PLEASE ENSURE BOTH MEASUREMENTS ARE IN THE SAME UNITS")
title_1.config(font = ("Arrus BT", 20))
title_1.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

lab_obj = tk.Label(tab1, text = "Input Dimension of Object")
lab_obj.grid(row = 1, column = 0, sticky = "NESW")

ent_obj = tk.Entry(tab1)
ent_obj.config(bg = "black", foreground = "lime", font=("Courier"))
ent_obj.grid(row = 1, column = 1, sticky = "NESW")

lab_img = tk.Label(tab1, text = "Input Dimension of Image")
lab_img.grid(row = 4, column = 0, sticky = "NESW")

ent_img = tk.Entry(tab1)
ent_img.config(bg = "black", foreground = "lime", font=("Courier"))
ent_img.grid(row = 4, column = 1, sticky = "NESW")

but_scale = tk.Button(tab1, text="Calculate magnification", bg="red", command = calc_scale)
but_scale.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")

output_scale = tk.Text(tab1, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output_scale.config(state="disabled", bg = "black", foreground="white", font=("Courier"))
output_scale.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW")

info_button = tk.Button(tab1, text="Get info", bg="red", command = get_info)
info_button.grid(row = 7, column = 0, sticky = "EW")

info_output = tk.Text(tab1, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
info_output.config(state="disabled", bg = "black", foreground="white", font=("Courier"))
info_output.grid(row = 7, column = 1, sticky = "NESW")






tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Conversion of Units")
tabControl.grid()

lab_var1 = tk.Label(tab2, text = "Input First Number")
lab_var1.grid(row = 0, column = 0, sticky = "NESW")

ent_var1 = tk.Entry(tab2)
ent_var1.config(bg = "black", foreground = "lime", font=("Courier"))
ent_var1.grid(row = 0, column = 1, sticky = "NESW")

lab_unit1 = tk.Label(tab2, text = "Input First Unit")
lab_unit1.grid(row = 1, column = 0, sticky = "NESW")

optionList1 = ["cm", "mm", "μm"]
optionVar1 = tk.StringVar(tab2) #This is keeping track of what the drop down is set to.  
optionVar1.set(optionList1[0]) #This initalizes your variable 
optionVar1.trace("w",change_2) #Runs the function change when we write to optionVar, which happens when we change the drop down
dropdown1 = tk.OptionMenu(tab2,optionVar1,optionList1[0],optionList1[1],optionList1[2])
dropdown1.grid(row = 1, column = 1)

lab_var2 = tk.Label(tab2, text = "Input Second Number")
lab_var2.grid(row = 2, column = 0, sticky = "NESW")

ent_var2 = tk.Entry(tab2)
ent_var2.config(bg = "black", foreground = "lime", font=("Courier"))
ent_var2.grid(row = 2, column = 1, sticky = "NESW")

lab2var4 = tk.Label(tab2, text = "Input Second Unit")
lab2var4.grid(row = 3, column = 0, sticky = "NESW")

optionList2 = ["cm", "mm", "μm"]
optionVar2 = tk.StringVar(tab2)
optionVar2.set(optionList2[0])
optionVar2.trace("w",change_1)
dropdown2 = tk.OptionMenu(tab2,optionVar2,optionList2[0],optionList2[1],optionList2[2])
dropdown2.grid(row = 3, column = 1)

button2eq2 = tk.Button(tab2, text="Convert Both Measurements to the Same Units", command = convert)
button2eq2.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW")

output2eq1 = tk.Text(tab2, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output2eq1.config(state="disabled", bg = "black", foreground = "white", font=("Courier"))
output2eq1.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")






tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Arithmetic")
tabControl.grid()

lab_num1 = tk.Label(tab3, text = "Input First Number")
lab_num1.grid(row = 0, column = 0, sticky = "NESW")

ent_num1 = tk.Entry(tab3)
ent_num1.config(bg = "black", foreground = "lime", font=("Courier"))
ent_num1.grid(row = 0, column = 1, sticky = "NESW")

lab_oper = tk.Label(tab3, text = "Input Operation")
lab_oper.grid(row = 1, column = 0, sticky = "NESW")

optionList3 = ["+", "-", "*", "/", "^"]
optionVar3 = tk.StringVar(tab3)
optionVar3.set(optionList3[0])
optionVar3.trace("w",change_3)
dropdown3 = tk.OptionMenu(tab3,optionVar3,optionList3[0],optionList3[1],optionList3[2],optionList3[3], optionList3[4])
dropdown3.grid(row = 1, column = 1)

lab_num2 = tk.Label(tab3, text = "Input Second Number")
lab_num2.grid(row = 2, column = 0, sticky = "NESW")

ent_num2 = tk.Entry(tab3)
ent_num2.config(bg = "black", foreground = "lime", font=("Courier"))
ent_num2.grid(row = 2, column = 1, sticky = "NESW")

button3eq1 = tk.Button(tab3, text="Calculate", command = calculate)
button3eq1.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW")

output3eq1 = tk.Text(tab3, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output3eq1.config(state="disabled", bg = "black", foreground = "white", font=("Courier"))
output3eq1.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW")

root.mainloop()
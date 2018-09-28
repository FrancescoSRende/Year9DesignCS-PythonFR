import tkinter as tk
import math

def submit():

	print("Submit pressed")
	radius = float(ent_r.get())
	height = float(ent_h.get())
	volume = math.pi*radius*radius*height
	volume = round(volume,3)

	output.config(state="normal")
	outputValue = "Given\nradius: "+str(radius)+" units\nheight: "+str(height)+" units\nThe volume is: "+str(volume)+" units cubed\n\n"
	
	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")

root = tk.Tk()
root.title("Volume of Cylinder")

lab_r = tk.Label(root, text="radius")
lab_r.pack()
ent_r = tk.Entry(root)
ent_r.pack()

lab_h = tk.Label(root, text="height")
lab_h.pack()
ent_h = tk.Entry(root)
ent_h.pack()

button = tk.Button(root, text="Calculate", command=submit, background="red")
button.pack()

output = tk.Text(root, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()
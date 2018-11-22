import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Formula 1")
tabControl.grid()

lab1var1 = tk.Label(tab1, text = "Input Variable 1")
lab1var1.grid(row = 0, column = 0)

ent1var1 = tk.Entry(tab1)
ent1var1.grid(row = 0, column = 1)

button1eq1 = tk.Button(tab1, text="Calculate nested equation", bg="red")
button1eq1.grid(row = 1, column = 0, columnspan = 2)

output1eq1 = tk.Text(tab1, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output1eq1.config(state="disabled")
output1eq1.grid(row = 2, column = 0, columnspan = 2)

lab1var2 = tk.Label(tab1, text = "Input Variable 2")
lab1var2.grid(row = 3, column = 0)

ent1var2 = tk.Entry(tab1)
ent1var2.grid(row = 3, column = 1)

button1eq2 = tk.Button(tab1, text="Calculate full equation", bg="red")
button1eq2.grid(row = 4, column = 0, columnspan = 2)

output1eq2 = tk.Text(tab1, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output1eq2.config(state="disabled")
output1eq2.grid(row = 5, column = 0, columnspan = 2)





tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Formula 2")
tabControl.grid()

lab2var1 = tk.Label(tab2, text = "Input Variable 1")
lab2var1.grid(row = 0, column = 0)

ent2var1 = tk.Entry(tab2)
ent2var1.grid(row = 0, column = 1)

button2eq1 = tk.Button(tab2, text="Calculate nested equation", bg="red")
button2eq1.grid(row = 1, column = 0, columnspan = 2)

output2eq1 = tk.Text(tab2, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output2eq1.config(state="disabled")
output2eq1.grid(row = 2, column = 0, columnspan = 2)

lab2var2 = tk.Label(tab2, text = "Input Variable 2")
lab2var2.grid(row = 3, column = 0)

ent2var2 = tk.Entry(tab2)
ent2var2.grid(row = 3, column = 1)

button2eq2 = tk.Button(tab2, text="Calculate full equation", bg="red")
button2eq2.grid(row = 4, column = 0, columnspan = 2)

output2eq2 = tk.Text(tab2, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output2eq2.config(state="disabled")
output2eq2.grid(row = 5, column = 0, columnspan = 2)

root.mainloop()
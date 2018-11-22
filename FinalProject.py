import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Formula 1")
tabControl.pack(expand=1, fill="both")

lab1var1 = tk.Label(tab1, text = "Input Variable 1")
lab1var1.pack()

ent1var1 = tk.Entry(tab1)
ent1var1.pack(padx = 10)

lab1var2 = tk.Label(tab1, text = "Input Variable 2")
lab1var2.pack()

ent1var2 = tk.Entry(tab1)
ent1var2.pack()







tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Formula 2")
tabControl.pack(expand=1, fill="both")

root.mainloop()
import tkinter as tk
from tkinter import ttk

def clicked():
	print("Button clicked")

def hitReturn(event):
	print("User pressed return")

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

entry1tab1 = tk.Entry(tab1)
entry1tab1.pack()
entry1tab1.bind("<Return>",hitReturn)

button1tab2 = tk.Button(tab2, text="Button2", command=clicked)
button1tab2.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

root.mainloop()
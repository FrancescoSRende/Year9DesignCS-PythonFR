import tkinter as tk

root = tk.Tk()

output = tk.Text(root)
output.config(state = "disable", bg = "red", fg = "blue", height = 10, width = 50)
output.grid(row = 0, column = 0, columnspan = 2)

root.mainloop()
import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text = "Enter a number: ")
lab.grid(row = 0, column = 0)

entry = tk.Entry(root)
entry.grid(row = 1, column = 0)

button = tk.Button(root, text = "Submit")
button.grid(row = 2, column = 0)

output = tk.Text(root)
output.configure(state = "disable", bg = "black")
output.grid(row = 0, column = 1, rowspan = 3)
root.mainloop()
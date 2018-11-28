import tkinter as tk
from tkinter import ttk
import os
import webbrowser

username = ""
password = ""
attemptUN = ""
attemptPW = ""

def account():

	username = entSetUN.get()
	password = entSetPW.get()
	if username == password:
		os.system("say -v Alex Security error: username and password cannot be the same")
		print("Security error: username and password cannot be the same")
	else:
		os.system("say -v Alex Username and password set")
		print("Username and password set")

def check():

	username = entSetUN.get()
	password = entSetPW.get()
	attemptUN = entUN.get()
	attemptPW = entPW.get()
	if username == attemptUN and password == attemptPW:
		os.system("say -v Alex Access granted")
		print("Access granted")
	else:
		os.system("say -v Alex Access denied: incorrect username and/or password")
		print("Access denied: incorrect username and/or password")
		webbrowser.open("https://www.youtube.com/watch?v=okZ-qEJ3VXQ")

root = tk.Tk()
root.title("GUI Tabs")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")
tabControl.pack(expand=1, fill="both")

labSetUN = tk.Label(tab1, text = "Set Username")
labSetUN.pack()

entSetUN = tk.Entry(tab1)
entSetUN.configure(bg = "red")
entSetUN.pack(padx = 10)

labSetPW = tk.Label(tab1, text = "Set Password")
labSetPW.pack()

entSetPW = tk.Entry(tab1, show = "*")
entSetPW.configure(bg = "blue")
entSetPW.pack()

button = tk.Button(tab1, text = "Submit", command = account)
button.pack()

labUN = tk.Label(tab2, text = "Input Username")
labUN.pack()

entUN = tk.Entry(tab2)
entUN.configure(bg = "red")
entUN.pack(padx = 10)

labPW = tk.Label(tab2, text = "Input Password")
labPW.pack()

entPW = tk.Entry(tab2, show = "*")
entPW.configure(bg = "blue")
entPW.pack()

button = tk.Button(tab2, text = "Submit", command = check)
button.pack()

root.mainloop()
import tkinter as tk
import webbrowser



root = tk.Tk()

def change(*args):
	genre = genreVar.get()

def get_music():

	if genre == "Alternative Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Alice in Chains [earlier]\nFaith No More\nRage Against the Machine\nWhite Zombie")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=97ScjPlULh4")
	elif genre == "Black Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Bathory\nGorgoroth\nVenom\nImmortal")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=NyQg8WAkLY0")
	elif genre == "Blues Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Cream\nZZ Top\nAerosmith\nLed Zeppelin")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=iCqWb4W4zGU")
	elif genre == "Death Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Death\nCannibal Corpse\nSepultura\nObituary")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=RDM2QP_xhLU")
	elif genre == "Doom Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Black Sabbath\nPentagram\nSaint Vitus\nAlice in Chains [later]")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=4YbD40UMwHQ")
	elif genre == "Funk Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Red Hot Chili Peppers\nJane's Addiction\nFaith No More\nLenny Kravitz")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=D4INE2zO9OU")
	elif genre == "Garage Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "The Stooges\nMC5\nThe White Stripes\nThe Count Five")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=3gsWt7ey6bo")
	elif genre == "Glam Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Van Halen\nMötley Crüe\nDef Leppard\nSkid Row")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=bX9RMdcFQAw")
	elif genre == "Glam Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "T-Rex\nDavid Bowie\nNew York Dolls\nLou Reed")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=gEeHOOudKOw")
	elif genre == "Groove Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Pantera\nGojira\nSepultura\nBlack Label Society")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=kOV2iTeGQik")
	elif genre == "Grunge":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Nirvana\nPearl Jam\nSoundgarden\nAlice in Chains [earlier]")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=OuEAUFsQf6Q")
	elif genre == "Hard Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "AC/DC\nGuns n' Roses\nLed Zeppelin\nDef Leppard")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=pAgnJDJN4VA")
	elif genre == "Heavy Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Iron Maiden\nJudas Priest\nDio\nMotörhead")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=Q_XJ-7jNqws")
	elif genre == "Metalcore":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Killswitch Engage\nSuicidal Tendencies [later]\nThe Dillinger Escape Plan\nPoison the Well")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=B4vTwppAfDg")
	elif genre == "Nu Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Slipknot\nSystem of a Down [earlier]\nLimp Bizkit\nKorn")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=Az_W_XOV5rs")
	elif genre == "Post-Grunge":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Foo Fighters\nAudioslave\nBush\nPuddle of Mudd")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=L182Xn6UlK8")
	elif genre == "Post-Punk":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Siouxsie and the Banshees\nU2\nThe Cure\nDevo")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=45oXyaL8mWc")
	elif genre == "Progressive Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Tool\nDream Theater\nQueensrÿche\nFantômas")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=yMMz2VwbhVI")
	elif genre == "Progressive Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Pink Floyd\nRush\nDavid Bowie\nKing Crimson")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=zz8frWcmthA")
	elif genre == "Psychedelic Rock":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "The Doors\nJimi Hendrix\nCream\nGrateful Dead")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=NFeUko-lQHg")
	elif genre == "Punk":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Sex Pistols\nGreen Day\nThe Offspring\nBlack Flag")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=K07Yq4zGTcI")
	elif genre == "Sludge Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Melvins\nAlice in Chains [later]\nMastodon\nCrowbar")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=p2sez21Cyyo")
	elif genre == "Stoner Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Blue Cheer\nKyuss\nFu Manchu\nCorrosion of Conformity")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=5vTMIYTR9c4")
	elif genre == "Thrash Metal":
		band_output.config(state = "normal")
		band_output.delete(1.0,END)
		band_output.insert(tk.INSERT, "Metallica\nMotörhead\nMegadeth\nSlayer")
		band_output.config(state = "disabled")
		webbrowser.open("https://www.youtube.com/watch?v=S7blkui3nQc")



label = tk.Label(root, text = "Choose Genre")
label.grid(row = 0, column = 0, sticky = "NESW")

genreList = ["Alternative Metal", "Black Metal", "Blues Rock", "Death Metal", "Doom Metal", "Funk Rock", "Garage Rock", "Glam Metal", "Glam Rock", "Groove Metal", "Grunge", "Hard Rock", "Heavy Metal", "Metalcore", "Nu Metal", "Post-Grunge", "Post-Punk", "Progressive Metal", "Progressive Rock", "Psychedelic Rock", "Punk", "Sludge Metal", "Stoner Metal", "Thrash Metal"]
genreVar = tk.StringVar(root)
genreVar.set(genreList[0])
genreVar.trace("w",change)
dropdown = tk.OptionMenu(root,genreVar,genreVar[0],genreVar[1],genreVar[2],genreVar[3],genreVar[4],genreVar[5],genreVar[6],genreVar[7],genreVar[8],genreVar[9],genreVar[10],genreVar[11],genreVar[12],genreVar[13],genreVar[14],genreVar[15],genreVar[16],genreVar[17],genreVar[18],genreVar[19],genreVar[20],genreVar[21],genreVar[22],genreVar[23])
dropdown.grid(row = 1, column = 0)

musicButton = tk.Button(root, text="Get Music", command = get_music)
musicButton.grid(row = 1, column = 1, sticky = "NESW")

band_output = tk.Text(root, relief=tk.GROOVE)
band_output.config(state="disabled", bg = "black", foreground="white", font=("Courier"))
band_output.grid(row = 2, column = 0, columnspan = 2, sticky = "NESW")



root.mainloop()
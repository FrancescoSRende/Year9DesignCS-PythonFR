#Loops run strings of code over and over

#There are two types of loops:
#Conditional loops (while loops): these loop as long as a condition is true
#Counted loops (for loops): these loop using a counter to keep track of how many times the loop has run

#Counted loops should be used if it is known how many times the loops will run.
#Otherwise, a conditional loop should be used
import os
import webbrowser
print("************************************************************")
word=""
while len(word) < 6 or word.isalpha() == False:
	word=input("Input a real word longer than 5 letters: ")
	if (len(word) < 6):
		os.system("osascript -e \"Set Volume 10\"")
		os.system("say You fool! I said longer than 5 letters, dumbass!")
		print("You fool! I said longer than 5 letters, dumbass!")
		webbrowser.open("https://www.youtube.com/watch?v=hpigjnKl7nI")
	if (word.isalpha() == False):
		os.system("osascript -e \"Set Volume 10\"")
		os.system("say You fool! I said a real word, dumbass!")
		print("You fool! I said a real word, dumbass!")
		webbrowser.open("https://www.youtube.com/watch?v=hpigjnKl7nI")
os.system("osascript -e \"Set Volume 10\"")
os.system("say Good job! You are a slightly less dumb ass!")
print(word+" is a very LONG word.")
webbrowser.open("https://www.youtube.com/watch?v=Q3E7L_RoyTU")
webbrowser.open("https://www.youtube.com/watch?v=Q3E7L_RoyTU")
webbrowser.open("https://www.youtube.com/watch?v=Q3E7L_RoyTU")
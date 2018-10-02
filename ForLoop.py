import os
import webbrowser
print("************************************************************")
for i in range (0,10,1):
	print(i)
	if (i % 2 == 0):
		os.system("osascript -e \"Set Volume 10\"")
		webbrowser.open("https://www.youtube.com/watch?v=Q3E7L_RoyTU")
	if (i % 3 == 0):
		os.system("osascript -e \"Set Volume 10\"")
		os.system("say I love numbers that are divisible by three! This calls for celebration!")
		webbrowser.open("https://www.youtube.com/watch?v=Vx88EFGT5Wc")
		webbrowser.open("https://www.youtube.com/watch?v=Vx88EFGT5Wc")
		webbrowser.open("https://www.youtube.com/watch?v=Vx88EFGT5Wc")
		webbrowser.open("https://www.youtube.com/watch?v=Vx88EFGT5Wc")
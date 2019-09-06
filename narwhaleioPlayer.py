import pyautogui
import time
import colorsys

print('press crtl + c to quit')
pyautogui.FAILSAFE = True
#this allows you to quit out of the program by moving the mouse to the top left

#following are variables for screen
sstopleft = (220, 220)
ssbottomright = (1220, 780)

#scale is which nth pixel you check
scale = 10

#player location
playertopleft = (300, 340)
playerbottomright = (960, 740)

#stuff used for loops
topwidth = int((ssbottomright[0]-sstopleft[0])/scale)
topheight = int((playertopleft[1]-sstopleft[1])/scale)
bottomheight = int((ssbottomright[1]-playerbottomright[1])/scale)
midheight = int((playerbottomright[1]-playertopleft[1])/scale)
midrightwidth = int((playertopleft[0]-sstopleft[0])/scale)
midleftwidth = int((ssbottomright[0]-playerbottomright[0])/scale)

#----------

def topWide(scrn):
#top wide box

	for x in range(topwidth):
		for y in range(topheight):
			pixCol = scrn.getpixel((x*scale, y*scale))
			pixCol = colorsys.rgb_to_hsv(pixCol[0], pixCol[1], pixCol[2])

			#searches for saturation value
			if pixCol[1] >= 0.5:
				#need to add numbers to r and c because they represent the values on the screenshot but we need the values in real life
				pyautogui.moveTo(x*scale+sstopleft[0], y*scale+sstopleft[1])
				pyautogui.press("space")
				print("topwide")
				return True
	return False

#----------

def botWide(scrn):
#bottom wide box

	for x in range(topwidth):
		for y in range(bottomheight):
			#note: 640 represents the real screen value, and -110 is to account for the screenshot value
			pixCol = scrn.getpixel((x*scale, y*scale+playerbottomright[1]-sstopleft[1]))
			pixCol = colorsys.rgb_to_hsv(pixCol[0], pixCol[1], pixCol[2])

			if pixCol[1] >= 0.5:
				pyautogui.moveTo(x*scale+sstopleft[0], y*scale+playerbottomright[1])
				pyautogui.press("space")
				print("botwide")
				return True
	return False

#----------

def midLeft(scrn):
#middle left box

	for x in range(midheight):
		for y in range(midleftwidth):
			pixCol = scrn.getpixel((x*scale, y*scale+playertopleft[1]-sstopleft[1]))
			pixCol = colorsys.rgb_to_hsv(pixCol[0], pixCol[1], pixCol[2])

			if pixCol[1] >= 0.5:
				pyautogui.moveTo(x*scale+sstopleft[0], y*scale+playertopleft[1])
				pyautogui.press("space")
				print("midleft")
				return True
	return False

#----------

def midRight(scrn):
#middle right box

	for x in range(midheight):
		for y in range(midrightwidth):
			pixCol = scrn.getpixel((x*scale+playerbottomright[0]-sstopleft[1], y*scale+playertopleft[1]-sstopleft[1]))
			pixCol = colorsys.rgb_to_hsv(pixCol[0], pixCol[1], pixCol[2])

			if pixCol[1] >= 0.5:
				pyautogui.moveTo(x*scale+playerbottomright[0], y*scale+playertopleft[1])
				pyautogui.press("space")
				print("midright")
				return True
	return False

#----------

try:
	print("5 second countdown now beginning")
	time.sleep(5)
	#gives you 5 seconds to open narwhaleio and click the play button
	print("running!")
	while True:
	#infinite loop that can only be quit by KeyBoardInterrupt
		scrn = pyautogui.screenshot(region=(sstopleft[0],sstopleft[1],ssbottomright[0],ssbottomright[1]))
						   				#x1, y1, x2, y2
		#takes a screenshot of the playable region in narwhaleio
		#region of the screen of player: 620, 440, 860, 640

		foundNarwhale = False		

		#if statements search for narwhales in 4 regions of the screen, designed to avoid the player
		#check def methods for dimensions

		if foundNarwhale == False:
			foundNarwhale = topWide(scrn)
		if foundNarwhale == False:
			foundNarwhale = botWide(scrn)
		if foundNarwhale == False:
			foundNarwhale = midLeft(scrn)
		if foundNarwhale == False:
			foundNarwhale = midRight(scrn)

except KeyboardInterrupt:
	print('\nDone.')


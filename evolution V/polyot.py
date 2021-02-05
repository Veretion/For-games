
from pyautogui import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import keyboard
import win32con
import win32api
import win32gui
import threading
import msvcrt
import sys
from random import randint, random, choice, choices, sample, shuffle
from time import sleep, time
from PIL import Image, ImageDraw
import mouse
import ast




# mass = [[488, 425],
# [640, 419],
# [803, 424],
# [971, 418],
# [470, 534],
# [628, 524],
# [787, 538],
# [968, 529],
# [478, 653],
# [624, 648],
# [804, 648],
# [943, 658],
# [466, 770],
# [638, 759],
# [808, 774],
# [945, 767]]

# mass = [[708, 358],
# [655, 409],
# [757, 417],
# [607, 463],
# [706, 461],
# [802, 465],
# [559, 521],
# [662, 513],
# [752, 524],
# [851, 515],
# [614, 572],
# [724, 564],
# [817, 562],
# [664, 616],
# [755, 624],
# [716, 666]]


mass = [[476, 219],
[527, 218],
[578, 225],
[667, 222],
[475, 279],
[530, 280],
[592, 280],
[651, 285],
[475, 349],
[539, 350],
[610, 334],
[656, 349],
[487, 400],
[542, 400],
[591, 394],
[669, 394]]

# нажатие по массиву
# while True:
# 	x, y = choice(mass)
# 	moveTo(x, y)
# 	sleep(0.01)
#
# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# 	sleep(0.02)
# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
# 	sleep(0.01)
# 	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# 	# sleep(0.04)
# 	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#
# 	if keyboard.is_pressed('alt'):
# 		exit()


ran = [131, 135, 1101, 746]
ter = [352, 172, 622, 430]
while True:
	try:
		# x, y = locateCenterOnScreen("grot1.PNG", region=ran, confidence=0.9)
		x, y = locateCenterOnScreen("vot.PNG", region=[131, 135, 1101, 546], confidence=0.90)
	except:
		sleep(0.1)

		# win32api.keybd_event(0x49, 0, 0, 0)  # =
		# sleep(0.05)
		# win32api.keybd_event(0x49, 0, win32con.KEYEVENTF_KEYUP, 0)  # =
		# sleep(1)
		continue
	moveTo(x-350, y-200)

	# try:
	# 	x, y = locateCenterOnScreen("let.PNG", region=ter, confidence=0.6)
	# 	moveTo(x, y - 200)
	#
	# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	# 	sleep(0.04)
	# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
	# 	sleep(5)
	# except:
	# 	moveTo(900, 350)
	if keyboard.is_pressed('alt'):
		exit()
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	sleep(0.04)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
	sleep(1)

	if keyboard.is_pressed('alt'):
		exit()
#
#
# # print(locateCenterOnScreen("coub.PNG", region=ran, confidence=0.80))








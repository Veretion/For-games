from pyautogui import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import keyboard
import win32con
import win32api
import msvcrt
import sys
from random import randint, random, choice
from time import sleep, time
from PIL import Image, ImageDraw


# print(locateCenterOnScreen('kaktus.JPG', confidence=0.85, region=(648, 378, 916, 582)))
window = Tk()
window.title("Полу-кликер")
window.geometry('400x100')


def black(x):
	if x % 2 == 0:
		# image = grab(region=(580, 500, 240, 100))
		image = grab(region=(600, 500, 190, 100))
	else:
		# image = grab(region=(670, 462, 100, 100))
		image = grab(region=(650, 452, 140, 70))

	# kaktus:
	bl = 0
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for j in range(height):
		for i in range(width):
			S = (pix[i, j][1] * 2) - (pix[i, j][0] + pix[i, j][2])
			S = 0 if S > 64 else 255
			if not S:
				bl += 1
		if bl > 700:
			return False if bl < 700 else True

	# ptica
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			S = pix[i, j][1] if pix[i, j][0] > pix[i, j][1] > pix[i, j][2] else 0
			S = 0 if 80 < S < 165 else 255
			if not S:
				bl += 1
		if bl > 750:
			return False if bl < 750 else True


def press_key():
	print('go')
	sleep(0.3)
	t = 0.6
	for x in range(40000000):
		win32api.keybd_event(0x53, 0, 0, 0)

		if x % 5 == 0:
			if keyboard.is_pressed('ctrl'):
				print('stop')
				print()
				break

			if keyboard.is_pressed('tab'):
				if t == 0.6:
					t = 0.4
				elif t == 0.4:
					t = 0.3
				elif t == 0.3:
					t = 0.2
				elif t == 0.2:
					t = 0.1
				elif t == 0.1:
					t = 0.05
				elif t == 0.05:
					t = 0.6
				sleep(0.3)
				print('t =', t)


		if black(x):
			win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.01)
			win32api.keybd_event(0x20, 0, 0, 0)
			sleep(t)
			win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.01)
			win32api.keybd_event(0x53, 0, 0, 0)


		# if x % 20 == 0:
		# 	if keyboard.is_pressed('ctrl'):
		# 		print('stop')
		# 		print()
		# 		break
			# if locateOnScreen('lose.JPG', confidence=0.9):
			#
			# 	if kaktus > 15:
			# 		print('game |', 'kaktus =', kaktus, ' bw =', base_window, 'bt =', base_time)
			#
			# 	win32api.keybd_event(0x57, 0, 0, 0)
			# 	sleep(0.1)
			# 	win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
			# 	sleep(0.05)


def clicked():
	keyboard.add_hotkey('alt', press_key)


btn = Button(window, text="Кликеp | alt", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()

clicked()






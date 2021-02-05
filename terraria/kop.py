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
import mouse


while True:
	sleep(0.01)

	# активация к
	if keyboard.is_pressed('-'):
		win32api.keybd_event(0x41, 0, 0, 0)  # A
		sleep(0.05)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		print('зажатия клавиш A и лкм')

		# move(-40, 0, 1)

	# активация к
	elif keyboard.is_pressed('+'):
		win32api.keybd_event(0x44, 0, 0, 0)  # D
		sleep(0.05)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		print('зажатия клавиш D и лкм')

		# move(40, 0, 1)

	# нажатия мыши
	elif mouse.is_pressed('x'):
		print('нажатия лкм мыши')
		while True:

			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.001)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.004)

			if keyboard.is_pressed('alt'):
				print('выкл нажатия лкм мыши\n')
				break

	elif keyboard.is_pressed('['):
		print('start')

		def lkm():
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.015)

		while True:

			if keyboard.is_pressed('alt'):
				print('stop')
				print()
				break

			for ii in range(8):
				lkm()
				sleep(0.15)
			sleep(1.5)


# рыбалка
	elif keyboard.is_pressed(']'):
		print('start')

		yar = 0
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		sleep(0.015)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		sleep(2)

		for x in range(50000000):
			if x % 4000 == 0:

				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.5)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

				sleep(0.2)

			if keyboard.is_pressed('alt'):
				print('stop')
				break

			bl = 0
			# image = grab(region=(433, 463, 183, 63))  # море
			# image = grab(region=(668, 468, 120, 61))  # пещера56
			image = grab(region=(515, 492, 99, 29))  # облака
			width = image.size[0]
			height = image.size[1]
			pix = image.load()
			for j in range(height):
				for i in range(width):
					S = (pix[i, j][2] * 2) - (pix[i, j][0] + pix[i, j][1])
					# S = 0 if S > 64 else 255  # море
					# S = 0 if S > 10 else 255  # пещера
					S = 0 if S > 150 else 255  # облака
					if not S:
						bl += 1

			# print(bl)
			# if (70 < bl < 200) or (2200 < bl < 2250) or (1900 < bl < 1950):
			if 15 < bl:

				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

				sleep(0.2)

				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

				sleep(0.9)



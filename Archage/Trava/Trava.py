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
from random import randint, random, choice
from time import sleep, time
from PIL import Image, ImageDraw
import mouse


def markers():
	dc = win32gui.GetDC(0)
	red = win32api.RGB(255, 255, 255)

	def zero(x, y):
		win32gui.SetPixel(dc, x, y, red)

	def krug(x, y):
		zero(x - 1, y - 2);zero(x, y - 2);zero(x + 1, y - 2)
		zero(x + 2, y - 1);zero(x + 2, y);zero(x + 2, y + 1)
		zero(x - 2, y - 1);zero(x - 2, y);zero(x - 2, y + 1)
		zero(x - 1, y + 2);zero(x, y + 2);zero(x + 1, y + 2)

	while True:
		sleep(0.001)
		# for i in range(808):
		zero(475, 355)

		for i in range(466, 818):
			zero(i, 352)
		zero(818, 352)
		for i in range(352, 707):
			zero(466, i)
		zero(818, 707)
		for i in range(466, 818):
			zero(i, 707)
		zero(466, 707)
		for i in range(352, 707):
			zero(818, i)


		# krug(442, 123)
		# krug(830, 121)
		# krug(439, 511)
		# krug(835, 508)


kam_x, kam_y = 818, 352
niz_x, niz_y = 100, 600

mass_x = []
for i in range(13):  # не пробивает камни, если 13
	mass_x.append(kam_x)
	kam_x -= 26

mass_y = []
for i in range(13):
	mass_y.append(kam_y)
	kam_y += 26

threading.Thread(target=markers).start()


def mains():
	dop = 0
	while True:
		# старт
		for _ in range(500000000):
			sleep(0.1)
			if keyboard.is_pressed('0'):
				print('run')
				break

		for n, y in enumerate(mass_y):
			if n < 0:
				continue
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				break

			for nx, x in enumerate(mass_x):

				# if nx == 12 and n == 13:
				# 	continue
				# elif nx == 0 and n == 13:
				# 	continue
				# elif nx == 12 and n == 0:
				# 	continue

				if dop > 0:
					dop -= 1
					continue

				if n != 13 and nx != 13:
					moveTo(x-130, y+100)
				elif nx == 13:
					moveTo(x - 200, y + 20)
				elif n == 13:
					moveTo(x - 70, y + 150)

				sleep(0.1)

				win32api.keybd_event(0x31, 0, 0, 0)
				sleep(0.1)
				win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
				sleep(0.1)

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					break

				moveTo(x, y, duration=0.35)
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break
				sleep(0.5)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.05)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.1)

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break

				rightClick()
				sleep(0.3)

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break

				sleep(0.5)

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break


mains()
# threading.Thread(target=mains).start()






















from pyautogui import *
# from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.ttk import Checkbutton
import keyboard
import win32con
import win32api
import win32gui
import ast
# import threading
# import msvcrt
# import sys
# from random import randint, random, choice
from time import sleep, time
# from PIL import Image, ImageDraw
# import mouse
# import ast
# import os

# координаты начала окна spore
# lk = [100, 89]  # локальная система координат
while True:
	sleep(0.1)
	if keyboard.is_pressed('shift'):
		lk = list(int(i) for i in str(position()).split('x=')[1].split(')')[0].split(', y='))
		break

house = [116+lk[0], 309+lk[1]]  # дом
center = [119+lk[0], 430+lk[1]]  # развлекательный центр
factory = [110+lk[0], 538+lk[1]]  # завод
tower = [100+lk[0], 677+lk[1]]  # башня

dura = 0.30

points =[
		[738+lk[0], 417+lk[1]],  # развлекательный центр 1
		[823+lk[0], 373+lk[1]],  # развлекательный центр 2
		[688+lk[0], 505+lk[1]],  # завод 1
		[552+lk[0], 502+lk[1]],  # завод 2
		[487+lk[0], 355+lk[1]],  # завод 3
		[614+lk[0], 309+lk[1]],  # завод 4
		[424+lk[0], 412+lk[1]],  # дома
		[372+lk[0], 564+lk[1]]]  # башни


def main():
	dc = win32gui.GetDC(0)

	def red(x, y):
		win32gui.SetPixel(dc, x, y, win32api.RGB(255, 0, 0))

	while True:
		sleep(0.01)
		if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl'):
			print('off')
			break

		# рисуем
		for x in range(519+lk[0], 709+lk[0]):
			red(x, 290+lk[1])
		for y in range(290+lk[1], 600+lk[1]):
			red(616+lk[0], y)

		if keyboard.is_pressed('j'):
			print('start')
			for i in range(2):
				if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl'):
					print('off')
					break
				moveTo(center)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.04)
				moveTo(points[i], duration=dura)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.02)

			for i in range(2, 6):
				if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl'):
					print('off')
					sleep(0.4)
					break
				moveTo(factory)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.04)
				moveTo(points[i], duration=dura)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.02)

			for i in range(5):
				if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl'):
					print('off')
					sleep(0.4)
					break
				moveTo(house)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.04)
				moveTo(points[6], duration=dura)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.02)

			for i in range(8):
				if keyboard.is_pressed('alt') and keyboard.is_pressed('ctrl'):
					print('off')
					sleep(0.4)
					break
				moveTo(tower)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.04)
				moveTo(points[7], duration=dura+0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.02)
			print()











main()








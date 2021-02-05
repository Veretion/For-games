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


# def maxim_gold():
# 	maxim = 0
# 	print('run')
# 	t1 = time()
#
# 	for x in range(100000000):
# 		if keyboard.is_pressed('alt'):
# 			print('stop')
# 			# print()
# 			break
#
# 		bl = 0
# 		image = grab(region=(150, 610, 800, 150))
# 		width = image.size[0]
# 		height = image.size[1]
# 		pix = image.load()
# 		for j in range(height):
# 			for i in range(width):
# 				S = 1 if 180 < pix[i, j][0] < 200 and 135 < pix[i, j][1] < 160 and 100 < pix[i, j][2] < 120 else 0
# 				if S:
# 					bl += 1
#
# 		if bl > maxim:
# 			if time() - t1 > 10:
# 				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# 				sleep(0.1)
# 				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
# 				print(maxim)
# 				print('stop')
# 				break
# 			else:
# 				print(maxim)
# 				maxim = bl


def maximd():
	maxim = 0
	print('run')
	t1 = time()

	for x in range(100000000):
		if keyboard.is_pressed('alt'):
			print('stop')
			# print()
			break

		sleep(0.01)

		bl = 0
		image = grab(region=(75, 610, 909, 40))
		width = image.size[0]
		height = image.size[1]
		pix = image.load()
		for j in range(height):
			for i in range(width):
				S = (pix[i, j][2] * 2) - (pix[i, j][0] + pix[i, j][1])
				S = 0 if S > 10 else 255
				if not S:
					bl += 1

		if bl > maxim:
			if time() - t1 > 6.5:
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.1)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				print(maxim)
				print('stop')
				break
			else:
				print(maxim)
				maxim = bl


for z in range(400000000):
	sleep(0.1)

	if keyboard.is_pressed(']'):
		t2 = time()
		print('Возьмите удочку в руки')
		sleep(1)

		s_on = 0.1
		s_po = 0.05

		fishs = 800
		for x in range(fishs):
			tt = time() - t2
			# if tt > 350:
			if tt > 800:
				break
			# 	print('в секунду:', round(tt / x, 3))
			# 	print('осталось времени:', (fishs - x) * (tt и/ x))
			win32api.keybd_event(0x1B, 0, 0, 0)  # esc
			sleep(s_on)
			win32api.keybd_event(0x1B, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(s_po)

			moveTo(469, 255)

			sleep(s_po)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
			sleep(s_on)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
			sleep(s_po)

			# moveTo(randint(0, 901), 700)
			moveTo(600, 733)

			sleep(s_po)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
			sleep(s_on)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
			sleep(s_po)

			win32api.keybd_event(0x1B, 0, 0, 0)  # esc
			sleep(s_on)
			win32api.keybd_event(0x1B, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(s_po)

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				break

		print('times')
		print()
		maximd()

	elif keyboard.is_pressed('['):
		maximd()
		# maxim_gold()

	elif keyboard.is_pressed('+'):
		print('йо-йо должно быть в ячейке 9')
		print('сачок должен быть в ячейке 8')
		sleep(3)
		moveTo(652, 495)

		while True:
			if keyboard.is_pressed('alt'):
				print('stop')
				break

			win32api.keybd_event(0x39, 0, 0, 0)  # клавиша 9
			sleep(0.1)
			win32api.keybd_event(0x39, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.05)
			# vsim
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(6)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

			win32api.keybd_event(0x38, 0, 0, 0)   # клавиша 8
			sleep(0.05)
			win32api.keybd_event(0x38, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.01)
			# vsim
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.2)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.1)

	elif keyboard.is_pressed('-'):
		print('run')
		kad = 1
		ttt = time()

		while True:
			if keyboard.is_pressed('alt'):
				print('stop')
				break


			for x in ['bots\\m1.PNG',
					  'bots\\m2.PNG',
					  'bots\\m3.PNG',
					  'bots\\m4.PNG',
					  'bots\\m5.PNG',
					  'bots\\m6.PNG',
					  'bots\\m7.PNG',
					  'bots\\a1.PNG',
					  'bots\\a2.PNG',
					  'bots\\a3.PNG',
					  'bots\\a4.PNG',
					  'bots\\a5.PNG',
					  'bots\\k1.PNG',
					  'bots\\k2.PNG',
					  'bots\\k3.PNG',
					  'bots\\k4.PNG',
					  'bots\\s1.PNG',
					  'bots\\z1.PNG',
					  'bots\\u1.PNG',
					  'bots\\ko1.PNG',
					  'bots\\ko2.PNG',]:

				if locateOnScreen(x, region=(250, 465, 400, 68), confidence=0.69):
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
					sleep(0.6)
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
					print(str(x), '| kps:', (kad - 1) / (time() - ttt))

				elif keyboard.is_pressed('alt'):
					print('stop2')
					break

				kad += 1






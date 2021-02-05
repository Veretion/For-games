from pyautogui import *
import keyboard
import win32con
import win32api
import threading
from time import sleep, time
from PIL import Image, ImageDraw






while True:
	sleep(0.05)
	if keyboard.is_pressed('='):
		print('run')
		for _ in range(10000000):

			# win32api.keybd_event(0x49, 0, 0, 0)
			# win32api.keybd_event(0x4F, 0, 0, 0)
			# sleep(0.1)
			# win32api.keybd_event(0x49, 0, win32con.KEYEVENTF_KEYUP, 0)
			# win32api.keybd_event(0x4F, 0, win32con.KEYEVENTF_KEYUP, 0)
			# sleep(0.5)
			# win32api.keybd_event(0x49, 0, 0, 0)
			# win32api.keybd_event(0x4F, 0, 0, 0)
			# sleep(0.1)
			# win32api.keybd_event(0x49, 0, win32con.KEYEVENTF_KEYUP, 0)
			# win32api.keybd_event(0x4F, 0, win32con.KEYEVENTF_KEYUP, 0)
			# sleep(5)

			## Ender
			# for i in range(40):
			# 	sleep(0.001)
			# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			# 	sleep(0.001)
			# 	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			# 	move(14)
			# 	if i == 20:
			# 		sleep(1)
			#
			# 	if keyboard.is_pressed('alt'):
			# 		print('выкл клик')
			# 		print()
			# 		break
			#
			# for i in range(40):
			# sleep(0.001)
			# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			# sleep(0.001)
			# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			# 	move(-14)
			# 	if i == 20:
			# 		sleep(1)
			#
			# 	if keyboard.is_pressed('alt'):
			# 		print('выкл клик')
			# 		print()
			# 		break

			# # Мусор
			# sleep(0.1)
			# for x in [0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39]:
			# 	win32api.keybd_event(x, 0, 0, 0)
			# 	sleep(0.1)
			# 	win32api.keybd_event(x, 0, win32con.KEYEVENTF_KEYUP, 0)
			# 	for i in range(110):
			# 		sleep(0.001)
			# 		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
			# 		sleep(0.001)
			# 		win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
			#
			# 	if keyboard.is_pressed('alt'):
			# 		print('выкл клик')
			# 		print()
			# 		break
			# break

			sleep(0.001)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
			sleep(0.001)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)




			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break






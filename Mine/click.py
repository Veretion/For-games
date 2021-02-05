from pyautogui import *
import keyboard
import win32con
import win32api
from random import randint


def clkm():
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
	sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
	sleep(0.01)


while True:

	sleep(0.01)
	if keyboard.is_pressed('v'):
		print('on click')
		sleep(0.00)
		for i in range(64):
			clkm()

			# move(randint(-500, 500), randint(-500, 500))

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

	sleep(0.01)
	if keyboard.is_pressed('k') and keyboard.is_pressed('l'):
		print('on click')
		sleep(0.00)
		while True:
			clkm()

			# move(randint(-500, 500), randint(-500, 500))

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

	# if keyboard.is_pressed('k') and keyboard.is_pressed('r'):
	# 	print('on click')
	# 	sleep(0.00)
	# 	while True:
	# 		win32api.keybd_event(0x44, 0, 0, 0)
	# 		sleep(1)
	# 		win32api.keybd_event(0x44, 0, win32con.KEYEVENTF_KEYUP, 0)
	#
	# 		sleep(1)
	#
	# 		win32api.keybd_event(0x41, 0, 0, 0)
	# 		sleep(1)
	# 		win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
	#
	# 		sleep(1)
	#
	# 		if keyboard.is_pressed('alt'):
	# 			print('выкл клик')
	# 			print()
	# 			break

	if keyboard.is_pressed('h') and keyboard.is_pressed('l'):
		print('on click')
		# sleep(0.00)
		for i in range(64):
			win32api.keybd_event(0x10, 0, 0, 0)
			sleep(0.04)

			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.04)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.04)

			win32api.keybd_event(0x10, 0, win32con.KEYEVENTF_KEYUP, 0)

			sleep(7.2)

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break
























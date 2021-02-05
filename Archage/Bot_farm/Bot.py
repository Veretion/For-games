from pyautogui import *
import keyboard
import mouse
import win32con
import win32api
from time import sleep, time
from PIL import Image, ImageDraw
# from pynput import Key



for z in range(400000000):
	sleep(0.01)

	if keyboard.is_pressed('3') and keyboard.is_pressed('2') and keyboard.is_pressed('1'):
		print('on click')
		sleep(0.01)

		def clkm(key):
			win32api.keybd_event(key, 0, 0, 0)
			sleep(0.003)
			win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.003)

		def pick(key, t):
			tt = time()
			while time() < (tt + t):
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					break
				clkm(key)

		for x in range(500000000):

			try:
				x, y = locateCenterOnScreen('ram.PNG', confidence=0.81)
				y += 65

				moveTo(x, y)

				sleep(0.5)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.05)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.1)


			except:
				sleep(0.01)
				continue



			# pick(0x34, 0.25)
			pick(0x33, 0.25)
			pick(0x32, 0.25)
			pick(0x35, 0.25)
			pick(0x52, 0.25)
			pick(0x53, 0.25)
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				break

			t = time()
			while time() < 3 + t:
				pick(0x31, 1)
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break
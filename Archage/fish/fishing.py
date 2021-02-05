from pyautogui import *
import keyboard
import win32con
import win32api
# import win32gui
# import threading
# import msvcrt
# import sys
# from random import randint, random, choice
from time import sleep, time
# from PIL import Image, ImageDraw
# import mouse
con = 0.90
X = ''
Y = 0

ran = (665, 808, 206, 80)
while True:
	sleep(0.1)
	if keyboard.is_pressed('+'):
		print('run')
		while True:
			print('con')

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

			# Y
			elif locateOnScreen('Y.PNG', region=ran, confidence=con):
				if X == 'Y':
					sleep(0.1)
					continue
				else:
					X = 'Y'
					Y = 0

					print(1)
					win32api.keybd_event(0x59, 0, 0, 0)
					sleep(0.05)
					win32api.keybd_event(0x59, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(0.7)

			# U
			elif locateOnScreen('U.PNG', region=ran, confidence=con):
				if X == 'U':
					sleep(0.1)
					continue
				else:
					X = 'U'
					Y = 0

					print(2)
					win32api.keybd_event(0x55, 0, 0, 0)
					sleep(0.05)
					win32api.keybd_event(0x55, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(0.7)

			# G
			elif locateOnScreen('G.PNG', region=ran, confidence=con):
				if X == 'G':
					sleep(0.1)
					continue
				else:
					X = 'G'
					Y = 0

					print(3)
					win32api.keybd_event(0x47, 0, 0, 0)
					sleep(0.05)
					win32api.keybd_event(0x47, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(0.7)

			# H
			elif locateOnScreen('H.PNG', region=ran, confidence=con):
				if X == 'H':
					sleep(0.7)
					continue
				else:
					X = 'H'
					Y = 0

					print(4)
					win32api.keybd_event(0x48, 0, 0, 0)
					sleep(0.05)
					win32api.keybd_event(0x48, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(0.7)

			# J
			elif locateOnScreen('J.PNG', region=ran, confidence=con):
				if X == 'J':
					sleep(0.1)
					continue
				else:
					X = 'J'
					Y = 0

					print(5)
					win32api.keybd_event(0x4A, 0, 0, 0)
					sleep(0.05)
					win32api.keybd_event(0x4A, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(0.7)

			else:
				if X == '':
					Y += 1
					if Y == 50:
						# win32api.keybd _event(0x54, 0, 0, 0)  # R
						# sleep(0.1)
						# win32api.keybd_event(0x54, 0, win32con.KEYEVENTF_KEYUP, 0)
						Y = 0
					sleep(0.05)
					continue
				else:
					X = ''
					sleep(0.05)
					continue






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
con = 0.8
X = ''
Y = 0

ran = (481, 854, 113, 18)
while True:
	sleep(0.1)
	if keyboard.is_pressed('+'):
		print('run')
		while True:

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

			# Y
			# elif locateOnScreen('test_sp.PNG', region=ran, confidence=con):
			# 	sleep(0.1)
			# 	print('con')

			else:
				win32api.keybd_event(0x52, 0, 0, 0)
				sleep(0.05)
				win32api.keybd_event(0x52, 0, win32con.KEYEVENTF_KEYUP, 0)
				sleep(10)





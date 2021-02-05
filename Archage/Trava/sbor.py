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

	if keyboard.is_pressed('='):
		print('on click')
		sleep(0.01)
		for x in range(50000000):
			win32api.keybd_event(0x46, 0, 0, 0)
			sleep(0.1)
			win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.3)

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				break






















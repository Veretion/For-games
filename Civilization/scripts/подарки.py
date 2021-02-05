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

con = 0.9

image = [345, 619, 592, 331]


def main():
	for i in range(5000):
		xc = locateCenterOnScreen('x1.PNG', region=image, confidence=0.96)
		moveTo(xc)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		sleep(0.03)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		moveTo(300, 300)
		sleep(0.03)
		if keyboard.is_pressed('alt'):
			print('выкл клик')
			print()
			return 1

		xc = locateCenterOnScreen('x2.PNG', region=image, confidence=0.96)
		moveTo(xc)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		sleep(0.04)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
		moveTo(300, 300)
		sleep(0.03)
		if keyboard.is_pressed('alt'):
			print('выкл клик')
			print()
			return 2


while True:
	sleep(0.5)
	if keyboard.is_pressed('ctrl'):
		main()
	elif keyboard.is_pressed('alt'):
		print('выход')
		print()
		exit()










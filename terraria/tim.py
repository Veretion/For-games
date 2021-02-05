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


def out_green(text):
	print("\033[92m {}".format(text))


def out_white(text):
	print("\033[37m {}".format(text))


while True:
	try:
		if locateOnScreen('AM.PNG', confidence=0.75, region=(967, 366, 82, 20)):
			if locateOnScreen('4.PNG', confidence=0.85, region=(965, 365, 25, 25)):
				for i in range(20):
					out_green('AAAAAAAAAAAAAAAAAAA')
				sleep(30)

			elif locateOnScreen('5.PNG', confidence=0.85, region=(967, 360, 82, 30)):
				for i in range(20):
					out_white('AAAAAAAAAAAAAAAAAAA')
				sleep(6 * 60)

				for i in range(40):
					print()

	except Exception as e:
		print(e)
		sleep(5)

	sleep(1)









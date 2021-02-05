from pyautogui import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import keyboard
import win32con
import win32api
import win32gui
import threading
import msvcrt
import sys
from random import randint, random, choice, choices, sample, shuffle
from time import sleep, time
from PIL import Image, ImageDraw
import mouse
import ast

os = [162, 137, 1117, 789]


def vas(osx, toch, slee, name):
	x, y = locateCenterOnScreen(name, region=osx, confidence=toch)
	moveTo(x, y)
	if keyboard.is_pressed('alt'):
		exit()

	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	sleep(0.04)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
	sleep(slee)


while True:
	try:
		try:
			if keyboard.is_pressed('alt'):
				exit()
			vas(os, .7, 1.4, "el.PNG")
			vas(os, .8, 2.7, "el1.PNG")
			vas(os, .8, 2.8, "el2.PNG")
			vas(os, .8, 2.6, "el3.PNG")
			vas(os, .9, 2.6, "el4.PNG")
			vas(os, .9, 2.6, "el5.PNG")
			vas(os, .9, 2.6, "el6.PNG")
			vas(os, .9, 2.6, "el7.PNG")
			vas(os, .9, 2.6, "el01.PNG")
			sleep(5)
		except:
			if keyboard.is_pressed('alt'):
				exit()
			vas(os, .50, 1, "el00.PNG")
			vas(os, .8, 1, "el0.PNG")
			vas(os, .8, 3, "el01.PNG")
			sleep(5)
	except:
		pass
























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


while True:
	sleep(0.1)
	if locateOnScreen("mass1.PNG", region=[772, 0, 122, 78], confidence=0.98):
		win32api.keybd_event(0x45, 0, 0, 0)  # =
		sleep(0.05)
		win32api.keybd_event(0x45, 0, win32con.KEYEVENTF_KEYUP, 0)  # =
		sleep(0.1)
		win32api.keybd_event(0x51, 0, 0, 0)  # =
		sleep(0.05)
		win32api.keybd_event(0x51, 0, win32con.KEYEVENTF_KEYUP, 0)  # =
		sleep(5)
		if keyboard.is_pressed('alt'):
			exit()
	if keyboard.is_pressed('alt'):
		exit()















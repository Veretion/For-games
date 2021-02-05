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

while True:
	if keyboard.is_pressed(']'):
		for i in range(10000):
			win32api.keybd_event(0x43, 0, 0, 0)  # esc
			sleep(0.01)
			win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)

			if keyboard.is_pressed('alt'):
				print('stop')
				break

# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# sleep(0.1)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)



















































































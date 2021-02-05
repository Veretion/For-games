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


for z in range(400000000):
	sleep(0.1)

	if mouse.is_pressed('x'):
		print('on click')
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
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
from random import randint, random, choice
from time import sleep, time
from PIL import Image, ImageDraw
import mouse


# def markers():
# 	dc = win32gui.GetDC(0)
# 	red = win32api.RGB(255, 0, 0)
#
# 	def zero(x, y):
# 		win32gui.SetPixel(dc, x, y, red)
#
# 	def krug(x, y):
# 		zero(x + 2, y + 2)
# 		zero(x + 1, y + 3);zero(x + 1, y + 4);zero(x + 1, y + 5)
#
# 	while True:
# 		sleep(0.001)
# 		krug(442, 123)

















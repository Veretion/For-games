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

window = Tk()
window.title("Полу-кликер")
window.geometry('600x300')


def press_key():
	for _ in range(40000000):
		if keyboard.is_pressed('ctrl'):
			print('stop')
			break
		# sleep(0.001)

		win32api.keybd_event(0x58, 0, 0, 0)
		# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
		sleep(0.001)
		win32api.keybd_event(0x58, 0, win32con.KEYEVENTF_KEYUP, 0)
		# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def clicked():
	keyboard.add_hotkey('alt', press_key)


btn = Button(window, text="Кликеp | alt", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()

clicked()

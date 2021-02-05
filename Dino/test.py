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

# name = 'test.PNG'
#
# end = '5'
#
# image = Image.open(name)
# draw = ImageDraw.Draw(image)
# width = image.size[0]
# height = image.size[1]
# pix = image.load()
# for i in range(width):
# 	for j in range(height):
# 		a = pix[i, j][0]
# 		b = pix[i, j][1]
# 		c = pix[i, j][2]
# 		S = (b + b) - (a + c)
# 		S = 0 if S > 64 else 255
# 		draw.point((i, j), (S, S, S))
#
# end_name1 = name[::-1].split('.', 1)[0][::-1]
# end_name0 = name[::-1].split('.', 1)[1][::-1] + '_kaktus_' + end
# end_name = end_name0 + '.' + end_name1
#
# image.save(end_name, "PNG")
#
#
# image = Image.open(name)
# draw = ImageDraw.Draw(image)
# width = image.size[0]
# height = image.size[1]
# pix = image.load()
# for i in range(width):
# 	for j in range(height):
# 		a = pix[i, j][0]
# 		b = pix[i, j][1]
# 		c = pix[i, j][2]
# 		S = b if a > b > c else 0
# 		S = 0 if 80 < S < 165 else 255
# 		draw.point((i, j), (S, S, S))
#
# end_name1 = name[::-1].split('.', 1)[0][::-1]
# end_name0 = name[::-1].split('.', 1)[1][::-1] + '_ptica_' + end
# end_name = end_name0 + '.' + end_name1
#
# image.save(end_name, "PNG")


def black():
	image = grab(region=(577, 446, 181, 200))

	# kaktus:
	bl = 9
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (b + b) - (a + c)
			S = 0 if S > 64 else 255
			if not S:
				bl += 1
	# draw.point((i, j), (S, S, S))

	# ptica
	draw = ImageDraw.Draw(image)
	width = image.size[0]
	height = image.size[1]
	pix = image.load()
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = b if a > b > c else 0
			S = 0 if 80 < S < 165 else 255
			if not S:
				bl += 1

	return bl
	# draw.point((i, j), (S, S, S))

while True:
	print(black())
	sleep(0.05)











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

import cv2


def pvp(name):
	while True:
		try:
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break
			if locateOnScreen(name, confidence=0.9, region=(481, 447, 338, 161)):
				x = locateCenterOnScreen(name, confidence=0.9, region=(481, 447, 338, 161))
				moveTo(x)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
				sleep(0.01)
				win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
				sleep(0.1)
			else:
				if round(time()) % 16 == 0:
					win32api.keybd_event(0x38, 0, 0, 0)  # R
					sleep(0.1)
					win32api.keybd_event(0x38, 0, win32con.KEYEVENTF_KEYUP, 0)
					sleep(1)

					if keyboard.is_pressed('alt'):
						print('выкл клик')
						print()
						break

					win32api.keybd_event(0x37, 0, 0, 0)
					sleep(0.1)
					win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)

				else:
					if keyboard.is_pressed('alt'):
						print('выкл клик')
						print()
						break

					sleep(0.3)

		except:
			sleep(0.01)


# pvp('pvp.PNG')


def detected(name):
	while True:
		if round(time()) % 10 == 0:
			try:
				click(locateCenterOnScreen('search_pak.PNG', confidence=0.9, region=(1085, 120, 116, 44)))
				click()
				sleep(0.1)

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break

				try:
					locateOnScreen(name, confidence=0.9, region=(1187, 207, 56, 29))
					print("\033[42m {}" .format('Норм'))
				except:
					if keyboard.is_pressed('alt'):
						print('выкл клик')
						print()
						break

					print("\033[41m {}" .format('AAAA'*999))
			except:
				sleep(0.01)

		else:
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break
			sleep(0.2)


# detected('92.PNG')


from PIL import Image, ImageGrab
import pytesseract
import cv2
import os

image = '92.PNG'


def image_to_text(image):

	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

	preprocess = "thresh"
	# preprocess = "blur"
	# preprocess = ''

	# загрузить образ и преобразовать его в оттенки серого
	image = cv2.imread(image)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# проверьте, следует ли применять пороговое значение для предварительной обработки изображения

	if preprocess == "thresh":
		gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# если нужно медианное размытие, чтобы удалить шум
	elif preprocess == "blur":
		gray = cv2.medianBlur(gray, 3)

	# сохраним временную картинку в оттенках серого, чтобы можно было применить к ней OCR

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)

	# cv2.imshow("Image", image)
	# cv2.imshow("Output", gray)
	# input('pause...')

	return text


sleep(1)

# pak = 'dush'
pak = 'ras_pis'

x, y = locateCenterOnScreen('dush.PNG', confidence=0.99)
# x, y = locateCenterOnScreen('dush100.PNG', confidence=0.99)
print(x, y)
if pak == 'dush':
	x, y, xx, yy = x + 90, y - 20, 60, 30
elif pak == 'ras_pis':
	xs, ys = 1248 - 1083, 243 - 227
	# xs, ys = 1248 - 1063, 243 - 227
	xs, ys = x + xs, y + ys
# xs, ys = xs + 167, ys
while True:
	try:
		# поиск кнопки "Поиск" и активация
		click(locateCenterOnScreen('search_pak.PNG', confidence=0.87, region=(921, 31, 349, 567)))
		# click(locateCenterOnScreen('search_pak100.PNG', confidence=0.87, region=(921, 31, 349, 567)))
		click()
		moveTo(500, 500)

		if keyboard.is_pressed('alt'):
			print('выкл клик')
			print()
			break

		if pak == 'ras_pis':
			moveTo(xs, ys)
			sleep(0.2)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.05)
			move(0, 250, duration=0.2)
			# move(0, 350, duration=0.2)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.1)


		if keyboard.is_pressed('alt'):
			print('выкл клик')
			print()
			break

		if pak == 'ras_pis':
			x, y = locateCenterOnScreen('ras_pis.PNG', confidence=0.95)
			# x, y = locateCenterOnScreen('ras_pis100.PNG', confidence=0.95)
			x, y, xx, yy = x + 90, y - 10, 50, 22

		red_img = ImageGrab.grab((x, y, x+xx, y+yy))
		red_img.save("92.PNG", 'PNG')
		text = image_to_text("92.PNG")
		print(text)
		text = text.split('%')[0]
		run = int(text)
		if pak == "ras_pis":
			if run >= 110:
				for _ in range(100):
					print("\033[41m {}".format((' ' * 99 + '\n') * 99))
					sleep(0.2)
					print("\033[0m {}".format((' ' * 99 + '\n') * 99))

					if keyboard.is_pressed('alt'):
						print('выкл клик')
						print()
						break
				sleep(0.2)

			elif run >= 100:

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break
				print(print("\033[43m {}" .format(' '*9999)))
				sleep(0.1)
			else:

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break
				print(print("\033[47m {}" .format(' '*9999)))
				print(text)

		if pak == "dush":
			if run >= 115:
				for _ in range(100):
					print("\033[41m {}".format((' ' * 99 + '\n') * 99))
					sleep(0.2)
					print("\033[0m {}".format((' ' * 99 + '\n') * 99))

					if keyboard.is_pressed('alt'):
						print('выкл клик')
						print()
						break
					sleep(0.2)

			elif run >= 100:

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break
				print(print("\033[43m {}" .format(' '*9999)))
				print(str(run))
				sleep(0.1)
			else:

				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break
				print(print("\033[47m {}" .format(' '*9999)))

	except Exception as e:
		# print(e)
		if keyboard.is_pressed('alt'):
			print('выкл клик')
			print()
			break
		sleep(0.1)












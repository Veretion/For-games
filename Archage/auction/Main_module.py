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
import pytesseract
import cv2
import os
from PIL import Image, ImageGrab

# requiriments
# разрешение экрана: 1280 1024
# размер интерфейса: 90%

sleep(3)


def man():
	z = 1
	while z:
		try:
			locateOnScreen('man.PNG', confidence=0.98)
			x = locateCenterOnScreen('man.PNG', confidence=0.98)
			z = 0
			return x

		except:
			print('название: "аукцион" не найдено:', z, 'раз')
			z += 1
			sleep(1)


def image_to_text(x, y, xx, yy):

	red_img = ImageGrab.grab((x, y, x + xx, y + yy))
	red_img.save("80.PNG", 'PNG')
	image = "80.PNG"

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


def detect(name):
	z = 1
	while z:
		if locateOnScreen(name, confidence=z):
			x = locateCenterOnScreen(name, confidence=z)
			print(x)
			print(z)
			break
		else:
			z = round(z - 0.01, 2)


# auc = man()
# moveTo(637, 198)
print(image_to_text(930, 371, 89, 19))












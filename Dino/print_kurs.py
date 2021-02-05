from pyautogui import *
import keyboard
from time import sleep


def cvet():
	while True:
		if keyboard.is_pressed('alt'):
			pos = tuple(int(i) for i in str(position()).split('x=')[1].split(')')[0].split(', y='))
			print('positio	n =', pos, '| cvet =', pixel(pos[0], pos[1]))
			sleep(0.3)


def region():
	while True:
		if keyboard.is_pressed('tab'):
			pos1 = list(int(i) for i in str(position()).split('x=')[1].split(')')[0].split(', y='))

			while keyboard.is_pressed('tab'):
				pos2 = list(int(i) for i in str(position()).split('x=')[1].split(')')[0].split(', y='))

			pos = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
			print(pos1 + pos)


region()
# cvet()

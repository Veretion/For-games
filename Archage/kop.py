from pyautogui import *
import keyboard
import mouse
import win32con
import win32api
from time import sleep, time
from PIL import Image, ImageDraw
# from pynput import Key
t = time()


for z in range(400000000):
	sleep(0.01)

	if keyboard.is_pressed('3') and keyboard.is_pressed('2') and keyboard.is_pressed('1'):
		print('on click')
		sleep(0.01)

		def clkm(key):
			win32api.keybd_event(key, 0, 0, 0)
			sleep(0.003)
			win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.003)

		def pick(key, t):
			tt = time()
			while time() < (tt + t):
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					break
				clkm(key)

		for x in range(50000000):
			pick(0x33, 0.25)
			sleep(0.05)
			pick(0x32, 0.25)
			sleep(0.05)
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				break

			t = time()
			while time() < 3 + t:
				pick(0x31, 1)
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					print()
					break

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

	# elif keyboard.is_pressed('+'):
	# 	print('on click')
	# 	sleep(0.01)
	# 	win32api.keybd_event(0x90, 0, 0, 0)
	# 	sleep(0.1)
	# 	win32api.keybd_event(0x90, 0, win32con.KEYEVENTF_KEYUP, 0)
	# 	sleep(0.1)
	# 	for x in range(50000000):
	#
	# 		win32api.keybd_event(0x54, 0, 0, 0)
	# 		sleep(0.1)
	# 		win32api.keybd_event(0x54, 0, win32con.KEYEVENTF_KEYUP, 0)
	# 		sleep(0.1)
	#
	# 		win32api.keybd_event(0x10, 0, 0, 0)
	# 		win32api.keybd_event(0x32, 0, 0, 0)
	# 		sleep(0.1)
	# 		win32api.keybd_event(0x10, 0, win32con.KEYEVENTF_KEYUP, 0)
	# 		win32api.keybd_event(0x32, 0, win32con.KEYEVENTF_KEYUP, 0)
	#
	# 		for _ in range(20):
	# 			sleep(0.5)
	# 			if keyboard.is_pressed('alt'):
	# 				print('выкл клик')
	# 				break
	#
	# 		if keyboard.is_pressed('alt'):
	# 			print('выкл клик')
	# 			print()
	# 			break

	elif keyboard.is_pressed('end') and keyboard.is_pressed('home'):
		print('test')
		sleep(5)
		win32api.keybd_event(0x23, 0, 0, 0)
		win32api.keybd_event(0x24, 0, 0, 0)
		sleep(0.1)

	elif keyboard.is_pressed('f'):
		try:
			if t + 0.1 < time():
				print('test')
			win32api.keybd_event(0x46, 0, 0, 0)
			sleep(0.01)
			win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(0.03)
			t = time()
		except:
			pass

	elif keyboard.is_pressed('-'):
		print('on click')
		sleep(0.01)
		for x in range(50000000):
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			sleep(0.01)
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			sleep(0.1)
			# win32api.keybd_event(0x52, 0, 0, 0)  # R
			# win32api.keybd_event(0x46, 0, 0, 0)
			# sleep(0.1)
			# win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)
			# win32api.keybd_event(0x52, 0, win32con.KEYEVENTF_KEYUP, 0) # R
			# sleep(0.1)

			# if win32api.GetKeyState(0x12):
			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

	# elif keyboard.is_pressed('-') and keyboard.is_pressed('+'):
	# 	print('on clickxxxx')
	# 	sleep(0.01)
	# 	for x in range(50000000):
	# 		sleep(0.2)
	# 		click(765, 392)
	# 		sleep(0.4)
	# 		click(910, 793)
	# 		sleep(0.4)
	# 		click(665, 488)
	# 		sleep(0.1)
	# 		click(665, 488)
	# 		sleep(0.4)
	# 		win32api.keybd_event(0x31, 0, 0, 0)
	# 		sleep(0.1)
	# 		win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0)
	# 		sleep(0.3)
	# 		click(604, 596)
	# 		# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	# 		# sleep(0.01)
	# 		# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
	# 		# sleep(0.1)
	# 		# win32api.keybd_event(0x52, 0, 0, 0)
	#
	# 		# if win32api.GetKeyState(0x12):
	# 		if keyboard.is_pressed('alt'):
	# 			print('выкл клик')
	# 			print()
	# 			break

	elif keyboard.is_pressed('0') and keyboard.is_pressed('1'):
		print('on click')
		sleep(0.01)
		for x in range(50000):
			win32api.keybd_event(0x30, 0, 0, 0)
			sleep(0.1)
			win32api.keybd_event(0x30, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(3)

			win32api.keybd_event(0x39, 0, 0, 0)
			sleep(0.1)
			win32api.keybd_event(0x39, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(3)

			win32api.keybd_event(0xA0, 0, 0, 0)
			win32api.keybd_event(0x37, 0, 0, 0)
			sleep(0.1)
			win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x37, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(3)

			win32api.keybd_event(0xA0, 0, 0, 0)
			win32api.keybd_event(0x34, 0, 0, 0)
			sleep(0.1)
			win32api.keybd_event(0xA0, 0, win32con.KEYEVENTF_KEYUP, 0)
			win32api.keybd_event(0x34, 0, win32con.KEYEVENTF_KEYUP, 0)
			sleep(3)

			for _ in range(60):
				sleep(0.25)
				if keyboard.is_pressed('alt'):
					print('выкл клик')
					break

			if keyboard.is_pressed('alt'):
				print('выкл клик')
				print()
				break

	# 11% 3237.12

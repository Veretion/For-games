

OR = 1785 + 2400 + 3000 + 2000 + 300
OR += 6*2500
print(OR)

pak = 0
rem = 37369
lvl = 3

while pak < 50:
	if lvl == 0:
		lvl = 1
	elif lvl == 1:
		lvl = 1
	elif lvl == 2:
		lvl = (100 - 5) / 100
	elif lvl == 3:
		lvl = (100 - 10) / 100
	elif lvl == 4:
		lvl = (100 - 15) / 100
	elif lvl == 5:
		lvl = (100 - 20) / 100
	elif lvl == 6:
		lvl = (100 - 20) / 100
	elif lvl == 7:
		lvl = (100 - 20) / 100
	elif lvl == 8:
		lvl = (100 - 20) / 100
	elif lvl == 9:
		lvl = (100 - 25) / 100
	elif lvl == 10:
		lvl = (100 - 30) / 100
	elif lvl == 11:
		lvl = (100 - 40) / 100

	OR -= lvl * 600
	rem += (lvl * 600) * 2
	pak += 1
	lvl = rem // 10000
	print(OR, lvl, rem, pak)
print(pak, OR)











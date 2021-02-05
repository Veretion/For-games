from itertools import combinations_with_replacement as comb, product


def vibor(param):
	test1 = []
	test2 = []
	test3 = []
	t1 = 0
	t2 = 0

	for i in tesot:
		if i[0][1] >= 0:
			test1.append(i)

	for i in test1:
		if i[0][2] >= t1:
			test2.append(i)
			t1 = i[0][2]
	test1 = []
	for i in test2:
		if i[0][2] == t1:
			test1.append(i)
	test2 = []

	for i in test1:
		if i[0][1] >= t2:
			test2.append(i)
			t2 = i[0][1]
	test1 = []
	for i in test2:
		if i[0][1] == t2:
			test1.append(i)
	test2 = []

	return test1[0]


# расклад города
ptk = [[1, 3, 4, 7, 9],  # каждый массив это место
	[11, 0, 2],  # каждый элемет в каждом массиве это связь
	[11, 1, 3],
	[2, 0, 4],
	[3, 0, 6, 5],
	[4],
	[4, 7],
	[6, 0, 8],
	[7, 9, 10],
	[8, 0, 10],
	[9, 11, 8],
	[10, 1, 2]]

num_points = 11
spor_pryan = 10.8  # пряности в минуту за ка
cen_dom = 25600
cen_raz = 12800
cen_zav = 19200
# ptk = [[2, 4, 6, 8, 9, 11],
# 	[2],
# 	[1, 0, 3, 4],
# 	[2],
# 	[2, 0, 5],
# 	[4, 6],
# 	[5, 0, 7],
# 	[6, 8],
# 	[7, 0, 9],
# 	[8, 0, 10, 11],
# 	[9, 0, 11],
# 	[10, 11]]
# ptk = [[2, 3, 7, 8],
# 	   [2],
# 	   [1, 0, 3],
# 	   [2, 0, 7, 4],
# 	   [3, 5, 6],
# 	   [4],
# 	   [4],
# 	   [4, 0, 8],
# 	   [7, 0, 9],
# 	   [8, 10],
# 	   [8, 9, 11],
# 	   [10]]
# ptk = [[2, 4, 6, 8, 10],
# 	[2],
# 	[0, 1, 3, 4],
# 	[2, 4],
# 	[0, 3, 2, 5, 6],
# 	[4],
# 	[4, 0, 8, 7],
# 	[6, 8],
# 	[7, 6, 0, 10],
# 	[10],
# 	[11, 9, 0, 8],
# 	[10]]
# ptk = [[2, 6, 8, 10],
# 	   [2],
# 	   [1, 0, 3, 4],
# 	   [2, 4],
# 	   [2, 3, 5, 6],
# 	   [4, 7],
# 	   [4, 0, 8],
# 	   [5, 8],
# 	   [0, 6, 7, 10],
# 	   [10],
# 	   [0, 8, 9, 11],
# 	   [10]]
# ptk = [[2, 4, 6, 8, 10],
# 	   [2],
# 	   [1, 3, 4, 0],
# 	   [2, 5],
# 	   [2, 0, 6, 5],
# 	   [3, 4, 6],
# 	   [0, 4, 5, 7, 8],
# 	   [6, 8],
# 	   [0, 6, 7, 9, 10],
# 	   [8, 10],
# 	   [0, 8, 9, 11],
# 	   [10]]
# ptk = [[8, 10],
# 	   [2],
# 	   [1, 4],
# 	   [5],
# 	   [2, 5, 6],
# 	   [3, 4],
# 	   [4, 7, 8],
# 	   [6, 8],
# 	   [6, 7, 0, 10],
# 	   [10],
# 	   [9, 8, 0, 11],
# 	   [10]]
ptk = [[1, 5, 6, 9],
	   [0, 2, 5],
	   [1],
	   [4, 5],
	   [3, 5],
	   [1, 0, 6, 5, 4],
	   [5, 0, 7],
	   [6, 8],
	   [7, 9],
	   [8, 0, 10],
	   [9, 11],
	   [10],]

points = []
tower = [0, 1, 2]

points.append(list(product(tower, repeat=num_points)))
points = points[0]
for n, i in enumerate(points):
	points[n] = [0] + list(i)

tesot = []
for p in points:
	place = [0, 0, 0, 0]
	okey = []
	if p == [0, 1, 0, 2, 2, 0, 0, 2, 0, 2, 0, 1]:
		print()
	for n, x in enumerate(p):

		okr1 = ptk[n]
		okr = [p[i] for i in okr1]
		if x == 0:
			place[0] += 15
			place[3] += cen_dom

			for ni, i in enumerate(okr):
				schet = str(n) + '-' + str(okr1[ni])
				if schet in okey:
					continue
				elif schet.split('-')[1] + '-' + schet.split('-')[0] in okey:
					continue
				else:
					okey.append(schet)

				if i == 1:
					place[1] += 1
				elif i == 2:
					place[2] += spor_pryan

		elif x == 1:
			place[1] += 1
			place[3] += cen_raz

			for ni, i in enumerate(okr):
				schet = str(n) + '-' + str(okr1[ni])
				if schet in okey:
					continue
				elif schet.split('-')[1] + '-' + schet.split('-')[0] in okey:
					continue
				else:
					okey.append(schet)

				if i == 0:
					place[1] += 1
				elif i == 2:
					place[1] -= 1

		elif x == 2:
			place[1] -= 1
			place[3] += cen_zav

			for ni, i in enumerate(okr):
				schet = str(n) + '-' + str(okr1[ni])
				if schet in okey:
					continue
				elif schet.split('-')[1] + '-' + schet.split('-')[0] in okey:
					continue
				else:
					okey.append(schet)

				if i == 0:
					place[2] += spor_pryan
				elif i == 1:
					place[1] -= 1
	tesot.append([place, p])


# просто лучшее значение
vis = vibor(tesot)
vis[0][2] = round(vis[0][2], 3)
vis[0][3] -= cen_dom

print()
print(vis[0])
print(vis[1])

# показать список значений >= -1
# itog = [i for i in tesot if i[0][1] >= -1]
# itog = sorted(itog, key=lambda x: x[0][2])[-400:]
# for i in itog:
# 	print(i)

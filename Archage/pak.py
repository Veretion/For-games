# 100%
# cen = 2612.87  # основная плата
cen = 2535.93
# cen = 2852
# cen = 3600
stavka = 70
srok = 115
dop_nad = 2
lvl = 8

res1 = 5 * 6
res2 = 300 * 1
cen_kraft = 50
zvezd = 2 * 130

# множители
stavka /= 100
srok /= 100
dop_nad = (100 + dop_nad) / 100


# формированиец цены
itog = cen * stavka
itog *= srok
itog *= dop_nad
if lvl == 0: lvl = 1
elif lvl == 1: lvl = 1
elif lvl == 2: lvl = (100 - 5) / 100
elif lvl == 3: lvl = (100 - 10) / 100
elif lvl == 4: lvl = (100 - 15) / 100
elif lvl == 5: lvl = (100 - 20) / 100
elif lvl == 6: lvl = (100 - 20) / 100
elif lvl == 7: lvl = (100 - 20) / 100
elif lvl == 8: lvl = (100 - 20) / 100
elif lvl == 9: lvl = (100 - 25) / 100
elif lvl == 10: lvl = (100 - 30) / 100
elif lvl == 11: lvl = (100 - 40) / 100

viu = str(round(itog, 2))
print('общая выручка: G' + viu.split('.')[0][::-1][2:][::-1] + ' S' + viu.split('.')[0][::-1][:2][::-1] + ' M' + viu.split('.')[1])


viu = str(round(itog*0.2, 2))
print('выручка производителя: G' + viu.split('.')[0][::-1][2:][::-1] + ' S' + viu.split('.')[0][::-1][:2][::-1] + ' M' + viu.split('.')[1])
viu = str(round(itog*0.8, 2))
print('выручка продавца: G' + viu.split('.')[0][::-1][2:][::-1] + ' S' + viu.split('.')[0][::-1][:2][::-1] + ' M' + viu.split('.')[1])
print()

itog -= res1
itog -= res2
itog -= cen_kraft
itog -= zvezd

viu = str(round(itog, 2))
print('монет: G' + viu.split('.')[0][::-1][2:][::-1] + ' S' + viu.split('.')[0][::-1][:2][::-1] + ' M' + viu.split('.')[1])

print('профит:', itog / (250 * lvl))








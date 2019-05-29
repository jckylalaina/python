# -*- coding: utf-8 -*-
tab = [0, 1]
print("la suite fibonacci entré un nombre")
n = input(">> ")
n = int(n)
for i in range(2, n):
    tab.append(i)
for i in range(1, n):
    tab[i + 1] = tab[i] + tab[i - 1]
print(tab)

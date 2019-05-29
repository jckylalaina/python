# -*- coding: utf-8 -*-
def tri(a):
    i = 0
    while i < len(a):

        j = i + 1

        while j < len(a):
            if a[j] > a[i]:
                x = a[i]
                a[i] = a[j]
                a[j] = x

            j += 1

        i += 1
    print(a)

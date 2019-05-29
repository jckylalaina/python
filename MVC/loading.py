import os
import time


def loading(result):
    i = 0
    a = ""
   
    while i < 25:
        
        print(result)
        time.sleep(0.08)
        os.system("clear")
        a += "#"
        print(a)
        i += 1

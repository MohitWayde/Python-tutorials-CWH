# 5-12-2020
# coroutines
# IF any particular code requires time to run then coroutine reduce the running time of code
# first time it will take required time 
# second time it will not take much time to run the code

import time
def fun_1():
    book = ['deepwork','tools of titans', 'rings of fire', 'ikigai']
#     some task require 4 sconds
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is no it the book")

ins = fun_1()
print("function started running")
next(ins)
print("next method ran")
ins.send("ikigai")
input("type anything")
ins.send("deepwork")

input("type anything...")
ins.send("rich dad poor dad")
ins.close()

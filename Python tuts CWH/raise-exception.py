# 13-12-2020
# Raise is use to fire exception when we dont want particular response (undesirable response) 
# so instead of running whole program we throws exception
a = input("enter the name")
if a.isnumeric():
    raise Exception("numbers are not allowed")
    
d = int(input("enter the salary"))
if d == 0:
    raise ZeroDivisionError("Zer0 is not allowed for salary input")

name = input("enter the name")
if name =="mmw":
    raise ValueError("mmw is blocked by admin")
    
    
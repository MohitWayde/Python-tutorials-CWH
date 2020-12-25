#try and except
try:
    num1 = int(input("enter the num 1 :\n"))
    num2 = int(input("enter the num 2 :\n"))
    print("addition of num1 and num2 is",num1+num2)
except Exception as e:
    print(e)
print("whatever the error is we are printing this msg >_<")
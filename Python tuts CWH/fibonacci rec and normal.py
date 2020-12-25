#fibbonacci series 
#17-10-2020
# 0+1+1+2+3+5+8+13........
# index wise fibonacci series
def fibonacci_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)
    
number = int(input("For which index location you want fibonacci series :"))
fibonacci_recursive(number)
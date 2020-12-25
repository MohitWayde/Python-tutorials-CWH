# 16-10-2020

def factorial_iterative(n):
    """
    factorial of number using iterative method
    f=f*(i+1)
    1=1*(0+1) is 1
    1=1*(1+1) is 2
    2=2*(2+1) is 6
    6=6*(3+1) is 24
    24=24*(4+1) is 120
    """
    f=1
    for i in range(n):
        f=f*(i+1)
    return f

def factorial_recursive(n):
    """
    5 * factorial_recursive(5-1)
    5 * 4 * factorial_recursive(4-1)
    5 * 4 * 3 * factorial_recursive(3-1) 
    5 * 4 * 3 * 2 * factorial_recursive(2-1)
    if n==0 or n==1:
        return 1
    5 * 4 * 3 * 2 * 1 = 120
    """
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

facto=int(input("enter the number :"))
print("Factorial of number using iterative method is :",factorial_iterative(facto))
print("Factorial of number using recuresive method is :",factorial_recursive(facto))
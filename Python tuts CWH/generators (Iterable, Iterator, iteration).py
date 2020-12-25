# 27-11-2020
# generators 
# Iterable - __iter__() or __getitem__()
# Iterator - __next__()
# And this is iteration-
# for i in range(5):
#     print(i)
# fibonacci and factorial programs for examples
def facto(m):
    if m==0 or m==1: #becoz 0 and 1 have factorial 1
        return 1
    else:
#         return m * facto(m-1)
        yield m * facto(m-1)
    
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
#         return fib(n-1) + fib(n-2) 
        yield fib(n-1) + fib(n-2) # this is generator we can use it when required
    
print("Fibonacci :",fib(7))
print("Factorial :",facto(7))



    
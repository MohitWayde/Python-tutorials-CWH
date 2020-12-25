# 31-10-2020
# map is used to  returns a map object(which is an iterator) of the results 
# after applying the given function to each item of a given iterable (list, tuple etc.)
# ------------MAP-------------

lis = [8,9,4,5,6,1,2,7,3,4]
# def squ(a):
#     return a * a
# def cub(b):
#     return b * b *b
maplistsqu = list(map(lambda x : x * x , lis))
maplistcub = list(map(lambda y : y * y * y,lis))
print(maplistsqu)
print(maplistcub)

def squ(a):
    return a * a
def cub(b):
    return b * b *b
allfunc=[squ,cub]
for i in range(5):
    maplist = list(map(lambda x : x(i) , allfunc))
    print(maplist)

    # --------------filter-------------
# Filter funtion filters the true values after passing an iterator
numlist = [1,2,3,4,5,6,7,8,9]
def greater_than_5(number):
    return number>5
filter_list = list(filter(greater_than_5, numlist))
print(filter_list)


# --------------REDUCE------------
# reduce function works same as map function
# it returns the result after iterating an iterator and apply particular given function

from functools import reduce
addlist = [1,2,3,4,5]
return_list=(reduce(lambda x, y :x + y, addlist))
print(return_list) #gives 1+2+3+4+5=15



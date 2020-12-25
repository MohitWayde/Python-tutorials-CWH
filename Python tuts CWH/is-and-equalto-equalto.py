# 13-12-2020
# "=="  represents value comparision
# "is" represents object comparision
a = [1,2,"3"]
b = [1,2,"3"]
print(a == b)#refers value
print(a is b) #refers object
c = ["mmw","smw","amw"]
d = c
if c==d:
    print("yes c is equal to equal to d")
if c is d:
    print("yes c is d")

e = a[:]
if e == a:
    print("yes e is equal to equal to a")
if e is a:
    print("e is a")
# 30-11-2020
# Python comprehentions

# ordinary way
li = []

for i in range(100):
    if i%2==0:
        li.append(i)
print("ordinary list",li)

# pythonic way - list comprehensions
li = [i for i in range(100) if i%2==0]
print("Pythonic list with comprehentions",li)

# 30-11-2020
# ordinary way
for i in range(10):
    dict1 = {i : f"item{i}"}
    print("Ordinary dictionary ",dict1)
    
# Pythonic way  - dictionary comprehentions
dict1 = {i : f"item{i}" for i in range(10)}
print("\nPythonic dictionary with comprehention",dict1)

# 30-11-2020
# Ordinary way of set

for i in {'dress1', 'dress2', 'dress1', 'dress2','dress1', 'dress2','dress1', 'dress2'}: 
    print("ordinary set",i)
# set comprehension pythonic way
set1 = {dress for dress in ['dress1', 'dress2', 'dress1', 'dress2','dress1', 'dress2','dress1', 'dress2']}
print(set1)

# 30-11-2020
# ordinary way of generators
def gener(n):
    for i in range(n):
        yield i

a = gener(5)
print(a.__next__())

# pythonic way of generators (but not working)
gener = (i for i in range(5))
a = gener
print(a.__next__())
print(a.__next__())
print(a.__next__())

# 30-11-2020
# Quiz
leng = 3 #int(input("Enter the length of the list"))
for i in range(leng):
    inp = list(input("enter the data :"))
what = input("what comprehentions:list/dict/set :")

if what == "dict":
        for i in range(len(inp)):
            dictn = {inp[i]: inp[i + 1] for i in range(0, len(inp),2)}
        
            print("\nPythonic dictionary with comprehention ",dictn)
elif what =="set":
    for i in range(3):
        set1 = {data for data in inp}
        print(set1)
else:
    print("something went wrong")

# Just for reference
# Python3 program to Convert a 
# list to dictionary

# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst),3)}
#     return res_dct

# Driver code
# lst = ['a', 1, 'b', 2, 'c', 3 ,'d', 4]
# print(Convert(lst))


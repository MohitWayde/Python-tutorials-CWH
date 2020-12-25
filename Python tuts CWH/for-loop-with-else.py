# 1-12-2020
# for loop with else
# content of else statement didnt work if we put break statement in for loop
lst = ["m","w","a","s"]
for i in lst:
    print(i)
else:
    print("The program terminated properly")

print("for loop with break statement")
for i in lst:
    print(lst[3])
    break
    
else:
    print("The program terminated properly")
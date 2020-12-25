size = int(input("Enter the size of the list :"))
calories = []
for i in range(size):
    calories.append(int(input("enter the elements of the list :")))
    print(calories)
# hardcoded list
# calories = [77,55,88,44,66,22,11]

# with inbuilt function 
reverse1 = calories[:]
reverse1.reverse()
print("reverse method 1 :")
print(f"1the original list is {calories}")
print(f"1The reversed list is {reverse1}")

# list slicing
reverse2 = calories[::-1]
print("reverse method 2")
print(f"2the original list is {calories}")
print(f"2the reversed list is {reverse2}")

# swapping
reverse3 = calories[:]
for i in range(0, len(reverse3)//2):
    # pythonic way
    reverse3[i], reverse3[len(reverse3)-i-1] = reverse3[len(reverse3)-i-1], reverse3[i]
'''
    for understanding purpose
    print(f"reverse3[{i}], reverse3[{len(reverse3)}-{i}-1] = reverse3[{len(reverse3)}-{i}-1], reverse3[{i}]")
    print(f"{i}->>{reverse3}")
'''
print("reverse method 3")
print(f"3The original list is {calories}")
print(f"3The reversed list is {reverse3}")
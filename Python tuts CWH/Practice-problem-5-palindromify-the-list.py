def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

# size = int(input("Enter the size of the list :"))
# numbers = []
# for i in range(size):
#     numbers.append(int(input(f"enter the number {i+1} element of the list :")))
#     print(numbers)
numbers = [1,6,59,89]
new_list = []
for i in numbers:
    if i > 10:
        s = next_palindrome(i)
        new_list.append(s)
    else:
        new_list.append(i)
print("palindromified the list is ",new_list)

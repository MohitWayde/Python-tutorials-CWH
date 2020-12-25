def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n


if __name__ == "__main__":
    size = int(input("Enter the size of the list :"))
    numbers = []
    for i in range(size):
        numbers.append(int(input("enter the elements of the list :")))

    for i in range(size):
        print(f"THe next palindrome of {numbers[i]} is {next_palindrome(numbers[i])}")
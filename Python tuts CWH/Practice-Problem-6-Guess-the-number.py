import random
def guess(target_number,chcount):
    print("Welcome to the game of guess the number")
    print(f"you have {chances} chances")
    while chcount !=chances:
        user_input1 = int(input(f"Enter your guess {chcount+1}:"))
        if user_input1 < target_number:
            print("You entered the LESSER number than target number")
            chcount += 1
        elif user_input1 == target_number:
            chcount += 1
            print(f"You required {chcount} chances to guess the number")
            break
        elif user_input1 > target_number:
            print("You entered the GREATER number than target number")
            chcount += 1
        else:
            print("Something went wrong!!")
    else:
        print("Your chances are completed!")
    return chcount


a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
chances = b//2
chcount = 0
print(f"The range of numbers is {a} to {b}")
print(f"Player 1 will play first")
target_number1 = random.randint(a,b)
p1 = guess(target_number1, chcount)

print(f"Player 2 will play now")
target_number2 = random.randint(a,b)
p2 = guess(target_number2, chcount)

if p1 < p2:
    print(f"player 1 won")
elif p1 > p2:
    print(f"player 2 won")
elif p1 == p2:
    print(f"tie game")
print(f"The targer number for player 1 is {target_number1}")
print(f"The targer number for player 2 is {target_number2}")

import random
ran_pos = random.randint(4,10)
def wrongMul(table_number):
    table_list = [i*table_number for i in range(1,11)]
    table_list[ran_pos-1] = table_list[ran_pos-1] + random.randint(1,10)
    print(table_list) # fraud table
    # print(len(table_list))


def isCorrectMul(table_number):
    table_list = [i*table_number for i in range(1,11)]
    table_list[ran_pos-1] = table_list[ran_pos-1] + random.randint(1,10)
    print("Wrong mul :", table_list)

    # Correct mul
    
    right_table = [i*table_number for i in range(1,11)]
    for j in range(10):
        if right_table[j] != table_list[j]:
            print(f"Fraud at position {j+1}")
    print("Right mul is", right_table)
    



if __name__ == "__main__":
    table_number = int(input("Enter the number for printing the table :"))
    a = wrongMul(table_number)
    fr = int(input("Check fraud, press 1 :"))
    if fr==1:
        b = isCorrectMul(table_number)





'''   
# CodeWithHarry's code
import random

def rohanMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            print("Check this ",table[i-1])
            return i - 1 

    return None

if __name__ == "__main__":
    # print(rohanMultiplication(7))
    number = int(input("Enter a number: "))
    myTable = rohanMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
'''   


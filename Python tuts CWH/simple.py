time='3pm'
if time=='9am':
    print("GOOD MORNING")
elif time=='3pm':
    print("GOOD AFTERNOON")
else:
    print("GOOD NIGHT")
    
    
time='9am'
if time=='9am':
    print("GOOD MORNING")

i=0
while i<10:
    print(i)
    i+=1
else:
    print("i is greate the than 10")
    
lst = [10, 20, 30, 40, 50]
product = 1
#iterating over the list
for ele in lst:
    product *= ele

print("Product is:",str(product))

def multiplication(a,b):
    c=a*b
    return c
multiplication(10,20)


#SWITCH CASE

def switch():
    a=int(input("enter the first operand :"))
    b=int(input("enter the second operand :"))
    print("1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n")
    ch=int(input("enter the choice :"))
    def addition():
        c = a + b
        print("addition is ",str(c))
    def subtraction():
        c = a - b
        print("subtraction is ",str(c))
    def multiplication():
        c = a * b
        print("multiplication is ",str(c))
    def division():
        c = a / b
        print("division is ",str(c))
        
    dictionary={
        1:addition,
        2:subtraction,
        3:multiplication,
        4:division
    }
    dictionary.get(ch)()   
    
switch()
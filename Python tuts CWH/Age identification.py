# age for driving vehicle
age=int(input("enter your age :"))
if age>=7 and age<18:
    print("your age is lesser than 18, You cannot drive")
elif age==18:
    print("issue your driving licence")
elif(age>18 and age<=100):
    print("your age is greater than 18, you can drive")
else:
    print("invalid input")
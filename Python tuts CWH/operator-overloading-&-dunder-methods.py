# 19-11-2020
# operator overloading & dunder methods
# Dunder methods are special methods used to do operator overloading
class Employee:
    def __init__(self,aname, asal):
        self.name = aname
        self.sal = asal
    def printname(self):
        print("The name is ",self.name)
        print("The salary is ",self.sal)
    def __add__(self,other):
        return self.sal + other.sal
    
    def __repr__(self): # have to call
        return f"The name is {self.name} and the salary is {self.sal}.This is repr"
    
    def __str__(self):# automatically call
        return f"The salary is {self.sal}, The name is {self.name}.This is str"

ob1 = Employee("mohit",5000)
ob2 = Employee("anu",400)
ob1.printname()

print(ob1 + ob2)
print(ob1)
print(repr(ob1))
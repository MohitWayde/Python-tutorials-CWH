# 9-11-2020
# class and object oriented programming

class Student:
    print("this is student class")
    def function_name(self):
        print("Function")
        return "method inside class \"Student\" printed successfully "
m = Student()
print(m.function_name())

# 9-11-2020 and 12-11-2020
# self and __init__ constructor
# self is used for identifying from which instance you are accessing particular method
# in above example "mohit" is went in "self"

class Collage_data:
    '''THis is docstring of class'''
    def __init__(self,abr,arn):
        self.br = abr
        self.rn = arn
    def print_data():
        return f"Branch is {br} & roll number is {rn}"
    
mohit = Collage_data("computer", 94)
rohit = Collage_data("mechatronics", 10)
print(mohit.br)
print(mohit.rn)
print(rohit.br)
print(rohit.rn)

print(mohit.__dict__) #dictionary for class information
print(mohit.__doc__) #docstring 
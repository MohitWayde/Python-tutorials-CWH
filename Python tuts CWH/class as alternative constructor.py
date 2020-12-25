# 12-11-2020
# class method as alternative constructor
class Collage_data:
    '''THis is docstring of class'''
    no_of_projects = 5
    def __init__(self,abr,arn):
        self.br = abr
        self.rn = arn
    def print_data():
        return f"Branch is {br} & roll number is {rn}"
    
    @classmethod
    def change_project(cls, newprojects):
        cls.no_of_projects = newprojects
    @classmethod
    def seperator_function(cls,anystring):
#        orthodox method
#         thestr = anystring.split("-")
#         return cls(thestr[0],thestr[1])

#        Pythonic method
        return cls(*anystring.split("-"))
    
mohit = Collage_data("computer", 94)
rohit = Collage_data("mechatronics", 10)
maruti = Collage_data.seperator_function("IT-27")

print("MOhit branch :",mohit.br)
print("Mohit roll number :",mohit.rn)
print("Rohit branch :",rohit.br)
print("Rohit roll number :",rohit.rn)

# Accessed by class method as alternative constructor
print("Branch of maruti :",maruti.br)
print("Roll number of maruti :",maruti.rn)
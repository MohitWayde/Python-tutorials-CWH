# 12-21-2020
# class methods are used to change the content of class ONLY.
# with the help of "@classmethod" decorator and "cls" argument , we can use classmethod
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
    
mohit = Collage_data("computer", 94)
rohit = Collage_data("mechatronics", 10)


print("MOhit branch :",mohit.br)
print("Mohit roll number :",mohit.rn)
print("Rohit branch :",rohit.br)
print("Rohit roll number :",rohit.rn)
print("No of projects are :", Collage_data.no_of_projects)
Collage_data.change_project(10)
print("changed projects are :",Collage_data.no_of_projects)

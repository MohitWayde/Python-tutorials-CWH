# 12-11-2020
# Inheritance= Deriving new class from base class

class student:
    def __init__(self,afirst,alast):
        self.first = afirst
        self.last = alast
    def printdata(self):
        print(f"first name is {self.first}")
        print(f"last name is {self.last}")
        return "This is a return statement"
    
class programer(student):
    pass

enrolled = programer("mohit","wayde")
print(enrolled.printdata())
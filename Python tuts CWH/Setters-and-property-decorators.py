# 23-11-2020
# Setter and property decorators
# if we want to convert function as an attribute, we'll use setter and property
class Employee:
    def __init__(self,afname, alname):
        
            self.fname = afname
            self.lname = alname
    def printname(self):
        return f"the full name of employee is {self.fname} {self.lname}"
    
    @property
    def printemail(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @printemail.setter
    def printemail(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    
    @printemail.deleter #for deleting setter
    def printemail(self):
        self.fname = None
        self.lname = None
        
        
zentex = Employee("Anish", "Khairnar")
print(zentex.printname())
print(zentex.printemail)
# after change
zentex.fname = "Anushka"
print(zentex.printemail)

del zentex.printemail#for deleting setter
print(zentex.printemail)

# Setting new one
zentex.printmail = "anish.khairnar@gmail.com"
print(zentex.printmail)
# 21-11-2020
# abstract method is used to set a rule for child classes that 
# any particular method is compulsory for all child classes

# NO need to import these files, it'll work without importing
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0
class Rect(Shape):
    def __init__(self):
        self.length = 5
        self.breadth = 5
    def print_area(self):
        return self.length * self.breadth
class Square(Shape):
    def __init__(self):
        self.side = 10
    def print_area(self):
        return self.side * 4

r = Rect()
s = Square()
r.print_area()
s.print_area() #run one by one (one method /class/ object at atime)
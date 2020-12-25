class A:
    def __init__(self):
        var1 = "I am var1 from A"
        var2 = "I am var2 from A"
        print(var1)
        print(var2)
        
class B(A):
    def __init__(self):
        var3 = "I am var3 from B"
        print(var3)
    def fun1(self):
        super().__init__()
        
a = A()
b = B()
b.fun1()
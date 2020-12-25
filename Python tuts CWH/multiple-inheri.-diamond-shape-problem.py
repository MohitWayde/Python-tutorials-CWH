# 19-11-2020
# multiple inheritance
# diamond shape problem
class A:
    def method_a(self):
        print("This is method of A class")
class B(A):
    pass

class C(A):
    pass

class D(B , C):
    pass

a = A()
b = B()
c = C()
d = D()
d.method_a()
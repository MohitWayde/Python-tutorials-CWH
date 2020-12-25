# 12-11-2020
# static methods are used for simplicity and effecient purpose
# If you dont waht to use self for methods OR want to do some static work 
# use decorator "@staticmethod" to use the functionality for static method
class employee_class:
    @staticmethod
    def static_method(a,b):
        print(a+b)
        print(a-b)
    def static_method2():
        print("this is second static method")

abc = employee_class.static_method(77,33)
xyz = employee_class.static_method2()
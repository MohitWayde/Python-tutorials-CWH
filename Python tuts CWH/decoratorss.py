# 4-10-2020
# Decorators are used to perform same operations on different multiple functions
# replicate abc = xyz(abc)
# replicate function1 = function2(function1)

# Yeh hai aam jindagi
def decorator1(function1):
    def nowexec():
        print("You are in nowexec waiting for decorator to execute")
        function1()
        print("The wait is over decorator function executed")
    return nowexec   
def in_parameter():
    print("11111111111111111this is the function for giving in parameter1111111")

in_parameter = decorator1(in_parameter)
in_parameter()

# Yeh hai decorator jindagi

@decorator1
def for_parameter():
    print("2222222222this is the second function for giving in the parameter2222222")
for_parameter()

def addition_decorator(funtion_as_param):
    def addo(a,b):
        return a+b
    return addo

@addition_decorator
def int_addition(a,b):
    print("Int values")

@addition_decorator
def float_addition(c,d):
    print("float values")
    
float_addition(64.4,135.6)
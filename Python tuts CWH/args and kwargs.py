# 22-10-2020
# *args and **kwargs
# *args=Argument which is dynamic as it update according to content
# **kwarge=Arguments that can allow key value pairing
def function_name_print(*args,**kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is {value}")
        
ar = ["mohit","programming","technology","passioneer","futuristic"]
kw = {"mohit":"passioneer", "hobby":"enjoying", "programming":"passion"}
function_name_print(*ar,**kw)
# 16-11-2020
# access specifier
#single underscore represents protected variable
#double underscore represents private variable
class Ele:
    _protected = 4       #single underscore represents protected variable
    __private = "private accessed" #double underscore represents private variable
a = Ele()
print(a._protected)
print(a._Ele__private) 

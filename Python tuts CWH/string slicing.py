mystr = "My name is MOHIT"
print(mystr[6])
print(mystr[0:6])
print(mystr[11:16])
print(mystr[11:])
print(mystr[:16])
print(mystr[:])
print(mystr[::])
print(mystr[::2])
print(mystr[::3])
print(mystr[::-1])
print(mystr[::-2])
print(mystr[:16:-2])

# len
print(len(mystr))
# isalnum
print(mystr.isalnum())
# isalpha
print(mystr.isalpha())
# endswith
print(mystr.endswith("MOHIT"))
print(mystr.endswith("mohit"))
# count
print(mystr.count("M"))
# capitalize
print(mystr.capitalize())
# find
print(mystr.find("MOHIT"))
# lower 
print(mystr.lower())
# upper
print(mystr.upper())
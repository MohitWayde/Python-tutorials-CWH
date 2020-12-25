# 4-12-2020
# Try, Except, finally, else
# You already know anout try and except
# finally is used to run particular code compulseryily irrespective of
# try or except is already ran or not
# finally is also used for code clean up
# else is used when except didnt run

try:
    f1 = open("demo.html")
except Exception as e:
    print(e)
else:
    print("This will run if except didnt work")

finally:
    print("this will run irrespective of anything :p")
    

print("Importent stuff!.....")


try:
    f1 = open("mohit.txt")
    
except Exception as e:
    print(e)
    
else:
    print("ELSE is running!!! because program doesnt go in except")
    
finally:
    print("this will run irrespective of anything :p")
 


print("Importent stuff!.....") 



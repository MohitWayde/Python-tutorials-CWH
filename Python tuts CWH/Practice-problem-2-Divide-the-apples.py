try:
    n = int(input("Enter the mangoes you have :"))
    min = int(input("Enter the min. no. of apples you want to give to the students"))
    max = int(input("Enter the max. no. of apples you want to give to the students"))

except Exception as e:
    print(e)
    
for i in range(min, max+1):
    if min==max:
        print(f"this is not a range OR min={min} is equal to max={max}")

    elif n%min==0:
        print(f"{n} is divisor of {min}, You can give equal number of apples to everyone")
        min+=1
    
    elif n%min!=0:
        print(f"{n} is not divisor of {min},You can give equal number of apples to everyone")
        min+=1

    

    else:
        print("Something went wrong")
    

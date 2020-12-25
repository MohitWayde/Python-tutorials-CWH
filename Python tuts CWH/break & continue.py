#5-10-2020
#break and continue
#WAP for accept input i.e less than hundred until it crossed 100,
#if number is greater than 100, print congrats
i=int(input("enter the number"))
while True:
    if i<100:
        print("the value is ",i)
        i=i+1
        continue
    else:
            print("congratulations you reached 100")
            break

# 23-10-2020
import time
import datetime
first=input("0 or 1 :")
if first=='1':
    initial=time.time() # returns time ticks which is seconds
    print(initial)
    for i in range(5):
        print("This is the program of time module with for loop")
        time.sleep(1) #sleep for given seconds
        print(time.time()-initial)

#     w=5
#     while w<10:
#         print("This is the program of time module with while loop")
#         w+=1
#         time.sleep(1) #sleep for given seconds
#         print(time.time()-initial)
elif first=='0':
    print(datetime.datetime.now())


import time
# globaltime = time.time()
mytime = time.strftime("%H %M")
print(mytime)


import time, datetime
with open("mohit_exercise.txt","a") as f1:
    mytime = time.strftime("%H"":""%M")
    f1.write(f"{mytime} : {datetime.datetime.now()} \n")
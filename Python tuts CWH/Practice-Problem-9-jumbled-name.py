
import random
n = int(input("Enter the number of student: "))
f = random.randint(1,n-1)
l = random.randint(1,n-1)

st_list=[]
for i in range(n):
    st_list.append((input(f"Enter the full name of the student number{i+1}: ")))
print(st_list)


for i in range(0,n):
    f=random.randint(0,n-1)
    s=random.randint(0,n-1)
    f1=st_list[f].split(' ',2)
    s1=st_list[s].split(' ',2)
    print(f"◆ {f1[0]} {s1[1]}")




'''
import random
list1=[]

def add_name(n):
	global list1
	for i in range(0,n):
		list1.append(input(f"Enter {i+1} no name :"))

def show_name(n):
	global list1
	print("Your Friend List :\n")
	for i in range(0,n):
		f=random.randint(0,n-1)
		s=random.randint(0,n-1)
		f1=list1[f].split(' ',2)
		s1=list1[s].split(' ',2)
		print(f"◆ {f1[0]} {s1[1]}")
		
n=int(input("Enter Numbers of friend :"))
print("\nEnter the name of your {} friends \n".format(n))
add_name(n)
show_name(n)

'''
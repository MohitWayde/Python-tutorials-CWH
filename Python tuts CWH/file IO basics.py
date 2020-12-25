# 10-10-2020
# Will cause error as no file not found so create a txt file and give it to this program
'''
File IO Basics
'r' - open file for reading
'w' - open file for writing
'x'- (exclusive) create file if not exist
'a' - (append) add more content to a file
't' - text mode
'b' - binary mode
'+' - read and write both
'''

f=open("mohit.txt", "rt")#read + text mode
content=f.read()
print(content)
f.close()

for line in content:
    print(line)

for line in f:
    print(line)

# print(f.readline())#used to print single line at a time
print(f.readlines())

# 11-10-2020
# File writing
f= open("mohit.txt","a")
f.write("I love to play tabla\n")
f.close()

f= open("mohit.txt","a")
f.write("I want to create projects\n")
f.close()

f= open("mohit.txt","r+")
f.write("Thank you\n")
f.close()

# 12-10-2020
f=open("mohit.txt")
print(f.readline())
print(f.tell())  #tell() used to tell new line's number(File pointer) 
print(f.readline())
print("Tell from where to start reading or to seek",f.seek(20))  #seek() used for read the file from given input
print(f.readline())
print(f.readline())
f.close()

# 13-10-2020
#In with block we dont needs to type close() for closing the file it automatically closes file
with open("mohit.txt") as f:
    a=f.readline(16)
    print(a)
    
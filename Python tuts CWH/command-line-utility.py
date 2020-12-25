# 14-12-2020
# create command line utility for faulty calculater
# https://www.youtube.com/watch?v=Qi-8zaBfRWI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=94
# 45*3=555 
# 56+9=77
# 56/6=4

# Save this in .py file and run with cmd
import argparse
import sys
def faulty(args):
#     first condition
    if args.a == 45 and args.b == 3 and args.o == 'mul':
        return '555'
    
#     second condition
    if args.a == 56 and args.b == 9 and args.o == 'add':
        return '77'
    
#     third condition
    if args.a == 56 and args.b == 6 and args.o == 'div':
        return '4'
    
        

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type=float)
    parser.add_argument('--b', type=float)
    parser.add_argument('--b', type=str)
    
    args = parser.parse_args()
    sys.stdout.write(str(faulty(args)))
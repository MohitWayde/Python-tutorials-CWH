# 20-10-2020
#External and built-in functions
import random
r=random.randint(100,200)
print(r)
# c = ('s','w','g')
ch=random.choice(('s','w','g'))
print(ch)

import seaborn as sns
a=[1,2,3]
b=[6,3,10]
sns.relplot(x=a,y=b)
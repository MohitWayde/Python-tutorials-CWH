# 2-12-2020
# Function caching(LRU cache)
# for doing function caching @lrucache decorator is used
# lrucache decorator used to shorten the execution time
# Suppose there is a function that tooks 10 seconds to run 
# So instead of waiting, We can store them in cache
# After calling first time it will get stored into cache and if we call the function again
# then it will invoke function from cache according to maxsize(n) argument

import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    print(f"{n} seconds wasted")


some_work(5)
print("Function ran")
some_work(5)
print("function ran again")
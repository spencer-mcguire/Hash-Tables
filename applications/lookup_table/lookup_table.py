import math
import random

cache = {}
def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    # takes in x and y
    # raises x to the power of y = v
    v = math.pow(x, y)
    
    #store in a cache  so this computation doesnt have to run again
    # if KEY: v exists in the cache use that value (factorial), else: compute and store the factorial 
    if v not in cache:
        print(f"NOT in cache: {v}")
        cache[v] = math.factorial(v)
        value = cache[v]
        value //= (x + y)
        value %= 982451653

        return value 
    
    else:
        print(f"in cache: {v}")
        stored = cache[v]
        stored //= (x + y)
        stored %= 982451653
        return stored


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

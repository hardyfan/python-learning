from functools import reduce

def add(x,y):
    return x*10+y

l = [1,3,5,7,9]
r = reduce(add,l)

print(r)
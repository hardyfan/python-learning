def is_odd(n):
    return n%2 == 1

l = [1,2,4,5,6,7,9,10,15]

r = list(filter(is_odd, l))

print(r)
# 迭代器
ll = [1, 2, 3, 4, 5]
it = iter(ll)

print(next(it))
print(next(it))
for x in it:
    print(x, end=",")

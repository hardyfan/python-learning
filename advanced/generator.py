# 生成器:生成器是创建迭代器的一种简便的方法


g = (x * x for x in range(1, 11))
print(g)
print(next(g))

for n in g:
    print(n, end='  ')

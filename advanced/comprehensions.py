from datetime import datetime

# 推导式


# 列表推导式
def getstrt(str, max):
    l = ["{i}.{s}\n".format(i=i, s=str) for i in range(max)]
    return ''.join(l)


# 字典推导式
def getdict(d):
    d1 = {k.lower():d.get(k.lower(),0)+d.get(k.upper(),0)
          for k in d
          if k.lower() in ['a','b']}
    return d1


def getset(l):
    return {x ** 2 for x in l}


if __name__ == '__main__':
    str = 'hello world!hello world!hello world!hello world!hello world!hello world!hello world!'
    max = 1000000

    btime = datetime.now()
    str3 = getstrt(str, max)
    etime = datetime.now()
    print(etime - btime)

    d = {'a': 10, 'b': 32, 'A': 4, 'C': 6, 'B': 0}
    d1 = getdict(d)
    print(d1)

    # 集合推导式
    s = getset([1, 1, 2, 4])
    print(s)

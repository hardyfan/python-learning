from datetime import datetime


def get_str(str, max):
    """
    列表推导式
    :param str:
    :param max:
    :return:
    """
    return ''.join(["{i}.{s}\n".format(i=i, s=str) for i in range(max)])


def get_dict(dict1):
    """
    字典推导式
    :param d:
    :return:
    """
    d1 = {k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0)
          for k in d
          if k.lower() in ['a', 'b']}
    return d1


def getset(l):
    """
    集合推导式
    :param l:
    :return:
    """
    return {x ** 2 for x in l}


if __name__ == '__main__':
    str = 'hello world!hello world!hello world!hello world!hello world!hello world!hello world!'
    max = 1000000

    btime = datetime.now()
    str3 = get_str(str, max)
    etime = datetime.now()
    print(etime - btime)

    d = {'a': 10, 'b': 32, 'A': 4, 'C': 6, 'B': 0}
    d1 = get_dict(d)
    print(d1)

    s = getset([1, 1, 2, 4])
    print(s)

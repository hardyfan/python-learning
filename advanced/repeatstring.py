from datetime import datetime


#字符串
def repstr_by_string(str, max):
    s = ''
    for i in range(max):
        s += f"{i}.{str}\n"
    return s


# 列表
def repstr_by_list(str, max):
    l = []
    for i in range(max):
        l.append(f"{i}.{str}\n")
    return ''.join(l)


# 列表推导式
def repstr_by_comp(str, max):
    l = [f"{i}.{str}\n" for i in range(max)]
    return ''.join(l)


if __name__ == '__main__':
    str = '123456789A123456789B123456789C123456789D123456789E123456789F123456789G123456789123456789H123456789J'
    max = 1000000

    # btime1 = datetime.now()
    # str1 = repstr_by_string(str, max)
    # etime1 = datetime.now()
    # print(f"repeat by string:{etime1-btime1}")

    btime2 = datetime.now()
    str2 = repstr_by_list(str, max)
    etime2 = datetime.now()
    print(f"repeat by list:{etime2-btime2}")

    btime3 = datetime.now()
    str3 = repstr_by_comp(str, max)
    etime3 = datetime.now()
    print(f"repeat by comp:{etime3-btime3}")

    btime4 = datetime.now()
    str4 = repstr_by_enum(str, max)
    etime4 = datetime.now()
    print(f"repeat by enum:{etime4 - btime4}")

    btime5 = datetime.now()
    str5 = repstr_by_aaa(str, max)
    etime5 = datetime.now()
    print(f"repeat by aaa:{etime5 - btime5}")

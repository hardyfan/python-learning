def reverse1(s):
    return s[::-1]


def reverse2(s):
    l = list(s)
    l.reverse()
    return ''.join(l)


def reverse3(s):
    l = list(s)
    m = len(l)
    for i in range(m//2):
        l[i], l[m-i-1] = l[m-i-1], l[i]
    return ''.join(l)


if __name__ == '__main__':
    s = '123456789'
    print('reverse string by slice:{s1}'.format(s1=reverse1(s)))
    print('reverse string by reverse:{s2}'.format(s2=reverse2(s)))
    print('reverse string by exchange:{s3}'.format(s3=reverse3(s)))

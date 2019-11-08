#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: hardyfan 
# Date: 2019-06-15 18:03

count = 10


def outer():
    global count
    print("global count :{count}".format(count=count))
    count = 1000
    print("outer count :{count}".format(count=count))


def inner():
    count = 100
    print("inner count: {count}".format(count=count))


if __name__ == '__main__':
    print("count:{count}".format(count=count))
    outer()
    print("count:{count}".format(count=count))
    inner()
    print("count:{count}".format(count=count))
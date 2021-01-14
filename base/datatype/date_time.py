# -*- coding: utf-8 -*-
# FileName: date_time
# Create by Hardy on 2021/1/14
# Description:

import datetime

if __name__ == '__main__':

    tn = datetime.datetime.now()
    tb = tn - datetime.timedelta(minutes=60)
    te = tn + datetime.timedelta(minutes=30)

    tb_time = tb.strftime("%H:%M")
    te_time = te.strftime("%H:%M")

    print(tb_time)
    print(te_time)
    my_time = "09:30"
    if tb_time < my_time < te_time:
        print("ok")
    else:
        print("no")




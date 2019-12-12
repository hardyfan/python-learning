#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
# print('rowcount =', cursor.rowcount)
# 关闭Cursor:
# cursor.close()
# 提交事务:
# conn.commit()
# 关闭Connection:
# conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

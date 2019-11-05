#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
from mysql_config import MYSQL_DATABASE, MYSQL_USER, MYSQL_PASS


def create_user():
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')


def insert_user():
    cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
    print('rowcount =', cursor.rowcount)
    conn.commit()
    cursor.close()


def select_user():
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    conn = mysql.connector.connect(user=MYSQL_USER,
                                   password=MYSQL_PASS,
                                   database=MYSQL_DATABASE)
    cursor = conn.cursor()

    select_user()
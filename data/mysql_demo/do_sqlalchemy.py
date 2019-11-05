#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from mysql_config import MYSQL_ENGINE

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


def insert_user():
    session = DBSession()
    new_user = User(id='5', name='Bob')
    session.add(new_user)
    session.commit()
    session.close()


def read_user():
    session = DBSession()
    user = session.query(User).filter(User.id == '5').one()
    print('type:', type(user))
    print('name:', user.name)
    session.close()


if __name__ == '__main__':
    # 初始化数据库连接:
    engine = create_engine(MYSQL_ENGINE)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建新User对象:
    # insert_user()
    # 读取User对象
    read_user()



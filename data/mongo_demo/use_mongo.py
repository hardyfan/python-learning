
#！/usr/bin/python3# -*- coding: utf-8 -*-
# FileName: use_mongo.py
# Create by Hardy on 2019-11-07
# Description:

import pymongo
from mongo_conf import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASSWORD, MONGO_DATABASE, MONGO_AUTHTYPE

client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client[MONGO_DATABASE]
db.authenticate(MONGO_USERNAME, MONGO_PASSWORD, mechanism=MONGO_AUTHTYPE)
my_col = db["students"]


def database_test():
    """
    列出所有数据库
    """
    db_list = client.list_database_names()
    for db_name in db_list:
        print(f'db:{db_name}')


def collection_test():
    """
    集合，相当于SQL中的表，只有插入数据后才被创建
    """
    collection_list = db.list_collection_names()
    for collection in collection_list:
        print(f'collection:{collection}')
    if "students" in collection_list:  # 判断 students 集合是否存在
        print(f"集合students已存在！")
    else:
        print(f"集合students不存在！")


def collection_insert():
    """
    插入单行或多行数据的demo
    :return:
    """
    my_dict = {"name": "Hardy", "alexa": "10000", "url": "https://www.loncol.com"}
    x = my_col.insert_one(my_dict)
    print(f'new col id:{x.inserted_id}')

    my_list = [
        {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
    ]
    x = my_col.insert_many(my_list)
    print(f'new col id:{x.inserted_ids}')


def collection_update():
    """
    执行更新操作，update_one和update_many
    :return:
    """
    my_query = {"alexa": "10000"}
    new_values = {"$set": {"alexa": "20000"}}
    my_col.update_many(my_query, new_values)

    for x in my_col.find():
        print(x)


def collection_delete():
    """
    执行删除操作，delete_one和delete_many
    :return:
    """
    my_query = {"name": "Hardy"}
    my_col.delete_one(my_query)
    for x in my_col.find():
        print(x)


def collection_find():
    """
    查询操作find
    :return:
    """
    x = my_col.find_one()
    print(x)

    # for x in my_col.find():
    #     print(x)

    for x in my_col.find({"name": "Hardy"}, {"_id": 0, "name": 1, "alexa": 1}):
        print(x)


def collection_sort():
    """
    排序操作：sort
    :return:
    """
    # my_doc = my_col.find().sort("alexa")
    my_doc = my_col.find().sort("_alexa")
    for x in my_doc:
        print(x)


if __name__ == '__main__':
    # database_test()
    # collection_test()
    # collection_insert()
    # collection_update()
    collection_delete()
    # collection_find()
    # collection_sort()



# -*- coding: utf-8 -*-
# Author: Hardy
# Date: 2019-11-05
# Description:
import time
from influxdb import InfluxDBClient
from influxdb_conf import INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASS, INFLUXDB_DB


def read_info():
    data_list = [{'measurement': 'win',
                  'tags': {'cpu': 'i7-7700HQ'},
                  'fields': {'cpu_info_usage': '80%',
                             'cpu_info_system': 'ubuntu',
                             'cpu_info_idle': 'idle',
                             'cpu_info_interrupt': 'rupt',
                             'cpu_info_dpc': 'dpc',
                             'cpu_info_dpc1': 'dpc1'
                             }}]
    return data_list


if __name__ == '__main__':
    client = InfluxDBClient(INFLUXDB_HOST,
                            INFLUXDB_PORT,
                            INFLUXDB_USER,
                            INFLUXDB_PASS,
                            INFLUXDB_DB)

    # 写入数据库
    # count = 0
    # while count < 5:
    #     count += 1
    #     client.write_points(read_info())
    #     print(f"{time.strftime('%H:%M:%S')}:第{count}次写入")
    #     time.sleep(2)

    # 读取数据库
    wins = client.query("SELECT * FROM win").get_points()
    for win in wins:
        # print(win)
        print(f"time={win['time']}, cpu={win['cpu']}, cpu_info_usage={win['cpu_info_usage']}")





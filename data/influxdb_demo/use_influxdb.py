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
                             'cpu_info_dpc': 'dpc'
                             }}]
    return data_list


if __name__ == '__main__':
    client = InfluxDBClient(INFLUXDB_HOST,
                            INFLUXDB_PORT,
                            INFLUXDB_USER,
                            INFLUXDB_PASS,
                            INFLUXDB_DB)
    counts = 0
    while counts < 10:
        counts += 1
        client.write_points(read_info())
        print(f"{time.strftime('%H:%M:%S')}:第{counts}次写入")
        time.sleep(5)




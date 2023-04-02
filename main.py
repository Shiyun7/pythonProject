#此函数可实现adb的连接和进行一次点击事件
import os

DeviceId = '192.168.12.2'
# 连接adb
def adb_connect(DeviceId):
    os.system(f"adb connect {DeviceId}")



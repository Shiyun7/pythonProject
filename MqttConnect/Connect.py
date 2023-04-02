import time
import paho.mqtt.client as mqtt
import json
import serial
import serial.tools.list_ports

MQTT_SERVER = '8.129.117.221'
MQTT_PORT = 1883


def openPort():
    port_list = list(serial.tools.list_ports.comports())

    if len(port_list) <= 0:
        print("无串口设备")
    else:
        print("可用的串口如下：")
    for i in port_list:
        print(list(i)[0], list(i)[1])
    ser = serial.Serial("COM6", 115200)
    if ser.isOpen():
        print("打开串口成功。")
        print(ser.name)
    else:
        print("串口打开失败。")

    ser.close()
    if ser.isOpen():
        print("串口未关闭")
    else:
        print("串口已关闭")


# 连接mqtt
def mqtt_connect():
    client = mqtt.Client()
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    client.loop_start()
    data = {
        "devNumList": ["88:79:5B:26:23:4F"],
        "upgrade": {
            "eid": 1,
            "chip": "9632",
            "model": "G30UE",
            "address": "https://gzc-download.weiyun.com/ftn_handler/efe31ad0e71bfd87c334994e29d5e48f94f5cc332906fce4434b5c6d4edd63d3ae393a74e1801612117778408c0f45187691f69468d7c15d5de5649db29fd0cc/IDP_9632_G30UE_V0.0.217_217.apk?fname=IDP_9632_G30UE_V0.0.217_217.apk&from=30013&version=3.3.3.3",
            "versioncode": 217,
            "md5": "93332cb2d8195a62da165158c8ca251c",
            "sTime": "2023-03-31 08:00:00",
            "eTime": "2023-03-31 19:00:00"
        }
    }
    msg = json.dumps(data)
    client.publish('idp3/upgrade', msg, 1)
    print('send:', data)

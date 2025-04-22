# -*- coding: utf-8 -*-
import serial
import re
import time
import urllib, urllib3

ser = serial.Serial("/dev/ttyUSB0", 38400)  # 打开对应串口,需要权限
ser.timeout = 1

ser.write("AT+VERSION?\r\n")  # 查询蓝牙固件版本
tmp = ser.read(22)
print(ser.name)
tmp.replace('', '')
tmp.replace('', '')
tmp.replace('\0', '')
tmp.replace('\n\r', '')
print("蓝牙硬件版本：", tmp)

ser.write("at+init\r\n")  # 初始化蓝牙
tmp = ser.read(20)
print("蓝牙初始化...")

ser.write("at+iac=9e8b33\r\n")  # 查询访问码为9E8B33的设备
tmp = ser.read(20)

ser.write("at+class=0\r\n")  # 指出设备类型，以及所支持的服务类型
tmp = ser.read(20)

ser.write("at+inqm=0,9,10\r\n")  # 不要显示RSSI信号强度,检测超过9个或超过10秒钟就停止
tmp = ser.read(15)
print("蓝牙配置...", tmp)

while 1:
    ser.timeout = 10
    ser.write("AT+INQ\r\n")
    print("搜索周围设备...")

    tmp = ser.read(1000)
    print("设备列表...")
    tmp.strip('\n')
    tmp.strip('\r')
    tmp.strip('\r\n')
    tmp.strip('\n\r')
    print(tmp)

    print("地址匹配...")

    pattern = re.compile(
        "(\+INQ:([A-Z]|\d){4}\W([A-Z]|\d){2}\W([A-Z]|\d){6}\W)|(\+INQ:([A-Z]|\d){2}:([A-Z]|\d){2}:([A-Z]|\d){5})\W")  # 正则匹配

    i = 0
    for m in pattern.finditer(tmp):
        print(m.group()[5:-1])

        i = i + 1
        print(i)# 计数器

        str = m.group()[5:-1]
        url = "http://192.168.43.146:8000/update_device/?address=%s&location=111" % str
        print(url)

        res = urllib3.urlopen(url)  # 提交

    time.sleep(10)
ser.close()
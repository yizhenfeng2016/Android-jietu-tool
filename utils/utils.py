#coding:utf-8
__author__ = 'Administrator'

import subprocess
import os
import sys
import time

#adb.exe完整路径

globalStartupInfo = subprocess.STARTUPINFO()
globalStartupInfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.getcwd(), shell=False, startupinfo=globalStartupInfo)
    p.wait()
    re=p.stdout.read().decode()
    return re

app_path=""
if getattr(sys,'frozen',False):
    app_path=os.path.dirname(sys.executable) #sys.executable：python.exe所在目录
else:
    app_path=os.path.abspath('.')

adb=os.path.join(app_path,"tools\\adb.exe")
# print(adb)

#判断是否已连接上adb

def connect_adb(ip):
    cmd=adb+" connect "+ip
    device=runCmd(cmd)
    # print(device)
    return device

def is_connect_adb():
    cmd=[adb,'devices']
    mobilelist=runCmd(cmd)
    mobilelist=mobilelist.split('\r\n')[1:]
    return mobilelist

def jietu(path):
    #保存到本地电脑的图片路径
    try:
        timestamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        jietupath=path+timestamp+'.png'
        sdcardpath='/sdcard/screenshot.png'
        if os.path.exists(jietupath):
            os.remove(jietupath)
        # print('it is screenshoting to mobile.....')
        cmd=adb+' shell /system/bin/screencap -p '+sdcardpath
        # print(cmd)
        result=runCmd(cmd)
        # print('it is screenshot success.....')
        # print(result)
        # print('it is moving screenshot to pc.....')
        cmd=adb+' pull '+sdcardpath+' '+jietupath
        # print(cmd)
        result=runCmd(cmd)
        # print(result)
        return True
    except Exception as e:
        return False

# if __name__=="__main__":
#     flag=is_connect_adb()
#     print(flag)
#
#     if flag:
#         jietu(app_path+"img/")


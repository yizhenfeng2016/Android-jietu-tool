#coding:utf-8
__author__ = 'Administrator'

import gui
from PyQt4 import QtCore, QtGui
import sys
import os

app_path=""
if getattr(sys,'frozen',False):
    app_path=os.path.dirname(sys.executable) #sys.executable：python.exe所在目录
else:
    app_path=os.path.abspath('.')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
    _toUtf8=QtCore.QString.toUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

from utils import utils

class MyMainWindow(QtGui.QMainWindow,gui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)#将自己MyMainWindow作为对象，调用父类的setupUi的方法，从而获取组件
        self.initialize()

    def initialize(self):
        self.pushButton.clicked.connect(self.jietu)
        self.pushButton_2.clicked.connect(self.adb_connect)
        path=app_path+"\\img\\"
        self.lineEdit.setText(_fromUtf8(path))

    def adb_connect(self):
        ip=str(self.lineEdit_2.text())
        if ip:
            # print(ip)
            utils.connect_adb(ip)
        mobiles=[]
        mobile=utils.is_connect_adb()
        for x in mobile:
            if x:
                device=x.split('\t')
                x=device[0]
                mobiles.append(x)
        if len(mobiles)==1:
            QtGui.QMessageBox.about(self,"Info",_fromUtf8("设备 "+str(mobiles)+" 连接adb成功"))
        elif len(mobiles)>1:
            QtGui.QMessageBox.about(self,"Info",_fromUtf8("超过2个设备 "+str(mobiles)+" 连接adb成功，请只留其中一个，不然无法截图！"))
        else:
            QtGui.QMessageBox.about(self,"Info",_fromUtf8("没有设备连接"))

    def jietu(self):
        path=str(self.lineEdit.text())
        flag=utils.jietu(path)
        if flag:
            QtGui.QMessageBox.about(self,"Info",_fromUtf8("截图成功"))
        else:
            QtGui.QMessageBox.about(self,"Info",_fromUtf8("截图失败，请重新连接"))
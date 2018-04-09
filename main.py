#-*- coding:utf-8 -*-
__author__ = 'Administrator'

from mygui import MyMainWindow
from PyQt4 import QtGui
import sys

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    win=MyMainWindow()
    win.show()
    sys.exit(app.exec_())

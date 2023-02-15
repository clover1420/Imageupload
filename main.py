from PyQt6 import uic
from PyQt6.QtWidgets import *
import data
from tool import resource_path, FileChoose, StartUpload
import data
import sys, sys

class wm(QWidget):
    def __init__(self, path):
        super(QWidget,self).__init__()
        uic.loadUi(path,self)
        self.setWindowTitle('图片上传')
        self.pushButton.clicked.connect(lambda:self.an(self.stackedWidget, 0))
        self.pushButton_2.clicked.connect(lambda:self.an(self.stackedWidget, 1))

        self.choose.clicked.connect(lambda:FileChoose(self.lineEdit))
        self.Begin.clicked.connect(lambda:StartUpload(self))
        
        self.radioButton.clicked.connect(lambda:self.up(1,"bilibili"))
        self.radioButton_3.clicked.connect(lambda:self.up(1,"头条"))
        self.radioButton_4.clicked.connect(lambda:self.up(1,"网易严选"))

        self.radioButton_2.clicked.connect(lambda:self.up(2,"url"))
        self.radioButton_5.clicked.connect(lambda:self.up(2,"md"))
        self.radioButton_6.clicked.connect(lambda:self.up(2,"html"))
        data.bb = self
    
    # 单选按钮的值存储
    def up(self,id, nr):
        if id == 1:
            data.up_location = nr
        elif id == 2:
            data.return_link = nr
        else:
            pass
    
    # 页面切换
    def an(self, id, index: int):
        id.setCurrentIndex(index)

if __name__=='__main__':
    app=QApplication(sys.argv)
    path = resource_path("res\main.ui")
    mainwindow=wm(path)
    #禁止拉伸窗口大小
    mainwindow.setFixedSize(mainwindow.width(), mainwindow.height())
    
    mainwindow.show()
    app.exec()
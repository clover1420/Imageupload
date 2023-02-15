import os, sys, data, api
from PyQt6.QtWidgets import *
from threading import Thread

# 打包资源文件的读取
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 文件夹选择函数
def FileChoose(id):
    directory = QFileDialog.getExistingDirectory(None, "getExistingDirectory", "./")
    id.setText(directory)

# 获取图片大小
def size(filePath):
    with open(filePath, "rb") as f:
        size = len(f.read())
    return size / 1e6

def Upload(self):
    cg = 0
    awaitUp =[]
    locations = self.lineEdit.text()
    # 判断上传图片文件夹的路径是否为空
    if locations != "":
        # 整理出待上传的图片
        for i, j, k in os.walk(locations):
            for j in k:
                if j[-4:] == ".png" or j[-4:] == ".jpg" or j[-4:] == "jpeg":
                    awaitUp.append(j)

        # 开始上传待上传的图片
        self.label_8.setText(str(len(awaitUp)))
        for i in awaitUp:
            imgpath = locations + "/" + i
            url = api.upload(data.up_location, imgpath, i)
            self.plainTextEdit.appendPlainText(url)
            cg += 1
            self.label_2.setText(str(cg))
    else:
        self.label_6.setText("空路径")


def StartUpload(self):
    Thread(target=Upload, args=(self,)).start()
    #print(self.lineEdit.text())
    #self.textEdit.append(data.return_link)
    pass
import api
import config
import os
import random
import platform


# 获取图片大小
def size(filePath):
    with open(filePath, "rb") as f:
        size = len(f.read())
    return size / 1e6


def locations(imgsize):
    if imgsize < 2:
        return random.randint(0, 8)
    elif imgsize < 5:
        return random.randint(0, 7)
    elif imgsize < 10:
        return random.randint(0, 4)
    else:
        return 0


def run():
    # 获取当前系统
    if platform.system() == "Windows":
        sep = "\\"
    else:
        sep = "/"
    filepath = os.getcwd() + sep + "pic"
    for i, j, k in os.walk(filepath):
        for j in k:
            # 获取图片路径
            imgpath = filepath + sep + j
            # 获取图片名字
            name = j[:-4]
            imgsize = size(imgpath)
            location = locations(imgsize)
            for i in config.up_location:
                if i == None:
                    api.upload(location, imgpath, j)
                else:
                    api.upload(i, imgpath, j) 
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
    aa = ["bilibili", "网易严选", "搜狗", "美团", "今日头条", "一加论坛", "qq", "葫芦侠", "cnmo论坛", "起点阅读"]
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
            img_location = aa[location]
            for i in config.up_location:
                if i == None:
                    data = api.upload(location, imgpath, j)
                    print(f"{name}-上传成功:{data} --上传位置:{img_location}")
                else:
                    data = api.upload(i, imgpath, j)
                    print(f"{name}-上传成功:{data} --上传位置:{aa[i]}")

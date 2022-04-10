import os,api,random

#获取图片大小
def size(filePath):
    with open(filePath,"rb") as f:
        size = len(f.read())
    return size / 1e6

def locations(imgsize):
    if imgsize < 2:
        return random.randint(0,8)
    elif imgsize < 5:
        return random.randint(0,7)
    elif imgsize < 10:
        return random.randint(0,4)
    else:
        return 0

def run():
    aa = ["bilibili","网易严选","搜狗","美团","今日头条","qq","葫芦侠","cnmo论坛","起点阅读"]
    filepath = os.getcwd()+"\\pic"
    for i,j,k in os.walk(filepath):
        for j in k:
            #获取图片路径
            imgpath = filepath + "\\" + j
            #获取图片名字
            name = j[:-4]
            imgsize = size(imgpath)
            location = locations(imgsize)
            img_location = aa[location]
            data = api.upload(5,imgpath,j)
            print(f"{name}-上传成功--上传位置:{img_location}")

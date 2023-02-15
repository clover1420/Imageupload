import requests,json,cookie
import data as fhys
from bs4 import BeautifulSoup

def likcl(url,name):
    if fhys.return_link == "url":
        return " "+url
    elif fhys.return_link == "md":
        return f" ![{name}]({url})"
    elif fhys.return_link == "html":
        return f' <img src="{url}"  alt="{name}" />'
    else:
        return "返回样式参数错误"

def upload(a,path,name):
    #bilibili图床-20MB
    if a == "bilibili":
        url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"
        head = {
            "User-Agent": "bilibili",
            "Cookie": "SESSDATA=6644a6cd%2C1673324831%2C88e8a%2A71;"
        }
        file ={
            "file_up": (name, open(path, "rb"), "image/png"),
            "biz": (None,"text"),
            "category": (None,"daily")
        }
        zz = requests.post(url=url,files=file,headers=head).json()["data"]["image_url"]
        return zz
    
    #网易严选图床-10MB
    elif a == "网易严选":
        url = "http://you.163.com/xhr/file/upload.json"
        head = {
            "user-agent": cookie.ua_pc,
            "cookie": cookie.wyyx_cookie
        }
        file ={
            "file": (name, open(path, "rb"), "image/png")
        }
        zz = requests.post(url=url,files=file,headers=head).json()
        return likcl(zz["data"][0], name)
    
    #搜狗图床-10MB
    elif a == 999:
        url = "https://api.kinh.cc/Picture/SoGou.php"
        head = {
            "user-agent": cookie.ua_pc
        }
        file ={
            "FilePicture": (name, open(path +'/'+ name, "rb"), "image/png")
        }
        zz = requests.post(url=url,files=file,headers=head).json()
        return zz['link']
    #美团图床-10MB
    elif a == 2:
        url = "https://api.kinh.cc/Picture/MeiTuan.php"
        head = {
            "user-agent": cookie.ua_pc
        }
        file ={
            "FilePicture": (name, open(path +'/'+ name, "rb"), "image/png")
        }
        zz = requests.post(url=url,files=file,headers=head).json()
        return zz['link']
    #今日头条-10MB
    #elif a == 3:
        #url = "https://mp.toutiao.com/mp/agw/article_material/photo/upload_picture?type=ueditor&pgc_watermark=0&action=uploadimage&encode=utf-8&is_private=1"
       #head = {
            #"user-agent": cookie.ua_pc,
            #"cookie": cookie.jrtt_cookie
        #}
       # file ={
            #"upfile": (name, open(path +'/'+ name, "rb"), "image/png")
        #}
        #zz = requests.post(url=url,files=file,headers=head).json()
        #return zz['url']
    #qq图床-5MB
    elif a == 3:
        url = "https://pic.ihcloud.net/api2/qq.php"
        head = {
            "referer": "https://pic.ihcloud.net",
            "user-agent": cookie.ua_pc
        }
        file ={
            "image": (name, open(path +'/'+ name, "rb"), "image/png"),
            "file_id": (None,"0")
        }
        zz = requests.post(url=url,files=file,headers=head).json()["data"]["url"]
        return zz
    #遇见图床-葫芦侠接口-5MB
    elif a == 4:
        url = "https://www.hualigs.cn/api/upload"
        head = {
            "user-agent": cookie.ua_pc
        }
        file ={
            "image": (name, open(path +'/'+ name, "rb"), "image/png"),
            "token": (None,"f55a7e46fa8c5614108ff3fbc4986c86"),
            "apiType": (None,"huluxia")
        }
        zz = requests.post(url=url,files=file,headers=head).json()
        return zz['data']['url']['huluxia']
    #cnmo论坛-5MB
    elif a == 5:
        url = "https://bbs.cnmo.com/index.php?c=Api_Attachment&m=UploadImageNew"
        head = {
            "user-agent": cookie.ua_pc
        }
        file ={
            "img": (name, open(path +'/'+ name, "rb"), "image/png"),
            "uid": (None,"12273065")
        }
        zz = requests.post(url=url,files=file,headers=head).json()
        return zz['data']['url']
    #起点阅读图床-2MB
    elif a == 6:
        url = "https://my.qidian.com/ajax/headimage/uploadimg"
        head = {
            "user-agent": cookie.ua_pc,
            "cookie": cookie.qdyd_cookie
        }
        file ={
            "image": (name, open(path +'/'+ name, "rb"), "image/png")
        }
        zz = requests.post(url=url,files=file,headers=head).text
        soup = BeautifulSoup(zz,'html.parser')
        data = json.loads(soup.body.string)
        return "https:"+data["data"]["url"]
import requests,json,cookie
from bs4 import BeautifulSoup

def upload(location,imgpath,name):
    match location:
        #bilibili图床-20MB
        case 0:
            url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"
            head = {
                "User-Agent": "bilibili",
                "Cookie": cookie.bilibili_cookie
            }
            file ={
                "file_up": (name, open(imgpath, "rb"), "image/png"),
                "biz": (None,"text"),
                "category": (None,"daily")
            }
            zz = requests.post(url=url,files=file,headers=head).json()["data"]["image_url"]
            return zz
        #网易严选图床-10MB
        case 1:
            url = "http://you.163.com/xhr/file/upload.json"
            head = {
                "user-agent": "",
                "cookie": cookie.wyyx_cookie
            }
            file ={
                "file": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz["data"][0]
        #搜狗图床-10MB
        case 2:
            url = "https://api.kinh.cc/Picture/SoGou.php"
            head = {
                "user-agent": cookie.ua
            }
            file ={
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz['link']
        #美团图床-10MB
        case 3:
            url = "https://api.kinh.cc/Picture/MeiTuan.php"
            head = {
                "user-agent": cookie.ua
            }
            file ={
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz['link']
        #今日头条-10MB
        case 4:
            url = "https://mp.toutiao.com/mp/agw/article_material/photo/upload_picture?type=ueditor&pgc_watermark=0&action=uploadimage&encode=utf-8&is_private=1"
            head = {
                "user-agent": cookie.ua,
                "cookie": cookie.jrtt_cookie
            }
            file ={
                "upfile": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz['url']
        #qq图床-5MB
        case 5:
            url = "https://pic.ihcloud.net/api2/qq.php"
            head = {
                "referer": "https://pic.ihcloud.net",
                "user-agent": cookie.ua
            }
            file ={
                "image": (name, open(imgpath, "rb"), "image/png"),
                "file_id": (None,"0")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz["data"]["url"]
        #遇见图床-葫芦侠接口-5MB
        case 6:
            url = "https://www.hualigs.cn/api/upload"
            head = {
                "user-agent": cookie.ua
            }
            file ={
                "image": (name, open(imgpath, "rb"), "image/png"),
                "token": (None,"f55a7e46fa8c5614108ff3fbc4986c86"),
                "apiType": (None,"huluxia")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz['data']['url']['huluxia']
        #cnmo论坛-5MB
        case 7:
            url = "https://bbs.cnmo.com/index.php?c=Api_Attachment&m=UploadImageNew"
            head = {
                "user-agent": cookie.ua
            }
            file ={
                "img": (name, open(imgpath, "rb"), "image/png"),
                "uid": (None,"12273065")
            }
            zz = requests.post(url=url,files=file,headers=head).json()
            return zz['data']['url']
        #起点阅读图床-2MB
        case 8:
            url = "https://my.qidian.com/ajax/headimage/uploadimg"
            head = {
                "user-agent": cookie.ua,
                "cookie": cookie.qdyd_cookie
            }
            file ={
                "image": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url,files=file,headers=head).text
            soup = BeautifulSoup(zz,'html.parser')
            data = json.loads(soup.body.string)
            return "https:"+data["data"]["url"]
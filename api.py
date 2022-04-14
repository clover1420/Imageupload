import config
import json
import requests
from bs4 import BeautifulSoup


def upload(location, imgpath, name):
    try:
        # bilibili图床-20MB
        if location == 0:
            url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"
            head = {
                "User-Agent": "bilibili",
                "Cookie": config.bilibili_cookie
            }
            file = {
                "file_up": (name, open(imgpath, "rb"), "image/png"),
                "biz": (None, "text"),
                "category": (None, "daily")
            }
            zz = requests.post(url=url, files=file, headers=head).json()["data"]["image_url"]
            return zz
        # 网易严选图床-10MB
        if location == 1:
            url = "http://you.163.com/xhr/file/upload.json"
            head = {
                "user-agent": "",
                "cookie": config.wyyx_cookie
            }
            file = {
                "file": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz["data"][0]
        # 搜狗图床-10MB
        if location == 2:
            url = "https://api.kinh.cc/Picture/SoGou.php"
            head = {
                "user-agent": config.ua
            }
            file = {
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz['link']
        # 美团图床-10MB
        if location == 3:
            url = "https://api.kinh.cc/Picture/MeiTuan.php"
            head = {
                "user-agent": config.ua
            }
            file = {
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz['link']
        # 今日头条-10MB
        if location == 4:
            url = "https://mp.toutiao.com/mp/agw/article_material/photo/upload_picture?type=ueditor&pgc_watermark=0&action=uploadimage&encode=utf-8&is_private=1"
            head = {
                "user-agent": config.ua,
                "cookie": config.jrtt_cookie
            }
            file = {
                "upfile": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz['url']
        # 一加论坛-10MB
        if location == 5:
            url = "https://www.oneplusbbs.com/misc.php?mod=swfupload&operation=uploadimg&simple=1&type=image"
            head = {
                "user-agent": config.ua,
                "cookie": config.qdyd_cookie
            }
            file = {
                "Filedata": (name, open(imgpath, "rb"), "image/png"),
                "uid": (None, "3437606"),
                "hash": (None, "5e9cafdd8723d52408218f2bde4339d6")
            }
            data = {
                "mod": "swfupload",
                "operation": "uploadimg",
                "simple": 1,
                "type": "image"
            }
            zz = requests.post(url=url, data=data, files=file, headers=head).json()
            if zz['code'] == 200:
                return zz['link']
            else:
                return zz['msg']
        # qq图床-5MB
        if location == 6:
            url = "https://pic.ihcloud.net/api2/qq.php"
            head = {
                "referer": "https://pic.ihcloud.net",
                "user-agent": config.ua
            }
            file = {
                "image": (name, open(imgpath, "rb"), "image/png"),
                "file_id": (None, "0")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz["data"]["url"]
        # 遇见图床-葫芦侠接口-5MB
        if location == 7:
            url = "https://www.hualigs.cn/api/upload"
            head = {
                "user-agent": config.ua
            }
            file = {
                "image": (name, open(imgpath, "rb"), "image/png"),
                "token": (None, "f55a7e46fa8c5614108ff3fbc4986c86"),
                "apiType": (None, "huluxia")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz['data']['url']['huluxia']
        # cnmo论坛-5MB
        if location == 8:
            url = "https://bbs.cnmo.com/index.php?c=Api_Attachment&m=UploadImageNew"
            head = {
                "user-agent": config.ua
            }
            file = {
                "img": (name, open(imgpath, "rb"), "image/png"),
                "uid": (None, "12273065")
            }
            zz = requests.post(url=url, files=file, headers=head).json()
            return zz['data']['url']
        # 起点阅读图床-2MB
        if location == 9:
            url = "https://my.qidian.com/ajax/headimage/uploadimg"
            head = {
                "user-agent": config.ua,
                "cookie": config.qdyd_cookie
            }
            file = {
                "image": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).text
            soup = BeautifulSoup(zz, 'html.parser')
            data = json.loads(soup.body.string)
            return "https:" + data["data"]["url"]
    except Exception as e:
        return e

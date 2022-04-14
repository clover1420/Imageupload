import config
import json
import requests
from bs4 import BeautifulSoup


def upload(location, imgpath, name):
    aa = ["bilibili", "网易严选", "搜狗", "美团", "今日头条", "一加论坛", "qq", "葫芦侠", "cnmo论坛", "起点阅读"]
    try:
        # bilibili图床-20MB
        if location == 0:
            if config.bilibili_cookie != "":
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
                print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")
            else:
                print("bilibili上传需要cookie")

        # 网易严选图床-10MB
        if location == 1:
            if config.wyyx_cookie != "":
                url = "http://you.163.com/xhr/file/upload.json"
                head = {
                    "user-agent": "",
                    "cookie": config.wyyx_cookie
                }
                file = {
                    "file": (name, open(imgpath, "rb"), "image/png")
                }
                zz = requests.post(url=url, files=file, headers=head).json()["data"][0]
                print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")
            else:
                print("网易严选上传需要cookie")

        # 搜狗图床-10MB
        if location == 2:
            url = "https://api.kinh.cc/Picture/SoGou.php"
            head = {
                "user-agent": config.ua
            }
            file = {
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()['link']
            print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")

        # 美团图床-10MB
        if location == 3:
            url = "https://api.kinh.cc/Picture/MeiTuan.php"
            head = {
                "user-agent": config.ua
            }
            file = {
                "FilePicture": (name, open(imgpath, "rb"), "image/png")
            }
            zz = requests.post(url=url, files=file, headers=head).json()['link']
            print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")

        # 今日头条-10MB
        if location == 4:
            if config.jrtt_cookie != "":
                url = "https://mp.toutiao.com/mp/agw/article_material/photo/upload_picture?type=ueditor&pgc_watermark=0&action=uploadimage&encode=utf-8&is_private=1"
                head = {
                    "user-agent": config.ua,
                    "cookie": config.jrtt_cookie
                }
                file = {
                    "upfile": (name, open(imgpath, "rb"), "image/png")
                }
                zz = requests.post(url=url, files=file, headers=head).json()['url']
                print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")
            else:
                print("今日头条上传需要cookie")

        # 一加论坛-10MB
        if location == 5:
            url = "https://www.oneplusbbs.com/misc.php?mod=swfupload&operation=uploadimg&simple=1&type=image"
            head = {
                "user-agent": config.ua
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
                print(f"{name}-上传成功: {zz['link']} --上传位置:{aa[location]}")
            else:
                print(f"一加论坛上传失败:{zz['msg']}")

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
            zz = requests.post(url=url, files=file, headers=head).json()["data"]["url"]
            print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")

        # 遇见图床-葫芦侠接口-5MB
        if location == 7:
            if config.yjtc_token != "":
                url = "https://www.hualigs.cn/api/upload"
                head = {
                    "user-agent": config.ua
                }
                file = {
                    "image": (name, open(imgpath, "rb"), "image/png"),
                    "token": (None, config.yjtc_token),
                    "apiType": (None, "huluxia")
                }
                zz = requests.post(url=url, files=file, headers=head).json()['data']['url']['huluxia']
                print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")
            else:
                print("遇见图床-葫芦侠上传需要token")

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
            zz = requests.post(url=url, files=file, headers=head).json()['data']['url']
            print(f"{name}-上传成功: {zz} --上传位置:{aa[location]}")

        # 起点阅读图床-2MB
        if location == 9:
            if config.qdyd_cookie != "":
                print(9)
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
                img = soup.body.string
                if  img == None:
                    print("起点阅读cookie可能已过期，请更新cookie")
                else:
                    data = json.loads(img)["data"]["url"]
                    print(f"{name}-上传成功: https:{data} --上传位置:{aa[location]}")
            else:
                print("起点阅读上传需要cookie")

    except Exception as e:
        return e

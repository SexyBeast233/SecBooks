# Alibaba Nacos 控制台默认弱口令

## 漏洞描述

Alibaba Nacos 控制台存在默认弱口令 **nacos/nacos**，可登录后台查看敏感信息

## 漏洞影响

> [!NOTE]
>
> Alibaba Nacos

## 漏洞复现

发送如下请求

![](http://wikioss.peiqi.tech/vuln/nacos-12.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

返回200说明成功登录

## Goby & POC

> [!NOTE]
>
> 已上传 https://github.com/PeiQi0/PeiQi-WIKI-POC Goby & POC 目录中
>
> Alibaba_Nacos_Default_password.json

![](http://wikioss.peiqi.tech/vuln/nacos-13.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
# 通达OA v11.2后台任意文件上传漏洞

## 漏洞描述

通达OA v11.2后台存在文件上传漏洞，允许通过绕过黑名单的方法来上传恶意文件，导致服务器被攻击

## 影响版本

> [!NOTE]
>
> 通达OA v11.2

## 环境搭建

[通达OA v11.2下载链接](https://cdndown.tongda2000.com/oa/2019/TDOA11.2.exe)

下载后按步骤安装即可

## 漏洞复现

该漏洞存在于后台，需要通过登录后才能进行使用

登录后点击 **菜单 -> 系统管理 -> 附件管理**

![](http://wikioss.peiqi.tech/vuln/tongdaoa-13.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

点击添加附录存储管理添加如下(存储目录为 webroot 目录，默认为 **D:/MYOA/webroot/**)

![](http://wikioss.peiqi.tech/vuln/tongdaoa-14.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

点击 **组织 -> 系统管理员 -> 上传附件**

![](http://wikioss.peiqi.tech/vuln/tongdaoa-15.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

抓包使用 windows 的绕过方法 **shell.php -> shell.php.**

![](http://wikioss.peiqi.tech/vuln/tongdaoa-16.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

> [!NOTE]
>
> 2012 为目录
>
> 1717872192 为拼接的文件名
>
> 最后的shell名字为 1717872192.shell.php

![](http://wikioss.peiqi.tech/vuln/tongdaoa-17.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

访问木马文件

![](http://wikioss.peiqi.tech/vuln/tongdaoa-18.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
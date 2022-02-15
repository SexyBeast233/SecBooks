## Apache Kylin Console 控制台弱口令

## 漏洞描述

Apache Kylin Console 控制台存在默认弱口令 **admin：KYLIN**，可被登录控制台进一步利用其他漏洞

## 漏洞影响

> [!NOTE]
>
> Apache Kylin

## 漏洞复现

打开后目标站点使用默认账号密码**admin/KYLIN**登录，出现初始界面即为成功

![](http://wikioss.peiqi.tech/vuln/kylin-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

> [!NOTE]
>
> 已上传 https://github.com/PeiQi0/PeiQi-WIKI-POC Goby & POC 目录中
>
> Apache_Kylin_Console_Default_password.json

![](http://wikioss.peiqi.tech/vuln/kylin-26.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
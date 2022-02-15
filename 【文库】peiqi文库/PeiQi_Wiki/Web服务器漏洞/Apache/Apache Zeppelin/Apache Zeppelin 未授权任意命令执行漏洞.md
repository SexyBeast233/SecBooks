# Apache Zeppelin 未授权任意命令执行漏洞

## 漏洞描述

Apache Zeppelin 存在未授权的用户访问命令执行接口，导致了任意用户都可以执行恶意命令获取服务器权限

## 漏洞影响

> [!NOTE]
>
> Apache Zeppelin

## FOFA

> [!NOTE]
>
> icon_hash="960250052"

## 漏洞复现

含有漏洞的页面如下

![](http://wikioss.peiqi.tech/vuln/zep-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

点击 创建一个匿名用户在用户页面执行命令即可

![](http://wikioss.peiqi.tech/vuln/zep-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)


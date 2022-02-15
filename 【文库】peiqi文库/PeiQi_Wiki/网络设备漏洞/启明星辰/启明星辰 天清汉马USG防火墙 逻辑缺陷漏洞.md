# 启明星辰 天清汉马USG防火墙 逻辑缺陷漏洞

## 漏洞描述

启明星辰 天清汉⻢USG防⽕墙 存在逻辑缺陷漏洞，攻击者通过账号密码可以进入后台后更改任意用户权限升级为管理员

## 漏洞影响

> [!NOTE]
>
> 启明星辰 天清汉马USG防火墙

## FOFA

> [!NOTE]
>
> title="天清汉马USG防火墙"

## 漏洞复现

登录后台后管理界面点击下面的图标

![](http://wikioss.peiqi.tech/vuln/qm-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

更改权限为任意用户,刷新后得到用户权限

![](http://wikioss.peiqi.tech/vuln/qm-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
# 杭州法源软件 法律知识数据库系统 后台XSS漏洞

## 漏洞描述

杭州法源软件开发有限公司开发的实践教学平台系统下的法律知识数据库系统登录后台用户名处存在通用XSS漏洞

## 漏洞影响

> [!NOTE]
>
> 杭州法源软件 法律知识数据库系统

## FOFA

> [!NOTE]
>
> icon_hash="2018105215" || title="实践教学平台 - 杭州法源软件开发有限公司"

## 漏洞复现

登录后台后更改用户名，使用 td标签 闭合

![](http://wikioss.peiqi.tech/vuln/fy-8.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

![](http://wikioss.peiqi.tech/vuln/fy-9.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
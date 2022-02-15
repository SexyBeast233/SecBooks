# OneBlog 小于v2.2.1 远程命令执行漏洞

## 漏洞描述

OneBlog 小于v2.2.1 由于使用含有漏洞版本的Apache Shiro和默认的密钥导致存在远程命令执行漏洞

## 漏洞影响

> [!NOTE]
>
> OneBlog <= v2.2.1

## FOFA

> [!NOTE]
>
> app="OneBlog开源博客后台管理系统"

## 漏洞复现

登陆页面如下

![](http://wikioss.peiqi.tech/vuln/one-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

使用工具直接利用Apache Shiro漏洞即可

![](http://wikioss.peiqi.tech/vuln/one-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
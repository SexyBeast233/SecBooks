# Hue 后台编辑器命令执行漏洞

## 漏洞描述

Hue 后台编辑器存在命令执行漏洞，攻击者通过编辑上传  xxx.sh 文件即可达到命令执行的目的

## 漏洞影响

> [!NOTE]
>
> Hue 后台编辑器

## FOFA

> [!NOTE]
>
> title="Hue - 欢迎使用 Hue"

## 漏洞复现

登录页面如下

![](http://wikioss.peiqi.tech/vuln/hue-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

上传并编辑文件为执行的命令

![](http://wikioss.peiqi.tech/vuln/hue-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

按如下步骤点击即可执行想要执行的命令

![](http://wikioss.peiqi.tech/vuln/hue-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
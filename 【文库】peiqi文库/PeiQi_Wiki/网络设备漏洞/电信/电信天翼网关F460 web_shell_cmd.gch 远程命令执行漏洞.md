# 电信天翼网关F460 web_shell_cmd.gch 远程命令执行漏洞

## 漏洞描述

电信天翼网关F460 web_shell_cmd.gch文件存在命令调试界面，攻击者可以利用获取服务器权限

## 漏洞影响

> [!NOTE]
>
> 电信天翼网关F460

## FOFA

> [!NOTE]
>
> title="F460"

## 漏洞复现

出现漏洞的文件为 web_shell_cmd.gch

![](http://wikioss.peiqi.tech/vuln/dx-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

直接输入命令就可以执行 **cat /etc/passwd**

![](http://wikioss.peiqi.tech/vuln/dx-8.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)


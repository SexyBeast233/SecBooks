# Wayos 防火墙 后台命令执行漏洞

## 漏洞描述

Wayos 防火墙 后台存在命令执行漏洞，通过命令注入可以执行远程命令

## 漏洞影响

> [!NOTE]
>
> Wayos 防火墙 

## FOFA

> [!NOTE]
>
> body="Get_Verify_Info(hex_md5(user_string)."

## 漏洞复现

登录页面如下

![image-20210531224015364](http://wikioss.peiqi.tech/vuln/image-20210531224015364.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

登录后台后 ping 模块命令执行

![image-20210531224745218](http://wikioss.peiqi.tech/vuln/image-20210531224745218.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)




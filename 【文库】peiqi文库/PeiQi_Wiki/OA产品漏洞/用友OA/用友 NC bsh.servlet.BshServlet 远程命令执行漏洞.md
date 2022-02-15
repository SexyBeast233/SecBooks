# 用友 NC bsh.servlet.BshServlet 远程命令执行漏洞

## 漏洞描述

用友 NC bsh.servlet.BshServlet 存在远程命令执行漏洞，通过BeanShell 执行远程命令获取服务器权限

## 漏洞影响

> [!NOTE]
>
> 用友 NC 

## FOFA

> [!NOTE]
>
> icon_hash="1085941792"

## 漏洞复现

访问页面如下

![image-20210531220356962](http://wikioss.peiqi.tech/vuln/image-20210531220356962.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞Url为

```
/servlet/~ic/bsh.servlet.BshServlet
```

![image-20210531220503672](http://wikioss.peiqi.tech/vuln/image-20210531220503672.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
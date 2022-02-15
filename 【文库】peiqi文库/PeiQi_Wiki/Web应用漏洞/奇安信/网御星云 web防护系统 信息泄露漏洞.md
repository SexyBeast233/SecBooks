# 网御星云 web防护系统 信息泄露漏洞

## 漏洞描述

网御星云 web防护系统 存在信息泄露漏洞，通过访问特殊的Url获取部分敏感信息

## 漏洞影响

> [!NOTE]
>
> 网御星云

## FOFA

> [!NOTE]
>
> title="网页防篡改系统"

## 漏洞复现

登录页面如下

![image-20210615154709758](http://wikioss.peiqi.tech/vuln/image-20210615154709758.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

访问 

```
http://xxx.xxx.xxx.xxx/API/
```

![image-20210615154739222](http://wikioss.peiqi.tech/vuln/image-20210615154739222.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

部分 API请求 不需要登录即可访问获取信息，例如 **/user/list**

![image-20210615154821665](http://wikioss.peiqi.tech/vuln/image-20210615154821665.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)
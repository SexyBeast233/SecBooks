# 快排CMS 信息泄露漏洞

## 漏洞描述

快排CMS 默认开启日志记录，由于日志名为时间作为文件名，造成管理员的Cookie泄露

## 漏洞影响

> [!NOTE]
>
> 快排 CMS <= 1.2

## 环境搭建

https://gitee.com/qingzhanwang/kpcms

## 漏洞复现

文件 **thinkphp/library/think/log/driver/Socket.php** 

这里默认开启日志写入 

```
runtime/log/202104/06.log
```

![](http://wikioss.peiqi.tech/vuln/kp-6.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

其中可以看到泄露了管理员的Cookie信息和其他敏感信息

并且文件命名为 **年+月/日期.log**

![](http://wikioss.peiqi.tech/vuln/kp-7.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)



这里关注后台的日志文件中的 admin.php页面的cookie就可以获得管理员权限
